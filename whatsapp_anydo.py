from anydo_api.client import Client
from anydo_api.whatsapp import sendmessage
import schedule, time
from threading import Thread
from datetime import datetime
import argparse

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def notify(timing,phone,msg):
    schedule.every().day.at(timing).do(sendmessage,phone=phone,msg=msg)

if __name__ == "__main__":
    parse = argparse.ArgumentParser(prog='whatsapp_anydo.py',description='Anydo Whatsapp Remainder Unofficial')

    parse.add_argument('--email',help='Anydo account Email',required=True,action="store")
    parse.add_argument('--passwd',help='Anydo account password',required=True,action="store")
    parse.add_argument('--phone',help='phone number to notify',required=True,action="store")

    args = parse.parse_args()
    
    email = args.email
    password = args.passwd
    phone = args.phone
    
    user = Client(email=email, password=password)
    tasks = user.get_tasks()
    for task in tasks:
        timing = datetime.fromtimestamp(task['dueDate']/1000).strftime("%H:%M:%S")
        msg = task['title']
        notify(timing,phone,msg)
        print("Task scheduled at "+timing+" to "+phone+" for "+msg)

    t = Thread(target=scheduler)
    t.start()

