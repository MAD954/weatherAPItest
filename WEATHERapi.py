import requests
from datetime import datetime

api_address='http://api.openweathermap.org/data/2.5/weather?appid=d0b25e87e8fb662ab2e950cfc2c3c55e&q='

location= input("ENTER CITY NAME:")
new_address=api_address+location
json_data=requests.get(new_address).json()
weather_data=json_data['weather'][0]['main']
weather_description=json_data['weather'][0]['description']
hmdt=json_data['main']['humidity']
wind_spd=json_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print ("*************************************************************")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("*************************************************************")

print ("Current weather data  :",weather_data)
print ("Current weather desc  :",weather_description)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

print("=============================================================")


txtlist = [weather_data,weather_description,hmdt,wind_spd,date_time]

with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8') as f :     
                                    
    f.write("************************************************************* \n ")   
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n ************************************************************* \n")
    f.write("Current weather data is: \n".format(txtlist[0]))
    
    f.write("{},{} \n".format("Current weather description  :" ,txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :",txtlist[2],"%"))
    f.write("{},{},{} \n".format("Current wind speed    :",txtlist[3],"kmph"))
    f.write("====================================================")
