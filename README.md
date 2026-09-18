# Práctico 3 - Automatización de Calidad y Blindaje

Trabajo práctico realizado para la materia Metodología de Sistemas II.

## Objetivo

El objetivo de este trabajo es aplicar herramientas de control de calidad sobre un proyecto en Python, incorporando análisis estático, formateo automático, pruebas unitarias y controles antes de realizar un commit.

## Herramientas utilizadas

- Python
- Pytest
- Pytest-cov
- Ruff
- Black
- Git
- GitHub
- Visual Studio Code

## Controles de calidad

Para verificar la calidad del proyecto se utilizaron diferentes herramientas:

- **Black:** para comprobar y mantener un formato uniforme en el código.
- **Ruff:** para realizar análisis estático y detectar posibles problemas.
- **Pytest:** para ejecutar las pruebas unitarias.
- **Pytest-cov:** para medir la cobertura de las pruebas.

Luego de ampliar los casos de prueba se obtuvo una cobertura del 100%.

## Automatización

Se configuró un control automático de calidad mediante pre-commit.

Antes de realizar un commit se verifican:

1. El formato del código con Black.
2. El análisis estático mediante Ruff.
3. La ejecución de las pruebas unitarias mediante Pytest.

De esta manera, si alguno de los controles presenta errores, el commit no debería continuar hasta corregir el problema.

## Gestión de cambios

Para realizar las mejoras se utilizó una rama llamada:

`mejora-calidad-codigo`

También se creó un Issue para registrar las mejoras necesarias y posteriormente se realizó un Pull Request para incorporar los cambios a la rama principal.

Una vez verificadas las mejoras, el Pull Request fue aprobado e integrado a `main` y el Issue correspondiente quedó cerrado.

## Resultados obtenidos

Los controles realizados finalizaron correctamente:

- Black: correcto.
- Ruff: sin errores.
- Pytest: 6 pruebas superadas.
- Cobertura de pruebas: 100%.
- Pull Request integrado correctamente.
- Issue de mejora cerrado.

## Conclusión

Con este práctico se pudo comprobar cómo distintas herramientas permiten automatizar controles de calidad sobre un proyecto. La utilización de pruebas, análisis estático, formato automático y control previo a los commits ayuda a detectar problemas antes de incorporar cambios al código principal.
