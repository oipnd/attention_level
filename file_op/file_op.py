
import os


def ReadDataFromTextFile(FilePath):
    file_list = os.listdir(FilePath)
    mouse_data = []
    NameData = []
    for i in range(len(file_list)):
        SectionList = os.listdir(FilePath + '\\' + file_list[i])
        for S in SectionList:
            extraStr = '\\' + S
            HumanPath = FilePath + '\\' + file_list[i]
            each_file = HumanPath + os.sep + S
            txtList = os.listdir(HumanPath + extraStr)

            SingleFileData = []
            SingleName = []
            for j in range(len(txtList)):
                f = open(each_file + os.sep + txtList[j], 'r')
                linesAll = f.readlines()
                f.close()

                SingleFileData.append(linesAll)
                SingleName.append(txtList[j])
            mouse_data.append(SingleFileData)
            NameData.append(SingleName)
    return mouse_data, NameData


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
    print(data1)
    print(data2)
