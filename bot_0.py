import time
import pyautogui as pag
from random import randint
from pynput.keyboard import Controller

keyboard = Controller()
print(pag.size())
print(pag.position())

time.sleep(2)

flag_pc = 1
flag_img = 1

friends = 10

while friends:
    print("Friend no" + str(friends) + "complete.")
    friends -= 1
    try:
        chat = pag.locateCenterOnScreen("chat.png", confidence=0.8)
        chat_x = chat.x/2
        chat_y = chat.y/2
        pag.moveTo(chat_x, chat_y)
        pag.click()
    except:
        print("Chat already opened.")
    time.sleep(1)

    if flag_pc:
        flag_pc = 0
        paper_clip = pag.locateCenterOnScreen("pc.png", confidence=0.8)
        pc_x = paper_clip.x/2
        pc_y = paper_clip.y/2
        time.sleep(1)

    pag.moveTo(pc_x, pc_y)
    pag.click()
    time.sleep(0.5)

    if flag_img:
        flag_img = 0
        img = pag.locateCenterOnScreen("img.png", confidence=0.8)
        img_x = img.x/2
        img_y = img.y/2
        time.sleep(1)
    pag.moveTo(img_x, img_y)
    pag.click()
    pag.press("enter")

    keyboard.type("新年快樂！建盟祝大家身體健康萬事如意！")
    pag.press("enter")
    time.sleep(0.5)

    pag.press("down", presses=1)
    time.sleep(2)
    #time.sleep(randint(2,5))
