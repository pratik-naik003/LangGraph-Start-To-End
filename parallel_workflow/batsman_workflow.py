from langgraph.graph import StateGraph,START,END
from typing import TypedDict

class BatsmanState(TypedDict):
    runs:int
    balls:int
    fours:int
    sixes:int
    sr:float
    bpb:float
    boundry_percent:float
    summary:str
def calculate_sr(state:BatsmanState):
    sr=(state['runs']/state['balls'])*100
    return {'sr':sr}
    

def calculate_bpb(state:BatsmanState):
    bpb=state['balls']/(state['fours']+state['sixes'])
    return {'bpb':bpb}

def calculate_boundry_persent(state:BatsmanState):
    boundry_percent=(((state['fours']*4)+(state['sixes']*6))/state['runs'])*100
    return {'boundry_percent':boundry_percent}

def summary(state:BatsmanState):
    summary=f"""strike rate-{state['bpb']}\n
    balls per boundary -{state['boundry_percent']}"""
    return {'summary':summary}
graph=StateGraph(BatsmanState)
graph.add_node('calculate_sr',calculate_sr)
graph.add_node('calculate_bpb',calculate_bpb)
graph.add_node('calculate_boundry_percent',calculate_boundry_persent)
graph.add_node('summary',summary)

#edges
graph.add_edge(START,'calculate_sr')
graph.add_edge(START,'calculate_bpb')
graph.add_edge(START,'calculate_boundary_percent')
graph.add_edge('calculate_sr','summary')
graph.add_edge('calculate_bpb','summary')
graph.add_edge('calculate_boundry_percent','summary')

graph.add_edge('summary',END)

workflow=graph.compile()

intial_state={'run':100,
              'balls':50,
              'fours':6,
              'sixes':4}
final_state=workflow.invoke(intial_state)
print(final_state)
