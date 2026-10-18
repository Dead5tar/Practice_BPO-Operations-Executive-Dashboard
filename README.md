# A BPO & Manufacturing Operations Analytics (Python & Pandas)

## A Resumen del Proyecto
Este proyecto de análisis de datos utiliza **Python y Pandas** para evaluar la eficiencia operativa, los tiempos muertos (*idle times*) y las métricas de rendimiento en entornos híbridos de **BPO (Call Centers)** y **Manufactura/Confección**. El objetivo es identificar cuellos de botella operativos y prever riesgos de rotación de personal basados en la sobrecarga de trabajo.

### A Tecnologías Utilizadas
* **Python**: Lenguaje principal de programación.
* **Pandas**: Manipulación, limpieza, agrupación y filtrado de datos tabulares.
* **Business Intelligence**: Enfoque analítico orientado a la toma de decisiones gerenciales y reducción de costos operativos.

### A ¿Qué hace el script (`operations_analysis.py`)?
1. **Carga y Simulación de Datos:** Crea un DataFrame híbrido que simula métricas operativas de empleados tanto en sectores de servicios (BPO) como de producción física (Manufactura/Confección).
2. **Agregación por Turno y Sector:** Calcula el promedio de tiempos muertos agrupando los datos por sector económico y turno laboral (Día vs. Noche).
3. **Detección de Riesgo de Rotación (*Attrition*):** Filtra de forma automatizada a aquellos empleados que experimentan altos tiempos muertos (más de 30 minutos) y que terminaron renunciando, permitiendo aislar patrones de frustración operativa o mal diseño de turnos.

### A Hallazgos Clave y Aplicación de Negocio
* **Desbalance Operativo Nocturno:** Los turnos nocturnos tienden a presentar mayores picos de tiempo muerto debido a una subestimación o mala distribución del volumen de interacciones/producción.
* **Impacto Humano:** Las operaciones con alta inestabilidad temporal muestran una correlación directa con la fatiga del operario/agente y la renuncia temprana, elevando los costos de contratación de la empresa.

### A Cómo ejecutar el proyecto
1. Asegúrate de tener Python instalado con Pandas:
   ```bash
   pip install pandas
