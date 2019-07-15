import os

fileDic  = {}
dicArr = {}

dir = "/home/dev"
def dicUpdate(dirs,dic):
    for dir in dirs:
        dic.update({dir:{}})
        dicArr[dir] = dic[dir]
def getDirTree(dir = None):
    for cwd,dirs,files in os.walk(dir):
        parent = os.path.basename(cwd)
        if parent in dicArr:
            tempdic = dicArr[parent]
            if files:
                tempdic.update({"files":files})
            if dirs:
                tempdic.update({"dirs":{}})
                dicUpdate(dirs,tempdic["dirs"])
        else:
            tempdic = {}
            if files:
                tempdic.update({parent:{"files":files}})
            if dirs:
                tempdic.update({parent:{"dirs":{}}})
                dicUpdate(dirs,tempdic[parent]["dirs"])
            fileDic.update(dicArr)
    return fileDic

data = getDirTree(dir)

print data