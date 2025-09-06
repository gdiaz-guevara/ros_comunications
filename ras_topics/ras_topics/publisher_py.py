import rclpy
from std_msgs.msg import String
import time

def main():
    rclpy.init()
    node = rclpy.create_node('simple_string_publisher')
    pub = node.create_publisher(String, 'chatter', 10)
    i = 0
    while rclpy.ok():
        msg = String()
        msg.data = f'Hello ROS 2 Jazzy! Count: {i}'
        pub.publish(msg)
        node.get_logger().info(f'Published: "{msg.data}"')
        time.sleep(0.5)
        i +=1
    node.destroy_node()
    rclpy.shutdown()