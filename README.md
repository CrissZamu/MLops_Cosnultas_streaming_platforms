## INDICE:
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#INDICE">ÍNDICE</a></li>
    <li><a href="#INTRODUCCIÓN">INTRODUCCIÓN</a></li>
    <li><a href="#OBJETIVO">OBJETIVO</a></li>
    <li><a href="#SCOPE-OF-WORK">SCOPE OF WORK</a></li>
    <li><a href="#ESTADO">ESTADO</a></li>
    <li><a href="#EDA-ETL">EDA - ETL</a></li>
    <li><a href="#FastAPI">FastAPI</a></li>
    <li><a href="#Deploy">Deploy</a></li>
    <li><a href="#ACCESO-AL-PROYECTO">ACCESO AL PROYECTO</a></li>
    <li><a href="#TECNOLOGÍAS">TECNOLOGÍAS UTILIZADAS</a></li>
    <li><a href="#VIDEO">VIDEO</a></li>
  </ol>
</details>

## INTRODUCCIÓN
Este proyecto forma parte de la etapa Labs del curso de Data Science de la Academia Soy Henry. donde a partir de los set de las 4 plataformas mas usadas en streaming y las puntuaciones asignadas por los usuarios a sus contenidos se realizara un trabajo de Data Science.

las fuentes de información asociadas a las plataformas de streaming, son:
- Amazon Prime Video
- Disney Plus
- Hulu
- Netflix

Y 8 datasets de ratings que contiene las puntuaciones de los usuarios alos contenidos
## OBJETIVO
Diseñar una API que permita a los usuarios realizar 5 consultas diferentes sobre los data sets provistos y una consulta de tipo predictivo que le recomiende 5 titulos de peliculas a un usuario teniendo en cuenta sus gustos.

## SCOPE-OF-WORK
El proyecto se desarrolla en 6 estapas y parte de los [Datasets](https://github.com/HX-PRomero/PI_ML_OPS)
provistos para este trabajo.

estas son las etapas en las que se desarrollo el proyecto:

1. Extraer-Transformar y Cargar los datos con Python (ETL). Link: (https://github.com/CrissZamu/MLops_Cosnultas_streaming_platforms/blob/main/ETL/ETL.ipynb)
2. Análsisi exploratorio de los datos para ML (EDA) parte 1. Link: (https://github.com/CrissZamu/MLops_Cosnultas_streaming_platforms/blob/main/EDA/EDA%20for%20ML.ipynb)
3. Desarrollo de Modelo con Machine Learning (ML) parte 2 Link: (https://github.com/CrissZamu/MLops_Cosnultas_streaming_platforms/blob/main/EDA/EDA%20for%20ML.ipynb)
4. Desarollo de una API con FastAPI Link: (https://github.com/CrissZamu/MLops_Cosnultas_streaming_platforms/blob/main/main.py)
5. Deploy de la API en Render para las funciones de consulta y la funcion de recoemndacion Link: (https://api-consulta-streaming-platforms.onrender.com/docs)
6. Video Link: (https://youtu.be/5V-PLs3UDc8)

![arquitectura](https://github.com/CrissZamu/MLops_Cosnultas_streaming_platforms/blob/main/structure.png)

## ESTADO:
<h4 align="center">
 Proyecto Pendiente
 "En la API en la funcion get_prediction devulve Internal Server Error" 
</h4>

## ETL y EDA para ML
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width=40px height=40px/>  
Como paso inicial en la etapa de ETL, los datos fueron cargados con la libreria pandas realizar el respectivo análisis de los datos y las transformaciones solicitadas por el area encargada. como resultado obtenemos los CSV limpiados y transformados que puedes ver en la carper CSV ETL, aun se encuntran separados por plataformas para que los tiempos de carga en la API sean mas optimos.

En la carpeta ETL encuentras el la funcio desarollada para ingestar un csv limpiarlo, tranformalo y exportalo para que sea consumido por la API. lo puedes aqui Link: (https://github.com/CrissZamu/MLops_Cosnultas_streaming_platforms/blob/main/ETL/ETL.ipynb)

Para la etapa de EDA para ML se consumio de los datos limpiados y transformados en la etapa de de ETL, en esta etapa se realizo el analisis de los datos para conocer su comportamiento y se desarrollo a la par el Modelo de Machine Learning para exportarlo y que sea consumido por la API. lo puedes ver aqui LINK: (https://github.com/CrissZamu/MLops_Cosnultas_streaming_platforms/blob/main/EDA/EDA%20for%20ML.ipynb) 



## FastAPI
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width=40px height=80px/>
El desarollo de la API se encuentra en el codigo main.py. Con eso, se construyó la API localmente y se configuraron las funciones para realizar las peticiones de consulta y la peticion de predicción. La API carga el CSV que se solicita y retorna los valores esperados. lo puedes ver aqui Link: (https://github.com/CrissZamu/MLops_Cosnultas_streaming_platforms/blob/main/main.py)

## Deploy  
<img src="https://intellyx.com/wp-content/uploads/2019/08/Render-cloud-intellyx-BC-logo.png" width=40px height=40px/>
Para que la API sea consumible por cualquier usuario se realizo el deploy en la plataforma RENDER. donde se creo un servidor que contiene todo lo necesario para realizar las consultas de forma no local. las puedes consultar en el sigueinte link

Link deploy: https://api-consulta-streaming-platforms.onrender.com/docs


## ACCESO-AL-PROYECTO
            ## 🛠️ Abre y ejecuta el proyecto
            -  Para correr la api completa es necesario descomprimir el archivo que contiene el modelo, para que la api consuma de ese archivo, y como se subió la carpeta donde se desarrolló la api completa, debe correr.
            -Para visualizar la salida final en los Deploys podes ir al link de punto 7 y 8 del scope of work, o ingresar al alrchivo txt que contiene todos los links.
            
 
## TECNOLOGÍAS
 <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width=40px height=40px/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width=40px height=40px/> 
<img src="https://intellyx.com/wp-content/uploads/2019/08/Render-cloud-intellyx-BC-logo.png" alt="deta" width="40" height="80"/> 


## VIDEO
En el sigueinte video podras encontrar una explicación y demostración mas detallada del proceso de este proyecto 
https://youtu.be/5V-PLs3UDc8

Gracias por ver este desarrollo, podes seguir los futuros cambios dandole una estrellita en la parte superior derecha del repositorio. Podes Clonarlo, y/o podes hacer un PullRequest ya que todo aporte es bienvenido. 


