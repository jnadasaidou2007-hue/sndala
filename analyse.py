import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "superficie": [50, 60, 70, 80, 90, 100, 110, 120],
    "chambres": [1, 2, 2, 3, 3, 3, 4, 4],
    "anciennete": [20, 15, 12, 10, 8, 5, 4, 2],
    "prix": [400, 480, 530, 650, 700, 820, 850, 960]
})

print("Jeu de données :")
print(data)
print("\\nStatistiques descriptives :")
print(data.describe())
print("\\nPrix moyen :", data["prix"].mean(), "kDH")
print("Prix médian :", data["prix"].median(), "kDH")
print("Prix minimum :", data["prix"].min(), "kDH")
print("Prix maximum :", data["prix"].max(), "kDH")

data["prix_m2"] = data["prix"] * 1000 / data["superficie"]
print("\\nPrix au mètre carré :")
print(data[["superficie", "prix", "prix_m2"]].round(2))

print("\\nCorrélation superficie/prix :")
print(data["superficie"].corr(data["prix"]))

plt.scatter(data["superficie"], data["prix"])
plt.xlabel("Superficie (m²)")
plt.ylabel("Prix (milliers de DH)")
plt.title("Relation entre superficie et prix")
plt.grid(True)
plt.show()
