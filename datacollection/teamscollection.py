import pandas as pd

from models.team import Team


def collect_teams(teams_file_path: str) -> list[Team]:
    """
    Récupère les équipes à partir du fichier EXCEL spécifié.
    
    Retourne une liste d'objets `Team`.
    """

    teams_df = pd.read_excel(teams_file_path).dropna(how='all')

    team_size = 0
    for column_name in teams_df.columns:
        if column_name == f'conc_{team_size}_nom':
            team_size += 1

    teams_list: list[Team] = []

    for _, row in teams_df.iterrows():

        team_concs = [(str(row[f'conc_{i}_nom']), str(row[f'conc_{i}_prenom'])) for i in range(1, team_size+1)]

        teams_list.append(Team(
            int(row['puce']),
            int(row['dossard']),
            bool(row['ent']),
            str(row['mixite']),
            str(row['nom_equipe']),
            team_concs,
            str(row['contact'])
        ))
    
    return teams_list