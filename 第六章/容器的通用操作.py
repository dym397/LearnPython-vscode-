#for 循环 所有容器都是可以的


list1=[4,3,1,2,5]
tuple1=(4,3,1,2,5)
str1="abcdefg"
set1={4,3,1,2,5}
dict1={"key1":4,"key2":3,"key3":1,"key4":2,"key5":5,}
#max()找出最大元素
print(f"list1的最大元素为:{max(list1)}")
print(f"tuple1的最大元素为:{max(tuple1)}")
print(f"str1的最大元素为:{max(str1)}")
print(f"set1的最大元素为:{max(set1)}")
print(f"dict1的最大元素为:{max(dict1)}")#字符串的比较是按照ascii码的大小来的

#min()找出最小元素
print(f"list1的最小元素为:{min(list1)}")
print(f"tuple1的最小元素为:{min(tuple1)}")
print(f"str1的最小元素为:{min(str1)}")
print(f"set1的最小元素为:{min(set1)}")
print(f"dict1的最小元素为:{min(dict1)}")#字符串的比较是按照ascii码的大小来的 字典中是比较关键字的大小
#容器元素个数
print(f"list1的元素个数为:{len(list1)}")
print(f"tuple1的元素个数为:{len(tuple1)}")
print(f"str1的元素个数为:{len(str1)}")
print(f"set1的元素个数为:{len(set1)}")
print(f"dict1的元素个数为:{len(dict1)}")#字符串的比较是按照ascii码的大小来的 字典中是比较关键字的大小

#这几种容器都可以互相转换  但是不能转换成字典，因为字典的元素是一个键值对。字典在转换时，value都会丢失（除了转换为字符串的时候）

#sorted排序   排序后都会转换成列表类型
print(f"list1进行排序后:{sorted(list1)}")
print(f"tuple进行排序后:{sorted(tuple1)}")
print(f"str1进行排序后{sorted(str1)}")
print(f"set1进行排序后{sorted(set1)}")
print(f"dict1进行排序后:{sorted(dict1)}")
#降序
print(f"list1进行排序后:{sorted(list1,reverse=True)}")
print(f"tuple进行排序后:{sorted(tuple1,reverse=True)}")
print(f"str1进行排序后{sorted(str1,reverse=True)}")
print(f"set1进行排序后{sorted(set1,reverse=True)}")
print(f"dict1进行排序后:{sorted(dict1,reverse=True)}")

print(f"哎的Unicode值为:{ord("哎")},巴的Unicode值为{ord("巴")},所以哎>巴={"哎">"巴"}")  #汉字比较的是Unicode值