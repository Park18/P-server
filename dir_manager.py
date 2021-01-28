import os

import urllib.request

def create_file(url, path, file_name):
    if not os.path.exists(path):
        os.makedirs(path)

    urllib.request.urlretrieve(url, path + file_name)