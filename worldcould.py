

import  jieba                                      #分词
from matplotlib import pyplot as plt               #绘图，数据可视化（静态图片）
from wordcloud import WordCloud,STOPWORDS                    #词云
from PIL import  Image                             #图片处理
import numpy as np                                 #矩阵运算
import sqlite3


#从数据库内取出数据
con=sqlite3.connect("movie.db")
cur = con.cursor()
sql ='select instroduction from movie250'
data =cur.execute(sql)
text = ""
for item in data:
    text =  text + item[0]
    # print(item[0])
print(text)
cur.close()
con.close()

#将数据分词
cut= jieba.cut(text)
string = ' '.join(cut)
print(string)





#中文停用词
stopwords = set()
content = [line.strip() for line in open('stop.txt', 'r',encoding="utf-8").readlines()]    #需要使用python能懂得utf-8
stopwords.update(content)




img = Image.open(r'tree.jpeg')   #打开遮罩图片
img_arr= np.array(img)
wc= WordCloud(
    background_color="white",
    mask=img_arr,
    stopwords = stopwords,
    font_path="msyhbd.ttc"
)
wc.generate_from_text(string)



#绘制图片
flg= plt.figure(1)
plt.imshow(wc)
plt.axis('off')                     #是否显示坐标轴

# plt.show()                        #显示生成的词云图片


plt.savefig(r'.')

