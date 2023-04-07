import random
import my_module0
name = 'itheima'
message = '%s : is a shit %s' % (name, 666)
num1 = 19;
num2 = 666.6;
# print(message)
str = f"my name is {name} , num1 is {num1} , num2 is :{num2}"
print(str)
# str1 = input("who the fuxk are you:");
# print(type(str1))
num_random = random.randint(1, 100)
print(num_random)
f = open("123 (2).txt", "r", encoding="UTF-8")
# print(type(f))
# f.read()
lines = f.readlines()
# print(lines)
f1 = open("123.txt","r",encoding="UTF-8")
for line in f1:
    line  = line.strip( )
    words = line.split(" ")
print(words)


def add(x, y):
    """

    :param x: hhh
    :param y: ggg
    :return: None
    """
    result = x + y
    print(f"the result is {result}")
    return None
from my_module1 import *
test_A()
import my_package