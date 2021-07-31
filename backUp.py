import os 
import shutil

# os.system('date')
# os.getcwd()
# path = '/Users/pc/newfolder'
# os.mkdir(path)
path = input('Enter The Folder name to be sorted: ')
listofFiles = os.listdir(path)
for File in listofFiles:
    name,ext = os.path.splitext(File)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+File, path+'/'+ext+'/'+File)
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+File, path+'/'+ext+'/'+File)

        
    