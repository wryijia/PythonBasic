import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import time

"""
    爬取代理网站的免费代理并返回
"""


class Crawler(object):

    def get_crawler_proxy(self):
        proxy_list_xici = self.crawl_xici()
        proxy_list_66 = self.crawl_66()
        proxy_list_kuaidaili = self.crawl_kuaidaili()
        return proxy_list_xici + proxy_list_66 + proxy_list_kuaidaili

    def crawl_xici(self):
        """
            爬取西刺代理
        """
        print('爬取西刺代理......')
        proxy_list = []
        for i in range(1, 20):
            try:
                url = 'http://www.xicidaili.com/nn/' + str(i)
                # url = 'http://www.baidu.com'
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'www.xicidaili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                if res.status_code == 200:
                    doc = pq(res.text)
                    for odd in doc('.odd').items():
                        info_list = odd.find('td').text().split(' ')
                        # print(info_list)
                        if len(info_list) == 11:
                            proxy = info_list[1].strip() + ':' + info_list[2].strip()
                            proxy = proxy.replace(' ', '')
                            proxy_list.append(proxy)
            except Exception as e:
                continue
        print('爬取到西刺代理 %s 个' % len(proxy_list))
        return proxy_list


    def crawl_66(self):
        """
            爬取66代理
        """
        print('爬取66代理......')
        proxies = set()
        for i in range(2, 50):
            try:
                url = 'http://www.66ip.cn/' + str(i) + '.html'
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'www.66ip.cn',
                    'Referer': 'http://www.66ip.cn/',
                    'Cookie': 'yd_cookie=9ec1ced4-ed0d-4cc6f642d3cad3acd1e747a5d08e8699e047; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1543369812,1543391648,1543454297,1543800567; _ydclearance=16fa6a58623529898e43ea54-c25d-4351-890e-4671a1f592b9-1543838015; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1543830819',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                # print(res.status_code)
                # print(res.text)
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.select('.container table tr')

                for i in range(1, len(items)):
                    tds = items[i].select('td')
                    ip = tds[0].string
                    port = tds[1].string
                    proxy = ip + ':' + port
                    if proxy:
                        # print(proxy)
                        # print(proxy.replace(' ', ''))
                        proxies.add(proxy.replace(' ', ''))
            except Exception as e:
                continue
        print('爬取到66代理 %s 个' % len(proxies))
        return list(proxies)


    def crawl_kuaidaili(self):
        print('爬取快代理......')
        proxies = set()
        for i in range(1, 50):
            try:
                url = 'https://www.kuaidaili.com/free/inha/' + str(i)
                time.sleep(1)
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'www.kuaidaili.com',
                    'Referer': 'http://www.66ip.cn/',
                    'Cookie': 'channelid=0; sid=1543828498576461; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1543828501; _ga=GA1.2.2019923346.1543828501; _gid=GA1.2.1278257690.1543828501; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1543828618',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                # print(res.status_code)
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.select('#list tbody tr')
                for item in items:
                    tds = item.select('td')
                    ip = tds[0].string
                    port = tds[1].string
                    proxy = ip + ':' + port
                    if proxy:
                        proxies.add(proxy.replace(' ', ''))
            except Exception as e:
                continue
        print('爬取到块代理 %s 个' % len(proxies))
        return list(proxies)

