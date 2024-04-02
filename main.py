import os
import shutil
import threading

def sort_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1]
            ext_dir = os.path.join(path, ext[1:])
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.move(os.path.join(root, file), os.path.join(ext_dir, file))

def sort_dir(path):
    threads = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            t = threading.Thread(target=sort_files, args=(os.path.join(root, dir),))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()

sort_dir('Хлам')