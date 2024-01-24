from pathlib import Path

#absolute path
#relative path

#path = Path("emails")
#print(path.exists())


#print(path.mkdir())
#rint(path.rmdir())

#search for all py files

path1 = Path()
#to print all the files in the current workspace
for file in path1.glob('*.py'):
    print(file)