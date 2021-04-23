# Week4 - Python webscraper

Chang Wang 20036997
<br />
<br />
WeTV TV series Ranking
https://v.qq.com/biu/ranks/?t=hotsearch&channel=tv 

<img src="https://static.wixstatic.com/media/27541e_2152ad2683a7414090a5c8a507a994ad~mv2.jpg/v1/fill/w_1480,h_1767,al_c,q_90,usm_0.66_1.00_0.01/27541e_2152ad2683a7414090a5c8a507a994ad~mv2.webp" style="zoom: 50%;" />

<br />

WeTV Variety Ranking
https://v.qq.com/biu/ranks/?t=hotsearch&channel=variety 

<img src="https://static.wixstatic.com/media/27541e_9d7f51bca33540039a85e3cb612727bb~mv2.jpg/v1/fill/w_1480,h_1764,al_c,q_90,usm_0.66_1.00_0.01/27541e_9d7f51bca33540039a85e3cb612727bb~mv2.webp" style="zoom: 50%;" />
<br />

Pass the **url address** and **type** of the WeTV Hotlist into **main**

```python
url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=tv"
type = "电视剧" #TV series
main(url,type)

url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=variety"
type = "综艺" #Variety
main(url, type)
```

<br />

Then execute the **main**.

The first line gets the content by requesting the url using the **get** method in **requests**.

```python
def main(url=None,type=None):
    data = requests.get(url).content.decode()
    html = etree.HTML(data)
    list_data = html.xpath('.//li[@class="item_list item_odd item_1"]')
    search_page(list_data,type)
```

<br />

The next step is to parse the data into html using the etree class in lxml.

Then html can use the xpath method to match the elements in the page.

<br />

The matching elements are

```python
. //li[@class="item_list item_odd item_1"]
```

<br />

Then, pass the retrieved data into the search_page method

```python
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
            # 如果detail 不再url里边   另外逻辑处理
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
```

Traverse the element list_data in the search_page method.

<br />

Then match the corresponding elements one by one and get the values

```python
save_db(dict_data)
```

<br />

Finally, pass the assembled data into the save_db method.

```python
file = open("QQtop.txt","a")
def save_db(dict_data):
    print(dict_data)
    file.write(str(dict_data))
    file.flush()
```

The save_db method is used to manipulate files and write data to them.

<br />

Once the program has run, a file is generated. In the file is the information captured for the WeTV Hotlist.

![](https://static.wixstatic.com/media/27541e_ab37a6414c184a17a6b367cb899fb7a1~mv2.png/v1/fill/w_1480,h_872,al_c,q_90,usm_0.66_1.00_0.01/27541e_ab37a6414c184a17a6b367cb899fb7a1~mv2.webp)
