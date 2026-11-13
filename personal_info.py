import pandas as pd
from config import PERSONAL_INFO_PATH

def load_personal_info():
    # Load the dataset
    personal_info_data = pd.read_excel(PERSONAL_INFO_PATH)
    
    # Group by category and join values
    personal_info_data_grouped = personal_info_data.groupby("Category").agg(lambda x: ' | '.join(x.dropna().astype(str)))
    
    return personal_info_data_grouped.to_dict(orient="index")
