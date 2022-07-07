import requests
import time 
import os 
from datetime import datetime
def SendLogo():
    LOGO  = '''
       _____ ________   __              _____ _        _                _____ _               _             
      / ____|  ____\ \ / /             / ____| |      | |              / ____| |             | |            
     | |    | |__   \ V /   _ __ ___  | (___ | |_ __ _| |_ _   _ ___  | |    | |__   ___  ___| | _____ _ __ 
     | |    |  __|   > <   | '__/ _ \  \___ \| __/ _` | __| | | / __| | |    | '_ \ / _ \/ __| |/ / _ \ '__|
     | |____| |     / . \ _| | |  __/  ____) | || (_| | |_| |_| \__ \ | |____| | | |  __/ (__|   <  __/ |   
      \_____|_|    /_/ \_(_)_|  \___| |_____/ \__\__,_|\__|\__,_|___/  \_____|_| |_|\___|\___|_|\_\___|_|   
                                                                                                        Created by Kiyomi#9081

'''
                                                                                                         
    print(LOGO) 

def CheckStatusOfCFX():
    try:
        r = requests.get('https://status.cfx.re/api/v2/status.json')
        e = requests.get('https://status.cfx.re/metrics-display/1hck2mqcgq3h/day.json')
        data = r.json()
        data_2 = e.json()
        MS = round(data_2['summary']['mean'], 0)
        DESC = data['status']['description']
        #CAUSES = data['status']['indicator']
        if DESC != "All Systems Operational":
            print("====== OUTAGE DETECTED ======")
            print(datetime.now().strftime("%H:%M:%S"), " | FiveM // CFX.re Server Status: " + DESC)
           # print("Possible Root Issues: " + CAUSES)
            print("\t\tAverage CnL self-test time " + str(MS) + ' ms')
        else:
            print(datetime.now().strftime("%H:%M:%S"), " | CFX.re is live and working | Average CnL self-test time " + str(MS) + " ms")
    except:
        print("[Err]: Couldn't get request in enough time.")
os.system("cls") 
SendLogo()
CheckStatusOfCFX()
while True:
    time.sleep(30)
    os.system("cls") 
    SendLogo()
    CheckStatusOfCFX()