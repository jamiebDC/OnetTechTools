# This triggers the warning about a copy

import pandas as pd
ts = pd.read_excel(r'Technology Skills.xlsx')
ts.rename(columns={"O*NET-SOC Code": "Onetcode",
    "Commodity Code" :  "CCode",
    "Commodity Title":  "CTitle",
    "Hot Techology":    "HotTech"}, inplace=True)

# hot techs only; where the column HotTech = "Y"
tsh = ts.loc[ (ts.iloc[:,5] == 'Y')]

## How many of the Technology Skills examples are in ERP, or CAD, or neither?
df = tsh.copy()
df.rename(columns={
    "Commodity Code" :  "CCode",
    "Commodity Title":  "CTitle",
    "Hot Techology":    "HotTech"}, inplace=True)