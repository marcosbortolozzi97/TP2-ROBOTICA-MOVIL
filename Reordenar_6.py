import re

# Abrimos el archivo original
with open("log_Circulo.txt") as f_in, open("log_Circulo_carga.txt", "w") as f_out:
    # Escribimos encabezado
    f_out.write(" time_seg \ttime_nseg \t\tx \t\t\ty \t\t\tyaw \t\tv_lin \tv_ang\n")

    for line in f_in:
        # Extraer todos los números de la línea
        nums = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        if len(nums) >= 6:
            # Tomamos solo los 6 primeros (por si aparecen más)
            row = nums[:7]
            
            # Primeras dos columnas enteras, el resto con 6 decimales
            row_fmt = [row[0], row[1]] + [f"{float(val):.6f}" for val in row[2:]]

            # Escribir línea al archivo nuevo
            f_out.write("\t".join(row_fmt) + "\n")
