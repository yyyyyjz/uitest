import glob
import os
import shutil


def J_Statistical_File():
    path = './screenshot/csimg/'
    path_file_number = glob.glob(pathname = path + "/*.png")
    print(len(path_file_number))
    if len(path_file_number) > 50:
        print("截图超过50张清空文件夹")
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        print("继续加截图!")
    return len(path_file_number)

