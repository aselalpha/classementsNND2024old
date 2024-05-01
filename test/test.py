import unittest
import pandas as pd

from datacollection.teamscollection import get_size_of_teams, collect_teams
from datacollection.doigtscollection import clean_doigts_df, collect_doigts

from models.team import Team
from models.doigt import Doigt


class TestTeamsCollection(unittest.TestCase):

    def test_get_size_of_teams(self):
        teams_df: pd.DataFrame = pd.read_excel('JOURNEES/J1/teams.xlsx').dropna(how='all')
        self.assertEqual(get_size_of_teams(teams_df), 2)

    
    def test_collect_teams(self):
        teams_list: list[Team] = collect_teams('JOURNEES/J1/teams.xlsx', 1)

        self.assertEqual(len(teams_list), 142)
        self.assertEqual(teams_list[2], Team(1, 1915532, 3, False, 'mixte', 'Les pâ€™tits dangereux', [('Han', 'Vanessa'), ('Fagard', 'LÃ©o')], 'vanessa.han@student-cs.fr'))


class TestDoigtsCollection(unittest.TestCase):

    def test_clean_doigts_df(self):
        doigts_df: pd.DataFrame = pd.read_csv("JOURNEES/J1/TDJ2024_datas_graid.csv", skipinitialspace=True, sep=None, engine='python')
        cleaned_doigts_df: pd.DataFrame = clean_doigts_df(doigts_df)
        self.assertEqual(cleaned_doigts_df.shape, (128, 387))
    
    def test_collect_doigts(self):
        doigts_list = collect_doigts("JOURNEES/J1/TDJ2024_datas_graid.csv", 1)
        self.assertEqual(len(doigts_list), 128)

        doigt_5: Doigt = doigts_list[5]
        self.assertEqual(doigt_5.journee, 1)
        self.assertEqual(doigt_5.siid, 1097543)
        self.assertEqual(doigt_5.read_on, '2024-02-10 14:33:10')
        self.assertEqual(doigt_5.nb_of_records, 26)
        self.assertEqual(doigt_5.bip_badgeuses_list, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,30,21,22,23,24])
        self.assertEqual(doigt_5.bip_times_list[8], '10:09:37')
