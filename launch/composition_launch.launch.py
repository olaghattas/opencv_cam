"""
Dynamically compose OpencvCamNode and ImageSubscriberNode in a component_container.

Limitations of this container:
 -- stdout is not set to flush after each line, so the most recent log messages may be delayed
"""

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():

    camera_info_path = "/home/pose_detection/src/opencv_cam/config/camera_parameter.ini"

    container = ComposableNodeContainer(
        name='my_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='opencv_cam',
                plugin='opencv_cam::OpencvCamNode',
                name='image_publisher_1',
                parameters=[{
                    'file': False,
                    'index': 0, # device /dev/video_index
                    'camera_info_path': camera_info_path,
                    'camera_frame_id': 'cam_0',
                    'camera_info_topic': "camera_0/color/camera_info",
                    'camera_topic': "camera_0/color/image_raw",

                }],
                extra_arguments=[{'use_intra_process_comms': True}],
            ),
            ComposableNode(
                package='opencv_cam',
                plugin='opencv_cam::OpencvCamNode',
                name='image_publisher_2',
                parameters=[{
                    'file': False,
                    'index': 1, # device /dev/video_index
                    'camera_info_path': '/home/pose_detection/src/opencv_cam/config/camera_parameter.ini',
                    'camera_frame_id': 'cam_1',
                    'camera_info_topic': "camera_1/color/camera_info",
                    'camera_topic': "camera_1/color/image_raw",

                }],
                extra_arguments=[{'use_intra_process_comms': True}],
            ),

        ],
        output='screen',
    )

    return launch.LaunchDescription([container])
