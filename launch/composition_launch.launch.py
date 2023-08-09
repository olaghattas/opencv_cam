"""
Dynamically compose OpencvCamNode and ImageSubscriberNode in a component_container.

Limitations of this container:
 -- stdout is not set to flush after each line, so the most recent log messages may be delayed
"""

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():

    camera_info_path = "/home/olagh/nano_cam_repo/src/opencv_cam/config/camera_parameter.ini"

    container = ComposableNodeContainer(
        name='my_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='opencv_cam',
                plugin='opencv_cam::OpencvCamNode',
                name='image_publisher',
                parameters=[{
                    'file': False,
                    'index': 2, # device /dev/video_index
                    'camera_info_path': camera_info_path,
                    'camera_frame_id': 'ola',
                    'camera_info_topic': "camera/color/camerarte_info",
                    'camera_topic': "camera/color/image_rdfgdfgdfaw",

                }],
                extra_arguments=[{'use_intra_process_comms': True}],
            ),
            ComposableNode(
                package='opencv_cam',
                plugin='opencv_cam::OpencvCamNode',
                name='image_publisher',
                parameters=[{
                    'file': False,
                    'index': 0, # device /dev/video_index
                    'camera_info_path': camera_info_path,
                    'camera_frame_id': 'newola',
                    'camera_info_topic': "new/safasdfcolor/camerarte_info",
                    'camera_topic': "new/coloccccr/image_rdfgdfgdfaw",

                }],
                extra_arguments=[{'use_intra_process_comms': True}],
            ),

        ],
        output='screen',
    )

    return launch.LaunchDescription([container])
