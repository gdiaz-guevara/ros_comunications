import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main():
    rclpy.init()
    node = Node("add_two_ints_client")
    client = node.create_client(AddTwoInts, "add_two_ints")

    if not client.wait_for_service(timeout_sec=5.0):
        print("Service not available, exiting...")
        rclpy.shutdown()
        sys.exit(1)

    if len(sys.argv) != 3:
        print("Usage: ros2 run ras_services add_two_ints_client X Y")
        rclpy.shutdown()
        sys.exit(1)

    request = AddTwoInts.Request()
    request.a = int(sys.argv[1])
    request.b = int(sys.argv[2])

    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        print(f"Result: {request.a} + {request.b} = {future.result().sum}")
    else:
        print("Service call failed")

    rclpy.shutdown()

if __name__ == "__main__":
    main()