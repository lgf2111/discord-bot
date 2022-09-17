from automation import driver, By, WebDriverWait, EC, TimeoutException
import logging


def verify(email, password):
    try:
        driver.get("https://nypeservices.nyp.edu.sg/ifrs/bookfacility")
        email_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=email]"))
        )
        email_input.send_keys(email)
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[type=submit][value=Next]")
            )
        )
        next_button.click()

        password_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type=password]"))
        )
        password_input.send_keys(password)

        signin_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[type=submit][value='Sign in']")
            )
        )
        signin_button.click()
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-facility"))
            )
            return True

        except TimeoutException:
            return False

    except Exception as e:
        logging.info(f"Error: {e}")
        return None
