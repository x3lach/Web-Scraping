# Importation du module BeautifulSoup pour analyser le HTML
from bs4 import BeautifulSoup

# Ouvrir le fichier HTML téléchargé en mode lecture avec encodage UTF-8
with open("pizzas.html", "r", encoding="utf-8") as file:
    # Créer un objet BeautifulSoup pour analyser le contenu HTML du fichier
    soup = BeautifulSoup(file, "html.parser")

# Chercher tous les éléments span avec la classe "menu-entry"
pizzas = soup.find_all("span", class_="menu-entry")

# Parcourir la liste des éléments trouvés
for pizza in pizzas:
    # Extraire et afficher uniquement le texte de chaque balise <span>
    pizza_name = pizza.get_text(strip=True)
    if pizza_name:  # Only print non-empty names
        print(pizza_name)
