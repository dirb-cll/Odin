import json
import time
import datetime
import requests

urla = input("请输入要查询的hash值：")
urlb = "https://apilist.tronscan.org/api/transaction-info?hash="
url = urlb + urla
resp = requests.get(url,verify=False)
#print(f"当前状态为：{resp}")
resp_dict = resp.json()
#print(resp_dict.keys())
print( )
pepo = resp_dict['contractData']
popo = pepo['owner_address']
popc = pepo['contract_address']
times = resp_dict['timestamp']

#交易数量，及网络协议
quantity = resp_dict['tokenTransferInfo']
quantit = quantity['amount_str']
ssxinxi = quantity['symbol']
ssxxin = quantity['tokenType']
num_quantit = float(quantit)
print("交易数量为:",num_quantit/1000000,"\n交易币种:",ssxinxi,"\n交易网络:",ssxxin)

#交易信息

#时间戳转换时间
timestamp = times
time_local = time.localtime(timestamp/1000)
datr = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
print("交易时间为：",datr)
print( )
print(f"主地址是：{popo}\n次地址是:{popc}\n")

#地址判断
if popo != "TLX1LF1mjiEnqniWxQ6mELSqJmGMXoYHZG":
    print("此hash地址与交易地址不符，请输入正确hash")
elif num_quantit < 58:
    print('正确')
else:
    print('数量不对，请联系你爹处理')


