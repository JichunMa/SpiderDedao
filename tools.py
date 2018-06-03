import random
import requests
import time


def startDownload(self, url, name):
    # 随机停时间
    if removeChoice(name):
        return
    time.sleep(random.randint(1, 5))
    data = requests.get(url)
    if data.status_code == 200:
        # todo 名称提出去
        with open('./DeDaoData/' + name + '.m4a', 'wb')as f:
            f.write(data.content)
    else:
        print('download error')


# 自定义功能
def removeChoice(name):
    if '精选' in name:
        return True
    else:
        return False
