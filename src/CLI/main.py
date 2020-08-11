import winshell
import os

def beginning():
    r = list(winshell.recycle_bin())

    class DeletedObject:
        def __init__(self, obj, typeOfObj):
            self.obj = obj
            self.typeOfObj = typeOfObj

    dictOfObjs = {}


    fmt = "{0:3}|{1:7}|{2:100}"
    for i,v in enumerate(r):
        sr = i+1
        total = v.original_filename().split('\\')
        okPath = "\\\\".join(total)
        v.undelete()
        print(okPath)
        if os.path.isdir(okPath):
            typee = "Folder"
        elif os.path.isfile(okPath):
            typee = "File"
        winshell.delete_file(okPath)
        dictOfObjs[sr] = DeletedObject(v,typee)

        print(fmt.format(sr,typee,total[-1]))
        selectItem(dictOfObjs)


# print("dict", dictOfObjs[1].obj)
def selectItem(dictOfObjs):
    n = eval(input("Enter Number "))
    try:
        selected = dictOfObjs[n]
        print("----", selected.obj)
        x = selected.obj.original_filename().split("\\")
        selected_path = "\\\\".join(x)
        winshell.undelete(selected.obj.original_filename())
        print("NAME: ", x[-1])
        print("PATH: ",selected_path)
        if os.path.isfile():
            print("TYPE: FILE")
            print("SIZE: ", os.path.getsize(selected_path))
        winshell.delete_file(selected.obj.original_filename())
    except:
        print("Enter a valid serial number")
        selectItem(dictOfObjs)



# path = r[0].original_filename()
# r[0].undelete()
#
# print(path)

# import pathlib
# a = pathlib.Path("C:\\Users\\Shahzaib\\Desktop\\Wireframes")
# print(a)
#
# import os
# o = os.path.isdir("C:\\Users\\Shahzaib\\Desktop\\Wireframes")
# winshell.delete_file("C:\\Users\\Shahzaib\\Desktop\\Wireframes")
# print(o)