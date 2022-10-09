import os
import random
import shutil
import sys
 
 
def moveFile(source1,source2):

    dest1 = source1+'_'+source2+'/'


    if not os.path.exists(dest1):
        os.mkdir(dest1)
    pathDir = os.listdir(source1)  # 取图片的原始路径

    for dir in pathDir:


        train_test_dest = dest1 + dir + "/"
        if not os.path.exists(train_test_dest):
            os.mkdir(train_test_dest)
        
        
        sub_train_test = os.listdir(source1+'/'+dir+'/')
        for dir2 in sub_train_test:
            
            #print(dir2)
            image_dest = train_test_dest + dir2 + "/"
            if not os.path.exists(image_dest):
                os.mkdir(image_dest)

            #move dir2
            image_source1=source1+'/'+dir+'/'+dir2+'/'
            print(image_source1)
            pic_source1 = os.listdir(image_source1)
            print(pic_source1)
            num=0
            for pics in pic_source1:
                
                pic_dir = image_source1+pics
                print(pic_dir)
                print(image_dest)

                shutil.copy(pic_dir,image_dest)
                old_name = image_dest+pics
                new_name = image_dest+str(num)+'.jpg'
                os.rename(old_name, new_name)
                num=num+1

            #move2
            image_source2=source2+'/'+dir+'/'+dir2+'/'
            pic_source2 = os.listdir(image_source2)
            for pics in pic_source2:
                pic_dir = image_source2+pics
                shutil.copy(pic_dir,image_dest)
                old_name = image_dest+pics
                new_name = image_dest+str(num)+'.jpg'
                os.rename(old_name, new_name)
                num=num+1
 
if __name__ == '__main__':

    dir1='product_images'
    dir2='real_life'
    dir3='synthetic'

    moveFile(dir1,dir2)
    moveFile(dir1,dir3)
    moveFile(dir2,dir3)
