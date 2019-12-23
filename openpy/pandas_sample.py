# %%
import pandas as pd
import os
os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""

url = r'https://github.com/itcafe/opengithub/blob/master/openxlsx/ds.xlsx?raw=true'
df = pd.read_excel(url, sheet_name='nodeData')
# %%
