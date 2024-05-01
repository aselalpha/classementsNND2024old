import pandas as pd

from models.doigt import Doigt


def clean_doigts_df(doigts_dataframe: pd.DataFrame):
    """
    Ne garde que les colonnes utiles du fichier csv converti en DataFrame contenant les données des doigts.

    Garde les colonnes Read on, SIID, No. of records, Record i CN, Record i time.
    """
    
    useful_columns = ['Read on', 'SIID', 'No. of records']

    i = 1
    while f'Record {i} CN' in doigts_dataframe.columns:
        useful_columns.append(f'Record {i} CN')
        useful_columns.append(f'Record {i} time')
        i += 1

    return doigts_dataframe[useful_columns]




def collect_doigts(doigts_csv_path: str, num_journee: int) -> list[Doigt]:
    """Retourne une liste d'objets Doigt."""
    
    # Retirer les colonnes inutiles du fichier csv
    doigts_df = pd.read_csv(doigts_csv_path, skipinitialspace=True, sep=None, engine='python')
    useful_columns_df = clean_doigts_df(doigts_df)

    # Liste des doigts sous forme pd.Series, en droppant les cellules vides de chaque doigt
    doigts_serie_list = [row.dropna() for _, row in useful_columns_df.iterrows()]

    # Liste des doigts sous forme d'objets
    # doigt.axes[0] est la liste des noms de colonne d'un pd.Series
    doigts_list = [Doigt(
        num_journee,
        str(doigt['Read on']),
        int(doigt['No. of records']),
        int(doigt['SIID']),
        [int(doigt[col]) for col in doigt.axes[0] if 'CN' in col],  # badgeuses bip
        [str(doigt[col]) for col in doigt.axes[0] if 'time' in col] # heures bip
    ) for doigt in doigts_serie_list]

    return doigts_list