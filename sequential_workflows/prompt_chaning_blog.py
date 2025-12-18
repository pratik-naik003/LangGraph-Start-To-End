from langgraph.graph import StateGraph,START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()


model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
#state definition
class BlogState(TypedDict):
    title:str
    outline:str
    content:str

#create outline function (node 1)
def create_outline(state:BlogState)->BlogState:
    title=state['title']
    prompt=f"generate a detailed outline for a blog on tthe topic{title}"
    response=model.invoke(prompt)
    
    state['outline']=response.content
    return state

#create blog function (node 2)
def create_blog(state:BlogState)->BlogState:
    title=state['title']
    outline=state['outline']
    
    prompt=f"""write a detailed blog ion the topic \" {title}\"usign the follwing outline: {outline}"""
    
    response=model.invoke(prompt)
    state['content']=response.content
    
    return state

#build prompt chaining graph
graph=StateGraph(BlogState)
graph.add_node('create_outline',create_outline)
graph.add_node('create_blog',create_blog)

#add edges
graph.add_edge(START,"create_outline")
graph.add_edge("create_outline","create_blog")
graph.add_edge("create_blog",END)

#graph compile 
workflow=graph.compile()
#execute prompt chaining

final_state=workflow.invoke({"title":"the rise of AI in india"})
print(final_state["outline"])
print(final_state["content"])
