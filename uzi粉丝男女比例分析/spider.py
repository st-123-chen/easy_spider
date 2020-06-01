import requests
import json
import time
import re
import datetime
import pandas as pd





def get_data(url):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'cookie': '_T_WM=58075284350; ALF=1592902971; MLOGIN=1; WEIBOCN_WM=3349; H5_wentry=H5; backURL=https%3A%2F%2Fm.weibo.cn%2Fcomments%2Fhotflow%3Fid%3D4499162437718729%26mid%3D4499162437718729%26max_id%3D448493162834369%26max_id_type%3D0; WEIBOCN_FROM=1110006030; SCF=ApcjrmxLCNw870QcK7Tt7zUFT_YmXJ1OwRrkKW9lOpzOz2ViyjmX9b8zlnemShwx7-N1NH0yKuPG10PL18_PRiI.; SUB=_2A25zzhoZDeRhGeFO41YS8y3OzTWIHXVRMKZRrDV6PUJbktANLVLEkW1NQVNiEBGY2bojyzVocA1DwlElALoVgqbp; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5UVZex9zR5KQY7pEAg8_JO5JpX5K-hUgL.FoM71hB0e0eESo.2dJLoIEXLxK.LBKeL12-LxKBLBonL12-LxK.L1-zLB-2LxKBLBo.L12zLxK-L1K5L1-zt; SUHB=0LcCfAx_6CLyKh; SSOLoginState=1590323785; XSRF-TOKEN=ad7199; M_WEIBOCN_PARAMS=oid%3D4499162437718729%26luicode%3D20000061%26lfid%3D4505499607451131%26uicode%3D20000061%26fid%3D4499162437718729'

    }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()

        return res.text
    except Exception as e:
        print("error")


def parse_data(html):
    json_data = json.loads(html)['data']['data']

    contents = []
    try:

        for item in json_data:
            # print(item)
            content = []
            content.append(item['user']['screen_name'])
            content.append(item['user']['gender'])
            content.append(item['text'])
            # content.append(item['profile_url'])
            # content.append(json_data['user'])
            print(content)
            contents.append(content)


        return contents
    except Exception as e:
        print(contents)
        print(e)

def save_data(contents):
    filename = 'E:\爬虫项目\weibo_spider\spider.CSV'

    dataframe = pd.DataFrame(contents)
    dataframe.to_csv(filename, mode='a', index=False, sep=',', header=False)



def run():
    url = url = 'https://m.weibo.cn/comments/hotflow?id=4493285776740181&mid=4493285776740181&max_id_type=0'
    html = get_data(url)
    contents = parse_data(html)
    save_data(contents)
    # try:
    #     max_id = json.loads(html)['data']['max_id']
    #     print(max_id)
    # except:
    #     print("error_01")
    max_id = json.loads(html)['data']['max_id']

    while max_id:
        url = 'https://m.weibo.cn/comments/hotflow?id=4493285776740181&mid=4493285776740181&max_id='+str(max_id)
        html = get_data(url)
        max_id = json.loads(html)['data']['max_id']
        contents = parse_data(html)
        save_data(contents)






if __name__ == '__main__':

    run()



