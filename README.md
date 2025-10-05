
## Ejercicio 4

- Se corre la simulación de desde la terminal para abrir gazebo con un espacio donde se encuentra el robot waffle pi a utilizar en un mundo vacío,  
&nbsp;&nbsp;ros2 launch tb3_empty_world tb3_simulation_launch.py headless:=False  
nota: el archivo tb3_simulation_launch.py se encuentra en la carpeta launch dentro de tb3_empty_world en el paquete dev_ws.  
- En otra pestaña de la terminal se ejecuta la teleoperación por teclado,  
&nbsp;&nbsp;ros2 run teleop_twist_keyboard teleop_twist_keyboard  
- Una vez puesto en moviemiento el robot en la simulación, en una nueva pestaña de la terminal se redirecciona la salida con los datos a un archivo,  
&nbsp;&nbsp; cd ~/dev_ws/src  
&nbsp;&nbsp;./dump_odom.py > log.txt  

## Ejercicio 5

- En el directorio donde se generó el archivo log.txt se implementa un script que reordena los datos del mismo para generar una lectuta mas ordenada,  
&nbsp;&nbsp; python3 Reordenar_5.py  
- Con el script anterior se genera un archivo log_carga.txt que es el que utilizaremos para realizar las gráficas,  
&nbsp;&nbsp;python3 Ejercicio_5.py  

## Ejercicio 6

La ejecución corresponde al mismo procedimiento utilizado en los ejecicios 4 y 5, solo se modifican nombres de archivos y scripts,
&nbsp;&nbsp;ros2 launch tb3_empty_world tb3_simulation_launch.py headless:=False  
&nbsp;&nbsp;ros2 run teleop_twist_keyboard teleop_twist_keyboard  
&nbsp;&nbsp; cd ~/dev_ws/src  
&nbsp;&nbsp;./dump_odom.py > log_Circulo.txt  
&nbsp;&nbsp; python3 Reordenar_6.py  
&nbsp;&nbsp;python3 Ejercicio_6.py  
  

## Ejercicio 7

La 

