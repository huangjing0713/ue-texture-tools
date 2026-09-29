import os

def walk_and_filter(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            if f.lower().endswith(".png"):
                print(os.path.join(dirpath,f))

if __name__ == '__main__':
    walk_and_filter(r'D:\pythonProject')