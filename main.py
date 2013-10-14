from Tools.Scripts.treesync import raw_input
from file_manager import FileManager

__author__ = 'Artyom'

# Variables #
ruby_file_name = ""
all_ruby_files = []
ruby_file = ""

#*** That where we start ***#
print("Hello everybody")
print("Lets start analyzing!!!")
print("Please choose one of the presents files:")

all_ruby_files = FileManager.get_all_ruby_files_from_dir()

for index, file in enumerate(all_ruby_files):
    print(index + 1,")",file)

ruby_file_name = all_ruby_files[int(raw_input("Choose your file:")) - 1]
print(ruby_file_name)

