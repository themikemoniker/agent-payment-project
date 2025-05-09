from crewai.tools.base_tool import BaseTool
from nwc_client import NWCClient

class PayInvoiceTool(BaseTool):
    name: str = "PayLightningInvoice"
    description: str = "Pays a Lightning invoice using a provided NWC string."

    def _run(self, invoice: str, nwc_uri: str) -> str:
        try:
            nwc = NWCClient(nwc_uri)
            result = nwc.pay(invoice)  # runs the coroutine safely
            return result
        except Exception as e:
            return f"Failed to pay invoice: {e}"