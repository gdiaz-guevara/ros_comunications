import rclpy
from std_msgs.msg import String
import socket

def connect_to_esp32():
    global esp32 
    esp32 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    esp32.connect(("10.145.150.175",8080))

def message_callback(msg: String):
    global esp32
    esp32.send(msg.data.encode('utf-8'))

def main():
    global esp32
    rclpy.init()
    node = rclpy.create_node('wifi_transmitter')
    node.create_subscription(String, 'wifi/transmitter', message_callback, 10)
    connect_to_esp32()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()