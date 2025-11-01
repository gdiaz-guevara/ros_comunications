import rclpy
from std_msgs.msg import String
from ras_custom_interface.msg import RobotStatus

global node, pub, robot_name_param, battery_level_param, is_active_param, example
def callback_timer():
    global node, pub, robot_name_param, battery_level_param, is_active_param, example
            # 5 Crear cuerpo mensaje
    msg = RobotStatus()
    node.set_parameters([
        rclpy.Parameter('example',rclpy.Parameter.Type.INTEGER, 100),
        rclpy.Parameter('robot_name',rclpy.Parameter.Type.STRING, 'baxter')
    ])
    # 6 Llenar los campos del mensaje
    msg.name = node.get_parameter('robot_name').value
    msg.battery_level=node.get_parameter('battery_level').value
    msg.is_active=node.get_parameter('is_active').value
    # 7 Publicar el mensaje
    pub.publish(msg)

def main():
    global node, pub, robot_name_param, battery_level_param, is_active_param, example
    # 1 Crear comunicacion con ROS 2 
    rclpy.init()
    # 2 Crear nodo
    node = rclpy.create_node('ras_publisher')
    robot_name_param = node.declare_parameter('robot_name','davinci')
    battery_level_param = node.declare_parameter('battery_level',53.6)
    is_active_param = node.declare_parameter('is_active',True)
    example = node.declare_parameter('example', 1)
    # 3 Crear el publicador
    pub = node.create_publisher(RobotStatus, 'ras_msg_custom', 10)
    node.create_timer(0.5, callback_timer)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
