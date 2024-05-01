import pandas as pd


class Team:

    def __init__(self, journee: int, puce: int, dossard: int, ent: bool, mixite: str, team_name: str, concs_list: list[tuple[str,str]], contact: str):
        self.puce = puce
        self.dossard = dossard
        self.team_name = team_name
        self.ent = ent
        self.mixite = mixite
        self.concs_list = concs_list
        self.contact = contact
        self.journee = journee

    def __repr__(self):
        return f'Team({self.puce}, n°{self.dossard}, {self.team_name})'
    
    def __eq__(self, other):
        """Compare deux objets Team, qui sont considérées comme identiques si elles ont même nom, même numéro de puce, même numéro de dossard."""
        if isinstance(self, other.__class__):
            return self.journee == other.journee and self.puce == other.puce and self.dossard == other.dossard and self.team_name == other.team_name
        return False