def search(city):
    '''
    input: city name
    output: a dict include the cities and the code
    '''
    import requests
    import json
    url = r'http://toy1.weather.com.cn/search?cityname=' + city  + r'&callback=success_jsonpCallback&_=1610587632208'
    res = requests.get(url)
    res.encoding = 'utf-8'
    result0 = json.loads(res.text[22:-1])
    result1 = {}
    for item in result0:
        content = item['ref'].split('~')
        result1[content[-1] + content[2]] = content[0]
    #print(result1)
    return result1

def get_weather(city_code):
    '''
    input: city code
    output: tempurature, wind ...
    '''
    from bs4 import BeautifulSoup
    import requests
    url = r'http://www.weather.com.cn/weather1d/' + str(city_code)  + r'.shtml'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    re = requests.get(url, headers = headers)
    html = re.content.decode('UTF-8')
    bs_obj = BeautifulSoup(html, "html.parser")
    bs_obj = bs_obj.find('div',class_ = 't')
    h = bs_obj.find_all('h1')
    p = bs_obj.find_all('p')
    big = bs_obj.find_all('big')
    info = []
    daytime = {}
    daytime['time'] = h[0].text
    daytime['wea'] = p[0].text
    daytime['weap'] = big[0].get('class')[1]
    daytime['tem'] = p[1].span.text + p[1].em.text
    daytime['win'] = p[2].span.get('title') + p[2].span.text
    daytime['winp'] = p[2].i.get('class')[0]
    daytime['suntime'] = p[3].span.text
    info.append(daytime)
    night = {}
    night['time'] = h[1].text
    night['wea'] = p[4].text
    night['weap'] = big[1].get('class')[1]
    night['tem'] = p[5].span.text + p[1].em.text
    night['win'] = p[6].span.get('title') + p[2].span.text
    night['winp'] = p[6].i.get('class')[0]
    night['suntime'] = p[7].span.text
    info.append(night)
    return info

def debug(city_code):
    pass
