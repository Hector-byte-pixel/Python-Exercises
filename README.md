# Tres meses o nada — Python

Repositorio de ejercicios y apuntes del reto de tres meses de Python.

| Día | Tema | Tipo | Estado |
|-----|------|------|--------|
| [D1](#día-1--el-entorno-de-python) | Intérprete, PATH, venv y dependencias | Teoría (no evaluable) | ✅ Resuelto |

---

## Día 1 — El entorno de Python

> **Enunciado:** Cómo se ejecuta Python: intérprete, PATH, entornos virtuales (`venv`)
> y gestión de dependencias con `pip`, `requirements` y `pyproject.toml`.
> `Python · D1 · no evaluable`

### 1. El intérprete

El intérprete es el programa que **lee y ejecuta** el código Python. No compilamos a un
binario: el código fuente (`.py`) se traduce a *bytecode* (`.pyc`, cacheado en
`__pycache__/`) y una máquina virtual lo ejecuta.

Localizarlo y comprobar la versión en Linux:

```bash
which python3          # /usr/bin/python3  → ruta del ejecutable
which -a python3       # todas las coincidencias en el PATH, en orden
python3 --version      # Python 3.12.3
python3 -c "import sys; print(sys.executable)"   # el intérprete que se está usando ahora
```

> **Nota (Debian/Ubuntu):** solo existe `python3`. El comando `python` a secas no está
> disponible salvo que instales `python-is-python3` o actives un entorno virtual, que sí
> crea el alias `python` dentro del entorno.

Formas de ejecutar código:

```bash
python3 script.py           # ejecuta un archivo
python3 -m modulo           # ejecuta un módulo instalado (recomendado para pip, venv, http.server…)
python3 -c "print('hola')"  # ejecuta una expresión suelta
python3                     # REPL interactivo (salir con exit() o Ctrl+D)
```

### 2. PATH

`PATH` es una variable de entorno con una **lista de directorios separados por `:`** donde
el shell busca los ejecutables. Se recorre de izquierda a derecha y gana la primera
coincidencia — por eso el orden importa.

```bash
echo $PATH                    # ver el contenido
tr ':' '\n' <<< "$PATH"       # verlo en una línea por directorio, más legible
export PATH="/ruta/nueva:$PATH"   # anteponer un directorio (tiene prioridad)
export PATH="$PATH:/ruta/nueva"   # añadirlo al final (menor prioridad)
```

`export` solo afecta a la sesión actual. Para hacerlo permanente hay que añadir la línea
a `~/.bashrc` (o `~/.profile`) y recargar con `source ~/.bashrc`.

**Relación con los entornos virtuales:** activar un `venv` no hace magia — simplemente
antepone el directorio `bin/` del entorno al `PATH`, de modo que `python` y `pip` pasan a
resolverse dentro del entorno.

```bash
echo $PATH        # /home/hector/proyecto/.venv/bin:/usr/local/bin:/usr/bin:...
which python      # /home/hector/proyecto/.venv/bin/python
```

### 3. Entornos virtuales (`venv`)

Un entorno virtual es un directorio aislado con su propio intérprete y sus propios
paquetes. Sirve para que **cada proyecto tenga sus dependencias y versiones** sin
contaminar el Python del sistema (que en Linux usa el propio sistema operativo, y romperlo
es un problema real).

```bash
python3 -m venv .venv        # crear el entorno en la carpeta .venv
source .venv/bin/activate    # activar  (el prompt pasa a mostrar (.venv))
deactivate                   # desactivar
rm -rf .venv                 # eliminarlo: es desechable, se recrea cuando haga falta
```

Comprobar que estás dentro del entorno:

```bash
which python                 # debe apuntar a .venv/bin/python
python -c "import sys; print(sys.prefix)"
```

Buenas prácticas:

- Un entorno por proyecto, en la raíz, llamado `.venv`.
- **Nunca** se sube al repositorio: se añade `.venv/` al `.gitignore`.
- Lo que sí se versiona es la *lista* de dependencias (`requirements.txt` / `pyproject.toml`).

### 4. `pip`: gestión de paquetes

Se recomienda invocarlo como `python -m pip` para garantizar que instalas en el intérprete
que crees, y no en otro que esté antes en el `PATH`.

| Acción | Comando |
|--------|---------|
| Instalar | `python -m pip install requests` |
| Instalar una versión concreta | `python -m pip install requests==2.32.3` |
| Instalar con rango de versión | `python -m pip install "requests>=2.30,<3.0"` |
| Actualizar | `python -m pip install --upgrade requests` |
| Desinstalar | `python -m pip uninstall requests` |
| Listar instalados | `python -m pip list` |
| Ver info de un paquete | `python -m pip show requests` |
| Ver paquetes obsoletos | `python -m pip list --outdated` |
| Versión de pip | `python -m pip --version` |

### 5. `requirements.txt`

Archivo de texto plano, una dependencia por línea. Es la forma clásica de **congelar y
reproducir** un entorno.

```bash
python -m pip freeze > requirements.txt      # generar desde el entorno actual
python -m pip install -r requirements.txt    # reinstalar en otra máquina
```

Ejemplo de contenido:

```text
requests==2.32.3
rich==13.7.1
```

`pip freeze` vuelca **todo** lo instalado con versiones exactas, incluidas las dependencias
transitivas. Es ideal para desplegar de forma reproducible, pero ruidoso como declaración
de intenciones: para eso está `pyproject.toml`.

### 6. `pyproject.toml`

Es el estándar actual (PEP 518 / PEP 621) para describir un proyecto Python: metadatos,
dependencias y configuración de herramientas, todo en un único archivo.

```toml
[project]
name = "python-ejercicios"
version = "0.1.0"
description = "Ejercicios del reto de tres meses de Python"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.32",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "ruff>=0.5",
]

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"
```

Instalar el proyecto en modo editable, con y sin extras de desarrollo:

```bash
python -m pip install -e .          # instala las dependencias de [project]
python -m pip install -e ".[dev]"   # además, las del grupo dev
```

**Diferencia clave:** `pyproject.toml` declara *qué necesita el proyecto* (rangos amplios,
escrito a mano); `requirements.txt` fija *qué se instaló exactamente* (versiones exactas,
generado). No son excluyentes: se usan juntos.

### Flujo completo de un proyecto nuevo

```bash
mkdir mi_proyecto && cd mi_proyecto
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install requests
python -m pip freeze > requirements.txt
echo ".venv/" >> .gitignore
```

### Conceptos clave del día

- El intérprete es un ejecutable más del sistema; `which` y `sys.executable` dicen cuál se usa.
- El `PATH` decide **qué** `python` se ejecuta, y los entornos virtuales funcionan
  manipulando ese `PATH`.
- Un `venv` aísla dependencias por proyecto; es desechable y no se versiona.
- `python -m pip` evita instalar en el intérprete equivocado.
- `requirements.txt` reproduce; `pyproject.toml` declara.
