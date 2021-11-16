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

# How many unique Examples among the whole table?
dfu = df.Example.unique()

# How many erp, unique?  Answer:  275 
erp = df.loc[ df.CCode == 43231602 ]
erpu = erp.Example.unique()

# How many CAD, unique?  Answer:  355 
cad = df.loc[ df.CCode == 43232604 ]
cadu = cad.Example.unique()

#How many neither CAD nor ERP, unique?  
neither = df.loc[ ~ df.CCode.isin([43231602,43232604])]
neitheru = neither.Example.unique()
# Answer: 181. Expected 175, because 805 = 275+355+175

#How many unique Cmomodity codes altogether? 51
CommUniq = tsh.CCode.unique()
CommUniq.shape # 51
#How many unique Commodity Codes in each group? 
#How many unique Commodity Codes in the erp group? Answer:  1
erpCcodes = erp.CCode.value_counts()
#How many unique Commodity Codes in the cad group? Answer:  1
cadCcodes = cad.CCode.value_counts()
#How many unique Commodity Codes in the "neither" group? Answer:  49
neithercodes = neither.CCode.value_counts()
# Conclusion:  51 unique commodity codes in all. 