import pymxs
import random

rt = pymxs.runtime

def scatter_along_spline_distance(source_obj, spline_obj,
                                  distance=20.0,
                                  count=None,
                                  pos_jitter=rt.point3(5, 5, 0),
                                  scale_range=(0.8, 1.2),
                                  rot_x=False,
                                  rot_y=False,
                                  rot_z=True):
    if not (rt.isValidNode(source_obj) and rt.isValidNode(spline_obj)):
        print("ERROR: Select a spline first and the mesh second.")
        return

    shape = spline_obj
    spline_index = 1
    curve_length = rt.execute(f"curveLength ${shape.name}")

    if curve_length == 0:
        print("ERROR: Spline length is 0.")
        return

    is_closed = rt.isClosed(shape, spline_index)

    if count is not None:
        instance_count = count
    else:
        instance_count = int(curve_length // distance) + 1

    param_range = instance_count if is_closed else instance_count - 1

    for i in range(instance_count):
        param = i / float(param_range)
        pos = rt.pathInterp(shape, spline_index, param)
        tangent = rt.normalize(rt.pathTangent(shape, spline_index, param))

        # Add jitter
        jitter_x = random.uniform(-pos_jitter.x, pos_jitter.x)
        jitter_y = random.uniform(-pos_jitter.y, pos_jitter.y)
        jitter = rt.point3(jitter_x, jitter_y, 0)
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

        # Apply uniform scale
        s = random.uniform(*scale_range)
        inst.scale = rt.point3(s, s, s)

        # Apply local rotations conditionally
        if rot_x:
            angle_x = random.uniform(0, 360)
            rt.rotate(inst, rt.eulerAngles(angle_x, 0, 0))
        if rot_y:
            angle_y = random.uniform(0, 360)
            rt.rotate(inst, rt.eulerAngles(0, angle_y, 0))
        if rot_z:
            angle_z = random.uniform(0, 360)
            rt.rotate(inst, rt.eulerAngles(0, 0, angle_z))

    print(f"✅ {instance_count} instances of '{source_obj.name}' were created along the spline.")

def scatter_along_surface(source_obj, source_surface,
                                  count=50,
                                  scale_range=(0.8, 1.2),
                                  rot_x=False,
                                  rot_y=False,
                                  rot_z=True):
    if not (rt.isValidNode(source_obj) and rt.isValidNode(source_surface)):
        print("ERROR: Select a source object and Editable Poly surface second.")
        return
    if not rt.classof(source_surface) == rt.Editable_Poly:
        print("ERROR: Surface must be an Editable Poly object.")
        return
    
    #determinate bounding box limit(surface)
    bb_min, bb_max = rt.nodeGetBoundingBox(source_surface, rt.matrix3(1))

    #determinate bounding box limit(object)

    source_bb_min, source_bb_max = rt.nodeGetBoundingBox(source_obj, rt.matrix3(1))
    source_size = source_bb_max - source_bb_min
    separation = max(source_size.x, source_size.y)


    #Get the mesh to access your faces
    mesh = rt.snapshotAsMesh(source_surface)
    face_count = mesh.numfaces

    placed_points = []
    created = 0
    attempts = 0
    max_attempts = count * 10  # To avoid infinite loop if intersections fail

    while created < count and attempts < max_attempts:
        attempts += 1

        # Random point in the Bounding Box
        rand_x = random.uniform(bb_min.x, bb_max.x)
        rand_y = random.uniform(bb_min.y, bb_max.y)
        rand_z = bb_min.z
        candidate = rt.point3(rand_x, rand_y, rand_z)

        # check if the object is very close to each other
        if any(rt.length(candidate - p) < separation for p in placed_points):
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
                    # Apply uniform scale
                    s = random.uniform(*scale_range)
                    inst.scale = rt.point3(s, s, s)

                    # Apply local rotations conditionally
                    if rot_x:
                        angle_x = random.uniform(0, 360)
                        rt.rotate(inst, rt.eulerAngles(angle_x, 0, 0))
                    if rot_y:
                        angle_y = random.uniform(0, 360)
                        rt.rotate(inst, rt.eulerAngles(0, angle_y, 0))
                    if rot_z:
                        angle_z = random.uniform(0, 360)
                        rt.rotate(inst, rt.eulerAngles(0, 0, angle_z))
                    
                    placed_points.append(candidate)
                    created += 1
                    break
            except Exception as e:
                print(f"Error on facecara {i}: {e}")
    if created<count:
        print(f"surface is too small to create{count},were just created {created} along the surface.")
    elif count==created:
        print(f"{count} instances of '{source_obj.name}' were created along the surface.")