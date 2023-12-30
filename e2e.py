from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# The URL of your application's homepage
HOMEPAGE_URL = 'http://localhost:5000'  # Replace with the correct URL

# XPaths to the game elements on the homepage
GAME_LINKS_XPATH = [
    '//a[@href="/memory-game"]',
    '//a[@href="/guess-game"]',
    '//a[@href="/currency-roulette-game"]'
]


def test_games_links(driver, game_links_xpath):
    success = True

    for game_xpath in game_links_xpath:
        try:
            game_link = driver.find_element(By.XPATH, game_xpath)
            game_link.click()
            driver.back()  # Go back to the homepage
        except NoSuchElementException:
            print(f"Game link with XPath '{game_xpath}' not found on the homepage.")
            success = False

    return success


if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    web_driver = webdriver.Chrome(options=chrome_options)
    try:
        web_driver.get(HOMEPAGE_URL)
        result = test_games_links(web_driver, GAME_LINKS_XPATH)
        if result:
            print("All game links were successfully reached from the homepage.")
        else:
            print("Some game links could not be reached from the homepage.")
    finally:
        web_driver.quit()  # Quit the driver
