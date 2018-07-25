#!/usr/bin/python
#coding:utf-8
import re
#a = "电话13120696232 "
a = "【彭应起的房源店铺|彭应起】电话13120696232 - 赶集网"
#print (re.search('/^1[0-9]{10}$/', a)
m = re.findall(r"1\d{10}",a)
print(m)
#print (a)
