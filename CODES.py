#!/usr/bin/python
# open the user flair page and put the cursor in the css class box(first one)
# open the EDIT wiki page with the set lists and prepare to run this script and immediately switch the cursopr to the end of the first line
import pyautogui
import os
# Set a counter to count the # of exceptions occur
counter = 0

# Start the while loop
while True:
    try:
        pyautogui.time.sleep(1)

        pyautogui.keyDown('shift')
        pyautogui.press('home')
        pyautogui.keyUp('shift')

        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')


        pyautogui.keyDown('ctrl')
        pyautogui.press('tab')
        pyautogui.keyUp('ctrl')

        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('return')
        pyautogui.time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')

        pyautogui.keyDown('ctrl')
        pyautogui.press('tab')
        pyautogui.keyUp('ctrl')

        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('end')


# Exception handle when pyautogui can't locate the renew button on the screen
# or if it clicks away by mistake
# this section needs work and sometimes fails to function properly
    except Exception:
        print ("Exception thrown, calculating course of action")
        pyautogui.press('pgdn')
        counter += 1
        print ("counter =" + str(counter))
        if counter >= 3: counter = 0

