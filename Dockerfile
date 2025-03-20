# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code source dans le conteneur
COPY . .

# Exposer le port 5000 pour accéder à l'application Flask
EXPOSE 5000

# Commande pour démarrer l'application Flask, en écoutant sur toutes les interfaces réseau
CMD ["python", "app.py"]
