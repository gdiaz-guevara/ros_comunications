import rclpy
from std_msgs.msg import String

def callback(msg):
    print(f'I heard: {msg.data}')

def main():
    rclpy.init()
    node = rclpy.create_node('simple_string_subscriber')
    sub = node.create_subscription(String, 'chatter', callback, 10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()