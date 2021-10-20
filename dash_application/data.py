import os
from io import BytesIO
import requests
import pandas as pd
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname('__file__'))

load_dotenv(basedir + '\.env')

git_key = os.environ.get('GITHUB_TOKEN') 
owner = os.environ.get('REPO_OWNER') 
repo = os.environ.get('REPO_NAME')
paths = ['bicicletas.xlsx','subte.xlsx','vehiculos.xlsx', 'covid (1).xlsx']


# Load data from local
def movility_data():
    df_list = []
    files_dir = os.path.join(basedir, 'dash_application','datasets')
    print(basedir)
    for f in os.listdir(files_dir):
        
        excel_file = os.path.join(files_dir, f)
        df = pd.read_excel(excel_file)
        df.columns = ['DICIEMBRE_ENERO' if name == 'Diciembre Vs Enero' else name.upper()for name in df.columns.values]
        df_list.append(df)
    
    df = pd.concat(df_list)
    return df
    
df_estaciones = pd.read_excel(os.path.join(os.path.abspath('.'),"dash_application","datasets", "estaciones.xlsx"))

# For loading files directly from github
def external_movility():  
    session = requests.Session()
    df_list = []
    for path in paths:
        req = session.get(
            'https://api.github.com/repos/{owner}/{repo}/contents/{path}'.format(
            owner=owner, repo=repo, path=path),
        headers={
                'accept': 'application/vnd.github.v3.raw',
                'authorization': 'token {}'.format(git_key)
                    }
            )


        req_c = req.content

        df = pd.read_excel(BytesIO(req_c))
        df_list.append(df)

    df = pd.concat(df_list)
    
    return df

