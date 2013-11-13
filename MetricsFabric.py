__author__ = 'Artyom'

from ChepinMetric import ChepinMetric
from holsteda_metrics import HosltedaMetrics
from jilba_metric import JilbaMetric

class MetricsFabric:

    @staticmethod
    def create_metric(name, source_code):
        return {
            "Chepin Metric"     : ChepinMetric(source_code),
            "Holsteda Metrics"  : HosltedaMetrics(source_code),
            "Jilba Metrics"     : JilbaMetric(source_code)
        }[name]
