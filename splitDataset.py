import os
import random
import shutil
import sys
 
 
def moveFile(input1,save1,save2):
    pathDir = os.listdir(input1)  # 取图片的原始路径
    for dir in pathDir:
        source_dir = input1 + dir
        #train_dir = save1 + "/" + dir
        test_dir = save2 + "/" + dir
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)        

        random.seed(1)
        pic_list = os.listdir(source_dir)
        filenumber = len(pic_list)  # 原文件个数
        rate = 0.2  # 抽取的验证集的比例，占总数据的多少
        picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
        print(pic_list)
        print(source_dir)
        sample = random.sample(pic_list, picknumber)  # 随机选取需要数量的样本图片
        print(sample)

        for flie_name in sample:
            path_img=os.path.join(source_dir,flie_name)
            shutil.move(path_img,test_dir)
 
if __name__ == '__main__':
    input_path1='total/'
    save_train='/train'
    save_test='test'
    if not os.path.exists(save_test):
        os.mkdir(save_test)
    moveFile(input_path1,save_train,save_test)
