from langgraph.graph import StateGraph,START,END
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


checkpointer = MemorySaver()

load_dotenv()
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


llm=ChatCerebras(model='qwen-3-32b')

def chat_node(state:ChatState):
    #Take user query from state
    messges=state['messages']
    
    #send to LLm
    response=llm.invoke(messges)
    
    #response store state
    return {'messages':[response]}

thread_id = "nitesh-chat"
graph=StateGraph(ChatState)

graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpointer)
config = {
    "configurable": {
        "thread_id": thread_id
    }
}

intial_state={
    'messages':[HumanMessage(content="what is the capital of india")]
}
result=chatbot.invoke(intial_state)

while True:
    user_message=input('Type Here: ')
    print(user_message)
    if user_message.strip().lower() in ['exit','quit','bye']:
        break
    response=chatbot.invoke({'messages':[HumanMessage(content=user_message)]})
    print('AI',response['messages'][-1].content)

response = chatbot.invoke(
    {
        "messages": [HumanMessage(content=user_message)]
    },
    config=config
)




