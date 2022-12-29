import pandas as pd

def export_query_to_CSV(response, filename):
    df = pd.DataFrame(response)
    df.to_csv(filename, index=False)
