import random
import requests
import time

folder_name = '/Users/zero/Desktop/dedao/'

def startDownload(url, name):
    # 精选类型不下载
    if removeChoice(name):
        return
    # 随机停时间
    # time.sleep(random.randint(1, 3))
    data = requests.get(url)
    if data.status_code == 200:
        with open(folder_name + name + '.m4a', 'wb')as f:
            f.write(data.content)
    else:
        print('download error')


# 自定义功能(精选不下载)
def removeChoice(name):
    if '精选' in name:
        return True
    else:
        return False
