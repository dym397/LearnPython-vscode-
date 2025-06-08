#字典可以提供基于key检索Value
dict1={}#空字典的定义
dict2={"dym":99,666:888}
print(f"空字典为{dict1},dict2为{dict2}")
print(dict2["dym"])
print(dict2[666])


#字典也可以嵌套   value也可以是字典，但是key是不可以是字典的
score_dict={
    "dym":{
        "math":100,
         "sc":99,
         "ds":88
    },
    "wxy":{
        "math":66,
         "sc":88,
         "ds":75
    }
}
print(score_dict)
print(score_dict["dym"]["math"])#dym的math的分数