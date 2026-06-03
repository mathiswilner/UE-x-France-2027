import pandas as pd
import numpy as np

YEARS = list(range(2000, 2026))

budget_data = pd.DataFrame({
    "Année": YEARS,
    "Contribution brute": [
        15.5, 15.8, 16.2, 16.5, 17.0, 17.3, 17.8, 18.2, 18.5, 18.0,
        19.0, 19.5, 20.0, 20.5, 21.0, 21.3, 21.8, 22.0, 22.5, 23.0,
        23.5, 24.0, 25.0, 25.5, 26.0, 26.2
    ],
    "Retours directs": [
        11.0, 11.2, 11.5, 12.0, 12.3, 12.5, 13.0, 13.2, 13.5, 13.0,
        13.5, 14.0, 14.2, 14.5, 14.8, 15.0, 15.2, 15.5, 15.8, 16.0,
        16.2, 16.5, 17.0, 17.5, 18.0, 16.4
    ],
})
budget_data["Contribution nette"] = (
    budget_data["Contribution brute"] - budget_data["Retours directs"]
)

np.random.seed(42)
pib_reel = [100.0]
pib_sans_ue = [100.0]
for i in range(1, len(YEARS)):
    g = 1.3 + np.random.normal(0, 1.2)
    if YEARS[i] == 2009:
        g = -2.9
    elif YEARS[i] == 2020:
        g = -7.9
    elif YEARS[i] == 2021:
        g = 6.8
    pib_reel.append(pib_reel[-1] * (1 + g / 100))
    penalty = 0.25 + 0.005 * i
    pib_sans_ue.append(pib_sans_ue[-1] * (1 + (g - penalty) / 100))

pib_data = pd.DataFrame({
    "Année": YEARS,
    "PIB réel": pib_reel,
    "PIB sans UE": pib_sans_ue,
})
pib_data["Gain cumulé pct"] = (
    (pib_data["PIB réel"] / pib_data["PIB sans UE"] - 1) * 100
)

ide_data = pd.DataFrame({
    "Année": YEARS,
    "IDE totaux": [
        35, 40, 38, 32, 30, 55, 60, 65, 50, 25,
        30, 35, 25, 20, 15, 40, 35, 45, 55, 50,
        20, 35, 55, 60, 45, 50
    ],
    "dont intra UE": [
        18, 22, 20, 17, 16, 30, 33, 36, 28, 14,
        17, 19, 14, 11, 8, 22, 19, 25, 30, 27,
        11, 19, 30, 33, 25, 28
    ],
})
ide_data["IDE sans UE"] = ide_data["IDE totaux"] - ide_data["dont intra UE"] * 0.40

benefices = pd.DataFrame({
    "Canal": [
        "Marché unique (commerce)", "PAC (retours agricoles)",
        "Fonds structurels", "Recherche et innovation",
        "IDE additionnels", "Économie coûts d'emprunt (euro)",
        "Négociations commerciales", "Erasmus+ et mobilité",
    ],
    "Mds": [90, 9.5, 3.5, 2.8, 12, 25, 8, 0.7],
    "Catégorie": [
        "Commerce", "Budget direct", "Budget direct", "Budget direct",
        "Investissement", "Financier", "Commerce", "Capital humain",
    ],
})

scenarios = pd.DataFrame({
    "Scénario": [
        "EEE (Norvège)",
        "Accord bilatéral (Suisse/CETA)",
        "Sortie complète (OMC)",
    ],
    "PIB pct": [-2.0, -4.5, -7.0],
    "PIB mds": [-54, -122, -189],
    "Emplois k": [-150, -350, -550],
    "Coût ménage": [-750, -1700, -2650],
})

brexit = pd.DataFrame({
    "Indicateur": ["PIB", "Investissement", "Commerce", "Productivité", "Emploi"],
    "UK observé": [-6.5, -15, -25, -3.5, -3.5],
    "France projection": [-7.0, -18, -28, -4.0, -4.0],
})

CONTRIBUTION_NETTE = 10
BENEFICE_TOTAL = benefices["Mds"].sum()
RATIO = BENEFICE_TOTAL / CONTRIBUTION_NETTE
GAIN_PIB = pib_data["Gain cumulé pct"].iloc[-1]
