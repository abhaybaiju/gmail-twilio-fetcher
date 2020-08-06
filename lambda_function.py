import imaplib 
import os 
from twilio.rest import Client


def lambda_handler(event, context):
    os.environ["username"] = "YOUR GMAIL ADDRESS HERE"
    os.environ["password"] = "YOUR GMAIL PASSWORD HERE"
    os.environ["target"] = "YOUR TARGET EMAIL HERE"
    os.environ["twiliosid"] = "YOUR TWILIO ID HERE"
    os.environ["twiliokey"] = "YOUR TWILIO KEY HERE"
    os.environ["targetphone"] = "YOUR TARGET PHONE NUMBER HERE"
    os.environ["twiliophone"] = "YOUR TWILIO PHONE NUMBER HERE"
    
    imap = imaplib.IMAP4_SSL("imap.gmail.com") 
    
    result = imap.login(os.environ["username"], os.environ["password"]) 
    
    imap.select('"[Gmail]/All Mail"',  
    readonly = True)  
    
    response, messages = imap.search(None, '(UNSEEN)', '(FROM "%s")' % (os.environ["target"])) 
    messages = messages[0].split() 
    print(len(messages))
    flag = False
    if(len(messages) != 0):
        latest = int(messages[-1])     
        for i in range(latest, latest-1, -1): 
            res, msg = imap.fetch(str(i), "(RFC822)") 
            for response in msg: 
                if isinstance(response, tuple): 
                    msg = email.message_from_bytes(response[1]) 
                    print(msg["Date"]) 
                    print(msg["From"])
                    print(msg["Subject"]) 
                    if(msg["From"].find(os.environ["target"])):
                        flag=True
    if(flag):
        client = Client(os.environ["twiliosid"],os.environ["twiliokey"])
        client.messages.create(to=os.environ["targetphone"],from_=os.environ["twiliophone"],body="You have a new email from your sender")
