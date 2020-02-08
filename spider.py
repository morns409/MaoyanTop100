import json
import requests
from requests.exceptions import RequestException
import re
from multiprocessing import Pool


def get_one_page(url):
    """获取单页数据"""
    try:
        head = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        response = requests.get(url, headers=head)
        # 判断返回的状态码是成功的
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_on_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>'
                         + '.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        response = requests.get(item[1])
        with open('TopImage/' + item[2] + '.jpg', 'wb') as f:
            f.write(response.content)
            f.close()
        """yield 生成器"""
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    for item in parse_on_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    """
    for i in range(10):
        main(i*10)
    """
    pool = Pool()  # 使用多进程
    pool.map(main, [0,10,20,30,40,50,60,70,80,90,100])