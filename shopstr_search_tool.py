import os
from crewai.tools.base_tool import BaseTool
from playwright.sync_api import sync_playwright

class ShopstrSearchTool(BaseTool):
    name: str = "ShopstrSearchTool"
    description: str = "Searches Shopstr for a product by name and returns the first result's URL."

    def _run(self, search_query: str) -> str:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            try:
                page.goto("https://shopstr.store", timeout=20000)

                # Click "Start Shopping" if needed
                if page.locator("text=Start Shopping").is_visible():
                    page.click("text=Start Shopping")
                    page.wait_for_selector("input[placeholder*='Listing title']", timeout=10000)

                # Fill search bar
                page.fill("input[placeholder*='Listing title']", search_query)
                page.keyboard.press("Enter")

                # Wait for the title to appear
                title_selector = f"h2:has-text('{search_query}')"
                page.wait_for_selector(title_selector, timeout=10000)
                title_el = page.locator(title_selector).first

                # Walk up to card and find the first anchor tag
                card = title_el.locator("xpath=ancestor::div[contains(@class, 'card')]")
                link = card.locator("a[href*='/listing/naddr1']").first
                href = link.get_attribute("href")

                browser.close()
                return f"https://shopstr.store{href}" if href else "Listing found, but no URL."
            except Exception as e:
                browser.close()
                return f"No listings found or error: {str(e)}"
                context = browser.new_context()
                page = context.new_page()

                try:
                    page.goto("https://shopstr.store", timeout=20000)
                    
                    if not page.locator("input[placeholder*='Listing title']").is_visible():
                        page.click("text=Start Shopping", timeout=10000)
                        page.wait_for_selector("input[placeholder*='Listing title']", timeout=10000)

                    page.fill("input[placeholder*='Listing title']", search_query)
                    page.keyboard.press("Enter")

                    # Wait for product card with title matching the query
                    result_locator = page.locator(f"text={search_query}")
                    result_locator.wait_for(timeout=10000)

                    # Get the closest product card and extract its URL
                    card = result_locator.first.locator("xpath=ancestor::div[contains(@class, 'card')]")
                    link = card.locator("a[href*='/listing/naddr1']").first
                    href = link.get_attribute("href")

                    browser.close()
                    return f"https://shopstr.store{href}" if href else "Listing found but no URL."
                except Exception as e:
                    browser.close()
                    return f"No listings found or error: {str(e)}"