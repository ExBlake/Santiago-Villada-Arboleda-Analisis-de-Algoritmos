# Laboratorio evaluativo 1. Fundamentos, complejidad y recurrencias

**Autor:** SANTIAGO VILLADA ARBOLEDA

## Cómo reproducir el experimento

Desde la raíz del repositorio activo el entorno virtual (con `matplotlib` instalado, ver `requirements.txt`) y entro a la carpeta del laboratorio:

```bash
# Windows
env\Scripts\activate
# Mac / Linux
source env/bin/activate

pip install -r requirements.txt

cd laboratorios/lab1-fundamentos-complejidad-recurrencias
python parte3_casos.py        # Parte 3: genera graficas/parte3_comparaciones.png y graficas/parte3_tiempo.png
python parte4_complejidad.py  # Parte 4: genera graficas/parte4_tiempo.png e imprime los tiempos medidos
```

Las gráficas siempre quedan guardadas en la carpeta [graficas/](graficas/) de este laboratorio. Los datos los genero con una semilla fija (`42`), entonces cada vez que se corre salen los mismos lotes; lo único que puede cambiar un poquito son los tiempos, dependiendo del computador.

**Código del laboratorio:**

- [algoritmos.py](algoritmos.py): aquí están `insertion_sort` y `merge_sort`, y los dos cuentan las comparaciones entre elementos.
- [datos.py](datos.py): aquí están los generadores de los escenarios A (aleatorio), B (casi ordenado) y C (inverso).
- [parte3_casos.py](parte3_casos.py): la medición y las gráficas de la Parte 3.
- [parte4_complejidad.py](parte4_complejidad.py): la medición y la gráfica de la Parte 4.

**Sentido del orden:** quiero aclarar que mis dos algoritmos ordenan de forma **ascendente**, o sea, de menor a mayor índice de riesgo. Como Tamiza necesita la lista de **mayor a menor**, en producción solo habría que darle la vuelta al resultado (`ordenada[::-1]`). Eso cuesta Θ(n) extra, pero no cambia ni el número de comparaciones ni la complejidad de ninguno de los dos.

## Parte 1. Analizar el algoritmo antes de comprar hardware

Antes de comprar un servidor con el doble de velocidad, es necesario analizar primero el algoritmo que utiliza actualmente Tamiza. El hecho de que **insertion sort** lleve ocho años funcionando y entregue correctamente los registros no significa que siga siendo adecuado para la cantidad de información que maneja actualmente la plataforma.

En este caso hay que diferenciar entre dos cosas:

- **Corrección**: un algoritmo es correcto cuando nos da el resultado que esperamos; en el caso de Tamiza, esto significa ordenar los pacientes de mayor a menor según su índice de riesgo.
- **Eficiencia**: además de ser correcto, el algoritmo debe hacerlo utilizando los recursos disponibles y **dentro de la restricción establecida**. Actualmente, esa restricción es la ventana de **4 horas**, entre las 2:00 a. m. y las 6:00 a. m., y el sistema ya la está incumpliendo.

El principal problema de mantener insertion sort es que su comportamiento puede crecer demasiado cuando aumenta la cantidad de registros. Por ejemplo, en el caso de Tamiza pasó de trabajar con aproximadamente **20.000 registros** a tener **1.200.000**. Entonces, no estamos frente al mismo problema que existía hace ocho años. Duplicar la velocidad del servidor podría reducir el tiempo de ejecución, pero **no cambia la forma en que el algoritmo crece** cuando aumenta la cantidad de datos.

En el caso que propone el enunciado, se estaría intentando solucionar un problema del software aumentando la capacidad del hardware. Si los datos continúan creciendo, el problema volverá a aparecer, por lo que esta solución sería simplemente **a corto plazo y no a largo plazo**.

**Ejemplo propio:** en una empresa en la cual estuve hace ya un tiempo, tenían un algoritmo para detectar imágenes de algunas facturas.

- Se procesaban entre **1.500 y 3.000 imágenes al día**, dependiendo de la temporada.
- El algoritmo, programado por nosotros, se demoraba entre **2 y 3 horas** en analizarlas, principalmente porque algunas imágenes eran borrosas o difíciles de leer.
- La empresa necesitaba que el sistema entregara los resultados en **menos de una hora** para que los usuarios pudieran continuar con el proceso.

