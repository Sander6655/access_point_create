import subprocess
print("Turn your wifi off!")

ssid = input("What is the mame of your new wifi network?\n Name: ")
password = input("What is the new password of your wifi network?\n password: ")

command = 'sudo ./create_ap wlan0 eth0 ' + ssid + ' ' + password'

subprocess.call(command, shell=True)

