import time
from navigation import (Waypoint, set_home, mode_set, arm, mission_upload,
                        wp_detect_course, loiter_at_present, gain_track_point,
                        detect_completed, eliminate_error_target, command_retry,
                        gain_position_now, set_ground_speed, target_transfer,
                        wrong_number, wp_bombing_course, mission_current, bomb_drop,
                        loiter, return_to_launch, initiate_bomb_drop, reboot, system_check,
                        preflight_command, wp_detect_course_HeBei, gain_heading)
from pymavlink import mavutil
LEN_OF_TARGET_LIST = 50
TIME_DELAY_MS = 150
APPROACH_ANGLE = 260
DETECT_TIME_LIMIT = int(2 * 60 * 1000)
DETECT_ACC = 6  # m
wp_detect = Waypoint(38.5431345, 115.04109799999999, 30)
final_target_position = Waypoint(38.543192999999995, 115.0409772, 0)


wp_home = Waypoint(38.543056, 115.040833, 0)

the_connection = mavutil.mavlink_connection('/COM3', baud=57600)

# 盘旋等待任务上传
wp_list = wp_bombing_course(final_target_position, APPROACH_ANGLE)
mission_upload(the_connection, wp_list, wp_home)

preflight_command(the_connection, wp_home)

input("a")

while not mode_set(the_connection, 12):
    continue

# 盘旋等待任务角度合适
initiate_bomb_drop(the_connection, APPROACH_ANGLE)

# 切换为自动模式，进入投弹航线
while not mode_set(the_connection, 10):
    continue

# 到达预设投弹位置前，设置时间检查防止因为信号中断不投弹
while (mission_current(the_connection) < len(wp_list) - 15):
    print(mission_current(the_connection))

bomb_drop(the_connection)

'''
任务结束
'''

#return_to_launch(the_connection)