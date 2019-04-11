from sys import argv
import os

RESULT_FILE = 'ft_fun.c'


def read_pcap_file(file_name):
    with open(file_name, "r") as file:
        file_content = file.readlines()
        if "//file" in file_content[-1]:
            return int(file_content[-1].replace("//file", "")), file_content
        else:
            raise Exception(f"File: '{file_name}' is invalid.")


def create_file_from_dir(dir_name):
    files = {}
    last_index = 0
    
    for file_name in os.listdir(dir_name):
        file_name = os.path.join(dir_name, file_name)
        if os.path.isfile(file_name):
            file_index, file_content = read_pcap_file(file_name)
            files[file_index] = file_content
            if last_index < file_index:
                last_index = file_index
    with open(RESULT_FILE, "w") as file:
        for i in range(1, last_index + 1):
            file.writelines(files[i])
            file.write("\n")


if __name__ == '__main__':
    try:
        if len(argv) == 2:
            print(f"Reading files from {argv[1]}")
            create_file_from_dir(argv[1])
    except Exception as e:
        print(e)
