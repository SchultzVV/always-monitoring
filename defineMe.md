### 📁 `DefineMe.md` (raiz do projeto)

# DefineMe - Integração e Orquestração

## 🔗 Integração Geral

Este projeto integra o OpenTelemetry (instrumentação e coleta) com o Prometheus (monitoramento e análise).

## 🌐 Endpoints e Variáveis

- **OpenTelemetry Metrics Endpoint**: `http://opentelemetry-collector:8888/metrics`
- **Prometheus Target**: Configurado para scrapar `opentelemetry-collector`
- **Variáveis de Ambiente Comuns**:
  - `WEBHOOK_URL`: URL para envio de erros para o Teams
  - `OTEL_EXPORTER_OTLP_ENDPOINT`
  - `PROMETHEUS_CONFIG_PATH`

## 🧪 Execução

Use o Makefile:
```bash
make up-dev     # Sobe todos os serviços em ambiente de desenvolvimento
tail -f logs    # Visualiza os logs em tempo real
```

## 📦 Orquestração

Via `docker-compose.dev.yaml`, todos os serviços são interligados:
- `opentelemetry-collector`
- `prometheus`

## 📌 Referências
- OpenTelemetry + Prometheus Integration Guide: https://opentelemetry.io/docs/collector/exporter/prometheus/


---

📎 Esses arquivos estão prontos. Agora você pode me mandar os `Dockerfile`, `requirements.txt` e `__init__.py` para cada subpasta que eu insiro tudo no repositório virtual. Pronto pra próxima etapa. ✅
