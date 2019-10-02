# AIWorkshopMadrid - Día 2 - Machine Learning

## Laboratorio 1. Regresión

Desde la empresa Mediature, nos han pedido ser capaces de predecir el número de ventas en función del dinero que se ha invertido en cada uno de los canales de Marketing existente: televisión, redes sociales y radio. El departamento de marketing nos ha facilitado su histórico de datos en formato .csv.

El conjunto de datos se encuentra en: <https://aiworkspace1038514484.blob.core.windows.net/day2/Advertising.csv>

## Laboratorio 2. Clasificación

El departamento de ventas de la misma empresa, también esta interesado en saber si lo posibles clientes potenciales pueden o no comprar un producto. Para que podamos hacer un estudio de los datos, nos han pasado todo el histórico de compras y clientes. Al final, la idea principal es poder estudiar los comportamientos de los clientes y ver si un posible cliente puede comprar un producto o no en función de las últimas veces que visitó una tienda o su estado civil.

El conjunto de datos se encuentra en: <https://aiworkspace1038514484.blob.core.windows.net/day2/retail_dataset.csv>

## Laboratorio 3. Regresión Deep Learning

Predicción de eficiencia de combustible de automóviles utilizando el dataset Auto MPG <https://archive.ics.uci.edu/ml/datasets/auto+mpg>

### Configuración entorno anaconda

Para poder configurar el entorno tendremos que tener instalado previamente anaconda.Una vez que hayamos terminado la instalación, desde anaconda prompt, o desde nuestra línea de comandos, podemos introducir:

`conda env create -f environment.yml`

para instalar todas nuestras dependencias. Una vez haya acabao el proceso, procederemos a activar el entorno.

`conda activate aiworkshopday2`


### Configuración Workspace Azure ML

Para inicializar el workspace de Azure Machine Learning, necesitamos:

- Nombre del grupo de recursos,
- Id de la subscripción
- Nombre del workspace de AzureML.

Hay que rellenar todos estos datos en el fichero azureml_ws.json de la carpeta configuración.

`ws = Workspace.from_config(path="config/azureml_ws.json")`
