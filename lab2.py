import requests
s_city ="Moscow,RU"
appid ="988159431268db351f726d7f4e2aee68"
def weather_day():
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': s_city,'units':'metric','lang':'ru','APPID': appid})
    data = res.json()
    print("Город:", s_city)
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура", data['main']['temp_max'])
    print("Скорость ветра:", data['wind']['speed'])
    print("Видимость:", data['visibility'])
def weather_week():
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Прогноз погоды на неделю:")
    for i in data['list']:
        print("Дата <", i['dt_txt'], "> \r\nТемпература <",
              '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
              i['weather'][0]['description'], "> \r\nСкорость ветра <",
              i['wind']['speed'], "> \r\nВидимость <",
              i['visibility'], "> ")
        print("____________________________")
while (True):
    argument = int(input())
    match argument:
        case 1:
            (weather_day())
        case 2:
            print(weather_week())
            break
