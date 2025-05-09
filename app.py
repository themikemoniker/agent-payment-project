from flask import Flask, render_template, request, Response, stream_with_context
from flask_cors import CORS
from crewai import Crew, Agent, Task
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)
CORS(app)

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.5,
    streaming=True,
)

agent = Agent(
    role="Helpful Assistant",
    goal="Answer user questions clearly and concisely",
    backstory="An intelligent AI assistant that explains things simply.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["GET"])
def ask():
    user_input = request.args.get("user_input")

    task = Task(
        description=f"Respond to this user input: {user_input}",
        expected_output="A helpful and complete answer to the user's question.",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()

    def generate():
        yield f"data: {result}\n\n"
        yield "event: done\ndata: END\n\n"

    return Response(stream_with_context(generate()), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)
