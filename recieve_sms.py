#Weather APT
import pyowm


from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


# Enter Your OpenWeather Map API Key https://openweathermap.org
owm = pyowm.OWM(YOUR_API_KEY)

#Flask object
app = Flask(__name__)



def general_weather(loc):
    observation = owm.weather_at_place(loc)
    w = observation.get_weather()

    #Get temperature Data
    temp = w.get_temperature('fahrenheit')

    # Combines all weather data to make custom message
    message = "Temperature: " + str(round(temp['temp'],1)) + " degrees" + "\nConditions: " + w.get_status() + "\nLocation: " + loc

    return message

def test_location(name):
    try:
        own = owm.weather_at_place(name)
        return True
    except pyowm.exceptions.not_found_error.NotFoundError:
        return False


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    location = "Madison, WI"

    if(test_location(request.values.get('Body'))):
        location = request.values.get('Body')
    
    
    resp = MessagingResponse()
    resp.message(general_weather(location))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)