# Cerebro NYC — prototipo de rescate (segunda entrega)

**Integrantes declarados en la primera entrega:** Carlos David Sanchez Soto, Alejandro Garcia Cortes y Daniel Urbano Viana Polo. **Ciudad:** Nueva York.

## Ejecutar

1. Ponga el Excel original en esta carpeta como `Diccionario.xlsx`.
2. Ejecute `python build.py Diccionario.xlsx` para regenerar `fuentes.json`.
3. Ejecute `python -m http.server 8000` y abra `http://localhost:8000`.
4. Para publicar, suba `index.html` y `fuentes.json` a un hosting estático. **No se ha publicado desde este paquete.**

## Alcance y decisiones

Se muestra el mapa territorial de F01 mediante una API pública y las fichas documentales de las fuentes de la primera entrega. No se presentan cifras sin verificación. La página funciona en móvil y no requiere llave paga. **No cumple todavía el requisito de tres fuentes integradas en vistas**: las fichas de fuentes no equivalen a ingesta de datos. El archivo `build.py` convierte metadatos del diccionario, no constituye ingesta de las fuentes primarias. Tampoco se ha probado aquí una segunda herramienta visual.

**Uso:** la información procede de organismos públicos; se conserva literalmente la licencia del Excel, incluso cuando dice «no declara». No se infiere permiso de reutilización. **Protección:** no publicar datos a nivel de evento de F05 (coordenadas, fecha, ID de colisión), ni datos personales. En una versión final, publicar agregados por zona y mes, con control de celdas pequeñas.

**Preguntas:** el mapa responde qué divisiones territoriales cubre el sistema (F01). La comparación de población/vivienda (F19) y la distribución de servicios (F08–F15) siguen pendientes; no se presentan como resueltas.

## Exploración de herramientas — bitácora honesta

| Herramienta | Requisitos | Licencia | Dónde quedan los datos | Resuelve | Limitaciones | Estado |
|---|---|---|---|---|---|---|
| Leaflet | HTML/JS y navegador | BSD-2-Clause | Datos en API NYC; interfaz en hosting propio | Mapa de F01 | Depende de API y CDN | Implementada en este prototipo; verificar en navegador |
| Streamlit | Python, instalación y despliegue | Apache-2.0 | En servidor del despliegue y fuentes externas | Candidata a tablas y filtros | Requiere servidor Python | **No probada**; falta comparación empírica |

**Decisión provisional:** Leaflet para mapa sin backend; no se afirma que se hayan comparado dos herramientas sobre los mismos datos.

## Bitácora IA — ampliación

- Acierto documentado en entrega 1: F16, consulta de artículos de Wikipedia, comprobación de 9 artículos × 12 meses; las vistas no son personas únicas.
- Error documentado en entrega 1: fuente cultural `pfja-tk2j` devolvió registros cuestionables y fue sustituida por F13.
- En esta etapa: IA generó un prototipo y un exportador de metadatos. **Pendiente** contrastar la API, validar el sitio en móvil y ejecutar pruebas de ingesta. No confundir código generado con resultado probado.

## Reflexiones del taller

**Datos:** tener una URL pública no garantiza calidad, vigencia ni licencia de reutilización. Cada visualización debe vincular fuente, fecha y escala para evitar comparaciones engañosas.

**Seguridad:** eliminar nombres no basta para anonimizar registros georreferenciados. Las coordenadas exactas, identificadores y fechas de accidentes pueden facilitar reidentificación; se excluyen del sitio y se propone publicar agregados.

## Para defensa oral

- **¿Qué herramienta casi elegimos y descartamos?** Streamlit se consideró como alternativa, pero aún no se ha probado: no afirmamos descarte empírico.
- **¿Qué no mostramos?** Eventos individuales de accidentes y cifras temáticas sin verificar.
- **¿Qué cambiaría la decisión?** Una prueba con idénticos datos en ambas herramientas, mejor desempeño móvil, evidencia de privacidad y trazabilidad de tres fuentes integradas.

## Pendientes para cumplir la rúbrica completa

1. Recuperar y verificar scripts del lago original, o escribir tres ingestas reproducibles con fuentes reales.
2. Construir dos vistas que respondan dos preguntas originales con datos reales.
3. Ejecutar comparación Leaflet vs. Streamlit con el mismo conjunto de datos y registrar evidencias.
4. Actualizar Excel dejando solo fuentes realmente presentes, y registrar fechas de prueba y licencias comprobadas.
5. Verificar visualmente en móvil, desplegar, enlazar repositorio y documentar pruebas.
