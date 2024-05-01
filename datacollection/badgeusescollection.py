import pandas as pd

from models.poincon import Poincon


def collect_badgeuses(badgeuses_excel_path: str, num_journee: int) -> list[Poincon]:

    badgeuses_df = pd.read_excel(badgeuses_excel_path)
    poincons_list: list[Poincon] = []

    for _, row in badgeuses_df.iterrows():
        
        poincons_list.append(Poincon(
            num_journee,
            str(row['epreuve']),
            str(row['signaleur']),
            int(row['badgeuse']),
            str(row['fonction']),
            float(row['points'])
        ))
    
    return poincons_list