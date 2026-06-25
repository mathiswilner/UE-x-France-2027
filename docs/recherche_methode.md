# Méthode de recherche - Le prix du Frexit

## PRIORITÉ 1 : Vérifier les chiffres existants du site

### Contribution nette (10 Mds)
- [ ] Télécharger le rapport financier annuel UE (ec.europa.eu/budget/financialreport)
- [ ] Noter le montant exact versé par la France et les retours
- [ ] Choisir une année de référence (2023 ou moyenne 2021-2023)
- [ ] Vérifier avec le rapport du Sénat sur le prélèvement européen

### Chiffres Brexit (page Brexit)
- [ ] Télécharger Bloom et al. (2025, NBER) : nber.org/papers/w34459
- [ ] Noter les chiffres exacts avec intervalles de confiance
- [ ] Vérifier avec les chiffres OBR (Office for Budget Responsibility UK)
- [ ] Vérifier avec UK in a Changing Europe

### Statistiques d'opinion (page Accueil + Idées reçues)
- [ ] Eurobaromètre le plus récent : noter le numéro exact et la date
- [ ] Vérifier "44% estiment que l'UE existe aux dépens de la France"
- [ ] Vérifier "30% ont une bonne image de l'UE"
- [ ] Vérifier "61% reconnaissent que la France a bénéficié de l'UE"
- [ ] Vérifier "79% soutiennent l'euro"
- [ ] Vérifier "77% veulent une politique commune de migration"

## PRIORITÉ 2 : Recalculer le chiffre "151 milliards"

### Canal A : Marché unique (le plus gros)
- [ ] Lire Mayer, Vicard & Zignago (2018) CEPII
- [ ] Lire Fontagné & Yotov (2024)
- [ ] Trouver le gain spécifique pour la France (entre 3 et 7% du PIB)
- [ ] Choisir une hypothèse conservatrice et la documenter
- [ ] PIB France x taux = montant en milliards

### Canal B : PAC
- [ ] Données ASP (asp-public.fr) ou telepac.agriculture.gouv.fr
- [ ] Montant total des aides PAC versées en France (année récente)
- [ ] Chiffre attendu : 9 à 10 Mds

### Canal C : Fonds structurels
- [ ] Données europe-en-france.gouv.fr
- [ ] FEDER + FSE+ + FTJ + FEAMPA
- [ ] Montant 2021-2027 divisé par 7

### Canal D : Recherche et innovation
- [ ] Horizon Europe : retours France (country profile)
- [ ] Erasmus+ : montants France
- [ ] Chiffre attendu : 2,5 à 3,5 Mds

### Canal E : IDE additionnels
- [ ] Banque de France : IDE entrants (séries longues)
- [ ] Appliquer coefficient Bruno et al. (28 à 60%)
- [ ] Convertir en bénéfice économique (avec multiplicateur documenté)

### Canal F : Économie coûts d'emprunt (euro)
- [ ] Banque de France : taux OAT séries longues
- [ ] Estimer le différentiel attribuable à l'euro
- [ ] Appliquer à la dette publique (~3 000 Mds)
- [ ] Documenter l'incertitude (canal le plus fragile)

### Canal G : Négociations commerciales collectives
- [ ] Études d'impact des accords UE (CETA, UE-Japon, UE-Corée)
- [ ] DG Trade (Commission européenne)
- [ ] Estimer la part France

### Canal H : Erasmus+
- [ ] Budget Erasmus+ pour la France (directement disponible)

## PRIORITÉ 3 : Calibrer le calculateur personnel

### Table de contribution par revenu
- [ ] DGFiP : distribution des revenus par décile
- [ ] Structure des recettes fiscales (IR, TVA, IS)
- [ ] Calculer pour chaque décile : (part fiscale) x contribution nette UE

### Taux de bénéfice par secteur
- [ ] Pour chaque secteur : part des exports vers l'UE (Eurostat)
- [ ] Part de la valeur ajoutée dépendant des échanges intra-UE (OCDE TiVA)
- [ ] Appliquer le coefficient de gain du marché unique

### Fonds régionaux par habitant
- [ ] cohesiondata.ec.europa.eu : allocations FEDER/FSE+ par région
- [ ] asp-public.fr : PAC par région
- [ ] Additionner et diviser par population régionale (INSEE)

### Taux de perte Frexit
- [ ] Scénarios CEPII (Mayer et al., 2018) spécifiques France
- [ ] Comparer avec effets observés Brexit
- [ ] Produire 3 scénarios avec intervalles de confiance

## PRIORITÉ 4 : Estimations économétriques (mémoire)

### Modèle de gravité structurel
- [ ] Construire base panel (exportateur x importateur x année x secteur)
- [ ] Données BACI (CEPII) + CEPII Gravity database
- [ ] Estimation PPML avec effets fixes
- [ ] Exact Hat Algebra pour contrefactuels
- [ ] 3 scénarios Frexit

### Contrôle synthétique
- [ ] Donor pool : Australie, Canada, Japon, Nouvelle-Zélande, Norvège
- [ ] Données PIB/habitant longues séries (Banque mondiale WDI)
- [ ] Package R Synth ou Python pysynth
- [ ] Tests de robustesse (placebo, leave-one-out)

## PRIORITÉ 5 : Vérification page Idées reçues

### Idée reçue 2 : "L'euro nous a appauvris"
- [ ] Recalculer économie sur crédit immobilier (taux avec/sans euro)
- [ ] Vérifier économie annuelle État (25 Mds ?)

### Idée reçue 4 : "Immigration incontrôlée"
- [ ] Données réelles libre circulation intra-UE en France (INSEE, Eurostat)
- [ ] Textes traités sur les compétences nationales vs UE

### Idée reçue 5 : "Aucun pouvoir de décision"
- [ ] Vérifier nombre d'eurodéputés français (peut changer après élections)
- [ ] Articles du Traité de Lisbonne sur le veto

## SOURCES PRINCIPALES

- ec.europa.eu/budget/financialreport
- cohesiondata.ec.europa.eu
- europe-en-france.gouv.fr
- cepii.fr (BACI, Gravity database, working papers)
- banque-france.fr (IDE, taux OAT)
- insee.fr (données régionales, revenus par décile)
- eurobarometer.eu
- nber.org (Bloom et al.)
- asp-public.fr (PAC)

## CONTACTS POTENTIELS

- Vincent Vicard (CEPII) : auteur de référence sur le commerce UE
- Thierry Mayer (Sciences Po) : co-auteur du modèle de gravité
- Lionel Fontagné (PSE) : réévaluation du marché unique
- OFCE / France Stratégie : policy papers