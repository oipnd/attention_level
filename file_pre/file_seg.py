import os

from file_pre.file_op import ReadDataFromTextFile


def get_input_data(mouse_file):
    mouse_data=[]
    for i in range(len(mouse_file)):
        mouse_data.append(get_pure_mousedata(mouse_file[i]))

    return mouse_data

def cal_label():
    return 0


def get_pure_mousedata(file_content):
    mouse_data = []
    it=iter(file_content[0])
    for line in it:
        if line.startswith("mouse"):
            mouse_data.append(line)
    return mouse_data


if __name__ == '__main__':
    path = "D:\data\pc"
    raw_file,_=ReadDataFromTextFile(path)
    res=get_input_data(raw_file)
    print(res[1])