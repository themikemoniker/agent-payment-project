import os
from crewai.tools.base_tool import BaseTool
from playwright.sync_api import sync_playwright

class ShopstrPurchaseTool(BaseTool):
    name: str = "ShopstrPurchaseTool"
    description: str = "Visits a Shopstr product page, fills in contact info, and retrieves the Lightning invoice."

    def _run(self, product_url: str) -> str:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(product_url)

            try:
                page.wait_for_selector("text=Enter Contact Info", timeout=5000)
                page.fill("input[placeholder='@username or contact']", "@themikemoniker")
                page.fill("input[placeholder='contact type']", "nostr")
                page.fill("textarea[placeholder='delivery instructions']", "message me")
                page.click("text=Submit")

                page.wait_for_selector("text=Lightning Invoice", timeout=5000)
                invoice = page.locator("text=lnbc").first.text_content()
            except Exception as e:
                return f"Shopstr purchase failed: {e}"
            finally:
                browser.close()

        return invoice.strip() if invoice else "Invoice not found."