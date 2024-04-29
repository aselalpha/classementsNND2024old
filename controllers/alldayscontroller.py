import os

from .onedaycontroller import OneDayController


class AllDaysController:
    """
    Crée les objets OneDayController correspondant à chaque journée.

    Args:
    - `journees_folder`: chemin vers les dossiers de chaque journée.
    """
    
    def __init__(self, journees_folder: str) -> None:
        
        # Itérer sur chaque dossier journée du dossier de toutes les journées
        for folder in os.listdir(journees_folder):

            