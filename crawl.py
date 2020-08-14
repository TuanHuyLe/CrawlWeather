from bs4 import BeautifulSoup
import requests
import service

headers = requests.utils.default_headers()

def getToday():
    url = 'http://www.thoitiethanoi.com/'
    req = requests.get(url, headers)
    # lay trang web
    bs = BeautifulSoup(req.content, 'html.parser')
    cardcontent = bs.find(class_='weather-content')
    infos = cardcontent.find_all(class_='weather-infos')
    weather = []
    check = service.checkExists()
    for i in range(len(infos)):
        card = infos[i]
        title = card.find('h3').get_text()
        icon = card.find('img')
        src = icon['src']
        celsius = card.find(class_='w-celsius').get_text()
        desc = card.find(class_='w-desc').get_text()
        text = card.find_all(class_='w-text')
        high = text[0].get_text()
        low = text[1].get_text()
        update = text[2].get_text()
        weather.append({
            'title': title,
            'src': src,
            'celsius': celsius,
            'desc': desc,
            'high': high,
            'low': low,
            'update': update,
        })
        if check == True:
            service.insertUser(title, src, celsius, desc, high, low, update)
    return weather

def getTomorrow():
    url = 'http://www.thoitiethanoi.com/thoi-tiet-ngay-mai.html'
    req = requests.get(url, headers)
    # lay trang web
    bs = BeautifulSoup(req.content, 'html.parser')
    cardcontent = bs.find(class_='weather_forecast')
    infos = cardcontent.find_all(class_='home_forecast', limit=4)
    weather = []
    for i in range(len(infos)):
        card = infos[i]
        date = card.find(class_='date')
        title = date.find('h3').get_text()
        icon = card.find('img')
        src = icon['src']
        celsius = card.find(class_='current_temp').get_text()
        desc = card.find(class_='desc').get_text()
        text = card.find(class_='home_weather_desc').find_all('p')
        high = text[0].get_text()
        low = text[1].get_text()
        update = card.find(class_='update').get_text()
        weather.append({
            'title': title,
            'src': src,
            'celsius': celsius,
            'desc': desc,
            'high': high,
            'low': low,
            'update': update,
        })
    return weather
