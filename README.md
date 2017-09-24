Hello Welcom to SMS Weather. There are a few steps you need to do to get this application working

1. Regester for a Twilio Account https://www.twilio.com

2. Open send_sms.py

3. On line 4, put your Account SID in for the account_sid variable https://www.twilio.com/console

4. On line 7, put your Auth Token in for the auth_token varible https://www.twilio.com/console

5. On line 15, put your personal phone number format ==> "+1##########"

6. On line 17, put your twilio phone number

7. Go to https://openweathermap.org and register

8. Open recieve_sms

9. On line 10, enter you openweathermap API key https://home.openweathermap.org/api_keys

10. Install python on machine

11. Install pyowm on machine 'pip install pyowm'

11. Install ngrok on machine 'brew cask install ngrok'

12. Go to SMSWeather folder in Command Line and run 'recieve_sms.py'

13. Type 'ngrok http 5000'

14. Copy the last Forwarding address and add '/sms' to the end Ex: https://1ded6c50.ngrok.io/sms


15. Log into Twilio and go to phone numbers https://www.twilio.com/console/phone-numbers/

16. Click on the phone number entered in step 6

17. Change "A MESSAGE COMES IN" section to the ngrok address

18. Run 'python send_sms'