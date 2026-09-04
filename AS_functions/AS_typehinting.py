def cal_percentage(marks:float, tatal:float)->float:
    percentage:float=(marks/total)*100
    return percentage
marks:float=420
total:float=600
result:float=cal_percentage(marks,total)
print("first year percentage:",result)