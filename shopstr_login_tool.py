import os
from crewai.tools.base_tool import BaseTool
from playwright.sync_api import sync_playwright

class ShopstrLoginTool(BaseTool):
    name: str = "ShopstrLoginTool"
    description: str = "Logs into Shopstr using nsec and passphrase if user is not already logged in."

    def _run(self, _: str = "") -> str:
        nsec = os.getenv("SHOPSTR_NSEC")
        password = os.getenv("SHOPSTR_PASSWORD", "shopstr")

        if not nsec:
            return "Missing SHOPSTR_NSEC environment variable."

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://shopstr.store")

            try:
                page.locator("text=Sign In").first.click()
                page.wait_for_selector("text=nsec Sign-in")
                page.click("text=nsec Sign-in")
                page.fill("input[placeholder*='Nostr private key']", nsec)
                page.fill("input[placeholder*='passphrase']", password)
                page.click("button:has-text('nsec Sign-in')")
                page.wait_for_timeout(3000)
            except Exception as e:
                return f"Login failed: {e}"
            finally:
                browser.close()

        return "Shopstr login succeeded."