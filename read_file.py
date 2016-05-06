from sys import argv
script, file_name = argv


def read_file (file):
    print file.read()
 
 
current_file = open(file_name)
read_file (current_file)