Aunque el algoritmo encontraba correctamente los resultados, no era viable para esa situación porque incumplía la restricción de tiempo. En ese caso tampoco tendría mucho sentido depender únicamente de comprar un equipo más rápido si el algoritmo utilizado no escala bien con el aumento de información. Al final, nos dimos cuenta de que era un problema del algoritmo, ya que tenía mucha redundancia y una mala codificación, por eso es importante revisar el algoritmo y los recursos que usa.

**¿Por qué no escalaba?** Ya mirándolo bien, el tiempo total era básicamente *cantidad de imágenes x lo que se demoraba cada imagen*, y el problema era que cada imagen ya se demoraba demasiado, entonces cuando llegaban más imágenes el tiempo total se iba muy arriba:

- **Crecía:** la cantidad de imágenes del día, que en temporada alta se duplicaba (de 1.500 a 3.000), y el tiempo total subía con ella (de unas 2 horas a unas 3 horas).
- **Por qué cada imagen se demoraba tanto:** como dije, algunas imágenes eran borrosas o difíciles de leer, y además el código tenía mucha redundancia y mala codificación. Con 1.500 imágenes en 2 horas eran más o menos 4,8 s por imagen, y con 3.000 en 3 horas más o menos 3,6 s por imagen. Para que 3.000 imágenes salieran en menos de una hora, cada una tenía que demorarse como 1,2 s, o sea, unas 3 veces menos de lo que se demoraba.
- **Por qué el hardware no era suficiente:** un equipo el doble de rápido solo parte el tiempo a la mitad (de 2–3 h quedaría en 1–1,5 h), y aun así no cumplía la hora. Lo que de verdad servía era corregir la redundancia y la mala codificación del algoritmo, porque eso baja justo lo que se demora cada imagen, que es lo que se multiplica por la cantidad de imágenes.

Realmente considero que se debe evaluar y analizar minuciosamente el algoritmo y buscar estrategias que permitan hacer un mejor uso de los recursos del hardware. También se deben analizar otros tipos de algoritmos, como **merge sort**, que puede ser una alternativa para mejorar mucho el comportamiento del ordenamiento cuando aumenta la cantidad de datos. Por ende, Tamiza podría procesar los 1.200.000 registros dentro de la ventana de cuatro horas sin depender solamente de comprar un servidor más potente.

## Parte 2. Responsabilidad ambiental y ética de la implementación

Considero que escoger el algoritmo que va a utilizar Tamiza no es solamente una decisión sobre qué tan rápido funciona el sistema. También tiene consecuencias **ambientales** y **éticas**, especialmente porque estamos hablando de una plataforma relacionada con la salud de las personas y que trabaja todas las madrugadas con información de 1.200.000 pacientes. Por esto, considero que es un tema mucho más delicado que simplemente ordenar una lista de datos.

### Dimensión ambiental

Mientras más tiempo tarde el proceso, más tiempo tiene que estar trabajando el servidor y, por lo tanto, **se utiliza más energía**. Puede que en una sola madrugada la diferencia no parezca tan importante, pero Tamiza realiza este proceso **todos los días**. Si durante meses o años se mantiene un algoritmo que tarda mucho más de lo necesario, ese consumo adicional se va acumulando. Por eso, mejorar el algoritmo también puede ayudar a utilizar mejor los recursos y evitar un gasto de energía que realmente se podría reducir.

**Estimación aproximada.** Para ponerle números, usé los tiempos que medí en la Parte 4 (el cálculo está en la 4.3). Extrapolando, en Python y en mi computador, insertion sort se demoraría unas **8 horas** cada madrugada con 1.200.000 registros desordenados (y unas 16 horas en el peor caso), mientras que merge sort se demoraría unos **4 segundos**. Voy a suponer que el servidor consume más o menos **400 W** mientras trabaja (esto es un supuesto mío, no es un dato de Tamiza):

| | Tiempo por noche (estimado) | Energía por noche | Energía al año (365 noches) |
|---|---:|---:|---:|
| Insertion sort (caso promedio) | ≈ 8,2 h | ≈ 3,3 kWh | ≈ 1.200 kWh |
| Merge sort | ≈ 4 s | ≈ 0,0004 kWh | ≈ 0,15 kWh |

O sea, solo por ordenar la lista se estarían gastando alrededor de **1.200 kWh al año** que se podrían ahorrar. Si uso un factor aproximado de 0,13 kg de CO₂ por kWh para la red eléctrica de Colombia, eso serían unos **150 kg de CO₂ al año**. Obviamente son cifras aproximadas, porque dependen del servidor real, del lenguaje y de cuánto gaste el equipo cuando está quieto, pero sí dejan ver qué tan grande es la diferencia.

