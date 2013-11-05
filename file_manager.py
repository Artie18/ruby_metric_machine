__author__ = 'Artyom'

import os

class FileManager:

    RUBY_FILES_FOLDER = "ruby_test_scripts/"

    def __init__(self):
        pass

    @classmethod
    def get_all_ruby_files_from_dir(self):
        result = []
     #   os.chdir(FileManager.RUBY_FILES_FOLDER)
        for file in os.listdir(FileManager.RUBY_FILES_FOLDER):
            if file.endswith(".rb"):
                result.append(file)
        return result

    @classmethod
    def read_file(self, file_name):
        return open('ruby_test_scripts/ruby_test_1.rb', 'r').read()




