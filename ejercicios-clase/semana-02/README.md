# Entorno virtual

El proyecto utiliza un único entorno virtual llamado `venv`, ubicado en la raíz del repositorio. Este entorno debe ser utilizado para instalar y ejecutar las dependencias de todos los ejercicios.

### Crear el entorno virtual

Desde la raíz del repositorio, ejecutar:

```powershell
python -m venv venv
```

### Activar el entorno virtual en Windows

En PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Una vez activado, se debe verificar que el prefijo `(venv)` aparezca al inicio de la terminal. Por ejemplo:

```text
(venv) PS C:\Users\usuario\Analisis de Algoritmos>
```

Esta verificación confirma que las siguientes instalaciones y comandos se ejecutarán dentro del entorno virtual del proyecto.

### Instalar dependencias

Con el entorno virtual activado, se pueden instalar las dependencias necesarias:

```powershell
pip install -r requirements.txt
```

**Importante:** El entorno virtual `venv` es único para todo el repositorio y debe estar ubicado en la raíz del proyecto. La carpeta `venv` **no debe crearse dentro de** `ejercicios-clase`.
