import pandas as pd

from models.team import Team


def get_size_of_teams(teams_dataframe: pd.DataFrame) -> int:
    """Retourne la taille par défaut des équipes, selon le nombre de colonnes participants écrites dans le fichier équipes."""
    team_size = 0

    # Parcourt toutes les colonnes du DF
    for column_name in teams_dataframe.columns:
        if column_name == f'conc_{team_size+1}_nom':
            team_size += 1

    return team_size



def collect_teams(teams_file_path: str, num_journee: int) -> list[Team]:
    """
    Récupère les équipes à partir du fichier EXCEL spécifié.
    
    Retourne une liste d'objets `Team`.
    """

    teams_df: pd.DataFrame = pd.read_excel(teams_file_path).dropna(how='all')

    team_size: int = get_size_of_teams(teams_df)
    teams_list: list[Team] = []

    for _, row in teams_df.iterrows():

        team_concs = [(str(row[f'conc_{i}_nom']), str(row[f'conc_{i}_prenom'])) for i in range(1, team_size+1)]

        teams_list.append(Team(
            num_journee,
            int(row['puce']),
            int(row['dossard']),
            bool(row['ent']),
            str(row['mixite']),
            str(row['nom_equipe']),
            team_concs,
            str(row['contact'])
        ))
    
    return teams_list