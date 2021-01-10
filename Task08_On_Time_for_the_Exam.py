hour_exam = int(input())
minutes_exam = int(input())
hour_come = int(input())
minutes_come = int(input())

time_exam = 60 * hour_exam + minutes_exam
time_come = 60 * hour_come + minutes_come

if time_exam == time_come:
    print("On time")

elif time_exam < time_come:
    print("Late")
    if abs(time_come - time_exam) >= 60:
        if abs(time_exam - time_come) % 60 < 10:
            print(f"{abs(time_come - time_exam) // 60}:0{abs(time_exam - time_come) % 60} hours after the start")
        else:
            print(f"{abs(time_come - time_exam) // 60}:{abs(time_exam - time_come) % 60} hours after the start")
    else:
        print(f"{abs(time_come - time_exam)} minutes after the start")

else:
    if abs(time_exam - time_come) <= 30:
        print("On time")
        print(f"{abs(time_exam - time_come)} minutes before the start")
    else:
        print("Early")
        if abs(time_exam - time_come) >= 60:
            if abs(time_exam - time_come) % 60 < 10:
                print(f"{abs(time_exam - time_come) // 60}:0{abs(time_exam - time_come) % 60} hours before the start")
            else:
                print(f"{abs(time_exam - time_come) // 60}:{abs(time_exam - time_come) % 60} hours before the start")
        else:
            print(f"{abs(time_exam - time_come)} minutes before the start")




