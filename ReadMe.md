# Documentação Detalhada

## Visão Geral

Este projeto implementa um ambiente de monitoramento e observabilidade com dois serviços principais:

- **OpenTelemetry Service**: expõe métricas customizadas usando OpenTelemetry.
- **Prometheus Service**: expõe métricas no formato Prometheus e serve como endpoint para scraping.
- **Prometheus Server**: coleta métricas dos serviços via scraping.
- **Grafana**: (opcional) para visualização dos dados.

## Estrutura dos Sistemas

### 1. OpenTelemetry Service
Local: `source/services/opentelemetry`

- **Tecnologias:** Python, Flask, OpenTelemetry SDK
- **Endpoints:**
   - `/` : Status do serviço
   - `/metrics` : Métricas customizadas (ex: uso de CPU)
- **Como funciona:**
   - Simula métricas e as expõe via OpenTelemetry.
   - Pode ser acessado diretamente ou por Prometheus.
- **Dependências:**
   - flask
   - opentelemetry-api
   - opentelemetry-sdk

### 2. Prometheus Service
Local: `source/services/prometheus`

- **Tecnologias:** Python, Flask, Prometheus Client, OpenTelemetry SDK
- **Endpoints:**
   - `/` : Status do serviço
   - `/metrics` : Métricas no formato Prometheus (ex: temperatura)
- **Como funciona:**
   - Simula métricas e as expõe no padrão Prometheus.
   - Endpoint `/metrics` é raspado pelo Prometheus Server.
- **Dependências:**
   - flask
   - opentelemetry-api
   - opentelemetry-sdk
   - opentelemetry-exporter-prometheus
   - prometheus-client

### 3. Prometheus Server
Local: raiz do projeto, container oficial

- **Tecnologias:** Docker, Prometheus
- **Configuração:**
   - Arquivo `prometheus.yml` define os targets e intervalos de scraping.
   - Targets configurados: opentelemetry:5000, prometheus:5000

### 4. Grafana
Local: container oficial (opcional)

- **Tecnologias:** Docker, Grafana
- **Uso:** Visualização dos dados coletados pelo Prometheus Server.

## Como Executar

### Pré-requisitos
- Docker e Docker Compose instalados
- (Opcional) Make instalado para comandos facilitados

### Subindo o ambiente

1. Clone o repositório e acesse a pasta raiz
2. Execute:
   ```bash
   make up
   ```
   ou
   ```bash
   docker-compose up --build
   ```

### Parando o ambiente
```bash
make down
```
ou
```bash
docker-compose down -v
```

## Como acessar os serviços

- **OpenTelemetry Service:**
   - [http://localhost:5001/](http://localhost:5001/)
   - [http://localhost:5001/metrics](http://localhost:5001/metrics)
- **Prometheus Service:**
   - [http://localhost:5002/](http://localhost:5002/)
   - [http://localhost:5002/metrics](http://localhost:5002/metrics)
- **Prometheus Server:**
   - [http://localhost:9090/](http://localhost:9090/) (interface Prometheus)
- **Grafana:**
   - [http://localhost:3000/](http://localhost:3000/) (se ativado)

## Exemplos de Métricas

- OpenTelemetry: `simulated_cpu_usage` (gauge)
- Prometheus: `simulated_temperature` (gauge)

## Referências

- [OpenTelemetry Docs](https://opentelemetry.io/)
- [Prometheus Docs](https://prometheus.io/docs/)

---

- [DefineMe.md - OpenTelemetry](source/services/opentelemetry/DefineMe.md)
- [DefineMe.md - Prometheus](source/services/prometheus/DefineMe.md)

---
```bash
.
├── Makefile
├── docker-compose.yaml
├── docker-compose.dev.yaml
├── docker-compose.prd.yaml
├── .env


├── source/

│   └── services/

│       ├── opentelemetry/

│       │   ├── requirements-dev.txt
│       │   ├── main.py

│       │   ├── __init__.py

│       │   └── DefineMe.md

│           ├── requirements.txt
│           ├── requirements-dev.txt


│           ├── __init__.py

│           └── DefineMe.md
└── DefineMe.md
```

---



Sua aplicação
   ↓
OpenTelemetry SDK
   ↓
Exposição de métricas em /metrics
   ↓
Prometheus acessa via scraping
   ↓
Armazena e disponibiliza via PromQL
```