"""
步骤:
1 确定正确的url
   分析图片url
2 使用requests模块 数据（大范围数据）
3 数据解析
4 数据保存(本地文件。数据库)


"""
import requests
import json
import time
import pprint#换行
star_time=time.time()  #获取时间戳
# 1.确定正确url
base_url="https://pvp.qq.com/web201605/js/herolist.json"
#伪装表头
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54'}
# 2 .请求数据（大范围数据) ctr+/快速注释
response=requests.get(url=base_url,headers=headers)
#rint(response)
data_list=response.json()
#pprint.pprint(data_list) #gbk(windows系统默认的编码)  utf-8  get(明文请求) post(加密请求)

#3解释数据
for data in data_list:
    #打印字典
    #print(data_list)
    cname=data['cname']
    ename=data['ename']
    try:
     skin_name=data['skin_name'].split('|')
    except Exception as e:
        print(e)
    #print(cname,ename,skin_name)
    #构建英雄皮肤的循环
    for skin_num in  range(1,len(skin_name)+1):
        #http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/522/522-bigskin-1.jpg
        #http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/+英雄的id+/+英雄id-bigskin-皮肤序号+.jpg
        skin_url='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(ename)+'/'+str(ename)+'-bigskin-'+str(skin_num)+'.jpg'
        #print(skin_url)
        skin_data=requests.get(url=skin_url,headers=headers).content
        #数据保存
        with open('img\\'+cname+'-'+skin_name[skin_num - 1] +'.jpg',mode='wb') as f:
            print("正在下载皮肤:",cname+'-'+skin_name[skin_num - 1])
            f.write(skin_data)
end_time=time.time()
print('共花费世界:',int(end_time-star_time))
print('数据爬取完成')