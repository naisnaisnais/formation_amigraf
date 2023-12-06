import pandas as pd
import csv

# Selectionner l'une des 3 villes (New york city, Washington ou Chicago)
# Selectionner le mois (Janvier - Février - Mars - Avril - Juin, etc.)
low_memory=False
data_NY = pd.read_csv("projet/cleaned_new_york_city.csv", parse_dates=['Start Time'], infer_datetime_format=True)
data_washington = pd.read_csv("projet/cleaned_washington_city.csv", parse_dates=['Start Time'], infer_datetime_format=True)
data_chicago = pd.read_csv("projet/cleaned_chicago_city.csv", parse_dates=['Start Time'], infer_datetime_format=True)

# récupération du mois dans les 3 fichiers :
data_NY["mois"] = pd.to_datetime(data_NY["Start Time"], format="%m")
print(data_NY['mois'].dt.strftime("%m"))

data_washington["mois"] = pd.to_datetime(data_washington["Start Time"], format="%m")
print(data_washington['mois'].dt.strftime("%m"))

data_chicago["mois"] = pd.to_datetime(data_chicago["Start Time"], format="%m")
print(data_chicago['mois'].dt.strftime("%m"))

def choix_ville():
        print("""Choisir une ville :
                    1. New York
                    2. Washington
                    3. Chicago""")
        choix = input("Votre choix (1|2|3) : ")

        if choix == "1" :
                return "New York City", data_NY 
        elif choix == "2" :
                return "Washington", data_washington
        elif choix == "3" :
                return "Chicago", data_chicago 

        else:
            print("Erreur, réessayer ! \n\n")
            return choix_ville()

def choix_mois() :
        print("""Choisir le mois :
                 1. Janvier
                 2. Février
                 3. Mars
                 4. Avril
                 5. Mai
                 6. Juin
                 7. Juillet
                 8. Aout
                 9. Septembre
                 10. Octobre
                 11. Novembre
                 12. Décembre""")
        choix = input("Votre choix (1|2|3|4|5|6|7|8|9|10|11|12) : ")
        if choix in ("1","2","3","4","5","6","7","8","9","10","11","12"):
              return choix
        else :
              print("Erreur, réessayer !")
              return choix_mois()

def menu():
    ville = choix_ville()
    mois = int(choix_mois())

    data =(ville[ville[("Start Time")].dt.month == mois])
    print(data)
    print(f"\nStatistiques pour {ville} en {mois}:\n")
    print(data.head()) 
print(menu())

# Obtenez les informations traitées suivantes :
# Le jour de la semaine avec le plus d'activité.
# L'heure de démarrage la plus courante.
# La durée de voyage moyen sur la période (mois).
# Le total pour chaque catégorie de User.
# Le nombre total de femmes et d'hommes sur la période.
# L'année de naissance la plus ancienne.
# L'année de naissance la plus récente.
# L'année de naissance la plus courante sur la période (avec le nombre d'occurence).
