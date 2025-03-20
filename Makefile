.PHONY: init run test build docker_build docker_run clean

# Installer les dépendances via pip
init:
		pip install -r requirements.txt

# Lancer l'application Flask
run:
		python app.py

# Exécuter les tests unitaires
test:
		python -m unittest test.py

# Construire l'image Docker
docker_build:
		docker build -t health-calculator .

# Lancer le conteneur Docker
docker_run:
		docker run -p 5000:5000 health-calculator

# Nettoyer les images Docker inutilisées
clean:
		docker rmi health-calculator
