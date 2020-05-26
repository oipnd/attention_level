import os


def ReadDataFromTextFile(FilePath):
    file_list = os.listdir(FilePath)
    mouse_data = []
    name_data = []
    for i in range(len(file_list)):
        section_list = os.listdir(FilePath + '\\' + file_list[i])
        for S in section_list:
            extra_str = '\\' + S
            human_path = FilePath + '\\' + file_list[i]
            each_file = human_path + os.sep + S
            txt_list = os.listdir(human_path + extra_str)

            single_file_data = []
            single_name = []
            for j in range(len(txt_list)):
                f = open(each_file + os.sep + txt_list[j], 'r')
                linesAll = f.readlines()
                f.close()

                single_file_data.append(linesAll)
                single_name.append(txt_list[j])
            mouse_data.append(single_file_data)
            name_data.append(single_name)
    return mouse_data, name_data


def RenameFileWithSessions(FilePath):
    HumanList = os.listdir(FilePath)
    for i in range(len(HumanList)):
        SectionList = os.listdir(FilePath + '\\' + HumanList[i])
        for S in SectionList:
            extraStr = '\\' + S
            HumanPath = FilePath + '\\' + HumanList[i]
            #            print HumanPath

            FileList = os.listdir(HumanPath + extraStr)
            tmp = FileList[0].split('_')
            if tmp[-2] != S:
                for j in range(len(FileList)):
                    tmp = FileList[j].split('_')
                    NameChanged = ''
                    for t in range(len(tmp) - 1):
                        NameChanged = NameChanged + tmp[t] + '_'
                    NameChanged = NameChanged + S + '_' + tmp[-1]
                    os.rename(HumanPath + extraStr + '\\' + FileList[j], HumanPath + extraStr + '\\' + NameChanged)


if __name__ == '__main__':
    path = "D:\data\pc"
    data1, data2 = ReadDataFromTextFile(path)
    print(len(data1))
    print(len(data2))
