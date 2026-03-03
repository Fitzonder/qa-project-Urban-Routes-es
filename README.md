# Urban Routes Automated Testing project

## Descripción del Proyecto

Este proyecto tiene como objetivo implementar un framework de automatización de pruebas funcionales end-to-end para la aplicación web Urban Routes, una plataforma de solicitud de transporte bajo demanda.

Las pruebas se desarrollan en Python con Selenium WebDriver, permitiendo validar de forma automatizada flujos críticos como la configuración de rutas, autenticación por número telefónico, solicitud de servicios y gestión de métodos de pago.

Este enfoque asegura la verificación sistemática de la integridad funcional y la detección temprana de regresiones en la aplicación.

## Estructura del proyecto:

qa-project-Urban-Routes-es/

-- data.py              # Contiene los datos utilizados en las pruebas

-- CodeRetrieve.py      # Funcion auxiliar - obtención del código de confirmación

-- PageLocators.py      # Localizadores y métodos para interactuar con la página web

-- main.py              # Pruebas automatizadas

## Explicación de los Archivos

    data.py: Contiene valores como urban_routes_url, address_from, address_to, phone_number, card_number, etc. que se usan en los tests.

    CodeRetrieve.py: Contiene un metodo auxiliar el cual permite obtener códigos de verificación desde los logs de la red.

    PageLocators.py:  Este archivo define los elementos de la interfaz de usuario y las acciones que pueden ejecutarse sobre ellos. Incluye los localizadores de la página y métodos para interactuar con componentes como la selección de origen y destino, la adición de métodos de pago y otras operaciones dentro del flujo funcional.

    main.py: Contiene la clase TestUrbanRoutes, que agrupa las pruebas. Las pruebas incluyen escenarios como:
        Configuración de rutas
        Selección de taxi (opción de confort)
        Agregar número de teléfono y confirmarlo
        Agregar un método de pago
        Agregar un mensaje para el conductor
        Seleccionar requisitos adicionales (como mantas y helados)

## Tecnologías y Técnicas Utilizadas

- **Python**: Lenguaje de programación utilizado para escribir los scripts de prueba.
- **Selenium WebDriver**: Herramienta de automatización para la interacción con la interfaz de usuario de la aplicación web.
- **Edge**: Navegador utilizado para ejecutar las pruebas.
- **EdgeDriver**: Driver específico para controlar Edge mediante Selenium.
- **pytest**: Framework de pruebas para ejecutar y organizar los casos de prueba.

## Clonar el repositorio:
- git clone https://github.com/Fitzonder/qa-project-Urban-Routes-es

## Crear un entorno virtual:
- python -m venv env
- source env/bin/activate  # En Windows usa `env\Scripts\activate`

## Instalar las dependencias:
- pip install selenium pytest

## Asegúrate de tener un archivo requirements.txt que contenga:
- selenium==4.x.x
- pytest==x.x.x
- Edge
- EdgeDriver

## Ejecución de las Pruebas

- pytest tests/main.py

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si deseas proponer mejoras o nuevas funcionalidades, realiza un fork del repositorio, implementa los cambios correspondientes y envía un pull request para su revisión e integración.

Autor del proyecto: Carlos Lenis
