# DefineMe - OpenTelemetry

## 🧠 OpenTelemetry Overview

### 🔍 O que é um Trace?
Um trace representa o caminho completo de uma requisição em um sistema distribuído. Cada parte do caminho é chamada de "span", e juntos formam um trace.

### 📈 O que é uma Métrica?
Métricas são valores numéricos que representam o estado ou desempenho de um sistema (como latência, uso de CPU, etc.).

### 🧩 Principais Classes
- `TracerProvider`: Provê e configura o tracer.
- `MeterProvider`: Provê e configura o coletor de métricas.
- Exporters: Enviam dados para backends como Prometheus, Jaeger, etc.

### 📌 Referência
- Docs Oficiais: https://opentelemetry.io/

---