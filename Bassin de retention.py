import math

# Fonctions pour effectuer les calculs
def calcul_surface_active(S, Ca):
    return S * Ca  # Surface active en hectares

def calcul_debit_fuite(Sf, K):
    return Sf * K  # Débit de fuite en m³/s

def calcul_debit_specifique(Qf, Sa):
    return (6 * Qf) / Sa  # Débit spécifique en mm/min

def calcul_hauteur_maximale(Tm, qs, b):
    return Tm * qs * (-b / (b + 1))  # Hauteur maximale de pluie en mm

def calcul_volume_bassin(hmax, Sa):
    return 10 * hmax * Sa  # Volume du bassin en m³

# Fonction principale pour collecter les entrées et effectuer les calculs
def dimensionner_bassin_retenue():
    print("=== Dimensionnement du Bassin de Rétention ===")

    # Collecte des données utilisateur
    try:
        T = float(input("Entrez la période de retour (T) en années : "))
        a = float(input("Entrez le coefficient Montana (a) : "))
        b = float(input("Entrez le coefficient Montana (b, doit être < 0) : "))
        if b >= 0:
            raise ValueError("Le coefficient b doit être négatif.")
        S = float(input("Entrez la surface totale du bassin versant (S) en hectares : "))
        Ca = float(input("Entrez le coefficient d'apport (Ca, entre 0 et 1) : "))
        if not (0 <= Ca <= 1):
            raise ValueError("Le coefficient d'apport doit être compris entre 0 et 1.")
        K = float(input("Entrez la perméabilité du sol (K) en m/s : "))
        Sf = float(input("Entrez la surface d'infiltration (Sf) en m² : "))
    except ValueError as e:
        print(f"Erreur : {e}")
        return

    # Effectuer les calculs
    Sa = calcul_surface_active(S, Ca)  # Surface active en hectares
    Qf = calcul_debit_fuite(Sf, K)  # Débit de fuite (m³/s)
    qs = calcul_debit_specifique(Qf, Sa)  # Débit spécifique (mm/min)
    Tm = math.sqrt(T)  # Hypothèse : Tm = sqrt(T)
    hmax = calcul_hauteur_maximale(Tm, qs, b)  # Hauteur maximale de pluie (mm)
    V = calcul_volume_bassin(hmax, Sa)  # Volume du bassin (m³)

    # Préparer les résultats à afficher
    resultats = {
        "Surface Active (Sa)": (f"{Sa:.2f}", "ha"),
        "Débit de Fuite (Qf)": (f"{Qf:.4f}", "m³/s"),
        "Débit Spécifique (qs)": (f"{qs:.4f}", "mm/min"),
        "Temps Caractéristique (Tm)": (f"{Tm:.2f}", "min"),
        "Hauteur Maximale de Pluie (hmax)": (f"{hmax:.2f}", "mm"),
        "Volume du Bassin (V)": (f"{V:.2f}", "m³")
    }

    # Afficher les résultats
    print("\n=== Résultats ===")
    for key, value in resultats.items():
        print(f"{key}: {value[0]} {value[1]}")

if __name__ == "__main__":
    dimensionner_bassin_retenue()
