import logging

from controllers.onedaycontroller import OneDayController
from controllers.alldayscontroller import AllDaysController



def setup_logging():
    """Définition des paramètres de logging."""
    logging.basicConfig(
        level=logging.DEBUG,
        filename='logs.log',
        encoding='utf-8',
        filemode='w',
        format='[%(levelname)s]: %(message)s'
    )



def main():

    all_days_controller = AllDaysController('JOURNEES')
    




if __name__ == "__main__":
    setup_logging()
    main()