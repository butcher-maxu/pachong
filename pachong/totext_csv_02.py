import pandas as pd

 #读取news_data.csv，保存到新建的news_data.txt中
data = pd.read_csv('comment_weiboComments_spider0508.csv', encoding='utf-8')
with open('news_data_02.txt','a+', encoding='utf-8') as f:
    for line in data.values:
        #str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        # f.write((str(line[0])+','+str(line[3])+','+str(line[4])+'\n'))
        f.write((str(line[5])+'\n'))

