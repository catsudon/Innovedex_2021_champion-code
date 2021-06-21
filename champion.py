from tkinter import *
from time import sleep
import time
import pyfirmata


port = "COM3"
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

def start():
    L1.configure(text="started working...",fg="green")
    root.update()
    Main()
    L1.configure(text="stopped working",fg="red")

root = Tk()
root.geometry("1080x600")
root.option_add("*font", "comsolas 28")
startButton = Button(root, text="Start" , fg="blue",command=start)
startButton.pack()


L1 = Label(root, text = "stopped working" ,fg = "red")
L1.place(x=635,y=50)
L2 = Label(root, text = "นายสธน เลาลักษณเลิศ" ,fg ="black")
L2.place(x=600,y=150)
L3 = Label(root, text = "นายวชิรวิชญ์ ปิยะประภาพันธ์" ,fg ="black")
L3.place(x=600,y=200)
L4 = Label(root, text = "นายปัณณวัชร์ ปิยะโอฬารรุจน์" ,fg ="black")
L4.place(x=600,y=250)
L5 =Label(root, text = "คุณครูเสฏฐวุฒิ โมลานิล" ,fg="black") 
L5.place(x=600,y=300)


base = board.get_pin('d:8:s')
stretch = board.get_pin('d:9 :s')
left_sholder = board.get_pin('d:10:s')
glipper = board.get_pin('d:11:s')



# base 5-175 ขวา-ซ้าย
# sholderซ้าย 50ต่ำ 120สูง
# sholderขวา 90-150 ชักเข้าออก
# glipper 80degกาง 180=หุบ

def reset():
    base.write(140)
    stretch.write(120)
    glipper.write(110)
    x=90

    while(x<130):
        left_sholder.write(x)
        x=x+1
        sleep(0.005)
    

reset()

def use_glipper():
    while(glipper.read()<155):
      glipper.write(glipper.read()+5)
      time.sleep(0.005)

def release():
    while(glipper.read()>110):
      glipper.write(glipper.read()-5)
      time.sleep(0.005)

def stack():
    left_sholder.write(79)
    while(stretch.read()>132):
        stretch.write(stretch.read()-1)
        sleep(0.005)
    while(stretch.read()<132):
        stretch.write(stretch.read()+1)
        sleep(0.005)

def yok():
    while(stretch.read()>110):
        stretch.write(stretch.read()-1)
        sleep(0.005)
    while(stretch.read()<110):
        stretch.write(stretch.read()+1)
        sleep(0.005)
    beyond = left_sholder.read()
    while(beyond>73):
        left_sholder.write(beyond-1)
        beyond = beyond-5
        sleep(0.01)


def kom():
    stretch.write(134)
    sleep(0.05)
    beyond = left_sholder.read()
    while(beyond>65):
        left_sholder.write(beyond-1)
        beyond = beyond-5
        sleep(0.01)


def pos1():
    if (base.read() < 141):
        while(base.read() < 141):
            base.write(base.read()+1)
            sleep(0.005)
    else:
        while(base.read() > 141):
            base.write(base.read()-1)
            sleep(0.005)

def pos2():
    if (base.read() < 120):
        while(base.read() < 120):
            base.write(base.read()+1)
            sleep(0.05)
    else:
        while(base.read() > 120):
            base.write(base.read()-1)
            sleep(0.005)

def pos3():
    if (base.read() < 103):
        while(base.read() < 103):
            base.write(base.read()+1)
            sleep(0.005)
    else:
        while(base.read() > 103):
            base.write(base.read()-1)
            sleep(0.005)

def pos4():
    if (base.read() < 78):
        while(base.read() < 78):
            base.write(base.read()+1)
            sleep(0.005)
    else:
        while(base.read() > 78):
            base.write(base.read()-1)
            sleep(0.005)

def pos5():
    if (base.read() < 60):
        while(base.read() < 60):
            base.write(base.read()+1)
            sleep(0.005)
    else:
        while(base.read() > 60):
            base.write(base.read()-1)
            sleep(0.005)

def pos6():
    if (base.read() < 41):
        while(base.read() < 41):
            base.write(base.read()+1)
            sleep(0.005)
    else:
        while(base.read() > 41):
            base.write(base.read()-1)
            sleep(0.005)

def komyao():
    while(stretch.read()>139):
        stretch.write(stretch.read()-1)
        sleep(0.005)
    while(stretch.read()<139):
        stretch.write(stretch.read()+1)
        sleep(0.005)
    sleep(0.1)
    beyond = left_sholder.read()
    while(beyond>64):
        left_sholder.write(beyond-1)
        beyond = beyond-5
        sleep(0.01)

def stacksan():
    left_sholder.write(79)
    while(stretch.read()>127):
        stretch.write(stretch.read()-1)
        sleep(0.005)
    while(stretch.read()<127):
        stretch.write(stretch.read()+1)
        sleep(0.005)

def Main():
    #start here
    pos1()
    sleep(0.05)
    kom()
    sleep(0.1)
    use_glipper()
    sleep(0.05)
    yok()
    sleep(0.05)

    pos2()
    sleep(0.05)
    stack()
    sleep(0.05)
    release()

    yok()
    sleep(0.05)
    pos3()
    sleep(0.05)
    komyao()
    sleep(0.1)
    use_glipper()
    sleep(0.05)
    yok()
    sleep(0.05)
    
    pos4()
    sleep(0.05)
    stack()
    sleep(0.05)
    release()

    sleep(0.05)
    yok()
    sleep(0.05)
    pos5()
    sleep(0.06)
    kom()
    sleep(0.05)
    use_glipper()
    sleep(0.05)
    yok()
    sleep(0.05)

    pos6()
    sleep(0.05)
    stacksan()
    sleep(0.05)
    release()

root.mainloop()
sleep(3)