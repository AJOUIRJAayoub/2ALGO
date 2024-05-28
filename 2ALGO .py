def strategie_gloutonne(T, C, A, B):
    # Définition de la fonction avec les paramètres : 
    # T est une liste de valeurs numériques,
    # C est une liste de catégories associées à chaque valeur dans T,
    # A et B sont des coefficients utilisés dans les calculs de valeurs.

    n = len(T)  # Calcul de la longueur de la liste T, qui détermine le nombre d'itérations de la boucle.
    if n == 0:  # Vérifie si la liste T est vide.
        return 0, []  # Retourne 0 et une liste vide si T est vide.

    somme_max = 0  # Initialisation de la variable qui va accumuler la somme maximale.
    chemin = []  # Initialisation de la liste qui va enregistrer les indices des éléments ajoutés à la somme_max.
    dernier_index = -1  # Variable pour suivre l'indice du dernier élément traité; -1 indique qu'aucun élément n'a été traité.
    dernier_symbole = None  # Variable pour suivre le symbole de l'élément précédemment traité.

    for i in range(n):  # Boucle pour traiter chaque élément de T et C.
        if dernier_index == -1 or C[i] != dernier_symbole:  # Condition pour utiliser le coefficient B.
            valeur_actuelle = B * T[i]  # Calcul de la valeur actuelle en utilisant le coefficient B.
        else:  # Sinon, utilise le coefficient A si l'élément courant a le même symbole que le précédent.
            valeur_actuelle = A * T[i]  # Calcul de la valeur actuelle en utilisant le coefficient A.

        if valeur_actuelle > 0:  # Vérifie si la valeur actuelle est positive.
            somme_max += valeur_actuelle  # Ajoute la valeur actuelle à la somme maximale si elle est positive.
            chemin.append(i)  # Ajoute l'indice de l'élément courant au chemin.
            dernier_index = i  # Met à jour le dernier indice traité.
            dernier_symbole = C[i]  # Met à jour le dernier symbole traité.

    return somme_max, chemin  # Retourne la somme maximale calculée et le chemin des indices ajoutés.

# Test de la fonction

#EXEMPLE 1
T = [9, 7, 8, 7, 10, 7]
C = [2, 1, 1, 4, 4, 2]
A = -2
B = 5

#EXEMPLE 2
#T = [3, 9, 2, 7, 3, 1]
#C = [2, 2, 5, 4, 2, 1]
#A = 2
#B = -5

print(strategie_gloutonne(T, C, A, B))




def somme_max_recursive(T, C, A, B, i=0, dernier_symbole=None):
    # Définition de la fonction récursive pour calculer la somme maximale.
    # La fonction prend en paramètres :
    # T : une liste de valeurs numériques,
    # C : une liste de symboles ou de catégories associés à chaque valeur dans T,
    # A et B : les coefficients utilisés pour calculer les sommes maximales,
    # i : l'indice actuel à partir duquel on commence à calculer la somme maximale (défaut à 0),
    # dernier_symbole : le symbole du dernier élément visité (défaut à None).

    if i >= len(T):
        return 0
    # Cas de base : Si l'indice actuel dépasse la longueur de la liste T, on retourne 0.

    # Ne pas visiter l'emplacement i
    max_collecte = somme_max_recursive(T, C, A, B, i + 1, dernier_symbole)
    # Appel récursif pour calculer la somme maximale sans visiter l'emplacement i.

    # Visiter l'emplacement i
    if dernier_symbole is None or C[i] != dernier_symbole:
        collecte = B * T[i] + somme_max_recursive(T, C, A, B, i + 1, C[i])
    else:
        collecte = A * T[i] + somme_max_recursive(T, C, A, B, i + 1, C[i])
    # Appel récursif pour calculer la somme maximale en visitant l'emplacement i.
    # Le coefficient B est utilisé si c'est le premier élément visité ou si le symbole est différent du dernier symbole visité.
    # Sinon, le coefficient A est utilisé.

    return max(max_collecte, collecte)
    # Retourne la somme maximale entre ne pas visiter l'emplacement i et visiter l'emplacement i.

