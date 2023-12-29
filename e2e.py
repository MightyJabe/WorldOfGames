from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_scores_service():
    # get the URL from the user
    url = input("Please enter your URL: ")

    # open the URL in a web browser using Selenium WebDriver
    driver = webdriver.Chrome()  # You may need to download the appropriate webdriver for your browser
    print(f"Opening URL: {url}")
    driver.get(url)

    try:
        # Wait up to 10 seconds for the element to be present
        print("Waiting for the 'score' element to be present...")
        score = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, "score"))
        )

        score_value = int(score.text)
        print(f"Score value found: {score_value}")

        # check that it is a number between 1 and 1000
        if 1 <= score_value <= 1000:
            print("Test passed! Score is within the expected range.")
            return True
        else:
            print("Test failed! Score is outside the expected range.")
            return False

    except NoSuchElementException:
        print("Element with id 'score' not found.")
        return False
    finally:
        # Close the browser after the test
        print("Closing the browser.")
        driver.quit()


def main_function():
    # this function will call the test_scores_service() function, and return -1
    # as an os exit code if the tests failed, or 0 if the tests passed.
    if test_scores_service():
        return 0
    else:
        return -1


# Call the main function
if __name__ == "__main__":
    exit_code = main_function()
    print(f"Exit code: {exit_code}")
    exit(exit_code)
