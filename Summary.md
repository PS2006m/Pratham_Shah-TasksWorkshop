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
   converted zip to list for access in HTML file . And thus , My Mini Site was ready .
