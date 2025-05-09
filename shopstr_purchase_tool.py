# shopstr_purchase_tool.py

from crewai.tools.base_tool import BaseTool
from playwright.sync_api import sync_playwright
import time

class ShopstrPurchaseTool(BaseTool):
    name: str = "ShopstrPurchaseTool"
    description: str = (
        "Visits a Shopstr product page, submits contact info, and retrieves the Lightning invoice (BOLT11)."
    )

    def _run(self, product_url: str) -> str:
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(product_url, timeout=60000)

                page.click("text=Buy Now", timeout=5000)
                page.wait_for_selector("text=Enter Contact Info", timeout=5000)

                page.fill('input[placeholder="Contact"]', "@themikemoniker")
                page.fill('input[placeholder="Contact type"]', "nostr")
                page.fill('textarea[placeholder="Delivery instructions"]', "message me")

                page.click("text=Submit", timeout=5000)
                page.wait_for_selector("text=Lightning Invoice", timeout=10000)
                time.sleep(2)

                content = page.content()
                invoice_start = content.find("lnbc")
                invoice = content[invoice_start:].split('"')[0] if invoice_start != -1 else "Invoice not found"

                browser.close()
                return invoice

        except Exception as e:
            return f"Shopstr purchase failed: {str(e)}"