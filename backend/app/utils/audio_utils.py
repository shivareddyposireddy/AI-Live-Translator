import os

def delete_audio(file_path):

    if os.path.exists(file_path):
        os.remove(file_path)