# reading the log file
file = open("challenge.log", "r")
log_list = file.readlines()

# setting the params to do the calculations

new_log_list = []
response_time_list = []
hour_of_the_day_list = []
response_times_for_entity4_above_1500_list = []

# removing new line characters from the log list
for log in log_list:
    new_log_list.append(log.replace("\n", ""))

# first calculate the 95th percentile in response time
def calculate_95th_percentile_from_whole_logs(new_log_list, _filtered=False):
    response_times = []
    for log in new_log_list:
        if "SUCCESS" not in log:
            continue
        response_times.append(int(log.split(":")[2]))

    sorted_response_times = sorted(response_times)
    len_of_list = len(sorted_response_times)-1
    percentile_position = int(len_of_list * 0.95)

    if _filtered:
        print("For responses above 1500 and entity4")
        print(f"95th percentile response time: {sorted_response_times[percentile_position]}")
    else:
        print(f"95th percentile response time across the whole log file: {sorted_response_times[percentile_position]}")

def calculate_95th_percentile_for_every_hour(new_log_list, _filtered=False):
    hourly_percentile_map = {}
    percentile_per_hour = []
    num = 0
    for _ in range(24):
        hourly_percentile_map[str(num)] = []
        num += 1

    for log in new_log_list:
        if "SUCCESS" not in log:
            continue
        response_time = int(log.split(":")[2])
        time_stamp = log.split(":")[0]
        # changing the double numbered layout to an int to get rid of the 0 but then changing it back to a string to use the map
        hour = str(int(time_stamp[8:10]))
        hourly_percentile_map[hour].append(response_time)

    for hour in hourly_percentile_map:
        if not hourly_percentile_map.get(hour):
            continue

        sorted_response_times = sorted(hourly_percentile_map[hour])
        len_of_list = len(sorted_response_times)-1
        percentile_position = int(len_of_list * 0.95)
        percentile_per_hour.append(sorted_response_times[percentile_position])

    hour_for_return_string = 0

    if _filtered:
        print("For responses above 1500 and entity4")

    for _ in percentile_per_hour:
        print(f"95th percentile for hour {hour_for_return_string}: {_}")
        hour_for_return_string += 1

def calculate_95th_percentile_of_all_response_times_above_1500_for_entity4(new_log_list):
    filtered_list = []
    for log in new_log_list:
        if "SUCCESS" not in log:
            continue

        if "Entity4" not in log:
            continue

        if int(log.split(":")[2]) < 1500:
            continue

        filtered_list.append(log)

    calculate_95th_percentile_from_whole_logs(filtered_list, _filtered=True)

def calculate_95th_percentile_of_all_response_times_above_1500_for_entity4_per_hour(new_log_list):
    filtered_list = []
    for log in new_log_list:
        if "SUCCESS" not in log:
            continue

        if "Entity4" not in log:
            continue

        if int(log.split(":")[2]) < 1500:
            continue

        filtered_list.append(log)
    calculate_95th_percentile_for_every_hour(filtered_list, _filtered=True)

print("Hello thank you for giving me the chance to do this task \n"
      "which calculation do you wish to perform? \n \n"
      "if you want to calculate the 95th percentile for the entire log file input 1: \n \n"
      "if you want to calculate the 95th percentile for each hour for the entire log file input 2: \n \n"
      "if you want to calculate the 95th percentile for entity4 logs above 1500 for the entire log file input 3: \n \n"
      "if you want to calculate the 95th percentile for entity4 logs above 1500 for each hour input 4:")

user_input = input()
if user_input == "1":
    calculate_95th_percentile_from_whole_logs(new_log_list)
if user_input == "2":
    calculate_95th_percentile_for_every_hour(new_log_list)
if user_input == "3":
    calculate_95th_percentile_of_all_response_times_above_1500_for_entity4(new_log_list)
if user_input == "4":
    calculate_95th_percentile_of_all_response_times_above_1500_for_entity4_per_hour(new_log_list)


file.close()
