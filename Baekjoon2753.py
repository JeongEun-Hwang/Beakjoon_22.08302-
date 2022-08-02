# 윤년
# 입력 2000 결과 1
# 입력 1999 결과 0
year = int(input())

if 4000>=year>=1 and (year%400 == 0):
    print("1")

elif 4000>=year>=1 and  (year%4 ==0) and (year%100 != 0):
    print("1")

else:
    print("0")

# ---------------------------------------------------------------
# if (year%400 == 0) or ( (year%4 ==0) and (year%100 != 0)):
#     print("1")
# else:
#     print("0")

