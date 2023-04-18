from fastapi import FastAPI, Request, Form
import pandas as pd
import numpy as np
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import Optional
import pickle

app = FastAPI()

@app.get ('/')
def read_root():
    return {"Bienvenido al sistema de consulta de series y peliculas de plataformas de streaming"}

@app.get('/get_max_duration')
def get_max_duration(year:int, platform:str, duration_type:str):
    platform = platform.lower()
    duration_type = duration_type.lower()
    if isinstance(year,int):
        if isinstance (platform,str) and (platform == "amazon" or platform == "disney" or platform == "netflix" or platform == "hulu"):
            if isinstance(duration_type,str):
                name = "df_"+platform+".csv"
                df = pd.read_csv(f'CSV ETL/{name}',delimiter=',')
                df = df[(df["type"]=="movie") & (df["duration_type"]==duration_type) & (df["release_year"]==year)]
                if df.empty:
                    return None
                else:
                    duration_max = df["duration_int"].max()
                    movie_name = df["title"].loc[df["duration_int"] == duration_max]
                    return {movie_name.to_string(index=False)}
            else: return None
        else: return None           
    else: None      
    
"""
    Esta función filtra el dataframe de la plataforma por año y tipo de duración y devuelve el nombre de la
    pelicula que tuvo mayor duracion para este año
"""

@app.get ('/get_score_count')
def get_score_count(platform:str, score:float, year:int):
    if isinstance (platform,str):
        platform = platform.lower()
        if isinstance (score,float):
            if isinstance (year,int):
                name = "df_"+platform+".csv"
                df = pd.read_csv(f'CSV ETL/{name}',delimiter=',')
                df_score = pd.read_csv('CSV ETL/df_score.csv',delimiter=',')
                df2 = pd.merge(df, df_score, on='id')
                df2 = df2[(df2["type"]=="movie") & (df2["score"]>=score) & (df2["release_year"]==year)]
            return {len(df2)}
        
"""
    Esta función une el dataframe plataforma con el dataframe score, los filtra por año y score, e imprime la
    cantidad de registros de peliculas que cumplen la condicion
"""

@app.get('/get_count_platform')
def get_count_platform(platform):
    if isinstance (platform,str) and (platform == "amazon" or platform == "disney" or platform == "netflix" or platform == "hulu"):
        platform = platform.lower()
        name = "df_"+platform+".csv"
        df = pd.read_csv(f'CSV ETL/{name}',delimiter=',')
        filtro = df['type'] == 'movie'
        cant_movies = df[filtro].count()['type']
        return int(cant_movies)
    else:
        return None
"""
    Esta función recibe el nombre de la plataforma y devuelve la cantidad de peliculas que estan disponibles 
    en esa plataforma
"""
    
@app.get ('/get_actor')
def get_actor(platform:str, year:int):
    if isinstance (platform,str) and isinstance (year,int):
        platform = platform.lower()
        name = "df_"+platform+".csv"
        df = pd.read_csv(f'CSV ETL/{name}',delimiter=',')
        valor_mas_repetido = df[df['release_year'] == year] ['cast'].mode()
        if len(valor_mas_repetido) == 0:
            return None
        else: 
            return valor_mas_repetido.values[0]
        
"""
    Esta función recibe el nombre de la plataforma y el año y devuelve el nombre del actor que mas veces aparece
    en esa plataforma para ese anio
"""

@app.get ('/prod_per_country')
def prod_per_county(tipo:str,pais:str,anio:int):
    if isinstance (tipo,str):
        if isinstance (pais,str):
            if isinstance (anio,int):
                df_streaming = pd.read_csv ('CSV ETL/df_streaming.csv',delimiter=',')
                df_filtrado = df_streaming[(df_streaming['country'] == pais) & (df_streaming['release_year'] == anio) & (df_streaming['type'] == tipo)]
                cant_datos = df_filtrado['type'].count()
                if cant_datos == 0:
                    return "null"
                else:
                    resultado = {
                    'pais': pais,
                    'anio': anio,
                     tipo : int(cant_datos),
                }
                return resultado
            else: 
                return "null"
        else: 
            return "null"
    else: 
        return "null"

"""
    Esta función recibe el pais, el año y el tipo de producto a consultar (movie o tv show) y devuelve un 
    diccionario con el nombre del pais el año y la cantidad de productos del tipo que se consulto, que hay 
    disponibles en todas las cuatro plataformas de streaming
"""

def cargar_modelo():
    with open('C:/Users/Crist/OneDrive/Escritorio/MLops PI/users_predictions.pkl', 'rb') as archivo_modelo:
            model = pickle.load('users_prediction.pkl')
    return model

@app.get("/get_predictions")
def get_prediction (userId:int):
    with open('users_predictions.pkl', 'rb') as archivo:
        model = pickle.load(archivo)
    users_predictions = model.predict (userId)
    return users_predictions  