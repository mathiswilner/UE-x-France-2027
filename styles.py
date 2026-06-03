# =============================================================================
# IDENTITÉ VISUELLE — LE PRIX DU FREXIT
# Inspiré du Système de Design de l'État français (DSFR)
# =============================================================================

C = {
    # Fonds
    "bg": "#FFFFFF",
    "bg_alt": "#F6F6F6",
    "bg_dark": "#1B1B35",

    # Texte
    "text": "#1B1B35",
    "text_secondary": "#666666",
    "text_light": "#FFFFFF",

    # Accents
    "bleu_france": "#000091",
    "rouge_marianne": "#E1000F",
    "vert": "#18753C",
    "or": "#D4A017",

    # Utilitaires
    "border": "#DDDDDD",
    "border_strong": "#000091",
    "muted": "#929292",
    "highlight": "#F5F5FE",
}

# Police
FONT = "'Source Sans 3', 'Source Sans Pro', 'Segoe UI', 'Helvetica Neue', sans-serif"

# Pas d'ombres, coins droits, esprit gouvernemental
CARD = {
    "backgroundColor": C["bg"],
    "borderRadius": "2px",
    "padding": "24px",
    "marginBottom": "20px",
    "border": "1px solid " + C["border"],
}

CARD_HIGHLIGHT = {
    "backgroundColor": C["highlight"],
    "borderRadius": "2px",
    "padding": "24px",
    "marginBottom": "20px",
    "borderLeft": "4px solid " + C["bleu_france"],
}

CARD_ALERT = {
    "backgroundColor": "#FEF4F4",
    "borderRadius": "2px",
    "padding": "24px",
    "marginBottom": "20px",
    "borderLeft": "4px solid " + C["rouge_marianne"],
}

CARD_SUCCESS = {
    "backgroundColor": "#F5FBF8",
    "borderRadius": "2px",
    "padding": "24px",
    "marginBottom": "20px",
    "borderLeft": "4px solid " + C["vert"],
}

GC = {"displayModeBar": False}