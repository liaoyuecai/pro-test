import sys, os, shutil

file = open('F:/PycharmProjects/pro-test/engine_ppt/pic/test.ds', 'w')
bys = [1, 2, 3];
file.write(bys)
file.close()
file = open('F:/PycharmProjects/pro-test/engine_ppt/pic/test.ds', 'rb')
data = file.read()
file.close()
print(len(data))
