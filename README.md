
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
- Se ejecuta  
    &nbsp;&nbsp;&nbsp;&nbsp;python nombre_archivo.py   ejemplo: python left_cam.py
- Cuando finalice la ejecucion o se quiera salir del modo virtual  
    &nbsp;&nbsp;&nbsp;&nbsp;deactivate  
    &nbsp;&nbsp;&nbsp;&nbsp;cd

## Nota

La ejecución de los scripts se corresponden con el enunciado de la siguiente manera  
&nbsp;&nbsp;&nbsp;&nbsp;a) left_cam.py  
&nbsp;&nbsp;&nbsp;&nbsp;b) left_cam_nanoprecision.py  
&nbsp;&nbsp;&nbsp;&nbsp;c) images_groundtruth.py
