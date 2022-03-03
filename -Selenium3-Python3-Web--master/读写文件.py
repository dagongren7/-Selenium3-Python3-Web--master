# read() 一次性读全部内容

def readAll():
    with open("./config/test.txt", "r", encoding='utf-8') as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)

# 只读取文本第一行的内容，以字符串的形式返回结果
def readLine():
    with open("./config/test.txt", "r", encoding='utf-8') as f:
        data = f.readline()
        print(data)

# 读取文本所有内容，并且以数列的格式返回结果，一般配合for in使用
def readList():
    with open("./config/test.txt", "r",encoding='utf-8') as f:
        # readlines会读到换行符，可用如下方法去除：
        # data = f.readlines()
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            print(line)

def write():
    with open("./config/test.txt", "a+",encoding='utf-8') as f:
        # \r 回车操作，\n换行操作
        f.write("这是个测试！\r\n")  # 自带文件关闭功能，不需要再写f.close()
write()

'''
读写模式
要了解文件读写模式，需要了解几种模式的区别，以及对应指针

r :   读取文件，若文件不存在则会报错

w:   写入文件，若文件不存在则会先创建再写入，会覆盖原文件

a :   写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾

rb,wb：  分别与r,w类似，但是用于读写二进制文件

r+ :   可读、可写，文件不存在也会报错，写操作时会覆盖

w+ :   可读，可写，文件不存在先创建，会覆盖

a+ :  可读、可写，文件不存在先创建，不会覆盖，追加在末尾
'''