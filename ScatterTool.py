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
    def __init__(self, node,normal=None):
        self.node = node
        self.normal = normal
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

    def __init__(self,name,surface=None,spline=None,painter=None):
        self.name = name
        self.spline=spline
        self.surface=surface
        self.painter=painter
        self.instances = []
        self.controller=None #dummy for future use
        self.layer=None #layer for the groups
        self.params = {
            "count": None,
            "distance": None,
            "brush_size":None,
            "collision_enabled":None,
            "pos_jitterX": (-0.0, 0.0),
            "pos_jitterY": (-0.0, 0.0),
            "pos_jitterZ": (-0.0, 0.0),
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
            self.controller.wirecolor = rt.color(random.randint(80, 220),  # R
                                                random.randint(80, 220),  # G
                                                random.randint(80, 220)   # B
                                                )
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

    def shuffle_instances(self):
        children = self.controller.children
        if not children:
            print(f"DEBUG: No children found for '{self.name}'.")
            return

        child_count = len(children)
        if child_count == 0:
            return

        children= [c for c in self.controller.children if rt.isValidNode(c)]
        if not children:
            print(f"DEBUG: No valid children found for '{self.name}'.")
            return
        sources = [s for s in self.manager.get_all() if rt.isValidNode(s)]
        if not sources:
            print(f"DEBUG: No hay objetos fuente válidos para mezclar en '{self.name}'.")
            return

        for child in children:
            src= random.choice(sources)
            try:
                child.baseObject = src.baseObject
            except Exception as e:
                print(f"ERROR: Failed to assign new source to '{child.name}'. {e}")

        print(f"DEBUG: Shuffled positions of all children of '{self.name}'")
    

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
                random.uniform(*(self.params["pos_jitterX"])),
                random.uniform(*(self.params["pos_jitterY"])),
                random.uniform(*(self.params["pos_jitterZ"])),
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
        
        #Get the mesh to access your faces
        mesh = rt.snapshotAsMesh(self.surface)
        face_count = mesh.numfaces
    
        created = 0
        attempts = 0
        max_attempts = count * 10  # To avoid infinite loop if intersections fail
        placed_points = []

        collision= self.params.get("check_collisions", False)
        min_distance_factor= (self.ui.spinBox_colRadius.value()/100) if collision else 0.0

        while created < count and attempts < max_attempts:
            attempts += 1

            # Random point in the Bounding Box
            rand_x = random.uniform(bb_min.x, bb_max.x)
            rand_y = random.uniform(bb_min.y, bb_max.y)
            rand_z = random.uniform(bb_min.z, bb_max.z)
            candidate = rt.point3(rand_x, rand_y, rand_z)

            # check if the object is very close to each other
            if collision and self.check_collisions(candidate, placed_points, source_obj, min_distance_factor):
                continue

            for i in range(1, face_count + 1):
                try:
                    indices = rt.getFace(mesh, i)  # tupla con 3 índices
                    verts = [rt.getVert(mesh, indices[j]) for j in range(3)]
                    v0, v1, v2 = verts
                    print(f"DEBUG-Normals: Face {i} vertices: {v0}, {v1}, {v2}")

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
                        #get normal on surface face for orientation
                        face_normal = rt.getFaceNormal(mesh, i)
                        if not face_normal:
                            print(f"ERROR-Normal: getFaceNormal returned None for face {i}")
                            continue
                        face_normal = rt.normalize(face_normal)
                        print(f"DEBUG-Normal: Face {i} normal: {face_normal}")
                        #create instance
                        inst = rt.instance(random_source)
                        inst.position = candidate
                        inst.parent = self.controller
                        self.layer.addNode(inst)

                        self.apply_random_scale_and_rotation(inst)
                        
                        #store normal on each instance for future orientation adjustments
                        self.instances.append(ScatterInstance(inst, normal=face_normal))
                        created += 1

                        # store tuple (position, source) so collision checks can use source bbox
                        placed_points.append((candidate, random_source))
                        break
                except Exception as e:
                    print(f"Error on face {i}: {e}")
        if created<count:
            print(f"surface is too small to create{count},were just created {created} along the surface.")
        elif count==created:
            print(f"{count} instances of '{source_obj.name}' were created along the surface.")


    def scatter_painter(self, brush_position, brush_radius, density=5):

        """Scatter multiple source objects inside a brush circle on the surface."""

        if not (self.manager and self.manager.get_all() and rt.isValidNode(self.surface)):
            print("ERROR: No valid surface or source objects.")
            return

        mesh = rt.snapshotAsMesh(self.surface)
        face_count = mesh.numfaces
        placed_points = []

        created = 0
        attempts = 0
        max_attempts = density * 10

        while created < density and attempts < max_attempts:
            attempts += 1

            # Random point inside brush circle
            angle = random.uniform(0, 2 * 3.14159)
            radius = random.uniform(0, brush_radius)
            offset = rt.point3(
                radius * rt.cos(angle),
                radius * rt.sin(angle),
                0
            )
            candidate = brush_position + offset

            #check collisions
            if getattr(self, "collision_enabled", False) and self.check_collisions(candidate, placed_points, self.manager.get_random()):
                continue

            # Check which face contains the candidate point
            for i in range(1, face_count + 1):
                try:
                    indices = rt.getFace(mesh, i)
                    verts = [rt.getVert(mesh, indices[j]) for j in range(3)]
                    v0, v1, v2 = verts

                    def same_side(p1, p2, a, b):
                        cp1 = rt.cross(b - a, p1 - a)
                        cp2 = rt.cross(b - a, p2 - a)
                        return rt.dot(cp1, cp2) >= 0

                    inside = (
                        same_side(candidate, v0, v1, v2) and
                        same_side(candidate, v1, v0, v2) and
                        same_side(candidate, v2, v0, v1)
                    )

                    if inside:
                    # get a random source object from the list
                        source_obj = self.manager.get_random()
                        if not source_obj:
                            continue

                        # Create instance
                        inst = rt.instance(source_obj)
                        inst.position = candidate

                        # Calculate normal for orientation
                        normal = rt.normalize(rt.cross(v1 - v0, v2 - v0))
                        z_axis = normal
                        x_axis = rt.normalize(rt.cross(rt.point3(0,1,0), z_axis))
                        y_axis = rt.normalize(rt.cross(z_axis, x_axis))
                        inst.transform = rt.matrix3(x_axis, y_axis, z_axis, candidate)

                        inst.parent = self.controller
                        self.layer.addNode(inst)
                        self.apply_random_scale_and_rotation(inst)
                        self.instances.append(ScatterInstance(inst))
                        placed_points.append((candidate, source_obj))
                        created += 1
                        break
                except Exception as e:
                    print(f"Error on face {i}: {e}")
                    
    def check_collisions(self, candidate, placed_points, obj, min_distance_factor=1.0):
        # Return True if candidate collides (too close) with any placed point.
        bb_min, bb_max = rt.nodeGetBoundingBox(obj, rt.matrix3(1))
        size = bb_max - bb_min
        separation = max(size.x, size.y, size.z) * min_distance_factor

        for entry in placed_points:
            # placed_points is expected to contain tuples (pt, placed_obj); fall back if only points are present.
            if isinstance(entry, tuple) and len(entry) == 2:
                pt, placed_obj = entry
            else:
                pt = entry
                placed_obj = None

            # calculate distance between candidate and existing point
            dist = rt.length(candidate - pt)

            # get placed object's bbox-based separation if available
            if placed_obj and rt.isValidNode(placed_obj):
                bb_min2, bb_max2 = rt.nodeGetBoundingBox(placed_obj, rt.matrix3(1))
                size2 = bb_max2 - bb_min2
                separation2 = max(size2.x, size2.y, size2.z)
            else:
                separation2 = 0.0

            if dist < max(separation, separation2):
                return True
        return False
    
    def normal_direction(self,slider_value):
        print("DEBUG: funtion normal_direction start.")
    
    
        """Update orientation of instances based on slider value."""    
         
        slider_value = int(slider_value)
        # 2️⃣ Guardar valor actual para otros procesos
        self.params["direction_value"] = slider_value

        # 3️⃣ Normalizar valor a rango [-1, 1]
        s = max(-100, min(100, slider_value)) / 100.0

        # 4️⃣ Vectores base
        Z_UP = rt.point3(0, 0, 1)
        NEG_Z_UP = -Z_UP

        # 5️⃣ Verificar que existan instancias
        if not hasattr(self, "instances") or not self.instances:
            print("DEBUG: No instances to update orientation.")
            return

        # 6️⃣ Recorrer todas las instancias del scatter

        for idx, inst_data in enumerate(self.instances):
            inst = inst_data.node if hasattr(inst_data, "node") else inst_data.get("node")
            face_normal = inst_data.normal if hasattr(inst_data, "normal") else inst_data.get("normal")

            if not rt.isValidNode(inst):
                print(f"DEBUG: Instance {idx} is not valid.")
                continue

            n = rt.normalize(face_normal) if face_normal else rt.point3(0, 0, 1)
            print(f"DEBUG: Instance {idx} original normal: {face_normal}, normalized: {n}")

            # calcular vector z_axis
            s = max(-1.0, min(1.0, slider_value / 100.0))
            if s >= 0:
                alpha = s
                z_axis = rt.normalize((n * (1 - alpha)) + (rt.point3(0, 0, 1) * alpha))
            else:
                alpha = -s
                z_axis = rt.normalize((n * (1 - alpha)) + (rt.point3(0, 0, -1) * alpha))
            print(f"DEBUG: Instance {idx} z_axis after slider adjustment: {z_axis}")

            # sistema ortogonal
            up_ref = rt.point3(0, 1, 0)
            if abs(rt.dot(z_axis, up_ref)) > 0.99:
                up_ref = rt.point3(1, 0, 0)
            x_axis = rt.normalize(rt.cross(up_ref, z_axis))
            y_axis = rt.normalize(rt.cross(z_axis, x_axis))
            pos = inst.position
            inst.transform = rt.matrix3(x_axis, y_axis, z_axis, pos)



    
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
    
