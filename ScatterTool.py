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
