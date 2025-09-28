import pymxs
import random
rt = pymxs.runtime

from pymxs import runtime as rt
import random

#manage source objects list

class ElementsManager:

    def __init__(self):
        self.elements = []

    def add(self, obj):
        """add an object to the list if it's not already there."""
        if obj and obj not in self.elements:
            self.elements.append(obj)
            print(f"[Added] {obj.name}")

    def add_many(self, objs):
        """add multiple objects to the list."""
        for obj in objs:
            self.add(obj)

    def pick(self):
        """Pick an object from the scene and add it to the list."""
        try:
            picked = rt.pickObject()
            if picked:
                self.add(picked)
        except Exception as e:
            print(f"[Error picking] {e}")

    def remove(self, obj):
        """Remove an object from the list."""
        if obj in self.elements:
            self.elements.remove(obj)
            print(f"[Removed] {obj.name}")

    def replace(self, old_obj, new_obj):
        """Replace an object in the list with another."""
        if old_obj in self.elements and new_obj:
            idx = self.elements.index(old_obj)
            self.elements[idx] = new_obj
            print(f"[Replaced] {old_obj.name} → {new_obj.name}")

    def clear(self):
        """Clear the entire list."""
        self.elements.clear()
        print("[Cleared] All elements in the UI list was removed.")

    def get_random(self):
        """returns a random element from the list."""
        return random.choice(self.elements) if self.elements else None

    def get_all(self):
        """returns all elements in the list."""
        return self.elements

    def __repr__(self):
        return f"ElementsManager({[obj.name for obj in self.elements]})"

#manage individual instance transform
class ScatterInstance:
    def __init__(self, node):
        self.node = node
        self.update_from_node()

    def update_from_node(self):
        self.position = self.node.position
        self.rotation = self.node.rotation
        self.scale = self.node.scale

    def apply_to_node(self):
        self.node.position = self.position
        self.node.rotation = self.rotation
        self.node.scale = self.scale

