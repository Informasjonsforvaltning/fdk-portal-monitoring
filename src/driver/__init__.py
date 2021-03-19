import logging
import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

FDK_PORTAL_HOST = os.getenv("FDK_PORTAL_HOST", "http://fdk-portal:8080")
CHROME_PATH = os.getenv("CHROME_PATH", "chromedriver")


def create_driver():
    logging.info("Creating driver")
    try:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if "SKIP_HEADLESS_MODE" not in os.environ:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        return webdriver.Chrome(options=options, executable_path=CHROME_PATH)
    except WebDriverException:
        logging.info("Creating webdriver failed")
        return None
