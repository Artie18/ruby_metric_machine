from Tools.Scripts.treesync import raw_input
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
print("Please choose one of the presents files:")

all_ruby_files = FileManager.get_all_ruby_files_from_dir()

for index, file in enumerate(all_ruby_files):
    print(index + 1,")",file)

ruby_file_name = all_ruby_files[int(raw_input("Choose your file:")) - 1]

print("Your file name is", ruby_file_name)

file_as_a_string = FileManager.read_file('')

source_code = SourceCode(file_as_a_string)
try:
    if source_code.check_if_valid():
        print("Everything looks great in your source code")
        for index, metric in enumerate(METRICS):
            print(index + 1, metric)
        current_metric_name = METRICS[int(raw_input("Choose your metric:")) - 1]
        metric = MetricsFabric.create_metric(current_metric_name,source_code)
        final_result = metric.get_metric_result_as_string() # common method that is used by all metrics
        print(final_result)
except Exception:
    print('Something went wrong, please check your source file')