### Dimensión ética

Desde el punto de vista ético, considero que el problema es todavía más importante porque estamos hablando de salud. Un error en el orden de los pacientes no es simplemente que una información aparezca en un lugar equivocado.

1. **El paciente.** Por ejemplo, un paciente que tenga un índice de riesgo alto podría quedar por fuera de la lista o ser contactado después de otros pacientes si el proceso no termina a tiempo. Esto podría retrasar su valoración médica. Quien recibe directamente las consecuencias es el paciente, pero también existe una responsabilidad por parte de la Secretaría y del equipo encargado del sistema, porque son quienes deben garantizar que la información se procese correctamente.
2. **El operador del centro de contacto.** Si recibe una lista incompleta o mal ordenada, tendrá que trabajar con información que no muestra correctamente cuáles pacientes deberían ser contactados primero, lo que puede generar más trabajo, reprocesos y presión para los operadores. Por eso, el operador termina asumiendo parte de las consecuencias del error, aunque el problema realmente se origine en el funcionamiento del sistema.

### Una tensión adicional

Además, hay algo que considero todavía más importante: como Tamiza está relacionada con el sector de la salud, el ordenamiento de los datos debe ser **muy preciso**, especialmente al momento de definir qué pacientes tienen mayor prioridad. En la salud, muchas veces el tiempo puede ser muy importante e incluso puede representar una diferencia en la atención de una persona. Por eso, se debe garantizar que el ordenamiento sea correcto y preciso, para evitar que un error en el sistema pueda afectar a un paciente.

Pero la verdad, la tensión no es solo que sea preciso: **el orden de la lista es el que decide a quién se llama primero**. Como el centro de contacto no alcanza a llamar a todo el mundo en un mismo día, el puesto en el que queda cada paciente termina siendo, en la práctica, una decisión de quién se atiende primero. Entonces ordenar ya no es algo puramente técnico, sino que es repartir algo que no alcanza para todos (las llamadas) entre personas. Y eso, para mí, le agrega obligaciones a la Secretaría y a nosotros, que somos los que hacemos el sistema:

- **Poder explicar y revisar el orden:** cualquier paciente o funcionario debería poder saber por qué alguien quedó antes que otro (el criterio tiene que ser el índice de riesgo y nada más), y debería quedar un registro de cada lista que se genera.
- **Manejar los empates de forma justa:** cuando dos pacientes tienen el mismo índice, el desempate no puede quedar a la suerte del algoritmo. Hay que definir un criterio (por ejemplo, quién lleva más tiempo esperando) y usar un ordenamiento estable que lo respete. Merge sort e insertion sort son estables, entonces sí mantienen ese criterio.
- **Asegurar que la lista llegue completa y a tiempo:** si el proceso no termina dentro de la ventana, la lista puede quedar incompleta sin que nadie se dé cuenta. Por eso tiene que haber una verificación de que todos los registros quedaron ordenados y un plan B por si algo falla.

## Parte 3. Peor caso, mejor caso y caso promedio, demostrados en Python
 
### 3.1 Explicación
 
| Caso | Explicación |
|---|---|
| **Peor caso** | Es cuando tenemos una cantidad fija de datos y estos están organizados de la forma que más trabajo le genera al algoritmo. Es decir, de todas las entradas que tienen el mismo tamaño, buscamos la que hace que el algoritmo tarde más o haga más operaciones. |
| **Mejor caso** | Es lo contrario al peor caso. Tenemos la misma cantidad fija de datos, pero están organizados de una forma que hace que el algoritmo tenga que trabajar lo menos posible. De todas las entradas de tamaño, sería la que menos tiempo o menos operaciones necesita. |
| **Caso promedio** | Es una forma de saber cómo se comportaría normalmente el algoritmo. Para una cantidad fija de datos, se toma el comportamiento de diferentes entradas y se calcula un promedio entre ellas. |
 
**Caso que utilizaría en Tamiza**
 
Para Tamiza utilizaría el peor caso para decidir si el algoritmo puede entrar en producción. Esto se debe a que tenemos una condición muy clara: los 1.200.000 registros deben ser procesados entre las 2:00 a. m. y las 6:00 a. m., por lo que solamente tenemos cuatro horas.
 
