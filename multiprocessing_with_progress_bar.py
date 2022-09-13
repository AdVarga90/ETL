# multiprocessing with progress bars
from tqdm import tqdm
import multiprocessing
import pandas as pd

# list of segments 
list_multiprocess_segment = df_input_segment['segment'].unique().tolist()

# function iterating through records in df, limited per segment
def calc_with_mp (type_num):
    output_mp=pd.DataFrame() # should be defined outside of the function for clarity
    calc_type = list_multiprocess_segment[type_num]
    for i in tqdm(range(0,len(df_input_segment[df_input_segment['segment'] == calc_type]))):
        output_mp=output_mp.append(calculate_racv(df_input_segment[df_input_segment['segment'] == calc_type].iloc[i])) # replace calculate_racv with any iterable function
    return output_mp

# MP part where segment is parallelized; output is a list of pandas DFs
pool_obj = multiprocessing.Pool()
list_of_dfs = pool_obj.map(calc_with_mp, range(0,len(list_multiprocess_segment)))

# putting it all togethe
calc_output=pd.DataFrame()
for dfx in range(0,len(list_of_dfs)):
    calc_output = calc_output.append(list_of_dfs[dfx])

