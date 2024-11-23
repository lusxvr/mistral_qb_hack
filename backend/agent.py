from dotenv import load_dotenv
load_dotenv()

from system_prompt import prompt 

from datetime import datetime

from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.agent_toolkits.amadeus.toolkit import AmadeusToolkit
from langchain_community.tools.openweathermap.tool import OpenWeatherMapQueryRun
from langchain_community.agent_toolkits.load_tools import load_tools

def agent():
    llm = ChatMistralAI(model="mistral-large-latest")
    config = {"configurable": {"thread_id": "thread-1"}}

    search_tool = TavilySearchResults(
        max_results=5,
        include_answer=True,
        include_raw_content=True,
        include_images=True,
        search_depth="advanced",
        # include_domains = []
        # exclude_domains = []
    )
    def datetime_tool():
        """Returns the current date and time"""
        return datetime.now().isoformat()
    #amadeus_tool = AmadeusToolkit()
    weather_tool = OpenWeatherMapQueryRun()

    tools = [datetime_tool, weather_tool, search_tool]#, amadeus_tool

    graph = create_react_agent(llm, tools, state_modifier=prompt, checkpointer=MemorySaver())

    while True:
        try:
            user_input = {"messages": [("user", input("User: "))]}
            print_stream(graph, user_input, config)
            #stream_graph_updates(user_input)
        except:
            # fallback if input() is not available
            print("\nSorry incorrect input")
            break

def print_stream(graph, inputs, config):
    for s in graph.stream(inputs, config, stream_mode="values"):
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

agent()