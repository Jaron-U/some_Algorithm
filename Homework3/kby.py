if __name__ == '__main__':
    file = open("act.txt", "r")  # read act.txt file
    n_set = 0  # default the numbers of set is 0

    for line in file:
        n_activity = int(line)  # read the numbers of activity for each set
        # create 3 lists of each activity's numbers, start time, and end time
        activity_num = []
        start = []
        end = []
        for n in range(n_activity):
            activity_number, start_time, end_time = next(file).split()  # read the line (activitity number,start time,end time)
            activity_num.append(int(activity_number))  # add each activity number to list of activities
            start.append(int(start_time))  # add each start time to list of start
            end.append(int(end_time))  # add each end time to end of start
        act_time = [(activity_num[i], start[i], end[i]) for i in range(0, len(activity_num))]  # combine above three elements as tuples
        sorted(act_time, key=lambda x: x[1])  # sorted the start time by ascending order


        temp = [[] for i in range(n_activity)]  # create a list of lists

        for i in range(0, n_activity):  # for each activity
            for j in range(0, i):  # for each previous activity
                started = act_time[i][1]  # starting time the following activity
                previous_ended = act_time[j][2]  # endting time of the previous activity

                if (started >= previous_ended and len(temp[j]) > len(temp[i])):  # if the previous activity's end time is not exceed the following activity's start time, then it is reasonable to pick the previous activity, and ensure which solution will take the maximum activities.
                    temp[i] = temp[j].copy()
            temp[i].append(act_time[i][0])  # collect the activity's number

        output = []

        for i in range(n_activity):
            if (len(output) < len(temp[i])):
                output = temp[i].copy()  # copy the temp[i] to output

        n_set += 1
        print('Set {}'.format(n_set))
        print("Maximum number of activities = ", len(output))  # print maximum activites
        print(*output)  # print the acitivities
        print()




