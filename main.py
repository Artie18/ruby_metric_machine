from Tools.Scripts.treesync import raw_input
from file_manager import FileManager
from source_code import SourceCode

__author__ = 'Artyom'

# Variables #
ruby_file_name = ""
all_ruby_files = []
ruby_file = ""
#** +- 1 added to make batter ui  **#

#*** That where we start ***#
print("Hello everybody")
print("Lets start analyzing!!!")
print("Please choose one of the presents files:")

all_ruby_files = FileManager.get_all_ruby_files_from_dir()

for index, file in enumerate(all_ruby_files):
    print(index + 1,")",file)

ruby_file_name = all_ruby_files[int(raw_input("Choose your file:")) - 1]

print("Your file name is", ruby_file_name)

file_as_a_string = FileManager.read_file('')

source_code = SourceCode(file_as_a_string)
try:
    source_code.check_if_valid()
    print("Everything looks great in your source code")
except ValueError as e:
    print(e)
