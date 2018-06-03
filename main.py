import requests
from requests import Response

from model import DeDaoModel
from tools import startDownload

headers = {
    "X-App-Key": "android-4.0.0"
    , "X-Uid": "11772872"
    , "X-U": "11772872"
    , "X-Thumb": "xl"
    , "X-Dt": "phone"
    , "X-Ov": "8.0.0"
    , "X-Net": "WIFI"
    , "X-Os": "ANDROID"
    , "X-D": "bb10546ba86ea9c6"
    , "X-Dv": "DUK-AL20"
    , "X-Chil": "0"
    , "X-V": "2"
    , "X-Av": "4.0.0"
    , "X-Scr": "4.0"
    , "X-Adv": "1"
    , "X-Ts": "1528034608"
    , "X-S": "b271e66881c91499"
    , "X-Seid": "9868b3af52c2cdd12dad3654d975da91"
    , "X-Hitdot": ""
    , "X-Sign": "YjU3ZDdmOTk4NDVmN2ZjMTMwYTc4YzdmNDYwM2U3MGY="
    , "X-Nonce": "0e97cabc88a91263"
    , "X-Timestamp": "1528035689"
    , "X-Ts": "1528035689"
    , "Content-Type": "application/x-www-form-urlencoded"
    , "Content-Length": "561"
    , "Host": "entree.igetget.com"
    , "Connection": "Keep-Alive"
    , "Accept-Encoding": "gzip"
    , "User-Agent": "okhttp/3.10.0"
}
url = 'https://entree.igetget.com/acropolis/v1/audio/listall'
data = {'column_id': '2',
        'h': '{"u":"11772872","thumb":"xl","dt":"phone","ov":"8.0.0","net":"WIFI","os":"ANDROID","d":"bb10546ba86ea9c6","dv":"DUK-AL20","t":"json","chil":"0","v":"2","av":"4.0.0","scr":"4.0","adv":"1","ts":"1528035689","s":"b271e66881c91499","seid":"9868b3af52c2cdd12dad3654d975da91","hitdot":""}',
        'count': '574',
        'max_id': '0',
        'section': '0',
        'since_id': '0',
        'order': '1'}
if __name__ == '__main__':
    model_list = []
    info_list = []
    response_data = requests.post(url, headers=headers, data=data)
    if response_data.status_code == 200:
        json_data = response_data.json()
        info_list = json_data['c']['list']
        for info in info_list:
            audio_detail = info['audio_detail']
            if audio_detail:
                title = ''.join(audio_detail['title'])
                mp3_play_url = ''.join(audio_detail['mp3_play_url'])
                model = DeDaoModel(title, mp3_play_url)
                model_list.append(model)
            else:
                print('数据项为空')

        # 下载数据
        print('total--' + str(len(model_list)))
        finish_index = 0
        for model in model_list:
            startDownload(model.url, model.name)
            finish_index = finish_index + 1
            print('finish--' + str(finish_index))

else:
    print('接口请求失败')
