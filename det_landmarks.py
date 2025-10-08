import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker, MarkerArray
import math

# Se crea un nodo llamado 'det_landmarks'
class LandmarkDetector(Node):
    def __init__(self):
        super().__init__('det_landmarks')
        self.sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10) # Se suscribe al tópico /scan
        self.pub = self.create_publisher(MarkerArray, '/landmarks', 10) # Se publicará en el tópico /landmarks

    # Se procesan los datos del lidar
    def scan_callback(self, msg):
        # Distancias medidas por el laser, donde se mide el recorrido en angulos que ocupa cada cilindro
        ranges = msg.ranges
        angle_min = msg.angle_min
        angle_increment = msg.angle_increment

        clusters = [] # se guardan los puntos no infinitos que escanéa el láser
        current_cluster = []

        # Thresholds
        dist_thresh = 0.25   # distancia máx entre puntos del mismo cluster
        min_points = 4      # mínimo de puntos para aceptar un cluster

        prev_x, prev_y = None, None
        # Se recorren los valores del lidar y se descartan las lecturas que no interesan
        for i, r in enumerate(ranges):
            if math.isinf(r) or r <= 0.01 or r > 10.00:
                continue

            # Se convierte a coordenadas cartesianas
            angle = angle_min + i * angle_increment
            x = r * math.cos(angle)
            y = r * math.sin(angle)

            # Se van agrupando en distintos grupos cluster segun la cercanía de los puntos
            if prev_x is not None:
                d = math.sqrt((x - prev_x)**2 + (y - prev_y)**2)
                if d > dist_thresh and len(current_cluster) >= min_points:
                    clusters.append(current_cluster)
                    current_cluster = []

            current_cluster.append((x, y))
            prev_x, prev_y = x, y

        # Se guardan los cluster
        if len(current_cluster) >= min_points:
            clusters.append(current_cluster)

        # Calcular centroides de los clusters
        markers = MarkerArray()
        for i, cluster in enumerate(clusters):
            cx = sum(p[0] for p in cluster) / len(cluster)
            cy = sum(p[1] for p in cluster) / len(cluster)

            # Se define un Marker tipo CYLINDER en el frame del robot, para visualizar como marcadores cuyo frame id es base_link (importante al configurar en RViz)
            marker = Marker()
            marker.header.frame_id = "base_link"
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.id = i
            marker.type = Marker.CYLINDER
            marker.action = Marker.ADD
            marker.pose.position.x = cx
            marker.pose.position.y = cy
            marker.pose.position.z = 0.5
            marker.pose.orientation.w = 1.0
            # Se definen las características aproximadas segun fue creado en el simulador
            marker.scale.x = 0.3
            marker.scale.y = 0.3
            marker.scale.z = 1.0
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.color.a = 0.8
            markers.markers.append(marker)

        # Se hacen las publicaciones en el tópico /landamarks
        self.pub.publish(markers)
        self.get_logger().info(f"Detectados {len(clusters)} landmarks")

# Se define para que la clase LandmarkDetector pueda ejecutarse como nodo de ROS 2 independiente.
def main():
    rclpy.init()
    node = LandmarkDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

