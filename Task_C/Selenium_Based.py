from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import gradio as gr  

#This code is to go to my locally created django site , get the title , and enter the name 
#of person the user wants to delete , after that , the driver quits and outputs displays

def data_gather(text):
    driver=webdriver.Chrome()
    driver.get("http://localhost:8000")

    print("Page Title :",driver.title)

    time.sleep(5)

    try:
        search_box=driver.find_element(By.ID,"del")
        search_box.send_keys(text)
        time.sleep(3)
        search_box.send_keys(Keys.ENTER)

        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
    
    return "Deleted User"
    
delpower=gr.Interface(fn=data_gather,inputs="text",outputs="text",title="Delete Data")

delpower.launch()