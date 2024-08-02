from datetime import datetime
import warnings
import pyodbc
warnings.filterwarnings('ignore')

Source_server = 'SS'
Source_database = 'ali'
Source_driver = '{SQL Server}'
Source_user = 'alireza?!'
Source_passw = 'a123!'

SourceConnection = pyodbc.connect(
    'DRIVER='+Source_driver +';SERVER='+ Source_server  + ';DATABASE='+Source_database+ ';UID=' +Source_user+';PWD=' +Source_passw )

query = 'select * FROM [ali].[dbo].[salary]'

cursor = SourceConnection.cursor()
cursor.execute(query)
rows = cursor.fetchall()
SourceConnection.close()



Target_server = 'P2'
Target_database = 'T1'
Target_driver = '{SQL Server}'
Target_user = 'a'
Target_passw = 'a123'

TargetConnection = pyodbc.connect(
    'DRIVER='+Target_driver +';SERVER='+ Target_server  + ';DATABASE='+Target_database+ ';UID=' +Target_user+';PWD=' +Target_passw
    
    )


q1 = ''' 
CREATE TABLE t2 (
    phone varchar(20),
    city varchar(50),
    payment int
); 
'''


TargetConnection.execute(q1)
TargetConnection.commit()

q2 = 'insert into  [alireza].[dbo].[t2] ([phone],[city] ,[payment]) values(?,?,?) '

cursor = TargetConnection.cursor()

for row in rows:
    print(row)  # Print row to debug
    cursor.execute(q2, row)
    TargetConnection.commit()

TargetConnection.close()
