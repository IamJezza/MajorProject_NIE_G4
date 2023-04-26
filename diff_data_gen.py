import pandas as pd

data = pd.read_csv("transDATA.csv")
diff_data = pd.DataFrame()
for i in range(1, 9):
    for j in range(1, 29):
        diff_data['out'+str(i)+'[0; '+str(j)+']'] = data['out'+str(i)+'[0; '+str(j)+']']-data['out0[0]']


diff_data.to_csv("DIFF_DATA.csv", index=False)
