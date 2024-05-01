import unittest
import pandas as pd

from datacollection.teamscollection import get_size_of_teams, collect_teams

from models.team import Team


class TestTeamsCollection(unittest.TestCase):

    def test_get_size_of_teams(self):
        teams_df: pd.DataFrame = pd.read_excel('JOURNEES/J1/teams.xlsx').dropna(how='all')
        self.assertEqual(get_size_of_teams(teams_df), 2)

    
    def test_collect_teams(self):
        teams_excel_path: str = 'JOURNEES/J1/teams.xlsx'
        teams_list: list[Team] = collect_teams(teams_excel_path, 1)

        self.assertEqual(len(teams_list), 142)
        self.assertEqual(teams_list[2], Team(1, 1915532, 3, False, 'mixte', 'Les pâ€™tits dangereux', [('Han', 'Vanessa'), ('Fagard', 'LÃ©o')], 'vanessa.han@student-cs.fr'))