# Test de la fonction
print(somme_max_recursive(T, C, A, B))
# Appel de la fonction pour tester son fonctionnement avec les valeurs données pour T, C, A et B.




def somme_max_top_down(T, C, A, B):
    # Définition de la fonction qui calcule la somme maximale en adoptant une approche dynamique top-down.
    # Prend en paramètres :
    # T : une liste de valeurs numériques,
    # C : une liste de symboles ou de catégories associés à chaque valeur dans T,
    # A et B : les coefficients utilisés pour calculer les sommes maximales.

    n = len(T)  # Calcul de la longueur de la liste T.
    memo = {}  # Initialisation du dictionnaire pour la mémoïsation des sous-problèmes.

    def calculate(i, dernier_symbole):
        # Fonction récursive interne pour calculer la somme maximale à partir de l'indice i et avec le dernier symbole donné.

        if i >= n:
            return 0  # Cas de base : retourne 0 si l'indice dépasse la longueur de la liste T.

        if (i, dernier_symbole) in memo:
            return memo[(i, dernier_symbole)]  # Retourne la valeur mémorisée si elle existe.

        # Calcul de la somme maximale en explorant les deux options : visiter ou ne pas visiter l'emplacement i.
        max_collecte = calculate(i + 1, dernier_symbole)

        if dernier_symbole is None or C[i] != dernier_symbole:
            collecte = B * T[i] + calculate(i + 1, C[i])
        else:
            collecte = A * T[i] + calculate(i + 1, C[i])

        # Mémorisation de la somme maximale obtenue pour ce sous-problème.
        memo[(i, dernier_symbole)] = max(max_collecte, collecte)
        return memo[(i, dernier_symbole)]  # Retourne la somme maximale calculée.

    # Appel initial à la fonction récursive avec l'indice de départ 0 et aucun dernier symbole.
    return calculate(0, None)

# Test de la fonction
print(somme_max_top_down(T, C, A, B))


def somme_max_bottom_up(T, C, A, B):
    # Cette fonction utilise une approche dynamique "Bottom Up" pour calculer la somme maximale collectée lors du parcours,
    # en tenant compte des coefficients A et B, ainsi que des catégories associées à chaque valeur.

    n = len(T)  # Détermine la longueur de la liste T.
    if n == 0:  # Vérifie si la liste T est vide.
        return 0, []  # Si la liste T est vide, retourne 0 comme somme maximale et une liste vide pour les indices visités.

    # Initialisation des tableaux pour stocker les résultats intermédiaires et les indices des emplacements visités
    dp = [0] * (n + 1)  # Tableau pour stocker les résultats intermédiaires du calcul de la somme maximale.
    trace = [None] * n  # Tableau pour enregistrer les indices des emplacements visités.

    for i in range(n - 1, -1, -1):
        # Parcours de la liste T en partant de la fin pour calculer la somme maximale pour chaque emplacement.

        # Calcul de la somme maximale pour l'emplacement i en utilisant la formule dynamique "Bottom Up"
        dp[i] = max(dp[i + 1], (B if i == n - 1 or C[i] != C[i + 1] else A) * T[i] + dp[i + 1])

        # Mise à jour de l'indice visité dans le tableau trace
        if i == n - 1 or C[i] != C[i + 1]:  # Vérifie si l'élément actuel est le dernier ou s'il a un symbole différent du suivant.
            trace[i] = i
        else:
            trace[i] = trace[i + 1]

    # Reconstruction du chemin
    vrai_chemin = []  # Liste pour enregistrer les indices des emplacements visités dans l'ordre.
    i = 0
    while i < n and trace[i] is not None:
        vrai_chemin.append(i)  # Ajoute l'indice de l'emplacement visité à vrai_chemin.
        i += 1 if trace[i] == i else trace[i] - i  # Déplace l'indice à l'emplacement suivant du chemin.

    return dp[0], vrai_chemin  # Retourne la somme maximale et la liste des indices des emplacements visités.

# Test de la fonction
print(somme_max_bottom_up(T, C, A, B))





