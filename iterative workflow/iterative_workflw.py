from langgraph.graph import StateGraph,START,END
from typing import TypedDict ,Literal,Annotated
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
import operator
from pydantic import BaseModel
load_dotenv()
genertor_llm = ChatCerebras(
    model="qwen-3-32b",
    temperature=0.2
)

evaluator_llm=ChatCerebras(
    model="qwen-3-32b",
     temperature=0.2
)

optimizer_llm=ChatCerebras(
    model="qwen-3-32b"
)

class TweetState(TypedDict):
    topic:str
    tweet:str
    evalution:Literal["approved","needs_imporovement"]
    feed_back:str
    iteration:int
    max_intration:int
    
    tweet_history:Annotated[list[str],operator.add]
    feed_back_history:Annotated[list[str],operator.add]



def generate_tweet(state:TweetState):
    messages=[
    SystemMessage(content="You are a funny and clever Twitter influencer."),
    HumanMessage(content=f"""
Write a short, original, hilarious tweet on the topic: {state['topic']}

Rules:
- No Q&A format
- Max 280 characters
- Use humor, sarcasm, irony
- Simple English
""")]
    
    response=genertor_llm.invoke(messages)
    return{
        "tweet":response,
        "tweet_history":[response]
    }


class tweet_evalution(BaseModel):
    evalution:Literal["approved","needs_improvement"]
    feed_back:str


structured_evalutor=evaluator_llm.with_structured_output(tweet_evalution)

def evaluate_tweet(state:TweetState):
    messages=[
        SystemMessage(content="You are a ruthless Twitter critic."),
        HumanMessage(content=f"""
Evaluate the tweet below:

Tweet:
{state['tweet']}

Return:
- evaluation (approved / needs_improvement)
- feedback
""")]
    result=structured_evalutor.invoke(messages)
    
    return {
        "evalution":result.evalution,
        "feed_back":result.feed_back,
        "feedback_history":[result.feed_back]
    }
    
    

def optimize_tweet(state:TweetState):
    messages=[
        SystemMessage(content="You improve tweets using feedback."),
        HumanMessage(content=f"""
Improve this tweet based on feedback:

Tweet: {state['tweet']}
Feedback: {state['feed_back']}

Rules:
- Under 280 characters
- No Q&A
""")
    ]
    response=optimizer_llm.invoke(messages)
    
    return {
        "tweet":response.content,
        "iteration":state["iteration"]+1,
        "tweet_history":[response.content]
    }
    

def route_evalution(state:TweetState):
    if (state['evalution']=="approved" or state['max_interation']):
        return "approved"
    else:
        return "needs_improvement"
    

graph=StateGraph(TweetState)
graph.add_node("generate",generate_tweet)
graph.add_node("evalute",evaluate_tweet)
graph.add_node("optimize",optimize_tweet)

graph.add_edge(START,"generate")
graph.add_edge("generate","evalute")

graph.add_conditional_edges("evalute",route_evalution,{"approved":END,"needs_aprovement":"optimize"})

graph.add_edge("optimize","evalute")
workflow=graph.compile()

initial_state = {
    "topic": "Indian Railways",
    "iteration": 1,
    "max_iteration": 5,
    "tweet_history": [],
    "feedback_history": []
}

result = workflow.invoke(initial_state)
print(result) 

