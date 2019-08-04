import os

path="/home/kb"
for entry in os.listdir(path):
    print(entry)

print("Print Only Dirs")
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        print(entry)
