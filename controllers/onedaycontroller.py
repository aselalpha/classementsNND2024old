import json
import logging

from models.team import Team
from models.doigt import Doigt
from models.epreuves import EpreuveCourse, EpreuveActi
from models.poincon import Poincon

from datacollection.teamscollection import collect_teams
from datacollection.doigtscollection import collect_doigts
from datacollection.epreuvescollection import collect_epreuves
from datacollection.badgeusescollection import collect_badgeuses


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
        self.epreuves_list: list[EpreuveActi|EpreuveCourse] = collect_epreuves(data['epreuves_excel'], self.numero_journee)
        self.badgeuses_list: list[Poincon] = collect_badgeuses(data['badgeuses_excel'], self.numero_journee)
    

    def associate_data(self):
        """Combine les données entre elles."""

        self
    

    def _add_badgeuses_to_epreuves(self):
        """Ajoute les badgeuses lues dans badgeuses à l'épreuve correspondante de epreuves_list."""
        if show_log: print("Ajout des poinçons aux épreuves...")

        for _, row in self.polis_badgeuses.df.iterrows():
            epreuve: EpreuveCourse = self.get_epreuve(row['epreuve'])

            poincon_to_add = Poincon(epreuve, str(row['signaleur']), int(row['numero']), str(row['fonction']), float(row['points']))
            epreuve.badgeuses_list.append(poincon_to_add)
            
            if show_log: print(f"Ajout de la badgeuse {row['numero']} à l'épreuve {epreuve.name}")
            
            # Si présence d'un meilleur grimpeur dans l'épreuve, on arrange les poinçons pour qu'il n'y ait pas de doublon
            if epreuve.meilleur_grimpeur and poincon_to_add.role == 'fin':
                epreuve.clean_meilleur_grimpeur()
        
        if show_log: print("Toutes les badgeuses ont été ajoutées aux épreuves correspondantes.\n")