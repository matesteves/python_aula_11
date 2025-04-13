from example_class import Process_csv

file_path = './exemplo.csv'

df = Process_csv(file_path)
#print(df)
#print(df.dfs)
df.create_df()
#print(df)
#print(df.dfs)
print(df.df_filter(['estado', 'data'], ['SP', '20/01/2024']))