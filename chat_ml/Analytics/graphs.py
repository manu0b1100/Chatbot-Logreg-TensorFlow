import sqlalchemy
import pandas as pd
import dj_database_url
from ChatBot.settings import *

def initialise():
    # print(dj_database_url.config(conn_max_age=600))
    #
    # user = DATABASES['default']['USER']
    # password = DATABASES['default']['PASSWORD']
    # database_name = DATABASES['default']['NAME']
    # port=DATABASES['default']['PORT']
    # host=DATABASES['default']['HOST']
    #
    # database_url = 'postgresql://{user}:{password}@{host}:{port}/{database_name}'.format(
    #     user=user,
    #     password=password,
    #     database_name=database_name,
    #     host=host,
    #     port=port
    # )
    # engine=sqlalchemy.create_engine(database_url)

    engine = sqlalchemy.create_engine('sqlite:////home/manobhav/PycharmProjects/ChatBot/db.sqlite3')
    frame=pd.read_sql_table('chat_ml_userquery', engine,parse_dates=['date'])
    frame.drop('date',axis=1,inplace=True)
    return frame.to_dict(orient="records")


