from langgraph.graph import StateGraph,START,END
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
llm=ChatCerebras(model='qwen-3-32b')
class JokeState(TypedDict):
    topic:str
    joke:str
    explanation:str

def generate_joke(state:JokeState):
    prompt=f'generate a joke on the topic {state['topic']}'
    response=llm.invoke(prompt).content
    return {'joke':response}

def generate_explanation(state:JokeState):
    prompt=f'write an explanation for the joke {state['joke']}'
    response=llm.invoke(prompt).content
    return {'explanation':response}

graph=StateGraph(JokeState)

graph.add_node('generate_joke',generate_joke)
graph.add_node('generate_explanation',generate_explanation)
graph.add_edge(START,'generate_joke')
graph.add_edge('generate_explanation',END)

checkpointer=InMemorySaver()

workflow=graph.compile(checkpointer=checkpointer)

config1={"configurable":{"thread_id":"1"}}
result=workflow.invoke({'topic':'pizza'},config=config1)

#get the last state value
print(workflow.get_state(config1))

#getting all the state values 
print(list(workflow.get_state_history(config1)))
