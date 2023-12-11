import psycopg2
import pandas as pd
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="analiz_dann",
    user="postgres",
    password="1234"
)