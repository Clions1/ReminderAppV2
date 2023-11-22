import time
from datetime import datetime
reminderName=input("What do you want to remember : ")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"Current time is : {current_time}")
Time=input("Enter the remember time (HH:MM) : ")

while True:
    Standart_time=datetime.now().strftime("%H:%M")
    time.sleep(1)
    if Time==Standart_time:
        print(f"reminder working : {reminderName}")
        break