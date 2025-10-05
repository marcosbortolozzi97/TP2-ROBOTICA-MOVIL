import re

# Abrimos el archivo original
with open("log.txt") as f_in, open("log_carga.txt", "w") as f_out:
    # Escribimos encabezado
    f_out.write(" time_seg \ttime_nseg \tx \ty \tyaw \tv_lin \tv_ang\n")

    for line in f_in:
        # Extraer todos los números de la línea
        nums = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        if len(nums) >= 6:
            # Tomamos solo los 6 primeros (por si aparecen más)
            row = nums[:7]
            # Escribirlos separados por tabulación
            f_out.write("\t".join(row) + "\n")
