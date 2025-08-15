# =======================
# 🌱 Variáveis de ambiente
# =======================

include .env
export

ifeq ($(MAKECMDGOALS),prd-up)
	include .env.prd
endif
ifeq ($(MAKECMDGOALS),prd-down)
	include .env.prd
endif
ifeq ($(MAKECMDGOALS),prd-up-ghcr)
	include .env.prd
endif

TAG ?= latest

GHCR_USER = $(GITHUB_USERNAME)
GHCR_TOKEN = $(GITHUB_TOKEN)

IMAGE_NAME = ghcr.io/$(GHCR_USER)/site:$(TAG)

# Comando base para dev
COMPOSE = docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml --env-file .env

# =====================
# 🧪 Desenvolvimento
# =====================

up:  ## Sobe o ambiente de desenvolvimento
	$(COMPOSE) up --build

down:  ## Para e remove containers + volumes
	$(COMPOSE) down -v

restart-otel:  ## Reinicia apenas o serviço opentelemetry
	$(COMPOSE) restart opentelemetry

restart-prom:  ## Reinicia apenas o serviço prometheus
	$(COMPOSE) restart prometheus

redo-otel:  ## Rebuild completo apenas do opentelemetry
	$(COMPOSE) stop opentelemetry
	$(COMPOSE) rm -f opentelemetry
	$(COMPOSE) build opentelemetry
	$(COMPOSE) up -d opentelemetry

redo-prom:  ## Rebuild completo apenas do prometheus
	$(COMPOSE) stop prometheus
	$(COMPOSE) rm -f prometheus
	$(COMPOSE) build prometheus
	$(COMPOSE) up -d prometheus

logs-otel:  ## Logs em tempo real do opentelemetry
	$(COMPOSE) logs -f opentelemetry

logs-prom:  ## Logs em tempo real do prometheus
	$(COMPOSE) logs -f prometheus

# =====================
# 🚀 Produção
# =====================

prd-up:  ## Sobe o ambiente de produção com docker-compose
	docker-compose -f docker-compose.yaml -f docker-compose.prd.yaml --env-file .env.prd up -d

prd-down:  ## Para e remove containers de produção
	docker-compose -f docker-compose.yaml -f docker-compose.prd.yaml --env-file .env.prd down -v

prdlogs-otel:  ## Logs do serviço opentelemetry em produção
	docker-compose -f docker-compose.yaml -f docker-compose.prd.yaml --env-file .env.prd logs -f opentelemetry

prdlogs-prom:  ## Logs do serviço prometheus em produção
	docker-compose -f docker-compose.yaml -f docker-compose.prd.yaml --env-file .env.prd logs -f prometheus
