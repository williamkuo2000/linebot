import time
import pyautogui as pag
from random import randint
from pynput.keyboard import Controller
keyboard = Controller()

print(pag.size())
print(pag.position())

def moveToImgClick(img):
    coor = pag.locateCenterOnScreen(img, confidence=0.8)
    coor_x, coor_y = coor.x/2, coor.y/2
    pag.moveTo(coor_x, coor_y)
    pag.click()

def getNameBuf(nameCoor):
    pag.moveTo(nameCoor)
    pag.click()
    moveToImgClick("edit.png")

    pag.keyDown("shift")
    pag.press("left", presses=20)
    pag.keyUp("shift")

    pag.hotkey("command", "c")
    
    moveToImgClick("save.png")

def pasteNameBuf():
    pag.keyDown("command")
    pag.press("v")
    pag.keyUp("command")
    pag.press("right")

def tryChatOpen():
    try:
        chat = pag.locateCenterOnScreen("chat.png", confidence=0.8)
        chat_x = chat.x/2
        chat_y = chat.y/2
        pag.moveTo(chat_x, chat_y)
        pag.click()
    except:
        print("Chat already opened.")

time.sleep(2)

friends = 10
nameCoor = (412, 76)
flag_pc, flag_img = 1, 1

i = 1
while friends:
    print("Friend " + str(i) + " pcoressing...")
    friends -= 1
    i += 1
    time.sleep(1)

    tryChatOpen()

    keyboard.type("新年快樂！建盟祝您身體健康萬事如意！")
    pag.press("enter")

    moveToImgClick("pc.png")
    time.sleep(0.5)
    moveToImgClick("img.png")
    pag.press("enter")
    time.sleep(0.5)

    pag.press("down", presses=1)
    time.sleep(2)
    #time.sleep(randint(2,5))
