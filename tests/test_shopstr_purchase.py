import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shopstr_purchase_tool import ShopstrPurchaseTool

tool = ShopstrPurchaseTool()

product_url = "https://shopstr.store/listing/naddr1..."  # Replace with a real Shopstr product URL
result = tool._run(product_url)

print("🧪 Result:")
print(result)