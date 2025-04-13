import pandas as pd

class Process_csv:
    def __init__(self, path):
        self.path = path
        self.dfs = None
    
    def create_df(self):
        self.dfs = pd.read_csv(self.path, encoding='utf-8')
        return self.dfs

    def df_filter(self, columns: list[str], values: list[str]):
        if len(columns) != len(values):
            raise ValueError("Number of columns and values don't match")
        
        if len(columns) == 0:
            raise ValueError("Need at least one column")
        
        filter_column = columns[0]
        filter_value = values[0]

        filtered_df = self.dfs[self.dfs[filter_column] == filter_value]

        if len(columns) == 1:
            return filtered_df
        else:
            return self.df_filter(columns[1:], values[1:])