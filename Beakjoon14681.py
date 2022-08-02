#  사분면 고르기
x = int(input())
y = int(input())

# if x>0&y>0:
#     print("1")
#
# elif 0>x>-1000&y>0:
#     print("2")
#
# elif 0>x>-1000&0>y>-1000:
#     print("3")
#
# elif x>0&0>y>-1000:
#     print("4")

if x>0 and y>0:
    print("1")

elif 0>x>-1000 and y>0:
    print("2")

elif 0>x>-1000 and 0>y>-1000:
    print("3")

elif x>0 and 0>y>-1000:
    print("4")