import pandas as pd
import warnings
import pyodbc
warnings.filterwarnings('ignore')
from fast_to_sql import fast_to_sql as fts


Source_server = 'A'
Source_database = 'ali'
Source_driver = '{SQL Server}'
Source_user = 'ali'
Source_passw = 'a?'

SourceConnection = pyodbc.connect(
    'DRIVER='+Source_driver +';SERVER='+ Source_server  + ';DATABASE='+Source_database+ ';UID=' +Source_user+';PWD=' +Source_passw )

query = '''
select * from t2
'''


#df = pd.read_excrl()
df = pd.read_sql(query, SourceConnection)
SourceConnection.close()

Target_server = 'B'
Target_database = 'a'
Target_driver = '{SQL Server}'
Target_user = 'a'
Target_passw = 'a22'

TargetConnection = pyodbc.connect(
    'DRIVER='+Target_driver +';SERVER='+ Target_server  + ';DATABASE='+Target_database+ ';UID=' +Target_user+';PWD=' +Target_passw )


Statement = fts.fast_to_sql(df, 't5', TargetConnection , if_exists= 'append'
                            ,custom={'phone':'varchar(20)', 'city':'varchar(50)', 'payment':'int'})

TargetConnection.commit()
TargetConnection.close()
