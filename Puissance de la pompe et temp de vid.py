def calculate_pump_power(HMT, Q_water, rho, eta):
    """
    Calcule la puissance requise pour la pompe.

    Parameters:
    - HMT (float): Hauteur Manométrique Totale (m).
    - Q_water (float): Débit volumique de l'eau (m³/s).
    - rho (float): Masse volumique du fluide (kg/m³).
    - eta (float): Rendement de la pompe (entre 0 et 1).

    Returns:
    - float: Puissance requise (W).
    """
    g = 9.81  # Accélération gravitationnelle (m/s²)
    power = (rho * g * Q_water * HMT) / eta  # Formule pour la puissance
    return power


def calculate_drain_time(V, Q_pump_m3h):
    """
    Calcule le temps de vidange d'un réservoir.

    Parameters:
    - V (float): Volume du réservoir (m³).
    - Q_pump_m3h (float): Débit de refoulement de la pompe (m³/h).

    Returns:
    - float: Temps de vidange (secondes).
    """
    # Conversion du débit de m³/h en m³/s
    Q_pump = Q_pump_m3h / 3600  # Conversion de m³/h en m³/s
    if Q_pump == 0:
        raise ValueError("Le débit de la pompe (Q) ne peut pas être nul.")
    return V / Q_pump  # Calcul du temps de vidange


def main():
    print("=== Calcul de la Puissance de la Pompe et du Temps de Vidange ===\n")

    try:
        # Collecte des données d'entrée
        HMT = float(input("Entrez la Hauteur Manométrique Totale (HMT) en mètres : "))
        Q_water = float(input("Entrez le Débit Volumique de l'eau (Q) en m³/s : "))
        rho = float(input("Entrez la Masse Volumique du fluide (par défaut, eau = 1000 kg/m³) : ") or 1000)
        eta = float(input("Entrez le Rendement de la Pompe (entre 0 et 1, par exemple 0.8 pour 80%) : "))
        Q_pump_m3h = float(input("Entrez le Débit de Refoulement de la Pompe (Q) en m³/h : "))
        V = float(input("Entrez le Volume du Réservoir à vidanger (en m³) : "))

        # Vérification des entrées
        if eta <= 0 or eta > 1:
            raise ValueError("Le rendement de la pompe (eta) doit être compris entre 0 et 1.")
        if Q_pump_m3h <= 0:
            raise ValueError("Le débit de refoulement de la pompe (Q) doit être supérieur à 0.")
        if HMT <= 0 or V <= 0:
            raise ValueError("Les valeurs de HMT et V doivent être positives.")

        # Calculs
        pump_power = calculate_pump_power(HMT, Q_water, rho, eta)  # Débit volumique de l'eau (Q_water)
        drain_time = calculate_drain_time(V, Q_pump_m3h)  # Débit de refoulement de la pompe (Q_pump_m3h)

        # Résultats
        print("\n=== Résultats ===")
        print(f"Puissance requise pour la pompe : {pump_power:.2f} W ({pump_power / 1000:.2f} kW)")
        print(f"Temps nécessaire pour vidanger le réservoir : {drain_time:.2f} secondes ({drain_time / 60:.2f} minutes)")

    except ValueError as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
