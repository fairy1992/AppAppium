# coding: utf-8

import pytesseract
from PIL import Image

# image = Image.open("/Users/Fairy/Downloads/7.png")
# print 1
#
# code = pytesseract.image_to_string(image)
# print code


def getverify(name):
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 对于识别成字母的 采用表格进行修正
    rep = {'O': '0',
           'I': '1',
           'L': '1',
           'Z': '2',
           'S': '8'
           }
    # 打开图片
    im = Image.open(name)
    # 转化到灰度图
    imgry = im.convert('L')
    # 保存图像
    imgry.save('g'+name)
    # 二值化， 采用阈值分割法，threshold为分割点
    out = imgry.point(table,'1')
    out.save('b'+name)
    text = pytesseract.image_to_string(out)
    text = text.strip()
    text = text.upper()
    for r in rep:
        text = text.replace(r, rep[r])
    print text

    ttext = text.replace(',', '')
    ttext = ttext.replace(' ','')
    print ttext
    text1 = ttext[len(ttext)-4:]
    print text1

    return text1
getverify('8.jpg')


