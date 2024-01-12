# import rospy
# from geometry_msgs.msg import PoseStamped, Pose
# from std_msgs.msg import String


# def startup():
#     rospy.init_node('robot_control_node', anonymous=True)

#     robot_status_publisher = rospy.Publisher('/robot_status', String, queue_size=10)
#     rospy.sleep(1)
#     robot_status_publisher.publish(String('idle'))


# def move_to_goal(room):
#     pose = room['Pose']
#     position = pose['position']
#     orientation = pose['orientation']
#     x = position['x']
#     y = position['y']
#     z = orientation['z']
#     w = orientation['w']
#     # Call move_to_goal of Team Navigation and pass x, y, z, w
#     goal_coordinates = PoseStamped()
#     goal_coordinates.pose.position.x = x
#     goal_coordinates.pose.position.y = y
#     goal_coordinates.pose.orientation.z = z
#     goal_coordinates.pose.orientation.w = w

#     goal_coordinates_publisher = rospy.Publisher('/goal_coordinates', PoseStamped, queue_size=10)
#     rospy.sleep(1)
#     goal_coordinates_publisher.publish(goal_coordinates)

#     # Send status update to app
#     robot_status_publisher = rospy.Publisher('/robot_status', String, queue_size=10)
#     rospy.sleep(1)
#     robot_status_publisher.publish(String('delivering'))


# def goal_reached():
#     robot_status_publisher = rospy.Publisher('/robot_status', String, queue_size=10)
#     rospy.sleep(1)
#     robot_status_publisher.publish(String('goal reached'))