import datetime
import logging
from pathlib import Path

from apscheduler.schedulers.background import BlockingScheduler

from src.monitoring.search import navigate_through_all_search_results_and_details_pages


def start_selenium_tests():
    try:
        logging.error("Starting selenium tests")
        navigate_through_all_search_results_and_details_pages()
        logging.error("Finished selenium tests")
        next_run = datetime.datetime.now() + datetime.timedelta(minutes=1)
        scheduler = BlockingScheduler()
        scheduler.add_job(
            start_selenium_tests,
            next_run_time=next_run,
        )
        logging.error("Next run will start: ", next_run)
        scheduler.start()
    except RuntimeError:
        logging.error("Scheduler failed")
        scheduler.shutdown()


if __name__ == "__main__":
    ROOT_DIR = Path(__file__).parent.parent

    logging.error("Starting fdk-portal-monitoring")
    start_selenium_tests()

    logging.error("Shutdown fdk-portal-monitoring")
