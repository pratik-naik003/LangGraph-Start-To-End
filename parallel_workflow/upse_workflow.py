from pydantic import BaseModel,Field
from langgraph.graph import StateGraph,START,END
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,List,Annotated
import operator
load_dotenv()



class Evalutionschema(BaseModel):
    feedback:str=Field(description="detailed feedback")
    score :int =Field(ge=0,le=10,description="score out of 10")

# model=GoogleGenerativeAI(model='gemini-2.5-flash')

model=GoogleGenerativeAI(model='gemini-2.0-pro')

structured_model=model.with_structured_output(Evalutionschema)

class UPSCState(TypedDict):
    essay:str
    language_feedback=str
    analysis_feedback=str
    clarity_feedback=str
    overall_feedback=str
    individual_scores=Annotated(List[int],operator.add)
    average_score=float

def evaluate_language(state:UPSCState):
    result=structured_model.invoke(f"evalute language quality:\n{state['essay']}")
    return {"language_feedback":result.feedback,
            "individual_score":[result.score]
            }
    
def evaluate_analysis(state:UPSCState):
    result=structured_model.invoke(f"evalute depth of analysis of following essay and provide a feedback and  quality:\n{state['essay']}")
    return {"analysis_feedback":result.feedback,
            "individual_score":[result.score]
            }
    
def evaluate_thought(state:UPSCState):
    result=structured_model.invoke(f"evalute clarity of thought of the following essays:\n{state['essay']}")
    return {"clarity_feedback":result.feedback,
            "individual_score":[result.score]
            }
    

def final_evalution(state:UPSCState):
    avg=sum(state['individual_score'])/len(state['individual_score'])
    summary_prompt=f"""
    Language feedback:{state['language_feedback']}
    analysis feedback:{state['language_feedback']}
    clarity feedback:{state['language_feedback']}
    """
    
    summary=model.invoke(summary_prompt).content
    
    return {
        "overall_feedback":summary,
        "average_score":avg}
    

graph=StateGraph(UPSCState)
graph.add_node('evaluate_language',evaluate_language)
graph.add_node('evaluate_analysis',evaluate_analysis)
graph.add_node('evaluate_thought',evaluate_thought)
graph.add_node('final_evalution',final_evalution)

#edges
graph.add_edge(START,'evaluate_language')
graph.add_edge(START,'evaluate_analysis')
graph.add_edge(START,'evaluate_thought')

graph.add_edge('evaluate_language','final_evalution')
graph.add_edge('evaluate_analysis','final_evalution')
graph.add_edge('evaluate_thought','final_evalution')

workflow=graph.compile()

essay="""The Indian AI Mission is a program started by the Indian government to develop artificial intelligence in the country. The main aim of this mission is to use AI in different areas like education, health, agriculture, and governance. AI can help India to become more digital and modern, but the mission is still in early stages.

India has a large population and a lot of data, which can be useful for AI systems. Through this mission, the government wants to support startups, researchers, and companies working on AI. Some training programs are also planned to teach students and professionals about AI. However, many people in rural areas still do not understand AI properly.

The mission also talks about ethical use of AI, but clear rules are not fully defined yet. There is also a problem of lack of good infrastructure and skilled experts in some regions. Funding is provided, but it may not be enough for large-scale impact.

Overall, the Indian AI Mission is a good step, but it needs better planning and execution. If not handled properly, the benefits of AI may reach only a few people instead of the whole country."""
intial_state={
    'essay':essay
}

final_state=workflow.invoke(intial_state)

print(final_state)
