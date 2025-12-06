import pandas as pd
import os 

csv_path= 'sales.csv'

if not os.path.exists(csv_path):

    data= [{'date':'2025-12-01',
            'product': 'camisa',
            'price':50,
            'quantity':2},

            {'date':'2025-12-01',
            'product': 'vestido',
            'price':200,
            'quantity':5},

            {'date':'2025-12-01',
            'product': 'calca',
            'price':400,
            'quantity':3},

            {'date':'2025-12-01',
            'product': 'blusa',
            'price':500,
            'quantity':1},


            {'date':'2025-12-01',
            'product': 'meia',
            'price':100,
            'quantity':9},


            {'date':'2025-12-01',
            'product': 'body',
            'price':150,
            'quantity':7},


            {'date':'2025-12-01',
            'product': 'saia',
            'price':300,
            'quantity':9},


            {'date':'2025-12-01',
            'product': 'touca',
            'price':70,
            'quantity':4},


            {'date':'2025-12-01',
            'product': 'luva',
            'price':45,
            'quantity':3},


            {'date':'2025-12-01',
            'product': 'regata',
            'price':95,
            'quantity':5},


         ]
    
    df_example= pd.DataFrame(data)
    df_example.to_csv(csv_path, index= False)
    print('uhul criou', csv_path)

df= pd.read_csv(csv_path, parse_dates=['date'])

required= {'date', 'product', 'price', 'quantity'}

if not required.issubset(set(df.columns)):
    print('as colunas estão erradas')

df['total']=df['price']*df['quantity']
df[['total']].to_csv('total.csv', index= False)
print('arquivo criado com sucesso')

