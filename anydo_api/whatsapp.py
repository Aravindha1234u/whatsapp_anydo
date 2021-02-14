import webbrowser as web
import pyautogui as pg
import time

def sendmessage(phone,msg):
    web.open("https://web.whatsapp.com/send?phone={}&text={}".format(phone,msg))
    time.sleep(20)
    width,height = pg.size()
    pg.click(width/2,height/2)
    pg.press('enter')
