import sqlalchemy
import pandas as pd
import dj_database_url

def initialise():
    print(dj_database_url.config(conn_max_age=600))
    engine=sqlalchemy.create_engine(dj_database_url.config(conn_max_age=600))
    # engine = sqlalchemy.create_engine('sqlite:////home/manobhav/PycharmProjects/ChatBot/db.sqlite3')
    frame=pd.read_sql_table('chat_ml_userquery', engine,parse_dates=['date'])
    frame.drop('date',axis=1,inplace=True)
    return frame.to_dict(orient="records")


