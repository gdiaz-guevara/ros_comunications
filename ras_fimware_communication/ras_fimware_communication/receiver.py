import rclpy
import serial
from std_msgs.msg import String

global arduino, node
def timer_callback():
    global arduino, node, pub
    if rclpy.ok() and arduino.is_open:
        data = arduino.readline().decode('utf-8').strip()
        msg = String()
        msg.data = str(data)
        pub.publish(msg)


def init_serial():
    global arduino, node
    port = node.get_parameter('port').value
    baud_rate = node.get_parameter('baud_rate').value
    arduino = serial.Serial(port, baud_rate, timeout=1.0)

def main(args=None):
    global node, pub
    rclpy.init(args=args)
    node = rclpy.create_node('serial_reciever')
    node.declare_parameter('port', '/dev/ttyACM0')
    node.declare_parameter('baud_rate', 9600)
    pub = node.create_publisher(String, 'transmitt_msg', 10)
    init_serial()
    node.create_timer(0.1, timer_callback)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