Si solamente analizamos el promedio, podría pasar que normalmente el algoritmo termine a tiempo, pero que cuando los datos estén organizados de una forma más complicada se demore demasiado y no alcance a terminar dentro de las cuatro horas.
 
Por eso considero que lo más seguro es revisar el peor escenario y comprobar que, aun en esa situación, el algoritmo pueda procesar los datos dentro del tiempo disponible. Esto es todavía más importante porque Tamiza trabaja con información relacionada con la salud de las personas.
 
**Predicción antes de realizar el experimento**
 
| Escenario | Predicción |
|---|---|
| **A. Aleatorio** | sería el caso promedio, porque los datos están mezclados y no están ni completamente ordenados ni completamente al contrario. |
| **B. Casi ordenado** | sería el mejor caso, porque el 98% de los datos ya están ordenados y el algoritmo tendría que hacer poco trabajo. |
| **C. Inverso** | sería el peor caso, porque los datos están completamente al contrario del orden que se necesita y, por lo tanto, Insertion Sort tendría que trabajar mucho más. |
 
### 3.2 Demostración experimental
 
**Comparaciones vs. tamaño de entrada:**
 
![Comparaciones de insertion sort en los tres escenarios](graficas/parte3_comparaciones.png)
 
**Tiempo de ejecución vs. tamaño de entrada:**
 
![Tiempo de ejecucion de insertion sort en los tres escenarios](graficas/parte3_tiempo.png)
 
Al ver las gráficas, el escenario C (orden inverso) fue el que más le costó al algoritmo: entre más registros había, más se disparaba tanto el número de comparaciones como el tiempo, así que ese fue el peor caso. El escenario B (casi ordenado) fue justo lo contrario: casi no le costó trabajo sin importar cuántos registros tuviera, porque casi todo ya venía en orden. El escenario A (aleatorio) quedó siempre en un punto intermedio entre los otros dos, ni tan rápido como B ni tan lento como C.

Estos son los valores que medí (son los mismos de las gráficas de arriba):

| n | Comparaciones A (aleatorio) | Comparaciones B (casi ordenado) | Comparaciones C (inverso) | Tiempo A | Tiempo B | Tiempo C |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 2.597 | 100 | 4.950 | 0,2 ms | < 0,1 ms | 0,4 ms |
| 800 | 160.699 | 866 | 319.600 | 13,1 ms | 0,1 ms | 26,3 ms |
| 3.200 | 2.591.685 | 4.172 | 5.118.400 | 0,21 s | 0,4 ms | 0,41 s |
| 6.400 | 10.212.819 | 10.277 | 20.476.800 | 0,84 s | 1,0 ms | 1,67 s |

- En **C**, las comparaciones dan exactamente n(n − 1)/2 (con n = 6.400: 6.400 · 6.399 / 2 = 20.476.800). Además, cuando duplico n de 3.200 a 6.400, tanto las comparaciones como el tiempo se multiplican casi por 4 (5,1 M → 20,5 M; 0,41 s → 1,67 s), que es justo lo que uno espera de algo cuadrático.
- En **A**, las comparaciones son más o menos la mitad de las de C (10,2 M contra 20,5 M con n = 6.400, cerca de n²/4), y también se multiplican por casi 4 al duplicar n. O sea, sigue siendo cuadrático, solo que hace la mitad del trabajo.
- En **B**, las comparaciones son apenas un poquito más que n (10.277 con n = 6.400) y el tiempo se queda alrededor de 1 ms. Aquí al duplicar n el trabajo solo se duplica, como pasa con algo lineal.
 
Esto coincide exactamente con lo que se había predicho antes de hacer las pruebas: que C sería el peor caso, B el mejor y A se comportaría como algo intermedio o normal. Como el resultado no contradijo la predicción, no hay nada que explicar o justificar de forma distinta; simplemente se confirmó lo que se esperaba.

## Parte 4. Complejidad de merge sort e insertion sort: cálculo y validación

## 4.1 Cálculo teórico

### Merge Sort

Merge Sort funciona dividiendo una lista en partes cada vez más pequeñas. Si tenemos una lista de tamaño `n`, primero la divide en **dos partes de aproximadamente `n/2` elementos**. Luego vuelve a hacer lo mismo con cada una de esas partes hasta llegar a listas pequeñas que se puedan ordenar fácilmente.

Por eso tenemos:

```text
T(n) = 2T(n/2) + Θ(n)
```

El primer término:

```text
2T(n/2)
```

