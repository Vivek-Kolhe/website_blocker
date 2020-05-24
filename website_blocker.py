import time
from datetime import datetime as dt

hosts_temp = "hosts" #not required
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
blocked_websites = ["", "", ""] #pass the list of websites here to be blocked

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Websites are blocked for now.")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()
        print("You can access the websites now.")
    time.sleep(5)