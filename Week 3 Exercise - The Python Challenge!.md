# Week3 - Python challenge solutions to the first 7 challenges
Chang Wang 20036997

[[BLOG]](https://changw1006.wixsite.com/mysite/post/python-challenge-solutions-to-the-first-7-challenges)  

![](https://static.wixstatic.com/media/27541e_feba3dfc66e948d787f8e10d22f440d9~mv2.png/v1/fill/w_1200,h_549,al_c,q_90/27541e_feba3dfc66e948d787f8e10d22f440d9~mv2.webp)

[http://www.pythonchallenge.com/ ](http://www.pythonchallenge.com/) 



## **Level 0**

![](https://static.wixstatic.com/media/27541e_c6849efa764a44e192f11e2e361f3712~mv2.png/v1/fill/w_1200,h_549,al_c,q_90/27541e_c6849efa764a44e192f11e2e361f3712~mv2.webp)

The page shows the Hint: try to change the URL address. The picture shows 2 to the 38th power. I guess we need to work out the number, change the URL address and then we can move on to the next level.

````python
pow(2,38)
````

````python
274877906944
````

Replace the 0 in the URL address with 274877906944 and go to the next level.


* http://www.pythonchallenge.com/pc/def/274877906944.html  



## **Level 1**

![](https://static.wixstatic.com/media/27541e_ef3b7abeac8a44629f68cf1f38f3c129~mv2.png/v1/fill/w_1015,h_623,al_c,q_90/27541e_ef3b7abeac8a44629f68cf1f38f3c129~mv2.webp)

A string of incomprehensible letters is shown below the image. It is easy to find the pattern of these letters: the letter before it moves back two places is the letter after it. Based on our experience in the previous level, the current URL address is http://www.pythonchallenge.com/pc/def/map.html, and I guess that we need to replace the word “map”, and the rule of replacement is to push each letter back two places.

````python
text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
text_translate = ''for i in text:if str.isalpha(i):
        n = ord(i)if i >= 'y':
            n = ord(i) + 2 - 26else:
            n = ord(i) + 2
        text_translate += chr(n)else:
        text_translate += i
print(text_translate)
````

Get results: 
````python
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
````

The result prompts us to use “string.maketrans()” to do the calculation.
````python
import string

src_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# string.ascii_lowercase 
chars = string.ascii_lowercase
# string.maketrans()
trans = src_text.maketrans(chars, (chars[2:] + chars[:2]))
dst_text = src_text.translate(trans)print(dst_text)
````

````python
src_text = 'map'
dst_text = src_text.translate(trans)
print(dst_text)
````

````python
ocr
````

Change the “map” in the URL address to “ocr” and we can go to the second level.

* http://www.pythonchallenge.com/pc/def/ocr.html 



## **Level 2**

![](https://static.wixstatic.com/media/27541e_d29e860ce6a1496c87768d51caa3e1f8~mv2.png/v1/fill/w_1200,h_586,al_c,q_90/27541e_d29e860ce6a1496c87768d51caa3e1f8~mv2.webp)

The page shows MAYBE they are in the page source.

![](https://static.wixstatic.com/media/27541e_5fd6a6cb74334d5daf7a2c0aeba385fe~mv2.png/v1/fill/w_1480,h_820,al_c,q_90,usm_0.66_1.00_0.01/27541e_5fd6a6cb74334d5daf7a2c0aeba385fe~mv2.webp)

Hint: find the rare characters in the mess below.

````python
from collections import Counter
strings='''long characters'''
c = Counter(strings)
print(c.most_common())
````

The result is like this
````python
[(')', 6186), ('@', 6157), ('(', 6154), (']', 6152), ('#', 6115), ('_', 6112), ('[', 6108), ('}', 6105), ('%', 6104), ('!', 6079), ('+', 6066), ('$', 6046), ('{', 6046), ('&', 6043), ('*', 6034), ('^', 6030), ('\n', 1219), ('e', 1), ('q', 1), ('u', 1), ('a', 1), ('l', 1), ('i', 1), ('t', 1), ('y', 1)]
````
We can see that some letters appear once.

Print it out.
````python
from collections import Counter
strings='''long characters'''
c = Counter(strings)
print(c.most_common())
print(''.join([i[0] for i in c.items() if i[1]==1]))
````

The result is "equality".

* http://www.pythonchallenge.com/pc/def/equality.html  



## **Level 3**

![](https://static.wixstatic.com/media/27541e_ccdcdd963a0843d6b301b16ca82fca27~mv2.png/v1/fill/w_1200,h_586,al_c,q_90/27541e_ccdcdd963a0843d6b301b16ca82fca27~mv2.webp)

This level is similar to level 2. Hint: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides. As a rule of thumb, view the source code of the page.

![](https://static.wixstatic.com/media/27541e_6cd7bb005e534c43a2c3e1490a8d7cdf~mv2.png/v1/fill/w_1480,h_958,al_c,q_90,usm_0.66_1.00_0.01/27541e_6cd7bb005e534c43a2c3e1490a8d7cdf~mv2.webp)
````python
import requests
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
res = requests.get(url).text
text = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',res,re.S) #List change to str for traversing characters
str1 = ''.join(text)
````

````python
linkedlist
````

Change the URL address to http://www.pythonchallenge.com/pc/def/linkedlist.html. When we open the page, there is only one sentence “line linkedlist.php”, change the URL address again, get：

* http://www.pythonchallenge.com/pc/def/linkedlist.php 

This is the final result.



## **Level 4**

![](https://static.wixstatic.com/media/27541e_0282aa793f1545b19716b38ddaec057a~mv2.png/v1/fill/w_1480,h_722,al_c,q_90,usm_0.66_1.00_0.01/27541e_0282aa793f1545b19716b38ddaec057a~mv2.webp)

Click on the image, we can see a sentence “and the next nothing is 44827”. Still check the page source.

![](https://static.wixstatic.com/media/27541e_9d694af5f11e409e990c0ce77b61736b~mv2.png/v1/fill/w_1480,h_613,al_c,q_90,usm_0.66_1.00_0.01/27541e_9d694af5f11e409e990c0ce77b61736b~mv2.webp)

We can see that the green text suggests a library urllib, and then tells us DON'T TRY ALL NOTHINGS.
The URL address after we click on the image is http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345, and the text is “and the next nothing is 44827”.

````python
import requests
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
for i in range(400):
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+txt.split()[-1]
    r=requests.get(url)
    txt=r.text
    print(txt)
````

I tried about 400 times and printed out one of the times when it was about 250 or so, and this was the result:
````python
and the next nothing is 41643
and the next nothing is 23416
and the next nothing is 54432
and the next nothing is 4448
……………………
peak.html
and the next nothing is 72758
and the next nothing is 71301
````

It follows that replacing “linkedlist.php” in the previous level with “peak.html” will take us to the next level.

* http://www.pythonchallenge.com/pc/def/peak.html 



## **Level 5**

![](https://static.wixstatic.com/media/27541e_2e387eaa144d490cbde61dcaa53dc574~mv2.png/v1/fill/w_1480,h_713,al_c,q_90,usm_0.66_1.00_0.01/27541e_2e387eaa144d490cbde61dcaa53dc574~mv2.webp)

Hint: pronounce it. It doesn't seem to help. Let's check the page source.

![](https://static.wixstatic.com/media/27541e_031753c7a2b3427389a6cf27ad236b14~mv2.png/v1/fill/w_1206,h_586,al_c,q_90/27541e_031753c7a2b3427389a6cf27ad236b14~mv2.webp)

Get the notes: 
````python
<!-- peak hell sounds familiar ? -->
````

We can associate with the pickle library, get the URL address: http://www.pythonchallenge.com/pc/def/pickle.html. Open the page and we can see the phrase “yes! pickle!”

![](https://static.wixstatic.com/media/27541e_9db73189c00b4e35bf5f7e1812b257d1~mv2.png/v1/fill/w_521,h_224,al_c,lg_1,q_90/27541e_9db73189c00b4e35bf5f7e1812b257d1~mv2.webp)

The page title for this level is peak hell, and the source code of the modified page also has a peakhell tag. Let's try pickle.

````python
import pickle
from urllib.request import urlretrieve
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
urlretrieve(url, filename = 'five.pkl')
with open('five.pkl', 'rb') as f:
    r = pickle.load(f)
````

Results：
````python
[(' ', 95)], [(' ', 14), ('#', 5), (' ', 70), ('#', 5), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 6), ('#', 3), (' ', 6), ('#', 4), (' ', 3), ('#', 3), (' ', 9), ('#', 3), (' ', 7), ('#', 5), (' ', 3), ('#', 3), (' ', 4), ('#', 5), (' ', 3), ('#', 3), (' ', 10), ('#', 3), (' ', 7), ('#', 4), (' ', 1)], [(' ', 3), ('#', 3), (' ', 3), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 7), (' ', 5), ('#', 2), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 1), ('#', 7), (' ', 3), ('#', 4), (' ', 1), ('#', 7), (' ', 5), ('#', 3), (' ', 2), ('#', 3), (' ', 5), ('#', 4), (' ', 1)], [(' ', 2), ('#', 3), (' ', 5), ('#', 3), (' ', 2), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 3), ('#', 4), (' ', 4), ('#', 5), (' ', 4), ('#', 4), (' ', 2), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 5), ('#', 3), (' ', 3), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 4), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 2), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 10), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 7), ('#', 3), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 2), (' ', 3), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 7), ('#', 3), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 10), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 14), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 12), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 12), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 12), ('#', 4), (' ', 1)], [(' ', 2), ('#', 3), (' ', 6), ('#', 2), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 6), ('#', 2), (' ', 3), ('#', 4), (' ', 1)], [(' ', 3), ('#', 3), (' ', 4), ('#', 2), (' ', 3), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 11), (' ', 3), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 4), ('#', 3), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1)], [(' ', 6), ('#', 3), (' ', 5), ('#', 6), (' ', 4), ('#', 5), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 6), (' ', 4), ('#', 11), (' ', 4), ('#', 5), (' ', 6), ('#', 3), (' ', 6), ('#', 6)], [(' ', 95)]]
````

