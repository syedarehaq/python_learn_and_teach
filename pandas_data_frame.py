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
