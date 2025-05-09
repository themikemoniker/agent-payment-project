from flask import Flask, render_template, request
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from shopstr_purchase_tool import ShopstrPurchaseTool
from pay_invoice_tool import PayInvoiceTool
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# LLM setup
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

# Tools
shopstr_tool = ShopstrPurchaseTool()
nwc_tool = PayInvoiceTool()

# Agent definition
agent = Agent(
    role="Lightning Shopper",
    goal="Buy things from Shopstr using Bitcoin",
    backstory="You assist users by retrieving invoices from Shopstr listings and paying them with NWC.",
    tools=[shopstr_tool, nwc_tool],
    allow_delegation=True,
    verbose=True,
    llm=llm
)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        product_url = request.form.get("product_url")
        nwc_uri = request.form.get("nwc")

        task = Task(
            description=(
                f"Visit this Shopstr product: {product_url}, submit the contact info, retrieve the Lightning "
                f"invoice, and pay it using this NWC string: {nwc_uri}."
            ),
            expected_output="A confirmation that the invoice was paid.",
            agent=agent
        )

        crew = Crew(agents=[agent], tasks=[task])
        response = crew.kickoff()

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)