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
    spline_index = 1  # first spline
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
    
    instances = []

    for i in range(instance_count):
        param = i / float(param_range)
        pos = rt.pathInterp(spline_obj, 1, param)

        # Solo añade jitter si pos_jitter es distinto de cero
        jitter_x = random.uniform(-pos_jitter.x, pos_jitter.x) if pos_jitter.x != 0 else 0
        jitter_y = random.uniform(-pos_jitter.y, pos_jitter.y) if pos_jitter.y != 0 else 0
        jitter = rt.point3(jitter_x, jitter_y, 0)
        final_pos = pos + jitter

        inst = rt.instance(source_obj)
        inst.position = final_pos

        s = random.uniform(*scale_range)
        inst.scale = rt.point3(s, s, s)

        instances.append(inst)
        for inst in instances:
            rot_x_angle = random.uniform(0, 360) if rot_x else 0
            rot_y_angle = random.uniform(0, 360) if rot_y else 0
            rot_z_angle = random.uniform(0, 360) if rot_z else 0

            euler_rot = rt.eulerAngles(rot_x_angle, rot_y_angle, rot_z_angle)
            inst.rotation = rt.quat(euler_rot)

    print(f"✅ {instance_count} instances of '{source_obj.name}' were created along the spline.")