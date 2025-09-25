import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def add_two_ints_callback(request, response):
    response.sum = request.a + request.b
    print(f"Received request: {request.a} + {request.b} = {response.sum}")
    return response

def main():
    rclpy.init()
    node = Node("add_two_ints_server")
    srv = node.create_service(AddTwoInts, "add_two_ints", add_two_ints_callback)
    print("Service server ready: add_two_ints")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()