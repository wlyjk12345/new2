a = ( 2 , 3 , 4 )  # 不可变 tuple
b = [ 2 , 4 ,5 ]   # 可变 list
print(a)
print(b)
b += [3,5]       #接
print(b)
b.append(4)       #接
print(b)
print(b[2:4:1])
b.insert(3,3)       #插入
print(b)
b.remove(3)     # 移除一个
print(b)
print(b.pop(5)) # 移除一个
print(b)
c = range(1,10,2)   # 1 3 5 7 ......  range
print(c[2])
d ={1:'cj',2:'dd'}    #字典
print(d)
d[2] = ' ff'
print(d)
print(d.keys())