Significa que tenemos **2 subproblemas**, y cada uno tiene aproximadamente la mitad de los datos originales.

Después de ordenar las dos partes, hay que volver a unirlas en una sola lista ordenada. Esta parte la realiza `merge`, que va comparando los elementos de las dos partes y los va colocando en el orden correcto. Como tiene que recorrer los elementos para hacer esta unión, el costo de esta parte depende de `n`:

```text
Θ(n)
```

Por eso la recurrencia completa queda asi:

```text
T(n) = 2T(n/2) + Θ(n)
```

---

### Método maestro

Para resolver la recurrencia en mi caso voy a usar el **método maestro**.

Primero identificamos los valores de la fórmula:

```text
T(n) = aT(n/b) + f(n)
```

En nuestro caso:

```text
a = 2
b = 2
f(n) = Θ(n)
```

El `2` de `a` aparece porque Merge Sort se divide en dos partes, y el `2` de `b` aparece porque cada parte tiene `n/2` elementos.

Ahora calculamos:

```text
n^(log_b a)

= n^(log₂ 2)

= n¹

= n
```

Entonces tenemos:

```text
f(n) = Θ(n)
```

y:

```text
n^(log_b a) = Θ(n)
```

Los dos tienen el mismo orden de crecimiento. Por lo tanto, se cumple la condición del **caso 2 del método maestro**.

Aplicando este caso:

```text
T(n) = Θ(n log n)
```

Por lo tanto, la complejidad de **Merge Sort** es:

```text
Θ(n log n)
```

Esto quiere decir que aunque la cantidad de datos aumente, el crecimiento del algoritmo es más controlado.

---

### Insertion Sort

```python
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    arreglo = datos.copy()
    comparaciones = 0
    n = len(arreglo)

    for i in range(1, n):
        clave = arreglo[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1
            if arreglo[j] <= clave:
                break
            arreglo[j + 1] = arreglo[j]
            j -= 1

        arreglo[j + 1] = clave

    return arreglo, comparaciones
```

#### Revisando cada línea

| Línea                           | Cantidad aproximada de ejecuciones | Explicación                                                           |
| ------------------------------- | ---------------------------------: | --------------------------------------------------------------------- |
| `arreglo = datos.copy()`        |                                  1 | Se hace una sola copia de la lista.                                   |
| `comparaciones = 0`             |                                  1 | Se inicializa el contador una sola vez.                               |
| `n = len(arreglo)`              |                                  1 | Se obtiene el tamaño una sola vez.                                    |
| `for i in range(1, n)`          |                `n - 1` iteraciones | Se recorre la lista desde el segundo elemento hasta el último.        |
| `clave = arreglo[i]`            |                            `n - 1` | Se toma una vez por cada elemento que se va a insertar.               |
| `j = i - 1`                     |                            `n - 1` | Se ejecuta una vez por cada vuelta del `for`.                         |
| `while j >= 0`                  |          `Σ (tᵢ + 1)` (como máximo) | Es la parte que más cambia según cómo estén organizados los datos.    |
| `comparaciones += 1`            |                            `Σ cᵢ` | Cuenta cada comparación entre elementos.                              |
| `if arreglo[j] <= clave`        |                            `Σ cᵢ` | Se revisa cada vez que se compara un elemento.                        |
| `arreglo[j + 1] = arreglo[j]`   |                            `Σ tᵢ` | Solo se ejecuta cuando es necesario mover un elemento.                |
| `j -= 1`                        |                            `Σ tᵢ` | Se ejecuta cada vez que el elemento debe seguir buscando su posición. |
| `arreglo[j + 1] = clave`        |                            `n - 1` | Se coloca cada elemento en su posición.                               |
| `return arreglo, comparaciones` |                                  1 | Se devuelve el resultado una sola vez.                                |

Todas las sumas `Σ` van desde `i = 1` hasta `i = n − 1`, y uso estas dos letras:

- `tᵢ` es la cantidad de elementos que toca **correr** para meter `arreglo[i]` en su lugar (o sea, los elementos de antes que son mayores que la clave). Siempre pasa que `0 ≤ tᵢ ≤ i`.
- `cᵢ` es la cantidad de **comparaciones** en la vuelta `i`. Vale `tᵢ + 1` si el ciclo se sale por el `break`, o `tᵢ` si se sale porque `j` llegó a `−1`. En cualquier caso, `tᵢ ≤ cᵢ ≤ tᵢ + 1`.

