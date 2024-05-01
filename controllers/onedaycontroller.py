import json

from models.team import Team
from models.doigt import Doigt
from models.epreuves import EpreuveCourse, EpreuveActi
from models.badgeuse import Badgeuse

from datacollection.teamscollection import collect_teams
from datacollection.doigtscollection import collect_doigts


class OneDayController:
    
    def __init__(self, journee_folder_path: str, numero_journee: int) -> None:
        self.journee_folder_path = journee_folder_path
        self.numero_journee = numero_journee


    def collect_data(self):
        """
        Récupère les données contenues dans `initialisation.json` telles que l'heure de
        mass_start et les path vers les 5 fichiers de données.
        """

        with open(self.journee_folder_path+'initialisation.json') as json_file:
            data = json.load(json_file)
        
        self.mass_start: str|None = data['mass_start']

        self.teams_list: list[Team] = collect_teams(data['teams_excel'], self.numero_journee)
        self.doigts_list: list[Doigt] = collect_doigts(data['doigts_csv'], self.numero_journee)
        self.epreuves_list: list[EpreuveActi|EpreuveCourse] = collect_epreuves(data['epreuves_excel'])
        self.badgeuses_list: list[Badgeuse] = collect_badgeuses(data['badgeuses_excel'])