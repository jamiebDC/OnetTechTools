# Compare Hot Technology skills Examples, using data file downloaded from onetcenter.org
# 1. Excel's function to remove duplicates says there are 790 unique values
# 2. Pandas unique() function says there are 805 unique values
# 3. ONET support by email says there are 805 unique values in this file

import pandas as pd

ts = pd.read_excel(r'Technology Skills.xlsx')
ts.rename(columns={"O*NET-SOC Code": "Onetcode"}, inplace=True)

# hot techs only
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