#### Sumando los costos

Si digo que cada línea tiene un costo constante `c₁, c₂, …`, el tiempo total es sumar (lo que cuesta la línea × las veces que se ejecuta):

```text
T(n) = c₁·1 + c₂·1 + c₃·1                      (copia*, contador, len)
     + c₄·(n − 1) + c₅·(n − 1) + c₆·(n − 1)    (for, clave, j = i − 1)
     + c₇·Σ(tᵢ + 1) + c₈·Σcᵢ + c₉·Σcᵢ          (while, contador, if)
     + c₁₀·Σtᵢ + c₁₁·Σtᵢ                       (desplazamiento, j -= 1)
     + c₁₂·(n − 1) + c₁₃·1                     (colocar clave, return)
```

\* La copia `datos.copy()` en realidad cuesta Θ(n), pero como se hace una sola vez no cambia el resultado final.

Como `cᵢ` siempre queda entre `tᵢ` y `tᵢ + 1`, todo esto se puede agrupar en dos partes:

```text
T(n) = a·n + b·Σ tᵢ + d        (a, b, d constantes positivas)
```

O sea, **insertion sort cuesta Θ(n + Σ tᵢ)**: una parte lineal que siempre está (recorrer los n − 1 elementos) más todos los desplazamientos. Lo único que depende de cómo vengan los datos es `Σ tᵢ`, que es justamente el número de **inversiones** de la entrada (las parejas de elementos que están en el orden equivocado). Con esa fórmula me salen los tres casos:

| Caso | Valor de `tᵢ` | `Σ tᵢ` | `T(n)` |
|---|---|---|---|
| Mejor (ya ordenado) | `0` | `0` | `a·n + d = Θ(n)` |
| Peor (orden inverso) | `i` | `1 + 2 + … + (n − 1) = n(n − 1)/2` | `a·n + b·n(n − 1)/2 + d = Θ(n²)` |
| Promedio (aleatorio) | `i/2` en promedio | `≈ n(n − 1)/4` | `a·n + b·n(n − 1)/4 + d = Θ(n²)` |

Las primeras líneas tienen un costo que no cambia demasiado aunque aumentemos la cantidad de datos. También hay varias líneas que se ejecutan una vez por cada elemento.

La parte que realmente cambia el comportamiento de Insertion Sort es el `while`, porque depende de **cómo estén organizados los datos**, es decir, de `Σ tᵢ`.

---

### Mejor caso de Insertion Sort

El mejor caso ocurre cuando los datos ya están ordenados.

Por ejemplo:

```text
[1, 2, 3, 4, 5]
```

En este caso, cada elemento se compara con el anterior y rápidamente se encuentra que ya está en la posición correcta.

Para una lista de tamaño `n`, se hacen aproximadamente:

```text
n - 1 comparaciones
```

No es necesario hacer desplazamientos importantes de los elementos.

Por lo tanto:

```text
T(n) = Θ(n)
```

**Mejor caso: Θ(n)**

---

### Peor caso de Insertion Sort

El peor caso ocurre cuando los datos están completamente al contrario del orden que necesitamos.

Por ejemplo:

```text
[5, 4, 3, 2, 1]
```

En este caso, cada nuevo elemento tiene que compararse con todos los elementos que ya están antes de él.

Las comparaciones serían aproximadamente:

```text
1 + 2 + 3 + ... + (n - 1)
```

Esta suma se puede escribir como:

```text
n(n - 1) / 2
```

Desarrollando:

```text
(n² - n) / 2
```

El término que más crece es `n²`, por lo que:

```text
T(n) = Θ(n²)
```

Además, en este caso también se realizan muchos desplazamientos:

```python
arreglo[j + 1] = arreglo[j]
```

Por eso el algoritmo tiene un crecimiento cuadrático.

**Peor caso: Θ(n²)**

---

### Caso promedio de Insertion Sort

El caso promedio se presenta cuando los datos están desordenados, pero no completamente al contrario.

En este caso, algunos elementos estarán cerca de su posición y otros tendrán que moverse más. Por eso el número de comparaciones y desplazamientos queda entre el mejor y el peor caso.

Aunque el trabajo sea menor que en el peor caso, a medida que `n` aumenta el crecimiento sigue siendo cuadrático. Lo justifico así:

