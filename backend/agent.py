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

def agent():
    search_tool = TavilySearchResults(max_results=2)
    def datetime_tool():
        """Returns the current date and time"""
        return datetime.now().isoformat()

    tools = [search_tool, datetime_tool]

    llm = ChatMistralAI(model="mistral-small-latest")
    config = {"configurable": {"thread_id": "thread-1"}}
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

