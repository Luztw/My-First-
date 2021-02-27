"""檔案載入 (i.e try.txt"""
import os
path=os.getcwd()
os.chdir(path)
file=input("enter the file :")

f = open("data.txt", "w")


Data=open(file,"r", encoding='utf-8').readlines()

'''>>> Data
['\ufeffa\n', 'a\n', 'a er\n', 'a gieu\n', ]'''
n=[]
for i in Data:
    x=i.rstrip("\n")
    y=x.replace(" ","\n")
    f.write(y)
    f.write("\n")
   


f.close()