1. Cuando voy a meter el elemento `arreglo[i]`, antes de él ya hay `i` elementos ordenados. Si los datos vienen en orden aleatorio, la clave puede caer con la misma probabilidad en cualquiera de las `i + 1` posiciones, entonces **en promedio es mayor que la mitad de ellos y menor que la otra mitad**.
2. Por eso, en promedio toca correr la mitad de los elementos de antes: `tᵢ ≈ i/2`.
3. Sumando todas las vueltas:

```text
Σ tᵢ ≈ (1/2)·(1 + 2 + … + (n − 1)) = (1/2)·n(n − 1)/2 = n(n − 1)/4
```

4. Reemplazando en `T(n) = a·n + b·Σ tᵢ + d`:

```text
T(n) ≈ a·n + b·n(n − 1)/4 + d = (b/4)·n² + …
```

El término que manda sigue siendo `n²`; lo único que cambia es la constante (`1/4` en vez del `1/2` del peor caso). Hacer la mitad del trabajo no cambia la forma en que crece, por eso:

```text
T(n) = Θ(n²)
```

Y esto se ve en lo que medí en la Parte 3: con n = 6.400 el escenario aleatorio hizo 10.212.819 comparaciones, muy cerca de n²/4 = 10.240.000, o sea, casi exactamente la mitad de las 20.476.800 del orden inverso.

**Caso promedio: Θ(n²)**

---

### Complejidad esperada

| Algoritmo          | Mejor caso | Caso promedio |  Peor caso |
| ------------------ | ---------: | ------------: | ---------: |
| **Insertion Sort** |       Θ(n) |         Θ(n²) |      Θ(n²) |
| **Merge Sort**     | Θ(n log n) |    Θ(n log n) | Θ(n log n) |

Entonces, **Insertion Sort depende mucho de cómo estén organizados los datos**. Cuando ya están ordenados puede funcionar muy bien, pero cuando la cantidad de datos aumenta y están desordenados, su crecimiento puede ser bastante grande.

Merge Sort, en cambio, mantiene **Θ(n log n)** en los tres casos, ya que siempre divide los datos y después los vuelve a combinar. Esto hace que se espere un comportamiento más estable cuando aumenta la cantidad de registros.

### 4.2 Validación experimental
 
Al observar la gráfica, podemos ver que Merge Sort es mejor para Tamiza, especialmente cuando aumenta la cantidad de registros. En tamaños pequeños la diferencia entre los dos algoritmos no es tan grande, pero a medida que aumenta el tamaño de la entrada, Insertion Sort crece mucho más rápido, mientras que Merge Sort mantiene una curva más controlada. Esto es importante para Tamiza porque debe procesar alrededor de 1.200.000 registros de pacientes dentro de una ventana de cuatro horas, por lo que utilizar un algoritmo que tenga un mejor comportamiento cuando aumentan los datos es una opción más adecuada.

El resultado de la gráfica coincide con lo calculado en la Parte 4.1. Insertion Sort tiene una complejidad promedio y de peor caso de Θ(n²), mientras que Merge Sort tiene una complejidad de Θ(n log n). En los tamaños pequeños puede haber poca diferencia entre ambos debido a factores del equipo y del tiempo de ejecución, pero cuando aumenta la cantidad de datos la diferencia se hace mucho más evidente. Por esto, según los resultados obtenidos en la gráfica, Merge Sort sería la mejor opción para Tamiza.

**Merge Sort vs. Insertion Sort:**

![Tiempo de ejecución de insertion sort y merge sort con datos aleatorios para n de 100 a 6.400](graficas/parte4_tiempo.png)

Para esta gráfica usé los mismos tamaños de la Parte 3 (de 100 a 6.400) y el escenario aleatorio (A). Estos son los valores que medí con [parte4_complejidad.py](parte4_complejidad.py) (tomando el mínimo de 3 repeticiones):

| n | Insertion sort | Merge sort | Insertion / Merge |
|---:|---:|---:|---:|
| 100 | 0,20 ms | 0,12 ms | ≈ 1,7× |
| 200 | 0,80 ms | 0,25 ms | ≈ 3,2× |
| 400 | 3,1 ms | 0,58 ms | ≈ 5,4× |
| 800 | 13,0 ms | 1,3 ms | ≈ 10× |
| 1.600 | 51,3 ms | 2,7 ms | ≈ 19× |
| 3.200 | 0,211 s | 5,8 ms | ≈ 37× |
| 6.400 | 0,837 s | 12,3 ms | ≈ 68× |

