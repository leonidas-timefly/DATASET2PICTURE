import os
import sys

list_dir0 = "ImageNet100-224/train/"
list_dir1 = "ImageNet1K-224/train/"

dir_list0 = os.listdir(list_dir0)
dir_list1 = os.listdir(list_dir1)

num = 0
temp = []
for dir1 in dir_list0:
    for dir2 in dir_list1:
        if dir1 == dir2:
            print(dir_list0.index(dir1), dir_list1.index(dir2))
            print(dir1, dir2)
            temp.append(dir_list1.index(dir2))

print(temp)
print(len(temp))

'''
[517, 526, 505, 498, 482, 459, 454, 457, 443, 418, 421, 432, 414, 376, 370, 360, 357, 352, 312, 313, 297, 299, 292, 267, 273, 259, 261, 263, 254, 248, 240, 233, 238, 210, 212, 195, 193, 177, 170, 153, 157, 148, 145, 126, 123, 129, 104, 101, 100, 89, 81, 40, 25, 1, 6, 988, 973, 977, 951, 953, 945, 950, 936, 938, 907, 901, 903, 885, 864, 863, 849, 841, 823, 809, 780, 764, 763, 752, 740, 728, 732, 725, 705, 694, 701, 683, 677, 664, 673, 671, 628, 622, 607, 614, 576, 569, 551, 559, 537, 546]
'''
