import time
from selenium.webdriver.common.by import By


def apply_filter(browser, select_element, label_text):
    """
    React-safe dropdown selection
    """

    browser.execute_script(
        """
        const select = arguments[0];
        const label = arguments[1];

        for (let option of select.options) {
            if (option.text.includes(label)) {
                select.value = option.value;
                select.dispatchEvent(new Event('change', { bubbles: true }));
                return true;
            }
        }
        return false;
        """,
        select_element,
        label_text
    )


def safe_clear_filter(browser):
    """
    Click clear filter only if present
    """

    try:
        clear_btn = browser.find_element(
            By.XPATH,
            "//button[@title='Clear filter']"
        )

        browser.execute_script(
            "arguments[0].click();",
            clear_btn
        )

        time.sleep(3)

    except:
        pass