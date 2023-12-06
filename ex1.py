import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import seaborn as sb

file_path = "./projet/cleaned_autos.csv"

df = pd.read_csv(file_path)

# Nombre total de véhicules en vente selon le type de véhicule.
nb_par_type = (df.groupby("vehicleType").size().sort_values(ascending=False).head(10))
print(nb_par_type)
"""plt.figure(facecolor="#ccccff")
plt.bar(nb_par_type.index,nb_par_type, color="#9999cc")
plt.xlabel("Type de véhicules", color="#000066")
plt.ylabel("Nombre de véhicules", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()"""

# Répartition des véhicules en fonction de l'année d'immatriculation
nb_par_annee = (df.groupby("yearOfRegistration").size().sort_values(ascending=False))
print(nb_par_annee)
"""plt.figure(facecolor="#ccccff")
plt.scatter(nb_par_annee.index,nb_par_annee, color="#9999cc")
plt.xlabel("Année d'immatriculation", color="#000066")
plt.ylabel("Nombre de véhicules", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()"""

# Nombre de véhicules par marque
nb_par_marque = (df.groupby("brand").size().sort_values(ascending=False).head(15))
print(nb_par_marque)
"""plt.figure(facecolor="#ccccff")
plt.stackplot(nb_par_marque.index,nb_par_marque, color="#9999cc")
plt.xlabel("Marque", color="#000066")
plt.ylabel("Nombre de véhicules", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()"""

# Prix moyen des véhicules par type de véhicule et type de boîte de vitesses
prix_moy_vehicule_boite = (df.groupby(["vehicleType", "gearbox"])["price"].std().sort_values(ascending=False))
print(prix_moy_vehicule_boite)
plt.figure(facecolor="#ccccff")
plt.bar(prix_moy_vehicule_boite.index,prix_moy_vehicule_boite, color="#9999cc")
plt.xlabel("Type", color="#000066")
plt.ylabel("Prix moyen", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()

# Prix moyen des véhicules selon le type de carburant et le type de boîte de vitesses
prix_moy_carburant_boite = (df.groupby(["fuelType","gearbox"])["price"].std().sort_values(ascending=False))
print(prix_moy_carburant_boite)
"""plt.figure(facecolor="#ccccff")
plt.bar(prix_moy_carburant.index,prix_moy_carburant, color="#9999cc")
plt.bar(prix_moy_boite.index,prix_moy_boite, color="#660000")
plt.xlabel("Type carburant et boîte de vitesse", color="#000066")
plt.ylabel("Prix moyen", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()"""


# Dans la ville de Frankfort, il voudrait une concession exclusivement pour la partie aisée de la population. 
# Il voudrait savoir quelles sont les 2 marques principales qu'il pourrait avoir dans sa concession et les 2 catégories de véhicule
# (en lien avec les 2 marques) qui colleraient le mieux à la population aisée, toujours dans sa concession.
# Il faudra donc trouver les Prix moyens des véhicules par type de véhicule et marque.
prix_moy_type_marque = df.groupby(["vehicleType","brand"])["price"].mean().reset_index()
prix_moy_type_marque= prix_moy_type_marque.sort_values(by = "price", ascending=False)
print(prix_moy_type_marque)

# Avec une dernière représentation graphique sous forme de heatmap, il faudra le convaincre de la solution que vous réussi à extraire de votre analyse.
# https://www.practicalpythonfordatascience.com/ap_seaborn_palette
heatmap = prix_moy_type_marque.pivot_table(index = "brand", columns = "vehicleType", values = "price")
plt.figure(figsize=(12, len(heatmap)*0.30))
sb.heatmap(heatmap, cmap = "YlGn", annot=True, fmt=".2f", linewidth="0.5")
plt.xlabel("Marque")
plt.ylabel("Type de véhicule")
plt.title("Prix")

plt.tight_layout()
plt.show()
plt.savefig("./projet/graphiquevert.png")
