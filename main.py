import logging

from controllers.onedaycontroller import OneDayController
from controllers.alldayscontroller import AllDaysController

# Selon si le classement se fait par points ou par temps
CLASSEMENT_PAR_POINTS = False


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

    all_days_controller = AllDaysController('JOURNEES/')

    for one_day_controller in all_days_controller.onedaycontrollers_list:

        one_day_controller.collect_data()
        one_day_controller.associate_data()
        one_day_controller.compute_running_times()
        one_day_controller.rank(convert_time_to_points=CLASSEMENT_PAR_POINTS)
    
    all_days_controller.rank()    




if __name__ == "__main__":
    setup_logging()
    main()