def calcular_total_factura(cantidad_sin_igv, porcentaje_igv=18):
    total_igv = cantidad_sin_igv * (porcentaje_igv / 100)
    total_factura = cantidad_sin_igv + total_igv
    return total_factura
cantidad_sin_igv = 100
total_con_igv = calcular_total_factura(cantidad_sin_igv)
print("Total de la factura con IGV al 18%:", total_con_igv)

porcentaje_igv_personalizado = 20
total_con_igv_personalizado = calcular_total_factura(cantidad_sin_igv, porcentaje_igv_personalizado)
print("Total de la factura con IGV al 20%:", total_con_igv_personalizado)