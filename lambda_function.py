import json

def lambda_handler(event, context):
    # TODO implement
    reply=""
    
    greet = ["hi", "hello", "hey"]
    
    if event["message"] in greet:
        reply = 'Hello! How can I help?'
      
    elif event["message"].find("weather") >= 0:
        reply = "Please turn on your location services"
    
    elif event["message"].find("food") >= 0:
        reply = "You seem hungry! What kind of cuisine would you like to have?"
    
    else:
        reply = "Your wish is my command. I will serve you soon!"
        
    return reply

