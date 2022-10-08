import requests
import json
import datetime


cityid =input("请输入城市ID（身份证号前六位）：")
url = "https://api.map.baidu.com/weather/v1/?district_id="+cityid+'&data_type=all&ak=o2a72xt7WfcKAfPXj3jo6xcYc6l3ZOFP'


#canshu = '&data_type=all&ak=o2a72xt7WfcKAfPXj3jo6xcYc6l3ZOFP'
#apikey = 'o2a72xt7WfcKAfPXj3jo6xcYc6l3ZOFP'
#geturl = url + cityid + canshu


resp = requests.get(url)
resp_dict = resp.json()

# print(resp_dict.keys())


#地区获取
result = resp_dict['result']
location = result['location']
dq = list(location.values())[:3]
for key in dq:
    print(key,end='')
print( )



#地区温度获取
now = result['now']
tq = list(now.values())[:5]
#print("天气:",tq[0])
lieb = ['今日天气:','当前温度:','体感温度','湿度:','风速:','风向:']
tq1 = dict(zip(lieb,tq))
for tq12,value in tq1.items():
    print(tq12,value,end=' \n')



 #地区获取总和
#nowwather = "今日天气:",how + '当前温度:',dangqian + '体感温度:',feels_like + '湿度:',rh + '风速',wind_class + '风向:',wind_dir
#print(result)
#print(locationss)
#print("今日天气:",how,'\n当前温度:',dangqian,'\n体感温度:',feels_like,'\n湿度:',rh,'\n风速',wind_class,'\n风向:',wind_dir)

