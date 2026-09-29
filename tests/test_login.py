import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            headless=False
        )

        page = browser.new_page()

        # 1. Launch Automation Exercise
        page.goto("https://www.automationexercise.com/")

        # 2. Navigate to Login
        page.get_by_text("Signup / Login").click()

        # 3. Enter registered email
        page.locator('[data-qa="login-email"]').fill(EMAIL)

        # 4. Enter registered password
        page.locator('[data-qa="login-password"]').fill(PASSWORD)

        # 5. Submit login
        page.locator('[data-qa="login-button"]').click()

        # 6. Verify successful login
        logged_in_text = page.get_by_text("Logged in as").first
        logged_in_text.wait_for()

        assert logged_in_text.is_visible()

        browser.close()