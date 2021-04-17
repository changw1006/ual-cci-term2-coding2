import datetime
import hashlib
import time

import requests
from lxml import etree
file = open("QQtop.txt","a")
def save_db(dict_data):
    print(dict_data)
    file.write(str(dict_data))
    file.flush()

def search_page(list_data,type):
    for x in list_data:
        try:
            url = x.xpath("div[1]/a/@href")[0]
            num = x.xpath("div[1]/span/text()")[0]
            name = x.xpath("div[1]/a/@title")[0]
            search = requests.get(url).text
            search_html = etree.HTML(search)
            details_url = search_html.xpath(".//a[@class='figure result_figure']/@href")[0]
            img_url = search_html.xpath(".//a[@class='figure result_figure']/img/@src")[0]
            # If the detail is not in the url, the logic is handled separately
            # print(details_url)
            if "detail" not in details_url:
                if "cover" in details_url:
                    pass
                else:
                    try:
                        details_url = search_html.xpath(".//li[@class='list_item']/a/@href")[0]
                        img_url = search_html.xpath(".//li[@class='list_item']/a/img/@src")[0]
                    except:
                        continue

            dict_data = {}
            dict_data["source"] = "TENCENT"
            dict_data["sourcePsId"] = details_url.split('/')[-1].split(".")[0] + "_TENCENT"
            dict_data["topType"] = "热播榜"
            dict_data['dataType'] = type
            dict_data['time'] = str(datetime.datetime.now())[0:10]
            dict_data["heatIndex"] = ""
            dict_data["playIndex"] = ""
            dict_data["createTime"] = str(datetime.datetime.now())[0:19]
            dict_data['updateTime'] = str(datetime.datetime.now())[0:19]
            dict_data['num'] = int(num)
            dict_data['name'] = name
            dict_data['poster'] = "https:" + img_url
            dict_data['herf'] = details_url
            dict_data["_id"] = hashlib.md5((dict_data["source"] + dict_data["topType"] + dict_data['name'] + dict_data['time']).encode()).hexdigest()
            save_db(dict_data)
        except:
            import traceback
            traceback.print_exc()
            print("123")
            continue
def main(url=None,type=None):
    data = requests.get(url).content.decode()
    html = etree.HTML(data)
    list_data = html.xpath('.//li[@class="item_list item_odd item_1"]')
    search_page(list_data,type)
if __name__ == '__main__':
    # while 1:
        url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=tv"
        type = "电视剧"
        main(url,type)

        url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=variety"
        type = "综艺"
        main(url, type)

        # url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=cartoon"
        # type = "动漫"
        # main(url, type)
        #
        # url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=child"
        # type = "儿童"
        # main(url, type)
        #
        # url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=movie"
        # type = "电影"
        # main(url, type)
        #
        # url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=doco"
        # type = "纪录片"
        # main(url, type)
        # time.sleep(21600)

