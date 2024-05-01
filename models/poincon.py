class Poincon:
    """
    Un Poinçon représente un bip réalisé sur une badgeuse. Un poinçon est donc toujours attribué à 1 badgeuse.
    
    Une badgeuse peut servir à plusieurs poinçons (par exemple début puis fin d'une BO).

    Un poinçon peut avoir plusieurs rôles (par exemple dégel et début du meilleur grimpeur).
    """


    def __init__(self, journee: int, epreuve_name: str, signaleur: str, badgeuse_num: int, fonction: str, bonus_points: float) -> None:
        self.journee = journee
        self.epreuve_name = epreuve_name
        self.signaleur = signaleur
        self.badgeuse_num = badgeuse_num
        self.fonction = fonction
        self.bonus_points = bonus_points

        self.is_debut_mg = False
        self.is_fin_mg = False

    def __repr__(self) -> str:
        if self.is_debut_mg:
            debut_mg = 'Debut MG'
        else:
            debut_mg = ''
        if self.is_fin_mg:
            fin_mg = 'Fin MG'
        else:
            fin_mg = ''
        return f"Poincon({self.signaleur}, {self.badgeuse_num}, {self.fonction}, {debut_mg}{fin_mg})"