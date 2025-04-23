# flask-content-platform

# Cloud Content Platform

Une application Flask conteneurisée, déployée sur AKS, qui diffuse dynamiquement du contenu statique en JSON/YAML.

## Fonctionnalités

- API REST pour récupérer du contenu statique
- UI simple pour la visualisation
- Conteneurisée avec Docker
- CI/CD vers Azure Kubernetes Service (AKS)

## Structure
flask-content-platform/
│── app/
│   ├── main.py             # Fichier principal Flask
│   ├── routes.py           # Routes API
│   ├── static_data/        # JSON/YAML stockés ici
│   ├── templates/          # (optionnel) Page HTML
│── tests/
│   ├── test_api.py         # Tests Flask
│── Dockerfile              # Conteneurisation
│── requirements.txt        # Dépendances Python
│── .gitignore              # Exclusion fichiers inutiles
│── README.md               # Documentation
