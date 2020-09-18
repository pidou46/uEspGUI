import os

py_files=[]

files=os.listdir('lib')

for i in files:
        if '.py' in i:
            py_files.append(i)

print(py_files)