import pandas as pd

from models.epreuves import EpreuveActi, EpreuveCourse


def collect_epreuves(epreuves_excel_path: str, num_journee: int) -> list[EpreuveCourse|EpreuveActi]:

    epreuves_df = pd.read_excel(epreuves_excel_path).dropna(how='all')
    epreuves_list: list[EpreuveCourse|EpreuveActi] = []

    for _, row in epreuves_df.iterrows():
        if not 'meilleur grimpeur' in row['nom']:
            new_epreuve = create_epreuve_object(row, num_journee)
            epreuves_list.append(new_epreuve)
        else:
            append_mg_to_epreuve_course(row, epreuves_list)
            
    return epreuves_list


def create_epreuve_object(row: pd.Series, num_journee: int) -> EpreuveCourse|EpreuveActi:
    """Crée l'épreuve correspondante."""

    if row['type'] == 'acti':
        epreuve_object = EpreuveActi(
            num_journee,
            str(row['nom']),
            float(row['points_participation']),
            float(row['or']),
            float(row['argent']),
            float(row['bronze'])
        )

    else:
        epreuve_object = EpreuveCourse(
            num_journee,
            str(row['nom']),
            float(row['points_participation']),
            float(row['temps_ref']),
            float(row['points_gain_min']),
            float(row['points_perte_min']),
            str(row['type'])
        )
    
    return epreuve_object


def append_mg_to_epreuve_course(row: pd.Series, epreuves_list: list[EpreuveCourse]) -> None:
    """
    Update l'attribut `meilleur_grimpeur` de l'épreuve correspondante.
    Lève une exception si aucune épreuve avec le même nom que le meilleur grimpeur n'est trouvée.
    """

    mg_epreuve_name = str(row['nom']).replace(" meilleur grimpeur", '')
    for epreuve in epreuves_list:
        if epreuve.name == mg_epreuve_name:
            epreuve.meilleur_grimpeur = {'temps_ref': float(row['temps_ref']), 'points_gain_min': float(row['points_gain_min']), 'points_perte_min': float(row['points_perte_min'])}
            return
    
    raise MeilleurGrimpeurNotAffectableError(mg_epreuve_name)


class MeilleurGrimpeurNotAffectableError(Exception):
    """Si l'épreuve correspondant au meilleur grimpeur n'est pas trouvée."""
    def __init__(self, epreuve, *args, **kwargs):
        msg = f"Erreur sur l'affectation de la portion meilleur grimpeur à {epreuve} !\nVérifier que le nom de l'épreuve MG est bien de la forme '[nom_epreuve_classique] meilleur grimpeur' et que celle-ci est bien définie après '[nom_epreuve_classique]'. "
        super().__init__(msg, *args, **kwargs)