import rclpy
import serial
from std_msgs.msg import String

global arduino, node
def send_serial_callback(msg: String):
    global arduino, node
    print(f'send to arduino: {msg.data}')
    arduino.write(msg.data.encode('utf-8'))


def init_serial():
    global arduino, node
    port = node.get_parameter('port').value
    baud_rate = node.get_parameter('baud_rate').value
    arduino = serial.Serial(port, baud_rate, timeout=1.0)

def main(args=None):
    global node
    rclpy.init(args=args)
    node = rclpy.create_node('serial_transmitter')
    node.declare_parameter('port', '/dev/ttyACM0')
    node.declare_parameter('baud_rate', 9600)
    init_serial()
    node.create_subscription(String, 'receive_msg', send_serial_callback,10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
