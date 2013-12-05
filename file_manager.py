__author__ = 'Artyom'

import os

class FileManager:

    RUBY_FILES_FOLDER = "ruby_test_scripts/"
    RAILS_PROJECTS = "rails_test_scripts/"

    def __init__(self):
        pass

    @classmethod
    def get_all_rails_projects_from_dir(self):
        os.chdir(FileManager.RAILS_PROJECTS)
        result =  [d for d in os.listdir('.') if os.path.isdir(d)]
        os.chdir('..')
        return  result

    @classmethod
    def get_ruby_source_code_from_project(self, projectname):
        results = ""
        results = self.__read_files(FileManager.RAILS_PROJECTS + projectname, results)
        return results

    @classmethod
    def __read_files(self, dir_name, results):
        os.chdir(dir_name)
        for dirpath, dirnames, filenames in os.walk('.'):
            for dir in dirnames:
                if dir != "views":
                    results += self.__read_files(dir, results)
            filenames = os.listdir('.')
            for filename in [f for f in filenames if f.endswith(".rb")]:
                results += (open(os.path.abspath(filename), 'r').read())
        os.chdir('..')
        return results

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
        return open('ruby_test_scripts/' + file_name, 'r').read()




