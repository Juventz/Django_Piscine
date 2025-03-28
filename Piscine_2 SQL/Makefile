include .env
export $(shell sed 's/=.*//' .env)
COMPOSE=docker compose
DOCKER=docker
SERVICE=postgres
IMAGE=postgres:latest
CONTAINER_NAME=djangotraining-postgres

# Démarrer le conteneur PostgreSQL
up:
	$(COMPOSE) up -d
	@echo "✅ Conteneur PostgreSQL démarré."

# Arrêter le conteneur PostgreSQL
down:
	$(COMPOSE) down
	@echo "✅ Conteneur PostgreSQL arrêté."

# Supprimer le conteneur PostgreSQL
clean:
	@if $(DOCKER) ps -a --format "{{.Names}}" | grep -q "^$(CONTAINER_NAME)$$"; then \
		$(DOCKER) stop $(CONTAINER_NAME) > /dev/null || true; \
		$(DOCKER) rm $(CONTAINER_NAME) > /dev/null || true; \
		$(DOCKER) volume prune -f > /dev/null; \
		@echo "✅ Conteneur PostgreSQL supprimé."; \
	else \
		@echo "⚠️  Aucun conteneur PostgreSQL trouvé à nettoyer."; \
	fi

# Nettoyer les fichiers inutiles
clear:
	@echo "Cleaning up useless files..."
	@find . -name "*.pyc" -exec rm -f {} \;
	@find . -name "*.pyo" -exec rm -f {} \;
	@find . -name "__pycache__" -exec rm -rf {} \;
	@echo "✅ Fichiers inutiles supprimés."

# Supprimer l'environnement virtuel
clean_env:
	@echo "Cleaning up virtual environment..."
	@rm -rf django_env/
	@echo "✅ Environnement virtuel supprimé."

# Vérifier l'état du conteneur PostgreSQL
status:
	@if $(DOCKER) ps --format "{{.Names}}" | grep -q "^$(CONTAINER_NAME)$$"; then \
		@echo "✅ Conteneur $(CONTAINER_NAME) est en cours d'exécution."; \
	else \
		@echo "❌ Conteneur $(CONTAINER_NAME) n'est pas en cours d'exécution."; \
	fi

.PHONY: up down clean clear clean_env status
