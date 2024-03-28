project_data_analytics
==============================
A lo largo de la historia de nuestro país, el futbol ha formado parte importante de la vida de los mexicanos, provocando que sea uno de los deportes más populares en el país. 
Miles de mexicanos y mexicanas sienten una gran pasión por el futbol, ya sea jugándolo o disfrutándolo en la televisión. 

El dataset con el que se trabajó es del Mundial de futbol, el cual cuenta con 900 observaciones y 15 features entre ellas se pueden encontrar diferentes datos, como por ejemplo los años en los que se llevó a cabo cada mundial, los cuales van desde el Mundial de 1930 en Uruguay hasta el Mundial del 2018 en Rusia.

Se considera que es un tema interesante a analizar ya que, al ser un deporte tan conocido y relevante en el país, puede resultar atractivo ver tendencias de los países que más han ganado partidos y mundiales a lo largo de los años, así como ver el desarrollo que ha tenido la selección mexicana en este torneo tan importante.

Con este proyecto se pretende analizar el desempeño de México en los diferentes mundiales, así como visualizar cuáles países han sido los dominantes. También crear un modelo que, basándose en los datos, sea capaz de predecir o estimar los goles que puede meter la selección mexicana dependiendo de su oponente.

En el proyecto se pueden encontrar primeramente, las librerías que se van a utilizar para llevarlo acabo, como por ejemplo pandas, numpy, matplotlib, entre otras.

La programación tiene un orden en específico. Primero se visualiza si hay valores faltantes, en este caso sí hay en las columnas de 'winning_team', 'losing_team' y 'win_conditions'. Por cuestiones práticas se eliminó la columna de 'win_conditions', ya que no se considera relevante para el análisis del dataset y además porque casi no había registros en esa columna.
Para los valores faltantes en las otras dos features no se hizo ningún método para sustituirlos ya que los que faltaban se debían a los empates, por lo que no fue necesario.

Al hacer observaciones sobre cuál país ha ganado más mundiales, se pudo percatar que en el mundial de 1950 no se especificaba una Final como tal, ya que varios partidos indicaban 'Final Round' en la columna de stage, aquí sí fue necesario asignar la final, la cual fue entre Uruguay y Brasil, ganada por Uruguay.

Después de la limpieza de datos, se enucentra el EDA (Análisis Exploratorio de Datos) en donde se pueden encontrar diferentes insights interesantes así como gráficas para que sea más visual y entendible la información.

Por último se encuentra el apartado del modelo de predicción, en este caso se trabajó con Regresión Lineal, que pertenece al aprendizaje supervisado, para poder predecir los goles de México según su contrincante.


A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
