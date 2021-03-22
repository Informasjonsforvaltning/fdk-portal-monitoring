import logging
import os
from time import sleep

from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
)

from src.driver import create_driver

FDK_PORTAL_HOST = os.getenv("FDK_PORTAL_HOST", "http://fdk-portal:8080")
CHROME_PATH = os.getenv("CHROME_PATH", "chromedriver")


def navigate_through_all_search_results_and_details_pages():
    try:
        chrome_driver = create_driver()
        more_pages = True
        search_page = 0
        chrome_driver.implicitly_wait(5)
        chrome_driver.get(f"{FDK_PORTAL_HOST}/search-all?page={search_page}")

        def visit_search_hits():
            search_hit_elements = chrome_driver.find_elements_by_xpath(
                "//*/article/div[1]/div[2]/div[1]/h2/a[@href]"
            )
            search_hit_elements_refs = []

            for search_hit in search_hit_elements:
                search_hit_elements_refs.append(search_hit.get_attribute("href"))

            for ref in search_hit_elements_refs:
                chrome_driver.get(ref)
                sleep(2)

        def click_next_page():
            nonlocal search_page
            nonlocal more_pages
            chrome_driver.get(f"{FDK_PORTAL_HOST}/search-all?page={search_page}")
            sleep(2)
            search_page = search_page + 1
            next_button = chrome_driver.find_element_by_class_name(
                "next"
            ).find_element_by_tag_name("a")
            if next_button is None:
                more_pages = False
            else:
                next_button.click()
                sleep(2)

        while more_pages:
            visit_search_hits()
            click_next_page()

    except (NoSuchElementException, ElementNotInteractableException):
        logging.error("Avslutter chrome_driver")
        chrome_driver.quit()
