from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(
            package="ras_topics",
            executable="ras_publisher",
            name="my_example",
            output="screen",
            parameters=[{'battery_level': 0.00001}]
        ),
        Node(
            package="turtlesim",
            executable="turtlesim_node",
            name="tortuga",
            output="screen"
        )
    ])
