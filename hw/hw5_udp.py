from functools import reduce
import matplotlib.pyplot as plot

fig = plot.figure()
num0 = 2 ** 16
num1 = 0B0110011001100000
num2 = 0B0101010101010101
num3 = 0B1000111100001100
udpList = [num1, num2, num3]
print("original udp data package")
print(udpList)


def Complement(num):
    return 0xffff - num & 0xffffffff


def Calc_sum(num01, num02):
    num03 = num01 + num02
    num04 = num03 % num0
    if num04 < num01 or num04 < num02:
        num04 = num04 + 1
    return num04


def Check_sum(para_list):
    check = para_list[0]
    for i in range(len(para_list)-1):
        check = Calc_sum(check, para_list[i+1])
    udpList.append(Complement(check))
    return


def Distinguish(para_list):
    result = 0
    check = para_list[0]
    for i in range(len(para_list)-1):
        check = Calc_sum(check, para_list[i+1])
        result += (check == num0 - 1)
    return result


Check_sum(udpList)
print("add check number")
print(udpList)
print("start checking")
if Distinguish(udpList):
    print("success")
else:
    print("fail")

plot.scatter([1, 2, 3], [udpList[:3]], color="green", marker="^")
plot.scatter(4, udpList[3], color="red", marker="o")
plot.show()
