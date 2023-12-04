import pandas as pd
import matplotlib.pyplot as plt

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
plt.plot(nb_par_annee, color="#9999cc")
plt.xlabel("Année d'immatriculation", color="#000066")
plt.ylabel("Nombre de véhicules", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()"""

# Nombre de véhicules par marque
nb_par_marque = (df.groupby("brand").size().sort_values(ascending=False).head(15))
print(nb_par_marque)
"""plt.figure(facecolor="#ccccff")
plt.bar(nb_par_marque.index,nb_par_marque, color="#9999cc")
plt.xlabel("Marque", color="#000066")
plt.ylabel("Nombre de véhicules", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()"""

# Prix moyen des véhicules par type de véhicule et type de boîte de vitesses
prix_moy_vehicule = (df.groupby("vehicleType")["price"].std().sort_values(ascending=False))
prix_moy_boite = (df.groupby("gearbox")["price"].std())
print(prix_moy_vehicule)
print(prix_moy_boite)
"""plt.figure(facecolor="#ccccff")
plt.bar(prix_moy_vehicule.index,prix_moy_vehicule, color="#9999cc")
plt.bar(prix_moy_boite.index,prix_moy_boite, color="#660000")
plt.xlabel("Type", color="#000066")
plt.ylabel("Prix moyen", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()"""

# Prix moyen des véhicules selon le type de carburant et le type de boîte de vitesses
prix_moy_carburant = (df.groupby("fuelType")["price"].std().sort_values(ascending=False))
print(prix_moy_vehicule)

plt.figure(facecolor="#ccccff")
plt.bar(prix_moy_carburant.index,prix_moy_carburant, color="#9999cc")
plt.bar(prix_moy_boite.index,prix_moy_boite, color="#660000")
plt.xlabel("Type carburant et boîte de vitesse", color="#000066")
plt.ylabel("Prix moyen", color="#000066")
plt.grid(color="beige", axis="y")
plt.show()

