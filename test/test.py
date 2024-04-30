import unittest
import pandas as pd

from datacollection.teamscollection import get_size_of_teams


class TestTeamsCollection(unittest.TestCase):

    def setUp(self) -> None:
        self.teams_df: pd.DataFrame = pd.read_excel('JOURNEES/J1/teams.xlsx').dropna(how='all')


    def test_get_size_of_teams(self):
        self.assertEqual(get_size_of_teams(self.teams_df), 2)