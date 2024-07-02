from pydirectinput import(leftClick, mouseDown, mouseUp, keyDown, keyUp, press, LEFT)
import keyboard
import time

def sleep_t(t:int):
    time.sleep(t/1000)

def q_down():
    keyDown(key="q")

def q_up():
    keyUp(key="q")

def esc_down():
    keyDown(key="esc")

def esc_up():
    keyUp(key="esc")


def fly():
    leftClick()
    sleep_t(40)

    q_down()
    sleep_t(5)

    esc_down()
    sleep_t(15)

    sleep_t(35)

    esc_up()
    sleep_t(3)

    q_up()
    sleep_t(30)

    q_down()
    sleep_t(10)

    esc_down()
    sleep_t(70)

    q_up()
    esc_up()

if __name__ == "__main__":
    try:
        keyboard.wait(hotkey="1")
        time.sleep(3)
        fly()
        print("process end")
    except:
        ...