#manage scatter group
class ScatterGroup:

    def __init__(self,name,surface=None,spline=None):
        self.name = name
        self.spline=spline
        self.surface=surface
        self.instances = []
        self.controller=None #dummy for future use
        self.layer=None #layer for the groups
        self.params = {
            "count": None,
            "distance": None,
            "pos_jitter": rt.point3(0, 0, 0),
            "scale_rangeX": (1.0, 1.0),
            "scale_rangeY": (1.0, 1.0),
            "scale_rangeZ": (1.0, 1.0),
            "rot_x_range": (0, 0),
            "rot_y_range": (0, 0),
            "rot_z_range": (0, 0)
        }
        self._setup_group_in_scene()
        self.manager = None #source objects manager
        print(f"DEBUG: Created group '{self.name}' with controller '{self.controller.name}'")#DEBUG
    
    def _setup_group_in_scene(self,target_obj=None):
        self.target = target_obj  
        #setup controller and layer scene , if they already exist use them
        ctrl_name = f"{self.name}_CTRL"
        existing_ctrl = rt.getNodeByName(ctrl_name)

        if existing_ctrl and rt.isValidNode(existing_ctrl):
            self.controller = existing_ctrl
            print(f"DEBUG: Controller '{self.controller.name}' already exists.")  # DEBUG
        else:
            self.controller = rt.Point(name=ctrl_name)
            self.controller.size = 10
            self.controller.box = True
            self.controller.wirecolor = rt.color(255, 200, 0)
            print(f"DEBUG: Created new controller '{self.controller.name}'.")  # DEBUG
            # Position controller at the center of the target object
            if target_obj and rt.isValidNode(target_obj):
                if rt.superClassOf(target_obj) == rt.Shape:  # Spline
                    self.controller.position = rt.pathInterp(target_obj, 1, 0.0)
                elif rt.isKindOf(target_obj, rt.GeometryClass):  # Surface
                    bb_min, bb_max = rt.nodeGetBoundingBox(target_obj, rt.matrix3(1))
                    self.controller.position = (bb_min + bb_max) / 2
        #Group info in controller's user properties
        rt.setUserProp(self.controller, "ScatterGroup", self.name) #tag for identify the group from the controller

        # Layer
        existing_layer = rt.LayerManager.getLayerFromName(self.name)
        if existing_layer is None:
            self.layer = rt.LayerManager.newLayerFromName(self.name)
        else:
            self.layer = existing_layer
        if self.controller not in self.layer.nodes:
            self.layer.addNode(self.controller)
            # self.layer.isFrozen = True

    def set_spline(self, spline):
        self.spline = spline

    def set_surface(self, surface):
        self.surface = surface
        
    #clear instances
    def clear_instances(self, delete_nodes=False):
        # if no valid controller, exit
        if not hasattr(self, 'controller') or not rt.isValidNode(self.controller):
            return
        #if no instances, exit
        if not hasattr(self, 'instances') or not self.instances:
            return

        valid_instances = [inst for inst in self.instances if getattr(inst, 'node', None) and rt.isValidNode(inst.node)]
        if not valid_instances:
            return
        if delete_nodes:
            for inst in self.instances:
                node = getattr(inst, 'node', None)
                if node and rt.isValidNode(node):
                    print(f"DEBUG: Deleting node {node.name}")
                    rt.clearSelection()
                    rt.select(node)
                    rt.delete(node)
        # Remove invalid instances from the list
        self.instances = [inst for inst in self.instances if getattr(inst, 'node', None) and rt.isValidNode(inst.node)]
        remaining_nodes = [n.name for n in rt.objects if n.name.startswith(f"{self.name}_")]
        print(f"DEBUG: Remaining nodes in scene with group prefix = {remaining_nodes}")

    #show instance as box
    def set_display_as_box(self,enable=True):
        children = self.controller.children
        if not children:
            return

        for child in children:
            if hasattr(child, "boxMode"):
                child.boxMode = enable
            elif hasattr(child, "displayAsBox"):
                child.displayAsBox = enable

        print(f"DEBUG: Display mode changed to {'BOX' if enable else 'MESH'} for all children of '{self.name}'")


    def set_frozen_elements(self, freeze=True):
        children = self.controller.children
        if not children:
            print(f"DEBUG: No children found for '{self.name}'.")
            return

        for child in children:
            if hasattr(child, "isFrozen"):
                child.isFrozen = freeze

        print(f"DEBUG: Freeze status changed to {freeze} for all children of '{self.name}'")

    def set_viewport_display(self, percentage=100):
            children = self.controller.children
            if not children:
                print(f"DEBUG: No children found for '{self.name}'.")
                return
            #save in params
            self.params["viewport_percentage"] = percentage

            #save controller user prop
            rt.setUserProp(self.controller, "ScatterViewportPercentage", str(percentage))

            child_count = len(children)
            if child_count == 0:
                return
            
            children_visible = int((child_count * percentage) / 100)

            # Randomly select children to show
            children_visible = set(random.sample(range(child_count), children_visible))
            for idx, child in enumerate(children):
                if idx in children_visible:
                    rt.unhide(child)
                else:
                    rt.hide(child)

                
            print(f"DEBUG: Set viewport display to {percentage}% for all children of '{self.name}'")

    def apply_random_scale_and_rotation(self,inst): 
        # Apply scale
        if self.params.get("proportional_scale", True):
            s = random.uniform(*self.params["scale_rangeX"])
            inst.scale = rt.point3(s, s, s)
        else:
            sx = random.uniform(*self.params["scale_rangeX"])
            sy = random.uniform(*self.params["scale_rangeY"])
            sz = random.uniform(*self.params["scale_rangeZ"])
            inst.scale = rt.point3(sx, sy, sz)

        # Apply rotation
        rx = random.uniform(*self.params["rot_x_range"])
        ry = random.uniform(*self.params["rot_y_range"])
        rz = random.uniform(*self.params["rot_z_range"])
        
        rt.rotate(inst, rt.eulerAngles(rx, ry, rz))
    
    def scatter_spline(self,source_obj):
        self.clear_instances(delete_nodes=True)
        if not rt.isValidNode(self.spline):
            print("ERROR: invalid spline target.")
            return 

        shape = self.spline
        spline_index = 1
        curve_length = rt.execute(f"curveLength ${shape.name}")

        if curve_length == 0:
            print("ERROR: Spline length is 0.")
            return

        is_closed = rt.isClosed(shape, spline_index)
        count = self.params["count"]
        distance = self.params["distance"]


        if count is not None:
            instance_count = count
        else:
            if distance is None or distance <= 0:
                return
            instance_count = int(curve_length // distance) + 1

        param_range = instance_count if is_closed else instance_count - 1

        for i in range(instance_count):
            param = i / float(param_range)
            pos = rt.pathInterp(shape, spline_index, param)
            tangent = rt.normalize(rt.pathTangent(shape, spline_index, param))

            #add a random source object from the list
            
            if hasattr(self,'manager') and self.manager.get_all():
                source_obj = self.manager.get_random()
            if not source_obj:
                print("ERROR: No source object available.")
                return

            # Add jitter
            jitter = rt.point3(
                random.uniform(-self.params["pos_jitter"].x, self.params["pos_jitter"].x),
                random.uniform(-self.params["pos_jitter"].y, self.params["pos_jitter"].y),
                random.uniform(-self.params["pos_jitter"].z, self.params["pos_jitter"].z),
            )
            final_pos = pos + jitter

            # Build local coordinate system
            x_axis = tangent
            z_axis = rt.point3(0, 0, 1)
            y_axis = rt.normalize(rt.cross(z_axis, x_axis))
            z_axis = rt.normalize(rt.cross(x_axis, y_axis))
            base_tm = rt.matrix3(x_axis, y_axis, z_axis, final_pos)

            # Create instance and assign transform
            inst = rt.instance(source_obj)
            inst.transform = base_tm
            inst.parent = self.controller
            self.layer.addNode(inst)

            self.apply_random_scale_and_rotation(inst)
            self.instances.append(ScatterInstance(inst))
            # Reset controllers to avoid unexpected behavior
            inst.pos.controller = rt.Position_XYZ()
            inst.rotation.controller = rt.Euler_XYZ()

        print(f"✅ {instance_count} instances of '{source_obj.name}' were created along the spline.")

    def scatter_surface(self,source_obj):
        self.clear_instances(delete_nodes=True)

        if not (rt.isValidNode(source_obj) and rt.isValidNode(self.surface)):
            print("ERROR: Select a source object and Editable Poly surface.")
            return
        
        if not rt.classof(self.surface) == rt.Editable_Poly:
            try:
                self.surface = rt.convertToPoly(self.surface)
                print(f"DEBUG: Converted: {self.surface.name} to Editable Poly.")
            except Exception as e:
                print(f"ERROR: Failed to convert surface to Editable Poly. {e}")
                return
        
        count = self.params.get("count")
        if count is None:
            print("DEBUG: 'count' parameter is not defined. Scatter aborted.") #DEBUG
            return
        
        #determinate bounding box limit(surface)
        bb_min, bb_max = rt.nodeGetBoundingBox(self.surface, rt.matrix3(1))
        
        #determinate bounding box limit(object)

        source_bb_min, source_bb_max = rt.nodeGetBoundingBox(source_obj, rt.matrix3(1))
        source_size = source_bb_max - source_bb_min
        separation = max(source_size.x, source_size.y)

        #Get the mesh to access your faces
        mesh = rt.snapshotAsMesh(self.surface)
        face_count = mesh.numfaces

    
        created = 0
        attempts = 0
        count = self.params["count"]
        max_attempts = count * 10  # To avoid infinite loop if intersections fail
        placed_points = []

        while created < count and attempts < max_attempts:
            attempts += 1

            # Random point in the Bounding Box
            rand_x = random.uniform(bb_min.x, bb_max.x)
            rand_y = random.uniform(bb_min.y, bb_max.y)
            rand_z = random.uniform(bb_min.z, bb_max.z)
            candidate = rt.point3(rand_x, rand_y, rand_z)

            # check if the object is very close to each other
            if any(rt.length(candidate - self.params) < separation for self.params in placed_points):
                continue

            for i in range(1, face_count + 1):
                try:
                    indices = rt.getFace(mesh, i)  # tupla con 3 índices
                    verts = [rt.getVert(mesh, indices[j]) for j in range(3)]
                    v0, v1, v2 = verts

                    def same_side(p1, p2, a, b):
                        cp1 = rt.cross(b - a, p1 - a)
                        cp2 = rt.cross(b - a, p2 - a)
                        return rt.dot(cp1,cp2) >= 0

                    inside = (
                        same_side(candidate, v0, v1, v2) and
                        same_side(candidate, v1, v0, v2) and
                        same_side(candidate, v2, v0, v1)
                    )

                    if inside:
                        #get a random source object from the list
                        random_source = self.manager.get_random() if hasattr(self,'manager') and self.manager.get_all() else source_obj
                        #create instance
                        inst = rt.instance(random_source)
                        inst.position = candidate
                        inst.parent = self.controller
                        self.layer.addNode(inst)

                        self.apply_random_scale_and_rotation(inst)
                        self.instances.append(ScatterInstance(inst))
                        created += 1
                        break
                except Exception as e:
                    print(f"Error on face {i}: {e}")
        if created<count:
            print(f"surface is too small to create{count},were just created {created} along the surface.")
        elif count==created:
            print(f"{count} instances of '{source_obj.name}' were created along the surface.")

#manage multiple scatter groups

class ScatterTool:
    def __init__(self):
        self.groups = []
        self._load_existing_groups()

    def _load_existing_groups(self):
        """Load existing scatter groups from the scene based on naming convention."""
        for obj in rt.objects:
            if obj.name.endswith("_CTRL") and rt.isValidNode(obj): # Check if it's a valid node
                group_name = rt.getUserProp(obj, "ScatterGroup") 
                if group_name:# Check if user property exists
                    # Check if group already loaded
                    g = ScatterGroup.__new__(ScatterGroup)  # crea instancia vacía
                    g.name = group_name
                    g.target = None
                    g.controller = obj
                    g.layer = rt.LayerManager.getLayerFromName(group_name)
                    g.instances = []
                    g.manager = ElementsManager()
                    g.params = {
                    "count": None,
                    "distance": None,
                    "pos_jitter": rt.point3(0,0,0),
                    "scale_rangeX": (1.0,1.0),
                    "scale_rangeY": (1.0,1.0),
                    "scale_rangeZ": (1.0,1.0),
                    "rot_x_range": (0,0),
                    "rot_y_range": (0,0),
                    "rot_z_range": (0,0),
                    "proportional_scale": rt.getUserProp(obj,"ScatterProportionalScale")=="True",
                    "random": rt.getUserProp(obj,"ScatterRandom")=="True",
                    "viewport_percentage": int(rt.getUserProp(obj,"ScatterViewportPercentage") or 100)
                    }
                    elements = rt.getUserProp(obj, "ScatterElements")
                    if elements:
                        for name in elements.split(","):
                            node = rt.getNodeByName(name)
                            if rt.isValidNode(node):
                                g.manager.add(node)

                    # --- load target if exists ---
                    target_name = rt.getUserProp(obj, "ScatterTarget")
                    if target_name:
                        target_node = rt.getNodeByName(target_name)
                        if rt.isValidNode(target_node):
                            g.target = target_node
                            #assign target to spline or surface
                            if rt.superClassOf(target_node) == rt.Shape:
                                g.spline = target_node
                            elif rt.isKindOf(target_node, rt.GeometryClass):
                                g.surface = target_node
                    self.groups.append(g)

                    print(f"DEBUG: Loaded existing group '{group_name}' from controller '{obj.name}'")

    def create_group(self, source_obj, target_obj, mode=None):
        if not (rt.isValidNode(source_obj) and rt.isValidNode(target_obj)):
            print("ERROR: Scatter group must be valid.")
            return None
        
        #create a new group with unique name
        group_name = f"Scatter_{len(self.groups)+1:03d}"
        new_group = ScatterGroup(group_name)

        new_group._setup_group_in_scene(target_obj)
        if mode == "spline":
            new_group.set_spline(target_obj)
            new_group.scatter_spline(source_obj)
        else:
            new_group.set_surface(target_obj)
            new_group.scatter_surface(source_obj)
        
        self.groups.append(new_group)
        print(f"✅ Created new group '{group_name}' with mode '{mode}'")
        return new_group
    
    def get_group_by_selection(self):
        
        sel =list(rt.selection)
        if not sel:
            print("ERROR: No objects selected in the scene.")
            return None

        obj = sel[0]
        return self.get_group_by_controller(obj)

    def get_group(self, name):
        for g in self.groups:
            if g.name == name:
                return g
        return None
    
    def get_group_by_controller(self, obj):
        for g in self.groups:
            if rt.isValidNode(g.controller):
                if g.controller == obj or obj.parent == g.controller:
                    print(f"DEBUG: Found group '{g.name}' by {obj.name}")
                    return g
        return None
    