These numbers may represent the number of characters, change code:
````python
from urllib.request import urlretrieve
import pickle
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
urlretrieve(url, filename = 'five.pkl')
with open('five.pkl', 'rb') as f:
    r = pickle.load(f)
for i in r:
    for j in i:
        print(j[0] * j[1], end = '')
    print('\n')
````

Print: 

![](https://static.wixstatic.com/media/27541e_86c7c06b33b1437a935dcbfa03bb445f~mv2.jpg/v1/fill/w_1480,h_1302,al_c,q_90,usm_0.66_1.00_0.01/27541e_86c7c06b33b1437a935dcbfa03bb445f~mv2.webp)

It looks like the word channel, change the URL address and move on to the next level.

* http://www.pythonchallenge.com/pc/def/channel.html 



## **Level 6**

![](https://static.wixstatic.com/media/27541e_6ea7d07aea44459d941452eb63fd4d86~mv2.png/v1/fill/w_1480,h_733,al_c,q_90,usm_0.66_1.00_0.01/27541e_6ea7d07aea44459d941452eb63fd4d86~mv2.webp)

Check the page source.

![](https://static.wixstatic.com/media/27541e_40ac8617f21e4c8984c0a7b2e2a7f219~mv2.png/v1/fill/w_1480,h_497,al_c,q_90,usm_0.66_1.00_0.01/27541e_40ac8617f21e4c8984c0a7b2e2a7f219~mv2.webp)

One of the comments is 
````python
<! -- <-- zip --> 
````
and the picture also shows the zip on the trousers.


Change the URL address to  http://www.pythonchallenge.com/pc/def/channel.zip, we can download a zip file. Open it up and there are over nine hundred txt files in the folder, take a look around, the last one is a read me file.

![](https://static.wixstatic.com/media/27541e_7bf5e647026948558a95bc2b8a881099~mv2.png/v1/fill/w_871,h_286,al_c,lg_1,q_90/27541e_7bf5e647026948558a95bc2b8a881099~mv2.webp)

````python
import zipfile as zi

path = "C:\\Users\\sky\\Desktop\\channel.zip"

# Use the zipfile to decompress and read the contents of the file into files
files = {}
fzip = zi.ZipFile(path)
for name in fzip.namelist():
    with fzip.open(name) as fz:
        files[name] = fz.read().decode("utf-8")

# initial value of nothing in readme.txt
nothing = "90052"
while True:
    f = nothing + ".txt"
    strs=str(files[f])
    print(strs)
    try:
        nothing = strs.split()[-1]
    except:
        break
````

Results:
````python
……………………
Next nothing is 67824
Next nothing is 46145
Collect the comments.
````

Make changes to:
````python
import re
The code above
while True:
    fz = nothing + ".txt"
    # Get comment and output
    print(fzip.getinfo(fz).comment.decode("utf-8"), end="")
    if fz in files:
        # print(files[fz])
        result = re.search(r"Next nothing is (\d+)", files[fz])
        try:
            nothing = result.group(1)
        except:
            break
````

The result is: 
````python
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
````

Apparently, it's the word hockey. Get http://www.pythonchallenge.com/pc/def/hockey.html. Open the link, it's a line: it's in the air. look at the letters. 
![](https://static.wixstatic.com/media/27541e_d31ef6e7a9264e389ced1d199b30ea4e~mv2.png/v1/fill/w_778,h_263,al_c,lg_1,q_90/27541e_d31ef6e7a9264e389ced1d199b30ea4e~mv2.webp)

So the obvious answer is oxygen

* http://www.pythonchallenge.com/pc/def/oxygen.html 


## **Level 7**
![](https://static.wixstatic.com/media/27541e_7ab4cb6e3a6c4c27b02fea2556ab5bc3~mv2.png/v1/fill/w_1480,h_653,al_c,q_90,usm_0.66_1.00_0.01/27541e_7ab4cb6e3a6c4c27b02fea2556ab5bc3~mv2.webp)

A very thin image with a mosaic section in the middle of the image. Processing the image using PIL.
````python
from PIL import Image 
im = Image.open("oxygen.png")  # File path
width, height = im.size  # Get Size
pic = im.load()
h = height // 2
for x in range(width):  
    print(pic[x,h])
````

Results：
````python
……………………
(97, 97, 97, 255)
……………………
(100, 100, 100, 255)
……………………
……………………
(116, 116, 116, 255)
……………………
````

You can see that R, G, B are the same, so I guess it could be an ASCII code.
````python
from PIL import Image 
im = Image.open("oxygen.png")  # The path to the file, if there is no path it is the file in the current directory
width, height = im.size  # Get image size
pic = im.load()
h = height // 2
ss=0  # ss is a random intermediate variable that I define to store the last value
for x in range(width):
    r, g, b, x = pic[x, h]
    if r != g:
        continue
    if ss!=r:
        print(chr(r), end='')
    ss=r
````

Print：
````python
smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]
````

````python
answer = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for l in answer:
    print(chr(l), end='')
````

Output integrity. Get the new URL address.

* http://www.pythonchallenge.com/pc/def/integrity.html 


#### Done!



## **Summary**

0: http://www.pythonchallenge.com/pc/def/274877906944.html

1：http://www.pythonchallenge.com/pc/def/ocr.html

2：http://www.pythonchallenge.com/pc/def/equality.html

3：http://www.pythonchallenge.com/pc/def/linkedlist.php

4：http://www.pythonchallenge.com/pc/def/peak.html

5：http://www.pythonchallenge.com/pc/def/channel.html

6：http://www.pythonchallenge.com/pc/def/oxygen.html

7：http://www.pythonchallenge.com/pc/def/integrity.html
