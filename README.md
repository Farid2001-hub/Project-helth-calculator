# Health Calculator Microservice

Un microservice Python qui calcule des métriques de santé (IMC et MB) via une API REST. Projet conteneurisé avec Docker, géré avec Makefile, et déployé sur Azure via CI/CD.

## Fonctionnalités

- **Calcul d'IMC (Indice de Masse Corporelle)**
  - Formule utilisée: `IMC = poids (kg) / (taille (m))²`
  - Catégorisation (Insuffisance pondérale, Normal, Surpoids, Obésité)

- **Calcul de MB (Métabolisme de Base)** selon l'équation de Harris-Benedict
  - Pour les hommes: `MB = 88.362 + (13.397 × poids en kg) + (4.799 × taille en cm) - (5.677 × âge en années)`
  - Pour les femmes: `MB = 447.593 + (9.247 × poids en kg) + (3.098 × taille en cm) - (4.330 × âge en années)`

- **Interface utilisateur web**
  - Formulaires pour calculer l'IMC et le MB directement dans le navigateur
  - Documentation des API intégrée
```

## Prérequis

- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)
- Docker (pour la conteneurisation)
- Git (pour le versionnement)

## Installation et utilisation

### 1. Création de l'environnement virtuel Python

Avant d'installer les dépendances, il est recommandé de créer un environnement virtuel Python pour isoler votre projet:

```bash
# Création de l'environnement virtuel
python3 -m venv .venv

# Activation de l'environnement virtuel (Windows)
.venv\Scripts\activate

# Activation de l'environnement virtuel (Linux/macOS)
source .venv/bin/activate
```

Vous saurez que l'environnement virtuel est activé quand vous verrez `(.venv)` au début de votre ligne de commande.

### 2. Installation des dépendances

Une fois l'environnement virtuel activé:

```bash
make init
```

### 3. Exécuter les tests

```bash
make test
```

### 4. Lancer l'application en mode développement

```bash
make run
```

L'application sera accessible à l'adresse http://localhost:5000

### 5. Construction de l'image Docker

```bash
make build
```

### 6. Exécuter l'application dans un conteneur Docker

```bash
make docker-run
```

L'application conteneurisée sera accessible à l'adresse http://localhost:5000

### 7. Arrêter le conteneur Docker

```bash
make docker-stop
```

### 8. Nettoyer l'environnement

```bash
make clean
```

### 9. Désactivation de l'environnement virtuel

Lorsque vous avez terminé de travailler sur le projet:

```bash
deactivate
```

## Commandes du Makefile

| Commande | Description |
|----------|-------------|
| `make init` | Installe les dépendances nécessaires |
| `make run` | Lance l'application en mode développement |
| `make test` | Exécute les tests unitaires |
| `make build` | Construit l'image Docker |
| `make docker-run` | Lance l'application dans un conteneur Docker |
| `make docker-stop` | Arrête le conteneur Docker |
| `make clean` | Nettoie les fichiers temporaires et compilés |
