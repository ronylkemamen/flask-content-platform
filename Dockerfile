# Utiliser l'image Python officielle
FROM python:3.9

COPY requirements.txt /app

# Définir le répertoire de travail
WORKDIR /flask-content-plateform


# Copier le code dans le conteneur
COPY . /flask-content-plateform


# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app/routes.py"]

