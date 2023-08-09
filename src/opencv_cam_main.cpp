#include "opencv_cam/opencv_cam_node.hpp"

// Launch OpencvCamNode with use_intra_process_comms=true

int main(int argc, char **argv) {
    // Force flush of the stdout buffer
    setvbuf(stdout, NULL, _IONBF, BUFSIZ);

    // Init ROS
    rclcpp::init(argc, argv);

    // Create single-threaded executor
    rclcpp::executors::SingleThreadedExecutor executor;

    // Create and add camera node
    rclcpp::NodeOptions options{};
    options.use_intra_process_comms(true);

    std::vector <std::string> cam_names = {"camera_front", "camera_back"};
    std::string info_topic_name = "/camera/color_camera_info";

    std::vector <std::string> image_topic_name = {"camera/front", "camera/back"};
    std::vector <std::string> camera_frame_id = {"camera_front_", "camera_back_"};
    std::string camera_info_path = "/home/olagh/nano_cam_repo/src/opencv_cam/config/camera_parameter.ini";

    std::vector <std::shared_ptr<opencv_cam::OpencvCamNode>> nodes;

    for (size_t i = 0; i < cam_names.size(); ++i) {

        auto node = std::make_shared<opencv_cam::OpencvCamNode>(options, cam_names[i], image_topic_name[i],
                                                                info_topic_name,
                                                                camera_frame_id[i], camera_info_path);
        executor.add_node(node);
        nodes.push_back(node);
    }

    // Spin until rclcpp::ok() returns false
    executor.spin();

    // Shut down ROS
    rclcpp::shutdown();

    return 0;
}
