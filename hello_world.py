
print("hello world")
print(chr(98)) #chr转ASCII码
fp=open('note.txt','w') #打开文件
print('hello world',file=fp) #写入文件内容
fp.close() #关闭文件

##多条print函数输出结果一行显示
print('Gelatoni',end='-->')
print('玲娜贝儿')#没有修改结束符，会有空行
#加号连接字符串（只能连接字符串）
print('杰拉多尼'+'零纳贝尔')

#input函数使用
name=input('请输入姓名') #input保存为字符串
print('名字为:'+name)

## 输入整数类型的数据

num=input('input a number')
print('the number is:'+num)
num=int(num)#保存为整数
print('the number is：',num)#使用逗号在同一行输出

##代码缩进



#第一章作业1
print("人生苦短，我用python")

fp=open('note2.txt','w') #打开文件
print('人生苦短，我用python',file=fp) #写入文件内容
fp.close() #关闭文件



#第一章作业2
name=input('please input your name:')
age=input('please input your age:')
slogan=input('please input your slogan:')
print('your name is:'+name)
print('your age is:'+age)
print('your slogan is:'+slogan)


#查询保留字（保留字区分大小写）
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist)) #获取保留字个数

#变量的定义和使用
luck_number=16 #整形变量
my_name='syj' #字符型变量
print('the type of luck_number is:',type(luck_number)) #查看变量类型
print(my_name,'的幸运数字是:',luck_number)

#在python中允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(no))  #id()查看对象内存地址
print(id(number))

#常量定义
pi=3.1415 #定义一个变量
PI=3.1415 #定义一个常量
print(PI)

#整数的四种表示形式
num=987 #十进制
num2=0b1010101 #二进制
num3=0o765 #八进制
num4=0x87ABF #十六进制
print(num,num2,num3,num4)

#浮点数类型的使用
height=185.6
print(type(height))
print(0.1+0.2) #不确定的尾数问题0.30000000000000004
print(round(0.1+0.2,1)) #保留一位小数，0.3

#复数类型的使用
x=123+456j
print(x.real) #实数部分
print(x.imag) #虚数部分

#转义字符的使用
print('北京\n欢迎你') #\n换行符，可以连续换多行
print('北京\t欢迎你') #\t制表符
print('老师说\"好好学习，天天向上\"') #老师说"好好学习，天天向上"
print(r'北京\n欢迎你') #北京\n欢迎你,jia'r加入r,转义字符失效

#字符串索引和切片
s='HELLOWORLD'
print(s[0],s[-10]) #H H
print('北京欢迎你'[3]) #迎
print(s[2:7]) #LLOWO,从2开始到7结束不包含7
print(s[-8:-3]) #LLOWO
print(s[:5]) #默认N从0开始，HELLO
print(s[5:]) #默认切到字符串结尾，WORLD

#字符串类型的操作
x='2022'
y='北京冬奥会'
print(x+y)
print(x*10)
print('北京'in y) #True
print('北京'in x) #False

#布尔类型的使用
x=True
print(x)
print(type(x)) #<class 'bool'>
print(x+10) #11
print(False+10)
print(bool(18)) #测试18的布尔值 True
print(bool(0),bool(0.0))

#数据类型的转换
x=10
y=3
z=x/y
print(z,type(z)) #自动转换成浮点数

#float转成int类型，只保留整数
print('float类型转成int类型',int(3.14))

#chr() ord()一对
print(ord('杨')) #杨在unicode表中对应的整数值
print(chr(26472)) #26472整数在unicode表中对应的字符

#进制转换
print('十进制转成十六进制:',hex(26472))
print('十进制转成八进制:',oct(26472))
print('十进制转成二进制:',bin(26472))

#eval函数的使用
s='3.14+3'
print(s,type(s))
x=eval(s) #去掉字符串左右的引号,执行加法运算
print(x,type(x))


#eval函数经常与input()函数一起使用，用来获取用户输入的数值
age=eval(input('请输入你的年龄:')) #将字符串类型转换成了int类型，相当于int(age)
print(age,type(age))


