# Estimation du prix d'une maison

Mini-projet pédagogique (BTS IA) : analyse statistique de données immobilières
et prédiction du prix d'une maison avec une régression linéaire,
via une application Streamlit.

Lien de l'application : https://TON-APP.streamlit.app

## Fonctionnalités

- Exploration du jeu de données (8 maisons fictives)
- Statistiques descriptives (moyenne, médiane, min, max, étendue)
- Entraînement d'un modèle de régression linéaire (scikit-learn)
- Évaluation avec MAE et R²
- Estimation du prix selon la superficie, le nombre de chambres et l'ancienneté

## Structure du projet

- `app.py` : application Streamlit
- `analyse.py` : analyse statistique et graphique avec Python
- `requirements.txt` : bibliothèques nécessaires

## Installation et lancement

pip install -r requirements.txt
streamlit run app.py

L'application s'ouvre sur http://localhost:8501

## Limites

Les données sont fictives et très peu nombreuses (8 exemples) :
les estimations sont uniquement pédagogiques et ne doivent pas servir
pour une transaction immobilière.

## Auteure

Nada Saidou
