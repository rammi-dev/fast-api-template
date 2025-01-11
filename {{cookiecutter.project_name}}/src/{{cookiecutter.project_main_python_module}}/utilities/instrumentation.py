from starlette_exporter import PrometheusMiddleware, handle_metrics

# from prometheus_client import Gauge

# Create a metric to track time spent and requests made.
# <metric name> = Gauge('<app_name>_<name>',
#                       '<description>')

__all__ = ("handle_metrics", "PrometheusMiddleware")
