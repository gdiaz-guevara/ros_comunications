import rclpy
from std_msgs.msg import String
import socket

def connect_to_esp32():
    global esp32 
    esp32 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    esp32.connect(("10.145.150.175",8080))

def timer_callback():
    global pub, esp32
    msg = String()
    msg.data = esp32.recv(1024).decode('utf-8').strip()
    if msg.data:
        pub.publish(msg)

def main():
    global pub
    rclpy.init()
    node = rclpy.create_node('wifi_receiver')
    pub = node.create_publisher(String, 'wifi/receiver', 10)
    connect_to_esp32()
    node.create_timer(1.0, timer_callback)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
