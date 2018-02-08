from bs4 import BeautifulSoup
import requests,sys

class downloader(object):
    def __init__(self):
        self.server='http://www.37zw.net/0/761/'
        self.target='http://www.37zw.net/0/761/'
        self.names=[]
        self.urls=[]
        self.nums=0
    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = 'GBK'
        html = req.text
        div_bf = BeautifulSoup(html,"lxml")
        div = div_bf.find_all('div', id='list')
        a_bf = BeautifulSoup(str(div[0]),'lxml')
        a = a_bf.find_all('a')
        self.nums=len(a)
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.server+each.get('href'))

    def get_contents(self,target):
        req = requests.get(url=target)
        req.encoding = 'GBK'
        html = req.text
        bf = BeautifulSoup(html,'lxml')
        texts = bf.find_all('div', id='content')
        texts = texts[0].text.replace('\xa0' * 4, '\n\n')
        return texts

    def writer(self,name,path,text):

        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

dl = downloader()
dl.get_download_url()
print('《雪地悍刀行》开始下载：')
for i in range(dl.nums):
    dl.writer(dl.names[i], '雪地悍刀行.txt', dl.get_contents(dl.urls[i]))
    sys.stdout.write("  已下载:%.1f%%" %(i/dl.nums*100) + '\r')
    sys.stdout.flush()
print('《雪地悍刀行》下载完成')




