from file_manager import FileManager
from source_code import SourceCode
from MetricsFabric import MetricsFabric

__author__ = 'Artyom'

METRICS = ["Chepin Metric", "Holsteda Metrics", "Jilba Metrics"]

# Variables #
ruby_file_name = ""
all_ruby_files = []
ruby_file = ""
#** +- 1 added to make batter ui  **#

#*** That where we start ***#
print("Hello everybody")
print("Lets start analyzing!!!")
print("Choose between project and ruby")

print("Please choose one of the presents files:")
print("1) File")
print("2) Project")
type_value = int(input("Make a choise"))
if type_value == 2:
    input_value = FileManager.get_all_rails_projects_from_dir()
    for index, file in enumerate(input_value):
        print(index + 1,")",file)
    rails_project_name = input_value[int(input("Choose your project name:")) - 1]
    print("Your file name is", rails_project_name)
    file_as_a_string = FileManager.get_ruby_source_code_from_project(rails_project_name)
elif type_value == 1:
    input_value = FileManager.get_all_ruby_files_from_dir()
    for index, file in enumerate(input_value):
        print(index + 1,")",file)
    ruby_file_name = input_value[int(input("Choose your file:")) - 1]
    print("Your file name is", ruby_file_name)
    file_as_a_string = FileManager.read_file(ruby_file_name)

try:
    source_code = SourceCode(file_as_a_string)
    if source_code.check_if_valid():
        print("Everything looks great in your source code")
        while 1:
            for index, metric in enumerate(METRICS):
                print(index + 1, metric)
            current_metric_name = METRICS[int(raw_input("Choose your metric:")) - 1]
        current_metric_name = METRICS[int(input("Choose your metric:")) - 1]
            metric = MetricsFabric.create_metric(current_metric_name,source_code)
            final_result = metric.get_metric_result_as_string() # common method that is used by all metrics
            print(final_result)
except Exception as e:
    print('Something went wrong, please check your source file',e )
