# CodefestReto1

## Solución al reto 1

### Prerrequisitos

- keras `pip install keras`
- OpenCV `pip install opencv-python`
- numpy `pip install numpy`
- tensorflow `pip install tensorflow`

### ¡Rapido Inicio!

Dentro de la carpeta que contiene el main.py de tu proyecto, debes clonar este respositorio con el siguiente comando: `git clone https://github.com/Ferax-Hp/CodefestReto1`

Una vez clonado el repositorio puedes importar el paquete de python `from CodefestReto1 import *`, y podrías llamar la función llamada `detect_objects_in_video` 

Esta función toma como argumentos que son: Ruta absoluta o relativa donde se encuentra el vídeo y, la ruta de donde desea guardar el archivo .csv

### Procedimiento

Para el entrenamiento y desarrollo de esta libreria se llevaron acábo los siguientes pasos:

1. Optener los datos para entrenar la IA
   1. Se separan en distientas carpetas los frames que contienen las zonas de interes
      - Contrucciones
      - Areas de mineria
      - Vehiculos
   2. Además se separan muchos frames que no contengan ninguna de esta informacion para que sirvan de comparacion para la IA

2. Con la ayuda de [TeachableMachine](https://teachablemachine.withgoogle.com/train/image) entrenamos una IA capaz identificar que objetos se encuentran en dicha imagen
3. Descargamos el modelo entrenado provisto por la herramienta en formato [*.h5]().
4. Luego en python leemos este archivo con la ayuda de KERAS.
5. A travez de OpenCV leermos el video, y lo separamos en frames.
6. Donde cada frame es analizado y clasificado.