from pprint import pprint
dic = {'a':1, 'b':123, 'c':2, 'r':234235, 'z':3}
for key in sorted(dic, key=dic.get, reverse = False):
    print(dic[key])
pprint(dic)
