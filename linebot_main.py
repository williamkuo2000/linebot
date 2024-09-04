import pyautogui as pag
import easygui as eg
import pyperclip
import time
from random import randint
from tkinter import TK
from pynput.keyboard import Controller
keyboard = Controller()



def tryChatOpen():
    try:
        chat = pag.locateCenterOnScreen("chat.png", confidence=0.8)
        chat_x = chat.x/2
        chat_y = chat.y/2
        pag.moveTo(chat_x, chat_y)
        pag.click()
    except:
        print("Chat already opened.")

def click_coor(coor):
    pag.moveTo(coor)
    pag.click()

def click_img(img):
    coor = pag.locateCenterOnScreen(img, confidence=0.8)
    coor_x, coor_y = coor.x/2, coor.y/2
    pag.moveTo(coor_x, coor_y)
    pag.click()

def get_name(nameCoor):
    pag.moveTo(nameCoor)
    pag.click()
    click_img("edit.png")

    pag.hotkey("command", "a")
    pag.hotkey("command", "c")
    pag.press("enter")

def paste_name():
    root = TK()
    root.withdraw()
    string = root.clipboard_get()
    birth = int(string[3:5])
    sex = int(string[5])
    addressing = string[8:10]

    if sex:
        if birth <= 50: addressing += "大哥"
        else: addressing += "兄"
    else:
        if birth <= 45: addressing += "姊姊"
        elif 45 < birth and birth <= 55: addressing += "美女"
        else: addressing += "小姐"

    addressing += "您好\n"
    
    keyboard.type(addressing)
    pag.press("right")




eg.msgbox("注意事項：\n1.桌面越乾淨越好\n2.要先傳過一次，他預設開啟的資料夾才會是有圖片的資料夾")

inclusion = ["文字", "名字", "圖片"]
choices = eg.multchoicebox("選擇模式" , "Options", inclusion)
print(choices)

info_op = []
if "文字" in choices:
    info_op.append("文字")
if "圖片" in choices:
    info_op.append("圖檔名")
info_op.append("人數")

info = eg.multenterbox("Information", "Options", info_op)
print(info)



enter_coor = (0, 0)
name_coor = (0, 0)

for i in range(0, int(info[2])):
    print("Friend " + i + " pcoressing...")

    tryChatOpen()
    time.sleep(1)

    if "名字" in choices:
        get_name()
        click_coor(enter_coor)
        paste_name()
    else: click_coor(enter_coor)

    if "文字" in choices:
        keyboard.type("\n")
        pyperclip.copy(info[0])
        pag.hotkey("command", "v")
    keyboard.press("enter")

    if "圖片" in choices:
        pag.hotkey("command", "o")
        keyboard.type(info[1])
        pag.press("enter")
        time.sleep(1)
    
    pag.press("down")
    time.sleep(randint(1, 4))










