import requests

def iplocator():
    ip = raw_input('IP: ')
    url = 'http://ip-api.com/json/'+ip
    r = requests.get(url)
    sl = r.text
    dct = eval(sl)
    for i in dct:
        print(i, '-', dct[i])
iplocator()
