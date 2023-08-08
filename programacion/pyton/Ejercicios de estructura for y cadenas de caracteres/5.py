def formatear_fecha(fecha):
    dia = fecha[0:2]
    mes = fecha[3:5]
    anio = fecha[6:10]
    fecha_formateada = anio + '-' + mes + '-' + dia
    return fecha_formateada

fecha = str(input("Ingrese una fecha"))
fecha_formateada = formatear_fecha(fecha)
print(fecha_formateada)
