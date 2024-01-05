import time as t
from roslibpy import Ros, Topic, Message, Pose
from main import get_status

# 1. Verbindung zu TurtleBot
# Je nachdem welcher Turtlebot ausgewählt ist, soll roslibpy eine Verbindung zu ihm aufbauen
def connect_to_medibot(medibot="Medibot 1"):
    client = Ros(host='localhost', port=8765)
    if medibot == "Medibot 2":
        client = Ros(host='localhost', port=9090)
    if medibot == "Medibot 3":
        client = Ros(host='localhost', port=9091)
    return client

client = connect_to_medibot()
client.run()

topic_goal_coordinates = Topic(client, '/goal_coordinates', 'geometry_msgs/PoseStamped')
topic_robot_status = Topic(client, '/robot_status', 'std_msgs/String')
topic_robot_position = Topic(client, '/robot_position', 'geometry_msgs/Pose')

# 2. Roboter soll beladen werden und bei “Submit” zum gewählten Ziel fahren
# 4. Feedback: Turtlebot angekommen und abgeladen, soll wieder zurück zum Lager fahren
# 5. Feedback: Fehlermeldung, falls möglich auch wieder zurück zum Lager
# 2., 4. und 5.
def move_to_goal(target_room):
    room1 = {
        'header': {
            'seq': 2,
            'stamp': {
                t.secs: 1703250577,
                t.nsecs: 195683151
            },
            'frame_id': "map"
        },
        'pose': {
            'position': {
                'x': 0.4849998652935028,
                'y': 0.47999995946884155,
                'z': 0.0
            },
            'orientation': {
                'x': 0.0,
                'y': 0.0,
                'z': -0.7071067966408575,
                'w': 0.7071067657322372
            }
        }
    }

    room2 = {
        'header': {
            'seq': 5,
            'stamp': {
                t.secs: 1703250991,
                t.nsecs: 734503507
            },
            'frame_id': "map"
        },
        'pose': {
            'position': {
                'x': 4.590071678161621,
                'y': 0.6597763895988464,
                'z': 0.0
            },
            'orientation': {
                'x': 0.0,
                'y': 0.0,
                'z': -0.7048376094584169,
                'w': 0.709368694187264
            }
        }
    }

    room3 = {
        'header': {
            'seq': 4,
            'stamp': {
                t.secs: 1703250828,
                t.nsecs: 136227384
            },
            'frame_id': "map"
        },
        'pose': {
            'position': {
                'x': 4.016831874847412,
                'y': -1.9646360874176025,
                'z': 0.0
            },
            'orientation': {
                'x': 0.0,
                'y': 0.0,
                'z': 0.7145255477049307,
                'w': 0.6996093493350192
            }
        }
    }

    lager = {
        'header': {
            'seq': 3,
            'stamp': {
                t.secs: 1703250690,
                t.nsecs: 47779454
            },
            'frame_id': "map"
        },
        'pose': {
            'position': {
                'x': 0.4749995768070221,
                'y': -3.479999542236328,
                'z': 0.0
            },
            'orientation': {
                'x': 0.0,
                'y': 0.0,
                'z': 0.6961241420312367,
                'w': 0.7179214294623573
            }
        }
    }

    if target_room == "Room 1":
        topic_goal_coordinates.publish(room1)
    elif target_room == "Room 2":
        topic_goal_coordinates.publish(room2)
    elif target_room == "Room 3":
        topic_goal_coordinates.publish(room3)
    elif target_room == "Lager":
        topic_goal_coordinates.publish(lager)

def update_position(message):
    position = message['position']
    orientation = message['orientation']
    print(f"Position: x = {position['x']}\n"
          f"Position: y = {position['y']}\n"
          f"Position: z = {position['z']}\n"
          f"Orientation: w = {orientation['w']}")

# 3. Feedback: Signal empfangen, dass der Turtlebot an Zielkoordinate angekommen ist
# Welchen Status gibt es?
# 1. "idle" 2. "delivering" 3. "goal reached"

status = ''
def update_status(message):
    global status
    status = message['data']
    print(f"Status: {status}")
    
def get_status():
    return status

# Wenn eine Nachricht von dem ausgewählten Roboter geschickt wird, wird update_position aufgerufen
topic_robot_position.subscribe(update_position)
# Wenn eine Nachricht von dem ausgewählten Roboter geschickt wird, wird update_status aufgerufen
topic_robot_status.subscribe(update_status)
