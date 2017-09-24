from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "##################################"

# Your Auth Token from twilio.com/console
auth_token  = "################################"



client = Client(account_sid, auth_token)

message = client.messages.create(
    # Your personal phone number
    to="############", 
    # Your twilio phone number twilio.com/console/phone-numbers/incoming
    from_="############",
    body="Welcome to SMS Weather! This text based service allows you to get the weather conditions in Madison by just texting a letter. You can change the location by texting in another city.")

print(message.sid)


