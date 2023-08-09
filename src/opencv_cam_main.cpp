#include "opencv_cam/opencv_cam_node.hpp"

// Launch OpencvCamNode with use_intra_process_comms=true

int main(int argc, char **argv)
{
  // Force flush of the stdout buffer
  setvbuf(stdout, NULL, _IONBF, BUFSIZ);

  // Init ROS
  rclcpp::init(argc, argv);

  // Create single-threaded executor
  rclcpp::executors::SingleThreadedExecutor executor;

  // Create and add camera node
  rclcpp::NodeOptions options{};
  options.use_intra_process_comms(true);

  std::vector<std::string> cam_names = {"camera_front", "camera_back"};
  std::vector<std::shared_ptr<opencv_cam::OpencvCamNode>> nodes;
  for (auto name : cam_names) {
      auto node = std::make_shared<opencv_cam::OpencvCamNode>(options, name, );
      executor.add_node(node);
      nodes.push_back(node);
  }
  // Spin until rclcpp::ok() returns false
  executor.spin();

  // Shut down ROS
  rclcpp::shutdown();

  return 0;
}
