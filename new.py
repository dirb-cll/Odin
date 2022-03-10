# 开发者:odin
# 开发时间:2022/3/10
# 文件名称:PyCharm
# coding:UTF-8
'''
numbers = 3
price = 25.8
amount = numbers*price
print('数量：',numbers)
print('价格',price)
print('金额:{:.2f}元'.format(amount))

x = "a"
y = 'b'
print(x,end=' ')
print(y)

a = input('输入密码:')
print('你输入的密码是:',a)

pice = 20
num = input('请输入给岩岩买的数量：')
a = '商品编码'
b = '物品名称'
c = '数量'
d = '商品金额'
e = '12567'
f = 'Tank300'
g = num
h = ('{}'.format(int(num) * pice))
print(a,end="  ")
print(b,end='   ')
print(c,end='   ')
print(d)
print('-'* 25)
print(e,end=' ')
print(f,end='   ')
print(g,end='辆   ')
print(h,"万")
name = input('签名：')

print(2**15)

wid = input("wid=")
wid = 20
hig = 5 * 9
x = int(wid) * hig
print(x)

x="李明"
print(type(x))
print(id(x))
'''
num1 = 1
pri1 = 45.20
amount = num1
num2 = 1
pri2 = 59.30
amount = amount + num2
total =num1 * pri1 + num2 * pri2
discount = 40
payable = total - discount
aver = total / amount
print('商品总：',total)
print('商品优：',discount)
print('实付：'+str(payable))
print('平均：'+str(aver))