#算数运算符的使用
print('加法:',1+1)
print('减法:',1-1)
print('乘法:',3*5)
print('除法:',10/3)
print('整除',10//3)
print('取余数：',10%3)
print('幂运算:',2**4)

#赋值运算符
x=20
y=10
x=x+y
print(x)
x+=y #x=x+y
print(x+y)
#python支持链式赋值
a=b=c=100
print(a,b,c)
#python支持系列解包赋值
a,b=10,20
print(a,b)
#交换变量的值
a,b=b,a
print(a,b)

#比较运算符的使用
print('98大于90吗',98>90) #True
#逻辑运算符的使用
print(True and True)
print(True and False)
print(False and False)
print('—'*50)
print(True or False)
print(not(8>7))

#位运算符
print('按位与运算',12&8)
print('按位取反',~123)

##从键盘获取一个四位整数，分别输出个位，十位，百位，千位上的数字
num=eval(input('请输入一个四位整数:'))
print('个位上的数是:',num%10)
print('十位上的数是:',num//10%10 )
print('百位上的数是:',num//100%10)
print('千位上的数是:',num//1000)
#索引也可以
num=input('请输入一个四位整数:') #num是一个字符串类型
print('个位上的数是:',num[3])
print('十位上的数是:',num[2] )
print('百位上的数是:',num[1])
print('千位上的数是:',num[0])

##根据父母身高预测儿子的身高
father=float(input('请输入父亲的身高:'))
mother=float(input('请输入母亲的身高：'))
son=(father+mother)*0.54
print('儿子的身高为:',son)


#单分支结构
number=eval(input('请输入你的号码:'))
if number==2345: #结果为布尔类型
    print('恭喜你，中奖了')
if number!=2345:
    print('您未中奖')

x=input('请输入一个字符串')
if x:
    print('x是一个非空字符串')
if not x:
    print('x是一个空字符串')

#双分支结构
number=eval(input('请输入你的号码:'))
if number==2345: #结果为布尔类型
    print('恭喜你，中奖了')
else:
    print('您未中奖')

#多分支结构
score=eval(input('请输入您的成绩:'))
if score<60:
    print('您未及格')
elif 60<=score<=76:
    print('您的成绩为良')
elif 77<=score<=90:
    print('您的成绩为中等')
else:
    print('您的成绩为优秀')

#嵌套if的使用
answer=input('您喝酒了吗:')
if answer=='y':
    proof=eval(input('请输入酒精含量'))
    if proof>=60:
        print('您已醉驾')
    else:
        print('酒精含量在安全范围内')
else:
    print('你走吧。没你事')

#使用and连接多个条件
name=input('请输入您的姓名:')
password=input('请输入您的密码:')
if name=='syj'and password=='123456':
    print('密码正确！')
else:
    print('密码错误')


#使用or连接多个选择条件
score=eval(input('请输入你的考试成绩:'))
if score==0 or score>100:
    print('成绩无效')
else:
    print('成绩有效')

#python3.11新特性 模式匹配
score=input('请输入您的成绩:')
match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('中等')
    case 'D':
        print('差')
    case 'E':
        print('不及格')


#遍历字符串
for i in 'hello':
    print(i)

for i in range(1,20): #range函数，产生一个【n,m)的整数序列，包含n不包含m

    if i%2==0:
        print(i,'是偶数')
    else:
        print(i)


#计算1到10之间的累加和
sum=0
for i in range(1,21):
    sum+=i
print(sum)

print('-------100到999之间的水仙花数')
for i in range(100,1000):
    sd=i%10 #获取个位上的数字
    tens=i//10%10 #获取十位上的数字
    hundred=i//100
    #判断水仙花数
    if sd**3+tens**3+hundred**3==i:
        print(i,'是水仙花数')

#for...else结构
sum=0
for i in range(1,21):
    sum+=i
else:
      print(sum)
#无限循环while的使用
answer=input('你今天去上课吗？y/n')  #初始化变量
while answer=='y': #(2)条件判断
    print('好好学习，天天向上') #语句块
    answer=input('你今天去上课吗？y/n') #改变变量


#计算1到100的累加和
s=0
i=1 #初始化变量
while i<101: #(2)条件判断
    s+=i#语句块
    i+=1#改变变量
print(s)

#使用无限循环模拟用户登录
i=0 #(1)初始化变量
while i<3: #（2）条件判断
    user_name=input('请输入用户名：') #（3）语句块
    pass_word=input('请输入密码:')
    if user_name=='syj' and pass_word=='123456':
       print('用户名和密码正确，系统正在登陆')
       i=8 #（4）改变变量，目的：退出循环
    else:
        if i<2:
           print('用户名或密码不正确,您还有',2-i,'次机会')
        i+=1
if i==3:
    print('三次机会已用完')


#嵌套循环
for i in range(1,4): #控制行数
    for j in range(1,5): #控制列数
     print('*',end='')
    print() #换行

for i in range(1,6): #控制行数
    for j in range(1,i+1):
        print('*', end='')
    print()  # 换行


#倒三角形

for i in range(1,6):
    for j in range(1,7-i):
        print('*', end='')
    print()


#等腰三角形
for i in range(1,6):
    for j in range(1,7-i):
        print(' ',end='')
    for q in range(1,i*2):
        print('*',end='')
    print()


#菱形（奇数行 两个等腰三角形组成）
row=eval(input('请输入菱形的行数：'))#判断菱形行数
if row%2==0:
    print('无法打印菱形')

else:
    print('即将打印菱形')
    top_row=(row+1)//2+1
    for i in range(1,top_row):
       for j in range(1,top_row-i):
        print(' ',end='')
       for q in range(1,i*2):
          print('*',end='')
       print()
#菱形下半部分：直角三角形和倒着的三角形
    bottom_row=row//2
    for i in range(1,bottom_row+1):
     for j in range(1,i+1):
        print(' ',end='')
     for k in range(1,row-2*i+1): #第一行：range(1,6) 第二行：range(1,4) 第三行 range(1,2)
        print('*',end='')
     print('')


#空心菱形
row=eval(input('请输入菱形的行数：'))#判断菱形行数
if row%2==0:
    print('无法打印菱形')

else:
    print('即将打印菱形')
    top_row=(row+1)//2+1
    for i in range(1,top_row):
       for j in range(1,top_row-i):
        print(' ',end='')
       for k in range(1,i*2):
         if k==1 or k==i*2-1: #加个判断条件，看是不是在开头或是末尾
          print('*',end='')
         else:
          print(' ',end='')
       print()

    bottom_row=row//2
    for i in range(1,bottom_row+1):
     for j in range(1,i+1):
        print(' ',end='')
     for k in range(1,row-2*i+1): #第一行：range(1,6) 第二行：range(1,4) 第三行 range(1,2)
          if k == 1 or k == row-2*i:
             print('*', end='')
          else:
             print(' ', end='')
     print('')


#跳转语句break:退出循环结构
s=0
i=1
while i<11:
    s += i
    if s>20:
        print('累加和大于20的数是：',i)
        break
    i+=1 #改变变量


#break在遍历循环for中的使用
for i in 'hello':
    if i=='e':
        break
    print(i)


#continue:跳过本次循环，执行后续代码
##求1-100之间的偶数和
i=1
s=0
while i<=100:
    if i%2==1:
        i += 1 #如果没有这一句，会进入死循环
        continue #不再执行此循环（while）后面的代码了，重新回到条件判断
    s+=i
    i+=1
print('1-100间的偶数和是：',s)


#continue在for循环
s=0
for i in range(1,101):
    if i%2==1:
        i+=1
        continue
    s+=i
print('1-100间的偶数和是：',s)


#pass占位符
if True:
    pass

#判断年份
year=eval(input('请输入一个四位的年份：'))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,'年是闰年')
else:
    print(year,'年是平年')


#模拟10086查询功能(字符串搞不清)
print('————————————————————————————欢迎使用10086查询功能————————————————————————————')
print('输入1，查询当前话费余额')
print('输入2，查询当前流量余额')
print('输入3，查询当前剩余通话时长')
print('输入0，退出系统')

answer='y'
while answer=='y':
  choice = input('请输入您要执行的操作：')  # choice是字符串
  if choice=='1':
    print('当前话费余额为***')
  elif choice=='2':
    print('当前流量余额为***')
  elif choice=='3':
    print('当前剩余通话时长为***')
  elif choice=='0':
    print('已退出系统')
    break
  else:
    print('输入有误，请重新输入：')
  answer=input(('您还要继续操作吗：y/n'))


#使用嵌套循环输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end='\t') #一个制表位
    print()

#猜数游戏
import random
rand=random.randint(1,100) #随机产生1-100的随机数
count=1
number=eval(input('在我心中有个数，请你猜一猜：'))
while count<10:
    if number==rand:
        print('猜对啦！')
        break
    elif number>rand:
        print('大了')
    else:
        print('小了')
    number = eval(input('请重新输入：'))
    count+=1
if count<4:
    print('真聪明，一共猜了',count,'次')
elif 3<count<7:
    print('还行，一共猜了',count,'次')
else:
    print('次数有点多啊，一共猜了', count, '次')


##使用索引检索字符串中的元素
#正向递增索引
s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t') #0 h	1 e	2 l	3 l	4 o	5 w	6 o	7 r	8 l	9 d
print('\n')

#反向递减索引
s='helloworld' #字符串
for i in range(-10,0):
    print(i,s[i],end='\t')#-10 h		-9 e		-8 l		-7 l		-6 o		-5 w		-4 o		-3 r		-2 l		-1 d
print('\n')
print(s[9],s[-1]) #d d 两者效果一样


#序列切片操作 【start:end:step】(不包含end)
s='helloworld'
s1=s[0:5:2]
print(s1) #hlo
#省略开始位置时，start默认从0开始
s2=s[:5:2] #冒号不能省
print(s2) #hlo
#省略开始位置，省略步长（默认步长为1）
s2=s[:5:] #冒号不能省
print(s2) #hello
#省略结束位置（默认到序列的最后一个元素，包含最后一个元素）
s2=s[::] #冒号不能省
print(s2) #helloworld
#步长为负数（输出逆序）
s2=s[::-1] #冒号不能省
print(s2) #dlrowolleh
s2=s[-1:-11:-1] #冒号不能省
print(s2) #dlrowolleh


##序列的相加和相乘操作
s1='hello'
s2='world'
print(s1+s2)    #相加 helloworld
print(s1*5)     #相乘，s1输出5遍 hellohellohellohellohello
print('-'*40)
print('h'in s1) #含有，结果为True
print('a'in s1) #False
print('a'not in s1) #True
print(max(s1),min(s1)) #最大值o 最小值e
print(s1.index('h')) #0 序列s1中第一次出现h的位置
print(s1.count('l')) #2,序列s1中出现l的次数


##列表,也是一种序列
#创建列表
lst=['hello',98,200]
print(lst)
#创建列表
lst2=list('hello') #内置函数，每个字母都是列表元素
print(lst2)
lst3=list(range(1,10,2)) #[1, 3, 5, 7, 9]
print(lst3)
#列表相加
print(lst+lst2+lst3)
print(lst*3) #列表相乘
print(len(lst))
#列表删除
lst4=['hello','world']
print(lst4)
del lst4
print(lst4)


##列表遍历
#使用for循环遍历
lst=('python','java','c++')
for item in lst:
    print(item)

#使用for循环+range+len+索引遍历
lst=('python','java','c++') #0 ----> python 1 ----> java 2 ----> c++
for i in range(0,len(lst)):
    print(i,'---->',lst[i])

#使用enumerate函数遍历
for index,item in enumerate(lst): #index序号 item元素
    print(index,item) #index是序号不是索引，可以手动修改
#手动修改序号
for index,item in enumerate(lst,start=1): #index序号 item元素
    print(index,item) #index是序号不是索引，可以手动修改

##列表特有操作
lst=['python','c','java']
print('原列表：',lst,id(lst)) #查找内存地址:id(lst)
#增加元素
lst.append('sql')
print('增加元素后的列表列表：',lst,id(lst)) #内存地址不变
#指定位置插入元素
lst.insert(1,100) #序号为1的地方插入元素100
print(lst)
#删除元素
lst.remove('python')
print('删除元素后的列表列表：',lst,id(lst))
#pop删除：先根据索引移出，再删除
print(lst.pop(1)) #移出索引为1的元素
print('移出元素后的列表：',lst,id(lst))
#清除所有元素
#lst.clear()
#print(lst,id(lst))
#列表反向输出
lst.reverse()
print(lst) #['sql', 'java', 100]
#列表拷贝
new_lst=lst.copy()
print(lst,new_lst) #['sql', 'java', 100] ['sql', 'java', 100]
#列表修改：根据索引进行修改
lst[1]='mysql'
print(lst)
#列表排序
lst=[4,56,78,2,89]
print('原列表：',lst)
#默认升序
lst.sort()
print('排序后的列表为：',lst) #[2, 4, 56, 78, 89]]
#降序
lst.sort(reverse=True)
print('升序:',lst)
print('-'*20)
lst2=['banana','Apple','orange']
print(lst2)
lst2.sort(reverse=True)
print('升序:',lst2) #先小写后大写['orange', 'banana', 'Apple']
lst2.sort()
print('降序:',lst2) #先大写后小写['Apple', 'banana', 'orange']
#忽略字母大小写
lst2.sort(key=str.lower)
print('忽略字母大小写：',lst2) # ['Apple', 'banana', 'orange']

#列表生成式
import random #导入随机数
lst=[item for item in range(1,11)]
print(lst) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst=[item*item for item in range(1,11)]
print(lst) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lst=[random.randint(1,100) for _ in range(1,10)]
print(lst)
lst=[i for i in range(10) if i%2==0]
print(lst)
#二维列表的遍历与列表生成式
lst=[['城市','环比','同比'],
     ['北京',101,102],
     ['上海',103,104]

]
print(lst)\
#二维列表遍历
for row in lst: #行
    for item in row: #列
        print(item,end='\t')
    print() #换行
#列表生成式：生成一个五行四列的列表
lst=[[i for i in range(4)] for j in range(5) ]
print(lst)


#元组
