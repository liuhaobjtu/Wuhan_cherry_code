from PIL import Image, ImageDraw, ImageFont
import cv2
import os

def draw(pic):
    img = cv2.imread('pic/' + pic)
    img = img[:, :, (2, 1, 0)]  # 应该是BGR转RGB

    blank = Image.new("RGB", [len(img[0]), len(img)], "white")
    drawObj = ImageDraw.Draw(blank)

    n = 10

    # font = ImageFont.truetype('C:/Windows/Fonts/Microsoft YaHei UI/msyhbd.ttc', size=n - 1)
    font = ImageFont.truetype('SimHei.ttf', size=n - 1)               # ubuntu系统下，这个字体对汉字管用
    # font = ImageFont.truetype('Times New Roman.ttf', size=n - 1)    # ubuntu系统下，这个字体对汉字不管用

    for i in range(0, len(img), n):
        for j in range(0, len(img[i]), n):
            text = '武汉加油'
            drawObj.ink = img[i][j][0] + img[i][j][1] * 256 + img[i][j][2] * 256 * 256
            drawObj.text([j, i], text[int(j / n) % len(text)], font=font)
            # print('完成处理——', i, j)     # 尽量别打印，程序运行太慢

    blank.save('new/new_' + pic, 'jpeg')


filelist = os.listdir('pic')
for file in filelist:
    draw(file)
