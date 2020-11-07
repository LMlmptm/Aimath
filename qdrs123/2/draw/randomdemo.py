import random
import numpy as np
import matplotlib.pyplot as plt
import uuid

datalist = [0.1, 0.2, 0.3, 0.4, 0.5]

colorlist = ["blue", "red", "yellow", "black", "green"]

b = [0, 1, 2, 3, 4]
i = 0
data_color_list = []
while True:
    num = random.sample(b, 2)
    if num not in data_color_list:
        data_color_list.append(num)
        i += 1

    else:
        continue

    if i > 9:
        break

print(data_color_list)

print(uuid.uuid3(uuid.NAMESPACE_DNS,str(data_color_list)))


def test1():
    fig = plt.figure()
    axes = fig.add_subplot(111)
    for c in data_color_list:
        r = datalist[c[0]]
        # print(r)
        # 2.圆心坐标
        a, b = (c[0], c[1])

        theta = np.arange(0, 2 * np.pi, 0.01)
        x = a + r * np.cos(theta)
        y = b + r * np.sin(theta)

        plt.fill(x, y, colorlist[c[1]], alpha=0.5)
        plt.fill_between(x, y, facecolor='white')
        axes.plot(x, y)

        axes.axis('equal')
    plt.show()


test1()



# ascii_rev=[]
# for data in data_color_list:
#     for d in data:
#         print(chr(d+97))
#         ascii_rev.append(chr(d+97))
# print(ascii_rev)
#
#
#
# for cii in ascii_rev:
#     end_rev=ord(cii)-97
#     print(end_rev)