**Tamaños pequeños.** Con n = 100 la diferencia es mínima: 0,20 ms contra 0,12 ms, menos de una décima de milisegundo, y en la gráfica las dos curvas se ven pegadas al cero. Esto pasa porque con tan pocos datos n² y n log n todavía dan números parecidos, y además merge sort tiene unos costos extra que insertion sort no tiene (las llamadas recursivas, crear las sublistas con `arreglo[:mitad]` y la lista `resultado`). Entonces, para listas muy pequeñas insertion sort funciona bastante bien, y por eso muchas implementaciones reales lo usan para los pedacitos pequeños dentro de un algoritmo más rápido.

**Tamaños grandes.** Ya desde n = 800 merge sort es 10 veces más rápido, y cada vez que n se duplica la diferencia casi se duplica también: de 3.200 a 6.400, insertion sort pasó de 0,211 s a 0,837 s (casi ×4, cuadrático), mientras que merge sort pasó de 5,8 ms a 12,3 ms (como ×2,1, un poquito más que lineal, que es lo que da n log n). Esto es justo lo que dicen Θ(n²) y Θ(n log n) de la Parte 4.1.

### 4.3 Concepto técnico

**Recomendación.** Mi recomendación para la Secretaría es **cambiar insertion sort por merge sort** en el proceso de la madrugada de Tamiza, y hacerlo **antes** de pensar en comprar el servidor.

**¿Sirve de algo comprar un servidor el doble de rápido?** La verdad, no soluciona el problema. Con lo que medí puedo estimar cuánto se demoraría cada algoritmo con 1.200.000 registros. Eso sí, **esto es una extrapolación, no una medición**: estoy suponiendo que el crecimiento sigue igual que en mis mediciones, y son tiempos de Python en mi computador, no en el servidor de Tamiza.

- **Insertion sort (caso promedio):** si T(n) crece como n², el tiempo con 1.200.000 registros es el que medí con 6.400 multiplicado por (1.200.000 / 6.400)² = 187,5² ≈ 35.156:

  ```text
  0,837 s × 35.156 ≈ 29.400 s ≈ 8,2 horas
  ```

  En el peor caso (orden inverso, que en la Parte 3 dio 1,67 s con n = 6.400) serían unos 58.600 s, o sea, **16,3 horas**.

- **Con un servidor el doble de rápido:** los tiempos se parten a la mitad y quedan en unas **4,1 horas** en el caso promedio y unas **8,1 horas** en el peor caso. Los dos siguen **pasándose de la ventana de 4 horas**. Y como el crecimiento es cuadrático, con que los registros crezcan apenas un 42 % (√2 ≈ 1,41) el tiempo se vuelve a duplicar y se pierde todo lo que se ganó con la compra.

- **Merge sort:** si T(n) crece como n log n, el factor por el que hay que multiplicar es (1.200.000 · log₂ 1.200.000) / (6.400 · log₂ 6.400) ≈ 187,5 × (20,2 / 12,6) ≈ 300:

  ```text
  12,3 ms × 300 ≈ 3,7 s
  ```

  O sea, unos **4 segundos** con el servidor que ya tienen, sin comprar nada, y con muchísimo margen frente a las 4 horas aunque los registros sigan creciendo.

**Otras cosas a tener en cuenta:**

- **Memoria:** merge sort no ordena "en el mismo lugar"; necesita memoria extra Θ(n) para las sublistas y para unirlas, mientras que insertion sort solo necesita Θ(1) extra. Con 1.200.000 registros esto se puede manejar (estamos hablando de decenas de MB si se guardan los registros completos o referencias a ellos), pero toca verificar que el servidor tenga esa memoria libre durante la ventana.
- **Estabilidad:** merge sort, como lo implementé (con `<=` al unir), es **estable**: si dos pacientes tienen el mismo índice de riesgo, quedan en el mismo orden en que llegaron. Para Tamiza esto es importante porque deja definir un criterio de desempate justo y que no cambie (lo de la tensión ética de la Parte 2). Eso sí, si se quiere conservar ese desempate, es mejor ordenar directamente de mayor a menor (cambiando la comparación) en vez de darle la vuelta a la lista al final.
- **Que sea predecible:** merge sort es Θ(n log n) en el mejor, en el promedio y en el peor caso, entonces su tiempo no depende de cómo lleguen los datos. Insertion sort solo es rápido si los datos ya vienen casi ordenados, y eso Tamiza no lo puede garantizar.