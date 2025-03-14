import pyautogui
import time
import gradio as gr 

#This code is to create a notepad file , enter the data given by user in a new file , save that
# file with filename given by user and then after saving , exit the notepad back to UI
#with output as message of successful file creation

def auto_run(text):
    lines=text.split(".")
    file=lines[0]
    data=""
    for i in lines[1:]:
        data=data+i
    pyautogui.moveTo(300, 1020) 
    pyautogui.click()
    pyautogui.write("Notepad")
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.hotkey("ctrl","n")
    time.sleep(2)
    pyautogui.write(data) 
    time.sleep(2)
    pyautogui.hotkey("ctrl", "s")
    time.sleep(1)
    pyautogui.write(file)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey("alt","f4")
    pyautogui.hotkey("alt","f4")

    return "File Saved Successfully"

autofile=gr.Interface(fn=auto_run,inputs="text",outputs="text",title="File Creator",
    description="Enter any text and it will be saved in a new note pad file ,text before dot is file name , any onwards is text")


autofile.launch()