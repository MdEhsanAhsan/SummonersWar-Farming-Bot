import threading
from tkinter import *
import os.path
import time as t
from PIL import Image

import pyautogui as pg

running = False
h = 0  # hero
leg = 0  # legend
e = 0  # rare
f = 0  # fail run
r = 0  # run count
ra = 0  # Rainbowmon
us = 0  # unknown Scroll
ms = 0  # Mystical Scroll
ss = 0  # Summoning Stone
sOh = 0  # Symbol of harmony
sOt = 0  # Symbol of Transcendance
sOc = 0  # Symbol of Chaos
rp = 0  # RunePiece
ref = 0  # Refill count

path = "C:/GB12/img"

start_img = Image.open(os.path.join(path, "start.png"))
# xp_img = Image.open(os.path.join(path, "xp.png"))
# mana_img = Image.open(os.path.join(path, "mana.png"))
reward_img = Image.open(os.path.join(path, "reward.png"))
rare_img = Image.open(os.path.join(path, "rare.png"))
rep_img = Image.open(os.path.join(path, "rep.png"))
hero_img = Image.open(os.path.join(path, "hero.png"))
sOh_img = Image.open(os.path.join(path, "sOh.png"))
sOt_img = Image.open(os.path.join(path, "sOt.png"))
sOc_img = Image.open(os.path.join(path, "sOc.png"))
legend_img = Image.open(os.path.join(path, "leg.png"))
runePiece_img = Image.open(os.path.join(path, "rp.png"))
die_img = Image.open(os.path.join(path, "die.png"))
rainbow_img = Image.open(os.path.join(path, "ra.png"))
unknown_img = Image.open(os.path.join(path, "us.png"))
summoning_img = Image.open(os.path.join(path, "ss.png"))
mystical_img = Image.open(os.path.join(path, "ms.png"))
shop_img = Image.open(os.path.join(path, "shop1.png"))

x = 727  # leftSideScreen   RightSide = 1737
y = 402  # start location   RightSide = 402

sell_x = 383  # sell
sell_y = 443  # sell
ok_x = 366  # ok
ok_y = 351  # ok

replay_x = 310  # replay
replay_y = 320  # replay

hero_x = 513
hero_y = 447  # heroRune

sOh_x = 445  # sOh
sOh_y = 461

die_x = 559
die_y = 381

shop_x = 356
shop_y = 363

shop_ok_x = 462
shop_ok_y = 352

shop_close_x = 442
shop_close_y = 480


def start():
    if pg.locateOnScreen(start_img):
        pg.click(x, y)
        t.sleep(1)


def chest():
    global r
    if pg.locateOnScreen(reward_img):
        pg.click(x, y)
        t.sleep(1)
        pg.click(600, 400)
        t.sleep(1)
        r += 1


def sell():
    global e
    if pg.locateOnScreen(rare_img):
        t.sleep(2)
        pg.click(sell_x, sell_y)
        t.sleep(2)
        pg.click(ok_x, ok_y)
        t.sleep(1)
        e += 1


def rep():
    if pg.locateOnScreen(rep_img):
        pg.click(replay_x, replay_y)
        t.sleep(1)


def updater():
    label1['text'] = f"Total number of runs = {r}"

    label2['text'] = f"Total number of Sold Rune = {e}"

    label3['text'] = f"Total number of Hero Rune = {h}"

    label4['text'] = f"Total number of Legend Rune = {leg}"

    label5['text'] = f"Total number of Failed Runs = {f}"

    label6['text'] = f"Total Number of Rune Piece = {rp}"

    label7['text'] = f"Total Number of Rainbowmon = {ra}"

    label8['text'] = f"Total Number of unknownScroll = {us}"

    label9['text'] = f"Total Number of MysticalScroll = {ms}"

    label10['text'] = f"Total Number of Stone = {ss}"

    label11['text'] = f"Total Number of SOH = {sOh}"

    label12['text'] = f"Total Number of SOT = {sOt}"

    label13['text'] = f"Total Number of SOC = {sOc}"

    label14['text'] = f"Total Number of Refills = {ref}"


