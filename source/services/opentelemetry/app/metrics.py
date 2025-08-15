from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader

import random
import time

# Setup básico do MeterProvider
exporter = ConsoleMetricExporter()
reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)

meter = metrics.get_meter(__name__)
cpu_usage = meter.create_observable_gauge(
    name="simulated_cpu_usage",
    description="Simulated CPU usage (%)",
    unit="%",
    callbacks=[lambda options: [metrics.Observation(value=random.uniform(10, 90))]]
)

print("🧪 Métricas simuladas com sucesso (observação a cada 5 segundos)...")
