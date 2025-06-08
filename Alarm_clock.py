import datetime
from playsound import playsound
Hour=int(input("Enter Hour: "))
minute=int(input("Enter minute: "))
am_pm=input("Enter am/pm: ")

if am_pm == "pm":
    Hour+=12

while True:
    if Hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute:
        print("playing")
        playsound("Cafecito por la Manana - Cumbia Deli.mp3")
        break
print("Done")