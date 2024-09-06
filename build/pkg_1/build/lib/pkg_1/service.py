import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class service(Node):

    def __init__( self ) :
        super().__init__("service")   
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5 , self.timer_callback)
        self.gg=self.create_publisher(String, "topic",10)
    
    def timer_callback ( self ) :
        self.get_logger().info("Hello")


def main ( args = None ) :
    rclpy.init (args = args)
    node = service()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == " __main__ " :
    main ()