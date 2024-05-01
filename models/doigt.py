class Doigt:
    """    Un doigt renferme toutes les données de la journée d'une équipe."""

    def __init__(self, journee: int, read_on: str, nb_of_records: int, siid: int, bip_badgeuses_list: list[int], bip_times_list: list[str]):

        self.journee = journee
        self.read_on = read_on
        self.nb_of_records = nb_of_records
        self.siid = siid
        self.bip_badgeuses_list = bip_badgeuses_list
        self.bip_times_list = bip_times_list

    def __repr__(self) -> str:
        return f"Doigt({self.siid})"