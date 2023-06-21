import requests
import time
from flask import Flask, request
from flask_cors import CORS
import re
import os;
import datetime;

app = Flask(__name__)
CORS(app)

@app.route('/<m3u8>')
def index(m3u8):
    now = datetime.datetime.now();
    d
    m3u8 = request.url.replace('__', '/')
    source = m3u8.replace('https://erdoganladevam.herokuapp.com/', '')
    source = source.replace('%2F', '/')
    source = source.replace('%3F', '?')
    videoid = request.args.get('videoid')
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'tr-TR, tr;q=0.9',
        'origin': 'https://www.maltinok.com',
        'referer': 'https://www.maltinok.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    ts = requests.get(source, headers=headers)
    print(str(datetime.datetime.now()) +" - " + source + " istek cevap suresi: " + str(datetime.datetime.now() - now));

    tsal = ts.text.replace(videoid+'_', f'https://cors-proxy.fringe.zone/https://erdoganladevam.herokuapp.com/getstream?param=getts&source=https://edge10.xmediaget.com/hls-live/{videoid}/1/{videoid}_')
    if 'internal' in tsal:
        tsal = tsal.replace('internal', f'https://cors-proxy.fringe.zone/https://erdoganladevam.herokuapp.com/getstream?param=getts&source=https://edge10.xmediaget.com/hls-live/{videoid}/1/internal')
    if 'segment' in tsal:
        tsal = tsal.replace('\nmedia', f'\nhttps://cors-proxy.fringe.zone/https://erdoganladevam.herokuapp.com/getstream?param=getts&source=https://edge10.xmediaget.com/hls-live/{videoid}/1/media')
    return tsal

@app.route('/getm3u8', methods=['GET'])
def getm3u8():
    source = request.args.get('source')
    source = source.replace('%2F', '/')
    source = source.replace('%3F', '?')
    now = datetime.datetime.now()
    zaman = time.time();
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'tr-TR, tr;q=0.9',
        'origin': 'https://www.maltinok.com',
        'referer': 'https://www.maltinok.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    ts = requests.get(source, headers=headers)


    print(str(datetime.datetime.now()) +" - " + source + " istek cevap suresi: " + str(datetime.datetime.now() - now));
    tsal = ts.text
    tsal = tsal.replace(videoid+'_','https://erdoganladevam.herokuapp.com/getstream?param=getts&source=https://edge10.xmediaget.com/hls-live/'+videoid+'/1/'+videoid+'_')
    return tsal

@app.route('/getstream',methods=['GET'])
def getstream():
    param = request.args.get("param")
    now = datetime.datetime.now();
    if param == "getts":
        source = request.url
        source = source.replace('https://erdoganladevam.herokuapp.com/getstream?param=getts&source=','')
        source = source.replace('%2F','/')
        source = source.replace('%3F','?')
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'tr-TR,tr;q=0.9',
            'origin': 'https://www.maltinok.com',
            'referer': 'https://www.maltinok.com/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        ts = requests.get(source,headers=headers)
        print(str(datetime.datetime.now()) +" - " + source + " istek cevap suresi: " + str(datetime.datetime.now() - now));
        return ts.content
    if param == "getm3u8":
        videoid = request.args.get("videoid")
        veriler = {"AppId": "3", "AppVer": "1025", "VpcVer": "1.0.11", "Language": "tr", "Token": "", "VideoId": videoid}
        r = requests.post("https://1xlite-2023337.top/cinema",json=veriler)
        if "FullscreenAllowed" in r.text:
            veri = r.text
            veri = re.findall('"URL":"(.*?)"',veri)
            veri = veri[0].replace("\/", "__")
            veri = veri.replace('edge3','edge10')
            veri = veri.replace('edge100','edge10')
            veri = veri.replace('edge4','edge10')
            veri = veri.replace('edge2','edge10')
            veri = veri.replace('edge5','edge10')
            veri = veri.replace('edge1','edge10')
            veri = veri.replace('edge6', 'edge10')
            veri = veri.replace('edge7', 'edge10')
            veri = veri.replace(':43434','')
            veri = veri.replace('edge100','edge10')
            if "m3u8" in veri:
                '''return "https://erdoganladevam.herokuapp.com/getm3u8?source="+veri+'&videoid='+videoid'''
                return "https://erdoganladevam.herokuapp.com/"+veri+'&videoid='+videoid
        else:
            return "Veri yok"

if _name_ == '__main__':
    app.run()
