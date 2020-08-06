# gmail-twilio-fetcher
This is a python script I wrote when I was expecting my offer letter from my first job. Being an impatient person, I just had to know exactly when the email arrived.
In order to do so, I created a script which interacts with my Gmail inbox, fetches my emails, filters them on the basis of new and unseen, and then looks for the required sender.
If it finds an unread email from the sender email specified, it send me a message using the Twilio client alerting me. 

Next I wanted to run this script automatically every one hour. To achieve this I created an AWS Lambda function with this Python code.
Then I created a trigger for this function using AWS Cloudwatch. All this is possible just by using the free tier in AWS.

Now, the script runs successfully every hour send me a text message whenever I receive a new email from the specified email address. 
