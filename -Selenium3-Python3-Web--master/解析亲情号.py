from bs4 import BeautifulSoup
import requests
from 读写文件 import write
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "accessToken": "MC0yNTY5Ni02MjFkNzRmYmQxMzA1"
}
urls = ['http://119.3.108.139:48000/sgs-api/v1/mdmmanager/contactList?name=&phone=&page={}'.format(str(i))
        for i in range(1, 2)]

print(urls)


def get_res(urls, data=None):
    web_data = requests.get(urls, headers=headers)
    list = web_data.json()['data']['list']
    for i in list:
        #获取亲情号信息
        print(i[''])
    # 查看成员
    # for i in list:
    #     Id = i['Id']
    #     memberUrl = 'http://119.3.108.139:48000/sgs-api/v1/mdmmanager/contactMemberList?name=&phone=&page=1&contactId={}&permission='.format(
    #         str(Id))
    #     member = requests.get(memberUrl, headers=headers)
    #     memberList = member.json()['data']['list']
    #     for i in memberList:
    #         if (len((i['Id'])) == 0):
    #             print('yes')
    #         print(i['DisplayName'])

for titles in urls:
    get_res(titles)

write()