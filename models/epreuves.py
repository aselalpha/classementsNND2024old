class EpreuveCourse:

    def __init__(self, journee: int, name: str, points_participation: float, temps_ref: float, points_gain_min: float, points_perte_min: float, epreuve_type: str) -> None:
        self.journee = journee
        self.name = name
        self.points_participation = points_participation
        self.temps_ref = temps_ref
        self.points_gain_min = points_gain_min
        self.points_perte_min = points_perte_min
        self.epreuve_type = epreuve_type
        # Par défaut, l'épreuve n'est pas un meilleur grimpeur
        # Sinon, est de la forme {'temps_ref': float, 'points_gain_min': float, 'points_perte_min': float}
        self.meilleur_grimpeur: None|dict = None


class EpreuveActi:

    def __init__(self, journee: int, name: str, points_participation: float, pts_or: float, pts_argent: float, pts_bronze: float) -> None:
        self.journee = journee
        self.name = name
        self.points_participation = points_participation
        self.pts_or = pts_or
        self.pts_argent = pts_argent
        self.pts_bronze = pts_bronze
    