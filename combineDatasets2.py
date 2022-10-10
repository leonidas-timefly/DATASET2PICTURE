import os
import random
import shutil
import sys


def moveFile(input1,input2,input3):

    proportion = [20,40,60,80]
    for k in range(len(proportion)):

        tmp_dir1 = input3+str(proportion[k])+'/'
        if not os.path.exists(tmp_dir1):
            os.mkdir(tmp_dir1)

        pathDir = os.listdir(input3)

        for dir in pathDir:
            train_test_dest = tmp_dir1 + dir + "/"
            if not os.path.exists(train_test_dest):
                os.mkdir(train_test_dest)
            
            source2=input1+'_'+input2

            sub_train_test = os.listdir(input3+'/'+dir+'/')
            for dir2 in sub_train_test:
                ###get training picture from input3
                image_dest = train_test_dest + dir2 + '/'
                if not os.path.exists(image_dest):
                    os.mkdir(image_dest)

                image_source1 = input3+'/'+dir+'/'+dir2+'/'
                random.seed(1)
                pic_source1 = os.listdir(image_source1)
                set_num=len(pic_source1)
                picknumber = int(set_num*proportion[k]/80)
                sample = random.sample(pic_source1, picknumber)
                for file_name in sample:
                    path_img=image_source1+file_name
                    shutil.copy(path_img,image_dest)
                    print(path_img)

                ###get training picture from input1_input2
                image_source2 = source2+'/'+dir+'/'+dir2+'/'
                pic_source2 = os.listdir(image_source2)
                picknumber = int(set_num*(100-proportion[k])/80)
                sample = random.sample(pic_source2, picknumber)
                for file_name in sample:
                    path_img=image_source2+file_name
                    shutil.copy(path_img,image_dest)
                    print(path_img)
 
if __name__ == '__main__':
    path1='product_images'
    path2='real_life'
    path3='synthetic'

    moveFile(path1,path2,path3)
    moveFile(path1,path3,path2)
    moveFile(path2,path3,path1)
