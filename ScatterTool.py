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
        print("[Cleared] All elements removed.")

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
    
    #
    def _setup_group_in_scene(self):
        # Dummy
        self.controller = rt.Point(name=f"{self.name}_CTRL")
        self.controller.size = 10
        self.controller.box = True
        self.controller.wirecolor = rt.color(255, 200, 0)

        # Layer
        self.layer = rt.LayerManager.newLayerFromName(self.name)
        self.layer.addNode(self.controller)
       # self.layer.isFrozen = True

    def clear_instances(self, delete_nodes=False):
        if delete_nodes:
            for inst in self.instances:
                if rt.isValidNode(inst.node):
                    rt.delete(inst.node)
        self.instances.clear()

    def set_spline(self, spline):
        self.spline = spline

    def set_surface(self, surface):
        self.surface = surface
        
    #clear instances
    def clear_instances(self, delete_nodes=False):
        if delete_nodes:
            for obj in self.instances:
                if rt.isValidNode(obj):
                    rt.delete(obj)
        self.instances.clear()

    #show instance as box
    def set_display_as_box(self,enable=True):
        for obj in self.instances:
            if rt.isValidNode(obj): 
                obj.displayAsBox = enable

    def apply_random_scale_and_rotation(self,inst):
            # Apply scale
            sx = random.uniform(*self.params["scale_rangeX"])
            sy = random.uniform(*self.params["scale_rangeY"])
            sz = random.uniform(*self.params["scale_rangeZ"])
            inst.scale = rt.point3(sx, sy, sz)

            rx = random.uniform(*self.params["rot_x_range"])
            ry = random.uniform(*self.params["rot_y_range"])
            rz = random.uniform(*self.params["rot_z_range"])
            # Apply rotations
            rt.rotate(inst, rt.eulerAngles(rx, ry, rz))
    
    def scatter_spline(self,source_obj):
        self.clear_instances(delete_nodes=True)
        if not (rt.isValidNode(source_obj) and rt.isValidNode(self.spline)):
            print("ERROR: Select a spline first and the mesh second.")
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
                print("⚠ ERROR: 'distance' is not set, cannot calculate instance_count.")
                return
            instance_count = int(curve_length // distance) + 1

        param_range = instance_count if is_closed else instance_count - 1

        for i in range(instance_count):
            param = i / float(param_range)
            pos = rt.pathInterp(shape, spline_index, param)
            tangent = rt.normalize(rt.pathTangent(shape, spline_index, param))

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
            self.layer.addNode(inst)
            inst.pos.controller = rt.Position_XYZ()
            inst.rotation.controller = rt.Euler_XYZ()

        print(f"✅ {instance_count} instances of '{source_obj.name}' were created along the spline.")

    def scatter_surface(self,source_obj):
        self.clear_instances(delete_nodes=True)
        print(f"DEBUG: NODES WAS CLEARED")#DEBUG
        if not (rt.isValidNode(source_obj) and rt.isValidNode(self.surface)):
            print("ERROR: Select a source object and Editable Poly surface second.")
            return
        if not rt.classof(self.surface) == rt.Editable_Poly:
            print("ERROR: Surface must be an Editable Poly object.")
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
                        inst = rt.instance(source_obj)
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

    def create_group(self, source_obj, target_obj, mode=None):
        if not (rt.isValidNode(source_obj) and rt.isValidNode(target_obj)):
            print("ERROR: Scatter group must be valid.")
            return None
        
        #create a new group with unique name
        group_name = f"Scatter_{len(self.groups)+1:03d}"
        new_group = ScatterGroup(group_name)

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

        for g in self.groups:
            if rt.isValidNode(g.controller) and g.controller == obj:
                return g

        print("No existing group found for selection.")
        return None

    def get_group(self, name):
        for g in self.groups:
            if g.name == name:
                return g
        return None

