if selection.count < 2 then (
    format "❌ ERROR: Selecciona primero el objeto y luego el spline.\n"
) else (
    local source_obj = selection[1]
    local spline_obj = selection[2]

    format "🟡 Objeto fuente: %\n🟢 Spline: %\n" source_obj.name spline_obj.name

    local curve_length = 0

    try (
        curve_length = execute ("curveLength $" + spline_obj.name)
    )
    catch (
        format "❌ ERROR: No se pudo obtener la longitud de la spline.\n"
        return undefined
    )

    if curve_length == 0 then (
        format "❌ ERROR: La longitud de la spline es 0.\n"
        return undefined
    )

    local distance = 1000.0
    local instance_count = floor(curve_length / distance) + 1
    local param_range = instance_count - 1

    format "📏 Longitud spline: %\n" curve_length
    format "🔁 Número de instancias: %\n" instance_count

    -- Define el rango de escala mínima y máxima
    local scale_min = 0.8
    local scale_max = 1.2

    for i = 0 to instance_count - 1 do (
        local param = (i as float) / (param_range as float)
        local pos = pathInterp spline_obj 1 param

        format "📌 Instancia % - Posición: %\n" i pos

        local inst = instance source_obj
        inst.position = pos

        -- Rotación aleatoria solo en Z (0 a 360 grados)
        local rot_z = random 0 360
        inst.rotation = eulerangles 0 0 rot_z

        -- Escala aleatoria dentro del rango definido
        local s = random scale_min scale_max
        inst.scale = [s, s, s]
    )

    format "✅ % instancias creadas.\n" instance_count
)
