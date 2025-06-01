import pymxs
import random
rt = pymxs.runtime

def scatter_along_spline(source_obj, spline_obj, count=20,
                          pos_jitter=rt.point3(10, 10, 0),
                          rot_range=(0, 360),
                          scale_range=(0.8, 1.2),
                          align_to_path=True):
    if not (rt.isValidNode(source_obj) and rt.isValidNode(spline_obj)):
        print("❌ Error: Objeto o spline no válidos.")
        return

    shape = spline_obj
    for i in range(count):
        param = i / float(count - 1)
        pos = rt.pathInterp(shape, 1, param)

        # Aleatoriedad en plano X-Y
        jitter = rt.point3(
            random.uniform(-pos_jitter.x, pos_jitter.x),
            random.uniform(-pos_jitter.y, pos_jitter.y),
            0
        )
        final_pos = pos + jitter

        # Instanciar objeto
        inst = rt.instance(source_obj)
        inst.position = final_pos

        if align_to_path:
            tangent = rt.normalize(rt.pathTangent(shape, 1, param))
            up = rt.point3(0, 0, 1)  # eje Z como 'up'
            right = rt.normalize(rt.cross(up, tangent))
            up = rt.cross(tangent, right)  # recalcular up ortogonal
            tm = rt.matrix3(right, up, tangent, final_pos)
            inst.transform = tm
        else:
            # Rotación aleatoria si no se alinea a la curva
            inst.rotation = rt.eulerAngles(
                random.uniform(*rot_range),
                random.uniform(*rot_range),
                random.uniform(*rot_range)
            )

        # Escala aleatoria
        s = random.uniform(*scale_range)
        inst.scale = rt.point3(s, s, s)

    print(f"✅ Se distribuyeron {count} instancias sobre la spline.")