# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from snake_capa_msg.msg import Capa
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import serial
import time

# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

class MapCapaCam(Node):

    def __init__(self):
        super().__init__('CapaCam_mapper')
        self.subscription = self.create_subscription(
            Capa,
            'capa_sensor',
            self.mapper_listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def mapper_listener_callback(self, msg):
        capa0_val = msg.capa0
        capa1_val = msg.capa1
        capa2_val = msg.capa2
        print(capa0_val, capa1_val, capa2_val)


def main(args=None):
    rclpy.init(args=args)

    Capa_cam = MapCapaCam()

    rclpy.spin(Capa_cam)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    Capa_cam.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
