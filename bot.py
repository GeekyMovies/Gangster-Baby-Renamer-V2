import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "AAE1STI93wsA7MK9pma-MOKXU4Gww5KxwWk")

API_ID = int(os.environ.get("API_ID", "23311160"))

API_HASH = os.environ.get("API_HASH", "2a1366013eca4256bce853346dbcda49")

STRING = os.environ.get("STRING", "1BVtsOKwBuym_lqJMDg7bonwer9rHbFYd_q_SYm-uPEqXox2NEkciFfVCqJVKXPsQo6SGsMBHCHoNLn_UZI8EJCoosmc4w5tbwLuDF1Vec2vIoe8eb2pfvpDcp63_G-Cqp0n0aiZT8h713WR9ldVf7k1oFRgVqhuXfuhZgXbed_chgNuCPpOSjcVbavph-VjMpVk6L3-sLvQJiMG5nslkN2Rt6hSApvV58z-ktLPatQ_30xD33TGcdAGzxccALr-zvHE-UBIWZAx-RtsqViuQ1YusNRvQQS8I9reuloZ9Ccc11cGmLGgw6P5A_-48hNOI2LaivHRj4xHXE8NxVBUBFJVVX0nE_JA=")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
