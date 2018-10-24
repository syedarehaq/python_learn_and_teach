import pandas as pd
# %%
## Creating a dataframe
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series(['x', 'y', 'y'], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
## Filtering basid on single condition
single_condition_df = df[df['one'] > 1]

## Filtering based on two condition
## remember to use & instead of and; 
## also use brackets before and after each condition
multiple_condition = df[(df['one'] < 3) & (df['two'] == 'y')]

## filtering based on being in a list
single_condition_df = df[df['one'].isin([2,3])]

## Only keep specific columns from the dataframe
df_to_write = df[["country_id","state_id","Sh2Eh"]]
#https://stackoverflow.com/questions/11285613/selecting-multiple-columns-in-a-pandas-dataframe

## Create a dictionary from a dataframe:
df.set_index(KEY).to_dict()[VALUE]
# https://stackoverflow.com/questions/17426292/what-is-the-most-efficient-way-to-create-a-dictionary-of-two-pandas-dataframe-co