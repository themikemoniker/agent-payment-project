import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shopstr_search_tool import ShopstrSearchTool

tool = ShopstrSearchTool()

search_query = "test hackathon item"  # Use a real product keyword
result = tool._run(search_query)

print("🧪 Result:")
print(result)