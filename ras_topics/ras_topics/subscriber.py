import rclpy
from std_msgs.msg import String

def callback_string(msg):
    print(f'I heard {msg.data}')

def main():
    rclpy.init()
    node = rclpy.create_node('ras_sbuscriber')
    #1 Crear subscriptor
    sub = node.create_subscription(String,'ras_msg_str', callback_string, 10)
    #2 evitar matar el node
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()