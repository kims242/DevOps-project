IMAGE_NAME = mon-image
CONTAINER_NAME = mon-conteneur

.PHONY: init
init:
	python3 -m venv .venv
	. .venv/bin/activate

build:
	docker build -t $(IMAGE_NAME) .

install:
	pip install -r requirements.txt


run:
	docker run --name $(CONTAINER_NAME) -p 8000:8000 $(IMAGE_NAME)

# Arrêt du conteneur Docker
stop:
	docker stop $(CONTAINER_NAME)

# Suppression du conteneur Docker
rm:
	docker rm $(CONTAINER_NAME)

# Suppression de l'image Docker
rmi:
	docker rmi $(IMAGE_NAME)

# Nettoyage complet
clean: 
	stop rm rmi

test:
	python -m unittest health-calculator-service/test.py

.PHONY:
	venv build run stop rm rmi clean