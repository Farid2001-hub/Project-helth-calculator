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

### 4. Lancer test endpoint

```bash
make test-endpoint
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
| `make test endpoints` | Exécute les tests endpoints |
| `make build` | Construit l'image Docker |
| `make docker-run` | Lance l'application dans un conteneur Docker |
| `make docker-stop` | Arrête le conteneur Docker |
| `make clean` | Nettoie les fichiers temporaires et compilés |

## Utilisation des API

### Calcul de l'IMC

**Endpoint**: `/calculate_bmi` (POST)

**Corps de la requête**:
```json
{
  "height": 1.90,  // Taille en mètres
  "weight": 84     // Poids en kilogrammes
}
```

**Exemple avec curl**:
```bash
curl -X POST http://localhost:5000/calculate_bmi \
  -H "Content-Type: application/json" \
  -d '{"height": 1.90, "weight": 84}'

```

**Réponse**:
```json
{
  "bmi": 23.27
}

```

### Calcul du BMR (Métabolisme de base)

**Endpoint**: `/calculate_bmr` (POST)

**Corps de la requête**:
```json
{
  "height": 190,     // Taille en centimètres
  "weight": 84,      // Poids en kilogrammes
  "age": 24,         // Âge en années
  "gender": "male"   // Genre: "male" ou "female"
}

```

**Exemple avec curl**:
```bash
curl -X POST http://localhost:5000/calculate_bmr \
  -H "Content-Type: application/json" \
  -d '{"height": 190, "weight": 84, "age": 24, "gender": "male"}'

```

**Réponse**:
```json
{
  "bmr": 1989.27,
  "unit": "calories/day"
}
```


### Explications :
1. **Calcul de l'IMC** (`/calculate_bmi`) : L'endpoint attend les valeurs de taille (`height`) en mètres et de poids (`weight`) en kilogrammes, puis renvoie l'IMC calculé.
2. **Calcul du BMR** (`/calculate_bmr`) : L'endpoint attend la taille (`height`) en centimètres, le poids (`weight`) en kilogrammes, l'âge (`age`) en années et le genre (`gender`), puis renvoie le métabolisme de base calculé en calories par jour.

### À tester avec `curl` :
- **IMC** : Remplacez les valeurs dans le corps JSON pour tester avec vos propres données.
- **BMR** : Faites de même pour tester le calcul du métabolisme de base.

Cela vous permet de tester les API facilement sur votre machine locale en utilisant les commandes `curl`.

## CI/CD et Déploiement

Ce projet utilise **GitHub Actions** pour l'intégration continue et le déploiement continu (CI/CD), et **Azure App Service** pour l'hébergement.

### Création de l'Application sur Azure App Service

1. **Accédez au portail Azure** : Ouvrez [Azure Portal](https://portal.azure.com/) et connectez-vous à votre compte.
2. **Créez une nouvelle Application Web** :
   - Allez dans **App Services**.
   - Cliquez sur **Create** pour créer une nouvelle application web.
   - Sélectionnez les paramètres appropriés pour votre application, comme le nom de l'application (qui doit être unique).
   - Dans la section **Publish**, choisissez **Code** (si vous utilisez un fichier app.py ou un code Python).
   - Sélectionnez la pile d'exécution (par exemple, Python) et la région.
   - la liaison de azure avec le repo github
   - Terminez la création de l'application.

### Pipeline CI/CD

Le pipeline CI/CD est configuré dans le fichier `.github/workflows/main_helth-app.yml` et effectue les actions suivantes:

1. **Build**: 
   - Vérifie le code source.
   - Configure l'environnement Python.
   - Installe les dépendances.
   - Exécute les tests unitaires.
   - Construit l'image Docker.

2. **Deploy**:
   - Déploie l'image Docker sur **Azure App Service**.
   - Le déploiement est automatiquement déclenché lors d'un push sur la branche `main`.

### Application déployée

L'application est déployée et accessible à l'URL suivante:
```
https://helth-app-hpcec5cabgcecgdy.eastus-01.azurewebsites.net/
```




