from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.prometheus import PrometheusMetricReader

import random

# Exportador Prometheus
reader = PrometheusMetricReader()
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)

meter = metrics.get_meter(__name__)

# Simula uma métrica observável, como temperatura de sistema
def temperature_callback(options):
    value = random.uniform(20, 80)
    return [metrics.Observation(value=value)]

meter.create_observable_gauge(
    name="simulated_temperature",
    description="Simulated system temperature",
    unit="C",
    callbacks=[temperature_callback],
)

# Exportador Prometheus automaticamente serve em /metrics
