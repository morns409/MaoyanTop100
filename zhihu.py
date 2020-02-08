'''
项目:
    获取知乎粉丝信息
时间:
    2018-03-30
'''
# 导入相关模块 
import requests # pip install requests
import nobug

# 过程式编程
# 每页返回20条用户信息 所以要进行翻页
# 采用循环来翻页

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}

with open('zhihu.txt', 'a', encoding='utf-8') as ff:

    for m in range(0,100,20):
        # 每一页的网址
        url = 'https://zhuanlan.zhihu.com/api/columns/hsmyy/followers?limit=20&offset='+str(m)
        # 获取json文件
        html = requests.get(url, headers=header)
        # 打印访问网络的状态  如果返回200代表正常  否则代表错误
        print(html.status_code)
        # 动态判断每页返回多少个个人信息
        for n in range(len(html.json())):
            print(html.json())
            #profileUrl = html.json()['data'][n]
            # profileUrl 写入本地
            #ff.write(profileUrl+'\n')
            
#nobug.NoBug().foZu()
