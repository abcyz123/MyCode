# 1、获取用户输入的成绩
# 2、先检测用户输入是否为数值类型90
# 3、然后对用户输入进行分支判断，输出等级结果
while True:
    score = input("请输入分数 ,按q!退出:")
    if score == 'q!':
        break
    try:
        score = float(score)
        if 0 <= score < 60:
            print("E")
        elif 60 <= score <70:
            print("D")
        elif 70 <= score < 80:
            print("C")
        elif 80 <= score < 90:
            print("B")
        elif 90 <= score <= 100:
            print("A")
        else:
            print("分数输入超出范围")
    except:
        print("输入类型错误，请输入数字类型")
