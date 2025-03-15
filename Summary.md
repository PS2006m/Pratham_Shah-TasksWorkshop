My approach towards this has been with the pure ambition of learning new things , to transform what I had in mind to Code . 
In this tasks , I tried to create a unique UIs for the problem statements given , reusing knowledge I had and sometimes learning new information .
1. Approach towards Task A was clear , It needed a simple UI and needed inputs , dropdown and file . So I decided to make a Website for storing Information of a person
    The person's name is entered by the User , which included their name , a sport they like and their image . This all is uploaded to a database using Django's ORM .
     and add to the pile of data . User can also see all the person's Info they haved saved here in a proper way . User can also delete the any person they want using their name
   as input . Challenges faced by me during this was that if after entering a person's info and submitting , they click on refresh , the last post request is loaded and creates
   faulty data , To avoid this , I started using redirect after saving the data in database in views file . If the user sends a get request , then refreshing will give no harm
   but if user sends a post request , then they will be redirected back to site after saving data which gives a get request , so if refresh now , the last request will be a get
   one . But in using redirect , i was sending Infinite get requests and was creating a loop , so solved by using redirect only for the post request . Now that I am redirecting,
   I needed a way to use my database in HTML file as I wanted user to view the new data with the old data , the instance they submit, but i was not rendering ,
    simply redirecting . So I created a session to handle ,  but needed to combine two datas :-names and sports as I wanted to use them in same for loop , used zip to do it ,
   converted zip to list for access in HTML file .
   I applied the session for Django about returning httpResponse .  And thus , My Mini Site was ready .

3. Approach Towards task B was confusing as to which UI to select , Gradio or Streamlit , I settled on Gradio as it
    seemed simpler . Challenges I faced was to find proper code to load a model from Hugging Face ,the site did have lots of
   models om various subjects , but the code given in that site was giving problems when run on my terminal  , As I did not
   have time for Debugging , i compromised for a resnet18 model feom torchvision . It is about ImageClassification .
   I applied the session in workshop where the image classification was explained .And
   My Task_B was complete

5. For Task_C , I again chose gradio as it seemed simple . 2 files here , Selenium based  and PyAutoGui based .
    for Selenium , I decided to just take and enter data from my own DjangoSite from Task A .
   Automation was quite simple as i just had to find id for the Delete field . For Pyautogui , it was tough work as I was
   trying to automate opening a new notepad file , saving the  data entered by user  and saving as file name also entered
   by user . Had to the use the hotkeys syntax for ctrl+N and ctrl+S functions, which is something I learned new .
   first was to locate the windows search bar with mouse pointer coordinates , Took some timee . then give enough sleep
   time in between to avoid text overlapping . It ran properly after a lot of efforts . I beleive, the mouse pointer
   may not locate windows search bar sameway due to difference in screen sizes ,  you can adjust coordinates on your own
   or see the 2 proof videos of Pyautogui I have Included .
   I applied the session where in workshop , Automation was explained about loggin on instagram .
   and my Task_C was complete
