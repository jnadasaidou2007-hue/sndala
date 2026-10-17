import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Prédiction de réussite",
    page_icon="🎓"
)

st.title("🎓 Prédiction de réussite d'un étudiant")
st.write("Application simple de Machine Learning")

# 1. Création des données d'exemple
data = pd.DataFrame({
    "heures_revision": [
        1, 2, 1, 3, 2, 4, 5, 6, 4, 7,
        8, 6, 9, 3, 5, 8, 2, 7, 9, 10
    ],
    "absences": [
        10, 8, 12, 6, 9, 5, 3, 2, 5, 1,
        0, 3, 1, 8, 4, 0, 11, 2, 0, 1
    ],
    "note_precedente": [
        8, 9, 7, 10, 9, 12, 14, 15, 11, 16,
        17, 14, 18, 8, 13, 17, 7, 15, 19, 18
    ],
    "reussite": [
        0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
        1, 1, 1, 0, 1, 1, 0, 1, 1, 1
    ]
})

# 2. Séparation des variables
X = data[[
    "heures_revision",
    "absences",
    "note_precedente"
]]
y = data["reussite"]

# 3. Séparation entraînement / test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 4. Entraînement du modèle
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
model.fit(X_train, y_train)

# 5. Évaluation du modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.metric("Exactitude sur le jeu de test",
          f"{accuracy:.0%}")

st.divider()
st.subheader("Tester un étudiant")

heures = st.slider(
    "Heures de révision par jour",
    0, 12, 4
)

absences = st.slider(
    "Nombre d'absences",
    0, 20, 3
)

note = st.slider(
    "Note précédente sur 20",
    0, 20, 12
)

if st.button("Prédire"):
    nouvel_etudiant = pd.DataFrame([{
        "heures_revision": heures,
        "absences": absences,
        "note_precedente": note
    }])

    prediction = model.predict(nouvel_etudiant)[0]
    probabilites = model.predict_proba(
        nouvel_etudiant
    )[0]

    st.write(
        f"Probabilité estimée de réussite : "
        f"{probabilites[1]:.0%}"
    )

    if prediction == 1:
        st.success("Le modèle prédit une réussite.")
    else:
        st.warning("Le modèle prédit un risque d'échec.")

st.caption(
    "Projet pédagogique : les données sont fictives. "
    "Les prédictions ne sont pas fiables pour une "
    "décision réelle sans données représentatives."
)
