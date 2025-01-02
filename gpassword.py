import random
import string

def generer_mot_de_passe(longueur=12):
    """
    Génère un mot de passe sécurisé.
    
    Args:
        longueur (int): Longueur du mot de passe (par défaut 12).
    
    Returns:
        str: Un mot de passe sécurisé.
    """
    if longueur < 8:
        raise ValueError("La longueur minimale recommandée pour un mot de passe est de 8 caractères.")
    
    # Définir les caractères possibles
    lettres = string.ascii_letters  # Lettres majuscules et minuscules
    chiffres = string.digits        # Chiffres
    symboles = string.punctuation   # Symboles spéciaux

    # Garantir au moins un caractère de chaque type
    tous_les_caracteres = lettres + chiffres + symboles
    mot_de_passe = [
        random.choice(string.ascii_uppercase),  # Au moins une majuscule
        random.choice(string.ascii_lowercase),  # Au moins une minuscule
        random.choice(string.digits),          # Au moins un chiffre
        random.choice(string.punctuation)      # Au moins un symbole spécial
    ]

    # Compléter le reste du mot de passe avec des caractères aléatoires
    mot_de_passe += random.choices(tous_les_caracteres, k=longueur - 4)

    # Mélanger les caractères pour plus de sécurité
    random.shuffle(mot_de_passe)

    return ''.join(mot_de_passe)

# Exemple d'utilisation
mot_de_passe = generer_mot_de_passe(16)
print("Mot de passe généré :", mot_de_passe)
