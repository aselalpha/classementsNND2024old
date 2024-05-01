import unittest
import pandas as pd

from datacollection.teamscollection import get_size_of_teams, collect_teams
from datacollection.doigtscollection import clean_doigts_df, collect_doigts
from datacollection.epreuvescollection import collect_epreuves, append_mg_to_epreuve_course, create_epreuve_object, MeilleurGrimpeurNotAffectableError

from models.team import Team
from models.doigt import Doigt
from models.epreuves import EpreuveActi, EpreuveCourse


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


class TestEpreuvesCollection(unittest.TestCase):

    def test_collect_epreuves(self):
        epreuves_list: list[EpreuveCourse|EpreuveActi] = collect_epreuves("JOURNEES/J1/epreuves.xlsx", 1)
        self.assertEqual(len(epreuves_list), 19)

        epreuves_course_list: list[EpreuveCourse] = [epreuve for epreuve in epreuves_list if isinstance(epreuve, EpreuveCourse)]
        self.assertEqual(len(epreuves_course_list), 9)

        epreuve_course_1: EpreuveCourse = epreuves_course_list[1]
        self.assertEqual(epreuve_course_1.journee, 1)
        self.assertEqual(epreuve_course_1.name, "Obli 2 VTT")
        self.assertEqual(epreuve_course_1.points_participation, 0)
        self.assertEqual(epreuve_course_1.temps_ref, 99)
        self.assertEqual(epreuve_course_1.points_gain_min, 1.57)
        self.assertEqual(epreuve_course_1.points_perte_min, 0)
        self.assertEqual(epreuve_course_1.epreuve_type, "vtt")
        self.assertEqual(epreuve_course_1.meilleur_grimpeur, {'temps_ref': 8, 'points_gain_min': 6.91, 'points_perte_min': 0})
    

    def test_create_epreuve_object(self):
        row_10: pd.Series = pd.read_excel("JOURNEES/J1/epreuves.xlsx").dropna(how='all').iloc[10]
        self.assertIsInstance(create_epreuve_object(row_10, 1), EpreuveActi)

    def test_MeilleurGrimpeurNotAffectableError(self):
        with self.assertRaises(MeilleurGrimpeurNotAffectableError):
            collect_epreuves('test/test_files/epreuves_mg_fail.xlsx', 1)