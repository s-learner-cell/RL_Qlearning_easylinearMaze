import numpy  as np
import pandas as pd
N_STATES = 6
ACTIONS = ['left','right']
def build_q_table(n_states, actions):
    table=pd.DataFrame(
        np.zeros((n_states,len(actions))),
        columns=actions,

    )
    return table
#build_q_table(6, 2)
print(build_q_table(N_STATES,ACTIONS))