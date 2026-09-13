# Laboratorio evaluativo 1. Fundamentos, complejidad y recurrencias

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

Realmente considero que se debe evaluar y analizar minuciosamente el algoritmo y buscar estrategias que permitan hacer un mejor uso de los recursos del hardware. También se deben analizar otros tipos de algoritmos, como **merge sort**, que puede ser una alternativa para mejorar mucho el comportamiento del ordenamiento cuando aumenta la cantidad de datos. Por ende, Tamiza podría procesar los 1.200.000 registros dentro de la ventana de cuatro horas sin depender solamente de comprar un servidor más potente.

## Parte 2. Responsabilidad ambiental y ética de la implementación

Considero que escoger el algoritmo que va a utilizar Tamiza no es solamente una decisión sobre qué tan rápido funciona el sistema. También tiene consecuencias **ambientales** y **éticas**, especialmente porque estamos hablando de una plataforma relacionada con la salud de las personas y que trabaja todas las madrugadas con información de 1.200.000 pacientes. Por esto, considero que es un tema mucho más delicado que simplemente ordenar una lista de datos.

### Dimensión ambiental

Mientras más tiempo tarde el proceso, más tiempo tiene que estar trabajando el servidor y, por lo tanto, **se utiliza más energía**. Puede que en una sola madrugada la diferencia no parezca tan importante, pero Tamiza realiza este proceso **todos los días**. Si durante meses o años se mantiene un algoritmo que tarda mucho más de lo necesario, ese consumo adicional se va acumulando. Por eso, mejorar el algoritmo también puede ayudar a utilizar mejor los recursos y evitar un gasto de energía que realmente se podría reducir.

### Dimensión ética

Desde el punto de vista ético, considero que el problema es todavía más importante porque estamos hablando de salud. Un error en el orden de los pacientes no es simplemente que una información aparezca en un lugar equivocado.

1. **El paciente.** Por ejemplo, un paciente que tenga un índice de riesgo alto podría quedar por fuera de la lista o ser contactado después de otros pacientes si el proceso no termina a tiempo. Esto podría retrasar su valoración médica. Quien recibe directamente las consecuencias es el paciente, pero también existe una responsabilidad por parte de la Secretaría y del equipo encargado del sistema, porque son quienes deben garantizar que la información se procese correctamente.
2. **El operador del centro de contacto.** Si recibe una lista incompleta o mal ordenada, tendrá que trabajar con información que no muestra correctamente cuáles pacientes deberían ser contactados primero, lo que puede generar más trabajo, reprocesos y presión para los operadores. Por eso, el operador termina asumiendo parte de las consecuencias del error, aunque el problema realmente se origine en el funcionamiento del sistema.

### Una tensión adicional

Además, hay algo que considero todavía más importante: como Tamiza está relacionada con el sector de la salud, el ordenamiento de los datos debe ser **muy preciso**, especialmente al momento de definir qué pacientes tienen mayor prioridad. En la salud, muchas veces el tiempo puede ser muy importante e incluso puede representar una diferencia en la atención de una persona. Por eso, se debe garantizar que el ordenamiento sea correcto y preciso, para evitar que un error en el sistema pueda afectar a un paciente.