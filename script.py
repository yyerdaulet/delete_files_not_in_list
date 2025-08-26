import os
import shutil
import sys



input_files = sys.argv[1]
target_folder = sys.argv[2]


folders_to_save = []
def list_of_folders():
    with open(input_file) as file_names:
        for file_name in file_names:
            folders_to_save.append(file_name.split('/')[0])



def clean():
    for folder_name in os.listdir(target_folder):
        if folder_name == ".DS_Store":
            continue
        if folder_name not in folders_to_save:
            shutil.rmtree(os.path.join(target_folder,folder_name))



if __name__ == "__main__":
    list_of_folders()
    clean()






