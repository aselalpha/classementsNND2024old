import os
import logging

from .onedaycontroller import OneDayController


class AllDaysController:
    """
    Crée les objets OneDayController correspondant à chaque journée.

    Args:
    - `journees_folder`: chemin vers les dossiers de chaque journée.
    """

    def __init__(self, journees_folder_path: str) -> None:
        self.onedaycontrollers_list = self._create_onedaycontrollers(journees_folder_path)


    def _create_onedaycontrollers(self, journees_folder_path: str) -> list[OneDayController]:
        """Crée la liste des OneDayController permettant de gérer chaque journée."""

        odc_list: list[OneDayController] = []

        for folder in os.listdir(journees_folder_path):            
            odc_list.append(OneDayController(journees_folder_path+folder+'/'))
        
        return odc_list