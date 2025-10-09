
## Ejercicio 4

- Se corre la simulación de desde la terminal para abrir gazebo con un espacio donde se encuentra el robot waffle pi a utilizar en un mundo vacío,  
&nbsp;&nbsp;ros2 launch tb3_empty_world tb3_simulation_launch.py headless:=False  
nota: el archivo tb3_simulation_launch.py se encuentra en la carpeta /launch dentro de tb3_empty_world en el paquete dev_ws.  
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
  

## Ejercicio 8

Primero debemos diseñar el mundo con los cilindros y el waffle pi dentro, se modificó el archivo que contenia el mundo vacío y lo llamamos 'Ejercicio_8.xacro'. El mismo se encuentra en la carpeta /worlds dentro de tb3_empty_world. Comenzamos modificando el archivo tb3_simulation_launch.py,  
&nbsp;&nbsp;world = '/home/marcos/dev_ws/src/tb3_empty_world/worlds/Ejercicio_8.xacro' (segun la ubicación de su directorio particular)  
  
Creamos un paquete para el nodo **det_landmark**,  
&nbsp;&nbsp; cd ~/dev_ws/src  
&nbsp;&nbsp;ros2 pkg create --build-type ament_python tb3_landmarks  
Dentro del directorio del paquete tb3_landmarks/tb3_landmarks/ agregamos el archivo **det_landmarks.py**.  
Verificamos que en el archivo **setup.py** el siguiente bloque de código sea:  
entry_points={  
&nbsp;&nbsp;&nbsp;&nbsp;'console_scripts': [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'det_landmarks = tb3_landmarks.det_landmarks:main',  
&nbsp;&nbsp;&nbsp;&nbsp;],  
},  
  
Ejecutamos como sigue:  
&nbsp;&nbsp;ros2 launch tb3_empty_world tb3_simulation_launch.py headless:=False &nbsp;&nbsp; ![Simulación](https://github.com/marcosbortolozzi97/TP2-ROBOTICA-MOVIL/issues/2#issuecomment-3383680011) (*)  
En otra terminal ejecutamos para lanzar el nodo:  
&nbsp;&nbsp;cd ~/dev_ws  
&nbsp;&nbsp;colcon build --packages-select tb3_landmarks  
&nbsp;&nbsp;source install/setup.bash  
&nbsp;&nbsp;ros2 run tb3_landmarks det_landmarks ![Publicación_Nodo](https://github.com/marcosbortolozzi97/TP2-ROBOTICA-MOVIL/issues/6)  
En una tercera terminal verificamos que el nodo det_landmarks está publicando:  
&nbsp;&nbsp;ros2 topic echo /landmarks ![Resultado_Tópico](https://github.com/marcosbortolozzi97/TP2-ROBOTICA-MOVIL/issues/5)  
  
En RViz (abierto junto con Gazebo, sino se lo debe abrir) debemos abrir dentro de la sección Displays **Global Options**, y en la solapa a la derecha de **Fixed Frame** elegimos **base_link** (y enter). Destildar la opción **LaserScan**. En caso de no estar, agregar (solapa add) desde **by display type** el display **MarkerArray**, y una vez presente en la sección Displays abrimos y elegimos el **Topic** en la solapa a la derecha **/landmarks** (y enter). Debería vizualizarse el centro de los cilindros como puntos verdes. ![Visualización_RViz](https://github.com/marcosbortolozzi97/TP2-ROBOTICA-MOVIL/issues/3#issuecomment-3383685327)  
  
(*)Si queremos verificar que el laser scan esta publicando informacion de la simulacion en Gazebo abrimos otra terminal y ejecutamos **ros2 topic echo /scan**.
