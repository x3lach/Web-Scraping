# Importation du module BeautifulSoup pour analyser le HTML
from bs4 import BeautifulSoup

# Ouvrir le fichier HTML contenant les pizzas, en mode lecture avec encodage UTF-8
with open("pizzas.html", "r", encoding="utf-8") as file:
    # Créer un objet BeautifulSoup pour parser le HTML
    soup = BeautifulSoup(file, "html.parser")

# Trouver toutes les balises contenant les informations d'un produit
pizzas = soup.find_all("div", class_="product-container")

# Parcourir chaque bloc de pizza trouvé
for pizza in pizzas:
    # Extraire le nom de la pizza en cherchant la balise <span> avec la classe "menu-entry"
    name_element = pizza.find("span", class_="menu-entry")
    if name_element:
        name = name_element.get_text(strip=True)
        
        # Extraire la description de la pizza (si disponible)
        description_element = pizza.find("p", class_="menu-page-product-description")
        description = description_element.get_text(strip=True) if description_element else "Pas de description"
        
        # Essayer de trouver le lien de commande
        order_link_element = pizza.find("a", class_="order-now")
        order_link = order_link_element.get('href', "Pas de lien") if order_link_element else "Pas de lien"
        
        # Afficher les résultats formatés pour chaque pizza
        print(f"Nom: {name}")
        print(f"Description: {description}")
        print(f"Lien: {order_link}\n")  # \n pour une ligne vide entre chaque pizza
