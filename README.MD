# 📌 **Análisis de Caminos en Grafos Dirigidos**

## 📝 **Descripción del Proyecto**
Este proyecto implementa un **grafo dirigido** para analizar la conectividad entre nodos. Se enfoca en cuatro tareas principales:

1. 🔎 **Identificar el nodo más alcanzable desde el nodo '0'**: Se determina cuál es el nodo con mayor cantidad de rutas diferentes que lo alcanzan.
2. 📊 **Ordenar los caminos hacia el nodo más alcanzable según su costo**: Se analizan todas las rutas y se ordenan en función del costo total del trayecto.
3. 🏗️ **Introducir un nuevo nodo 'V\'' para modificar la estructura del grafo**:
   - 'V\'' debe volverse el nodo más alcanzable en lugar del nodo previamente identificado.
   - Los nodos que comparten una arista con 'V' no pueden compartir una arista con 'V\''.
4. ⚠️ **Manejo de restricciones**: Si la condición anterior no se puede cumplir, se muestra un mensaje de error explicativo.

---
## 🔍 **Lógica de Solución**

### 📌 **1. Identificación del Nodo Más Alcanzable**
El análisis inicia en el nodo **'0'**, explorando todas las posibles rutas hacia otros nodos. Se cuentan los caminos que llevan a cada nodo, y el nodo con el mayor número de rutas se considera el más alcanzable (**V**).

### 📌 **2. Ordenación de Caminos por Costo**
Una vez identificado el nodo más alcanzable:
- Se buscan todas las rutas desde **'0'** hasta dicho nodo.
- Se calcula el **costo** de cada ruta sumando los pesos de las conexiones.
- Los caminos se ordenan de **mayor a menor costo**, permitiendo evaluar su eficiencia.

### 📌 **3. Inserción del Nodo 'V\''**
Para modificar la estructura del grafo:
- Se introduce un nuevo nodo **'V\''** con conexiones estratégicas.
- Se seleccionan nodos que **no sean vecinos directos** del nodo más alcanzable (**V**).
- Se verifica que 'V\'' genere **más caminos** que 'V'.
- Si 'V\'' se vuelve más accesible, la modificación es **exitosa** y se imprime en el formato de entrada.
- Si la condición (3.b) no se puede cumplir, se muestra un mensaje de error explicando la imposibilidad.


## ⚙️ **Ejecución del Análisis**
El código sigue una estructura clara para ejecutar los cuatro pasos mencionados:

1️⃣ **Construcción del grafo** con nodos y conexiones predefinidas.

2️⃣ **Identificación del nodo más alcanzable** desde '0'.

3️⃣ **Ordenación de caminos** según el costo.

4️⃣ **Inserción de 'V\'' y validación** de su accesibilidad y restricciones.

5️⃣ **Manejo de errores** en caso de que la inserción no sea posible.

---
🚀 ¡Este análisis permite mejorar la estructura y eficiencia de los grafos dirigidos de manera estratégica! 🔥
