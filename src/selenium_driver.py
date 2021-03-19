import datetime
import logging
from pathlib import Path

from apscheduler.schedulers.background import BlockingScheduler

from src.monitoring.search import navigate_through_all_search_results_and_details_pages


def start_selenium_tests():
    logging.info("Starting selenium tests")
    navigate_through_all_search_results_and_details_pages()
    logging.info("Finished selenium tests")
    try:
        scheduler = BlockingScheduler()
        scheduler.add_job(
            start_selenium_tests,
            next_run_time=datetime.datetime.now() + datetime.timedelta(hours=23),
        )
        scheduler.start()
    except RuntimeError:
        logging.info("Scheduler failed")
        scheduler.shutdown()


if __name__ == "__main__":
    ROOT_DIR = Path(__file__).parent.parent
    logfile = Path.joinpath(ROOT_DIR, "src", "app.log")

    logging.basicConfig(
        filename=logfile,
        format="%(asctime)s %(levelname)s: %(message)s",
        level=logging.INFO,
    )

    logging.info("Starting main")
    start_selenium_tests()

    logging.info("Ending main")
