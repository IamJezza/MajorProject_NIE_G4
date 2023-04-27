import pandas as pd
import numpy as np

my_dict = {}
unDetectableFaults = []
diff_data = pd.read_csv('DIFF_DATA.csv')
for i in range(1, 9):
    for j in range(1, 29):
        my_list = np.array(diff_data['out'+str(i)+'[0; '+str(j)+']']).nonzero()
        if list(my_list[0]):
            my_dict['out'+str(i)+'[0; '+str(j)+']'] = list(my_list[0])
        else:
            unDetectableFaults.append('out'+str(i)+'[0; '+str(j)+']')


useful_diff_data = diff_data.drop(unDetectableFaults, axis=1)
unuseful_diff_data = pd.DataFrame(unDetectableFaults)

unuseful_diff_data.to_csv('UNUSEFUL_DIFF_DATA.csv', index=False, header=False)
