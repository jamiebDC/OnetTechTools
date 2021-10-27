# Compare Hot Technology skills Examples, using data file downloaded from onetcenter.org
# 1. Excel's function to remove duplicates says there are 790 unique values
# 2. Pandas unique() function says there are 805 unique values
# 3. ONET support by email says there are 805 unique values in this file

import pandas as pd

ts = pd.read_excel(r'Technology Skills.xlsx')
ts.rename(columns={"O*NET-SOC Code": "Onetcode",
    "Commodity Code" :  "CCode",
    "Commodity Title":  "CTitle",
    "Hot Techology":    "HotTech"}, inplace=True)

# hot techs only; where the column HotTech = "Y"
tsh = ts.loc[ (ts.iloc[:,5] == 'Y')]

# unique hot tech examples, as determined by pandas function unique()
tshuniq = tsh.Example.unique()
tshuniq.sort()  # that's how you sort an array
# that's 805! Excel found only 790 unique hot tech examples! What's the diff? 

df805 = pd.DataFrame(data = tshuniq, columns = ['Example'])

df790 = pd.read_excel(r'TechUniqueByExcel.xlsx')
#sort by ascii; diff from Excel
df790.sort_values(by=['Example'], inplace=True) 

# List the 15 that are in one list, not in the other list
df15 = df805.loc[ ~ df805.Example.isin(df790.Example), :] 
# List the 790 that are common
#df805.loc[  df805.Example.isin(df790.Example), :]  

df805upper = pd.DataFrame(data = df805.Example.str.upper(), columns=['Example'])
#That's still 805. Now how many are unique?
df805upperunique = pd.DataFrame(data = df805upper.Example.unique(), columns=['Example'])
#That produces 790. 
#is it the same as the other 790?
df790upper = pd.DataFrame(data = df790.Example.str.upper(), columns=['Example'])
df790upperunique = pd.DataFrame(data = df790upper.Example.unique(), columns=['Example'])
DiffUpper = df805upperunique.loc[ ~ df805upperunique.Example.isin(df790upperunique.Example), :] 
# That produces an empty dataframe. So it seems right -- 
# 805 examples distill down to 790 when you match uppercase versions of the examples

# Check to ensure the comparison of uppercase works in the other direction.
SameUpper = df805upperunique.loc[ df805upperunique.Example.isin(df790upperunique.Example), :] 
# result has 790 rows. Confirmed.

# Conclusion:  the differences are just in capitalization. 
# The data is inconsistent. 
# "SharePoint" vs "Sharepoint"
# "Microstation" vs "MicroStation"

## How many of the Technology Skills examples are in ERP, or CAD, or neither?
df = tsh.copy()
df.rename(columns={
    "Commodity Code" :  "CCode",
    "Commodity Title":  "CTitle",
    "Hot Techology":    "HotTech"}, inplace=True)

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