from dotenv import load_dotenv
load_dotenv()

# from .system_prompt import prompt 
# from .json_schema import TravelResponse

# from datetime import datetime

# from langchain_mistralai import ChatMistralAI
# from langgraph.prebuilt import create_react_agent
# from langgraph.checkpoint.memory import MemorySaver

# from langchain_community.tools.tavily_search import TavilySearchResults
# from langchain_community.agent_toolkits.amadeus.toolkit import AmadeusToolkit
# from langchain_community.tools.openweathermap.tool import OpenWeatherMapQueryRun

# llm = ChatMistralAI(model="mistral-large-latest")

# search_tool = TavilySearchResults(
#     max_results=5,
#     include_answer=True,
#     include_raw_content=True,
#     include_images=True,
#     search_depth="advanced",
#     # include_domains = []
#     # exclude_domains = []
# )
# def datetime_tool():
#     """Returns the current date and time"""
#     return datetime.now().isoformat()
# #amadeus_tool = AmadeusToolkit()
# weather_tool = OpenWeatherMapQueryRun()

# tools = [datetime_tool, weather_tool, search_tool]#, amadeus_tool

# llm = llm.bind_tools(tools)
# llm = llm.with_structured_output(TravelResponse)


# graph = create_react_agent(llm, tools, state_modifier=prompt, checkpointer=MemorySaver())


# def get_response(inputs, config):
#     messanges = []
#     for s in graph.stream(inputs, config, stream_mode="values"):
#         messanges.append(s["messages"][-1])
#     #print(messanges[-1].content)
#     return messanges[-1].content

from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.tools import tool
from langgraph.graph import MessagesState
from langchain_mistralai import ChatMistralAI

from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.agent_toolkits.amadeus.toolkit import AmadeusToolkit
from langchain_community.tools.openweathermap.tool import OpenWeatherMapQueryRun
from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver

from .unsplash_api import get_unsplash_image_url


#from system_prompt import prompt

class TravelRecResponse(BaseModel):
    """Respond to the user with this"""
    answer: str = Field(description="For the chat with the user: The ful answer for the user for the chat, very likely over multiple lines")
    city: str = Field(description="For the results carusel: The identified city of the trip")
    country: str = Field(description="For the results carusel: The identified country of the trip")
    title: str = Field(description="For the results carusel: The identified country of the trip")
    price: str = Field(description="For the results carusel: The price of the trip per person")
    travelMedium: str = Field(description="For the results carusel: The travel medium of the trip (e.g. Train, Bus, Car, Plane)")
    amountPeople: str = Field(description="For the results carusel: The amount of people on the trip")
    amountNights: str = Field(description="For the results carusel: The amount of night of the trip")
    travelTime: str = Field(description="For the results carusel: Total travel time one way to get to the destination")
    imgAddress: str = Field(description="For the results carusel: Single link to individual picture representative of the city")
    description: str = Field(description="For the results carusel: Short one-sentence description of the whole recommendation that gets placed in the results carusel")




# Inherit 'messages' key from MessagesState, which is a list of chat messages
class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: TravelRecResponse

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

# def image_tool(query: str) -> str:
#     """Returns a image url for the given query
#     Use this to generate an image representative of the trip and just copy the FULL result to the final answer"""
#     return get_unsplash_image_url(query)
#amadeus_tool = AmadeusToolkit()
weather_tool = OpenWeatherMapQueryRun()

memory = MemorySaver()

model = ChatMistralAI(model="mistral-large-latest")

tools = [datetime_tool, weather_tool, search_tool]#image_tool,


model_with_tools = model.bind_tools(tools)
model_with_structured_output = model.with_structured_output(TravelRecResponse)

# tools = [datetime_tool, weather_tool, search_tool, TravelRecResponse]

# # Force the model to use tools by passing tool_choice="any"
# model_with_response_tool = model.bind_tools(tools, tool_choice="any")


# Define the function that calls the model
def call_model(state: AgentState):
    response = model_with_tools.invoke(state["messages"])
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}


# Define the function that responds to the user
def respond(state: AgentState):
    # We call the model with structured output in order to return the same format to the user every time
    # state['messages'][-1] is the last Message in the convo, which we convert to a HumanMessage for the model to use
    # We could also pass the entire chat history, but this saves tokens since all we care to structure is the output of the tool
    response = model_with_structured_output.invoke([HumanMessage(content=state["messages"][-1].content)])
    # We return the final answer
    return {"final_response": response}



# Define the function that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    # If there is no function call, then we respond to the user
    if not last_message.tool_calls:
        return "respond"
    # Otherwise if there is, we continue
    else:
        return "continue"


# Define a new graph
workflow = StateGraph(AgentState)

# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("respond", respond)
workflow.add_node("tools", ToolNode(tools))

# Set the entrypoint as `agent`
# This means that this node is the first one called
workflow.set_entry_point("agent")

# We now add a conditional edge
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "respond": "respond",
    },
)

workflow.add_edge("tools", "agent")
workflow.add_edge("respond", END)
graph = workflow.compile(checkpointer=memory)

# print(user_input)
# answer = graph.invoke(input={"messages": [("human", user_input)]})["final_response"]

# print(answer)

def get_response(inputs, config):
    messages = []
    for s in graph.stream(inputs, config, stream_mode="values"):
        #print(s)
        messages.append(s["messages"][-1])
        if "final_response" in s.keys():
            messages.append(s["final_response"])
    print(messages[-1])
    return messages[-1]#.content

# from system_prompt import prompt
# user_input = prompt+input("User: I want to go surfing in biarritz")
# inputs = {"messages": [("user", user_input)]}
# config = {"configurable": {"thread_id": "thread-1"}}
# response = get_response(inputs, config)
# print(response)

# def print_stream(graph, inputs, config):
#     for s in graph.stream(inputs, config, stream_mode="values"):
#         message = s["messages"][-1]
#         if isinstance(message, tuple):
#             print(message)
#         else:
#             message.pretty_print()

# graph = get_agent()
# while True:
#     try:
#         user_input = {"messages": [("user", input("User: "))]}
#         print_stream(graph, user_input, config)
#     except:
#         print("\nI'm sorry the input was incorrect")
#         break

# graph = get_agent()
# inputs = {"messages": [("user", input("User: "))]}
# config = {"configurable": {"thread_id": "thread-1"}}
# response = get_response(graph, inputs, config)
# print(response)
