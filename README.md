# BotDetector

## Descripción

BotDetector es una herramienta diseñada para analizar cuentas de redes sociales (como Facebook e Instagram) para detectar posibles bots utilizando la Ley de Benford. Esta técnica matemática se aplica a los primeros dígitos de las cantidades de seguidores de las cuentas, permitiendo identificar patrones inusuales que pueden indicar la presencia de cuentas automatizadas o falsas.

## Estructura del proyecto

Este proyecto consta de los siguientes archivos:

- **`main.py`**: El script principal donde se ejecuta el análisis de los datos.
- **`Data.xlsx`**: Un archivo de ejemplo con los datos de cuentas de redes sociales y sus seguidores (reales y sospechosos).
- **`requirements.txt`**: El archivo de dependencias del proyecto, que contiene todas las librerías necesarias para ejecutar el código.

## Instalación

Para instalar y ejecutar BotDetector, sigue estos pasos:

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/BluerZu/BotDetector.git

2. Navega al directorio del proyecto:

   ```bash
   cd BotDetector
   
3. Crea un entorno virtual (opcional, pero recomendado):

   En Windows:

   ```bash
   python -m venv .venv

4. Activa el entorno virtual:
   - En Windows:

     ```bash
     .venv\Scripts\activate
     ```
     
5. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt

## Uso

1. Asegúrate de tener un archivo de datos con las cuentas y los seguidores (como `Data.xlsx`).
2. Ejecuta el script principal para analizar las cuentas:

   ```bash
   python main.py

## Requisitos

- **Python 3.x**
- Las dependencias del proyecto se encuentran en el archivo `requirements.txt`.
