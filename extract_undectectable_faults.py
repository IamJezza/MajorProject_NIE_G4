import pandas as pd
import numpy as np

unDetectableFaults = []
diff_data = pd.read_csv('DIFF_DATA.csv')
for i in range(1, 9):
    for j in range(1, 29):
        my_list = np.array(diff_data['out'+str(i)+'[0; '+str(j)+']']).nonzero()
        if list(my_list[0]):
            pass
        else:
            unDetectableFaults.append('out'+str(i)+'[0; '+str(j)+']')


useful_diff_data = diff_data.drop(unDetectableFaults, axis=1)
unuseful_diff_data = pd.DataFrame(unDetectableFaults)

useful_diff_data.to_csv('USEFUL_DIFF_DATA.csv', index=False)
unuseful_diff_data.to_csv('UNUSEFUL_CASES.csv', index=False, header=False)
