from django.shortcuts import render
import math,datetime,requests
# Create your views here.
def index(req):
    city_name='kochi'
    if req.method=='POST':
        city_name=req.POST['city']
        api_key='360e4bc3865e745ec844bd7ec054ca11'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        weather=requests.get(url)
        weather_data=weather.json()
        try:
               data={
					'city':city_name,
					'description':weather_data['weather'][0]['description']
				}
        except:
                city_name='kochi'
    api_key='360e4bc3865e745ec844bd7ec054ca11'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    weather=requests.get(url)
    weather_data=weather.json()
    rise=datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    set=datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
    data={
           'city':city_name,
           'description':weather_data['weather'][0]['description'],
           'temp':math.floor(weather_data['main']['temp']-273.15),
           'feels':math.floor(weather_data['main']['feels_like']-273.15),
           'sunrise':rise.strftime('%H:%M:%S'),
           'sunset':set.strftime('%H:%M:%S')
	}
    return render(req,'index.html',{'data':data})