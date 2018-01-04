Clone the repo.

Create Virtual Environment

Example: 

>virtualenv "name of the env"

Get into Virtual Env

Example: 

>source "name of the env"/bin/activate

Once into virtualenv run the below command to install the requiremnets

>pip install -r requirements.txt

After installing the requirments run the run.py file as below
>python run.py

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Once the Server is up, pass the below parameters


{  
  "to": "shiva@gmail.com", 
  "subject": "Check your email", 
  "body":"You wont find the mail in inbox, Please check your spam Folder.", 
  "from": "shiva123@gmail.com"
}