def claim():
    global h, sOh, leg, rp, sOt, sOc, ra, us, ss, ms

    if pg.locateOnScreen(hero_img):  # Hero Rune
        pg.click(hero_x, hero_y)
        t.sleep(1)
        h += 1

    if pg.locateOnScreen(legend_img):  # Legend Rune
        pg.click(hero_x, hero_y)
        t.sleep(1)
        leg += 1

    if pg.locateOnScreen(sOh_img):
        pg.click(sOh_x, sOh_y)
        t.sleep(1)
        sOh += 1

    if pg.locateOnScreen(sOt_img):
        pg.click(sOh_x, sOh_y)
        t.sleep(1)
        sOt += 1

    if pg.locateOnScreen(sOc_img):
        pg.click(sOh_x, sOh_y)
        t.sleep(1)
        sOc += 1

    if pg.locateOnScreen(runePiece_img):
        pg.click(sOh_x, sOh_y)
        t.sleep(1)
        rp += 1

    if pg.locateOnScreen(rainbow_img):
        pg.click(sOh_x, sOh_y)
        t.sleep(1)
        ra += 1

    if pg.locateOnScreen(unknown_img):
        pg.click(sOh_x, sOh_y)
        t.sleep(1)
        us += 1

    if pg.locateOnScreen(summoning_img):
        pg.click(sOh_x, sOh_y)
        t.sleep(1)
        ss += 1

    if pg.locateOnScreen(mystical_img):
        pg.click(sOh_x, sOh_y)
        t.sleep(1)
        ms += 1


def die():
    global f, r
    if pg.locateOnScreen(die_img):
        pg.click(die_x, die_y)
        t.sleep(2)
        pg.click(x, y)
        f += 1
        r = r + f
        t.sleep(1)
        pg.click(replay_x, replay_y)
        t.sleep(2)
        pg.click(x, y)


def refill():
    global ref

    if pg.locateOnScreen(shop_img):
        pg.click(shop_x, shop_y)
        t.sleep(2)
        pg.click(shop_x, shop_y)
        t.sleep(2)
        pg.click(shop_x, shop_y)
        t.sleep(2)
        pg.click(shop_ok_x, shop_ok_y)
        t.sleep(2)
        pg.click(shop_close_x, shop_close_y)
        t.sleep(1)
        ref += 1


def run():
    global running
    running = True
    if button['state'] == NORMAL:
        button['state'] = DISABLED
        button['bg'] = 'white'

    while running:
        start()
        chest()
        sell()
        claim()
        rep()
        refill()
        die()
        updater()
    button['bg'] = '#7CFC00'


def begin():
    if not running:
        # no thread is running, create new thread and start it
        threading.Thread(target=run, daemon=True).start()


def kill():
    global running
    running = False
    if button['state'] == DISABLED:
        button['state'] = NORMAL


root = Tk()
root.geometry('720x450')
background_image = PhotoImage(file='./img/bge.gif')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
root.title("GB12")
root.iconbitmap(r'img/icon.ico')

topFrame = Frame(root)
topFrame.grid()

bottomFrame = Frame(root)
bottomFrame.grid()
button = Button(topFrame, text='Run', command=begin, bg='#7CFC00', state=NORMAL)
button.grid(row=0, column=0, sticky=E)
button1 = Button(topFrame, text='Pause', command=kill, bg='#F0E68C')
button1.grid(row=0, column=1, sticky=E)
button2 = Button(topFrame, text='Terminate', command=root.destroy, bg='red')
button2.grid(row=0, column=2, sticky=E)

label1 = Label(bottomFrame, text='Total number of runs = 0')

label2 = Label(bottomFrame, text='Total number of Sold Artifacts = 0')

label3 = Label(bottomFrame, text='Total number of Hero Artifacts = 0')

label4 = Label(bottomFrame, text='Total number of Legend Artifacts = 0')

label5 = Label(bottomFrame, text='Total number of Failed Runs = 0')

label6 = Label(bottomFrame, text='Total Number of Rune Piece = 0')

label7 = Label(bottomFrame, text='Total Number of Rainbowmon = 0')

label8 = Label(bottomFrame, text='Total Number of unknownScroll = 0')

label9 = Label(bottomFrame, text='Total Number of MysticalScroll = 0')

label10 = Label(bottomFrame, text='Total Number of Stone = 0')

label11 = Label(bottomFrame, text='Total Number of SOH = 0')

label12 = Label(bottomFrame, text='Total Number of SOT = 0')

label13 = Label(bottomFrame, text='Total Number of SOC = 0')

label14 = Label(bottomFrame, text='Total Number of Refills = 0')

label1.grid(row=0, column=0, sticky=W)

label2.grid(row=0, column=1, sticky=W)

label3.grid(row=1, column=0, sticky=W)

label4.grid(row=1, column=1, sticky=W)

label5.grid(row=2, column=0, sticky=W)

label6.grid(row=2, column=1, sticky=W)

label7.grid(row=3, column=0, sticky=W)

label8.grid(row=3, column=1, sticky=W)

label9.grid(row=4, column=0, sticky=W)

label10.grid(row=4, column=1, sticky=W)

label11.grid(row=5, column=0, sticky=W)

label12.grid(row=5, column=1, sticky=W)

label13.grid(row=6, column=0, sticky=W)

label14.grid(row=6, column=1, sticky=W)
root.mainloop()
