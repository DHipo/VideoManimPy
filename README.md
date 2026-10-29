# 🎬 Manim Video Studio & Animation Pipeline

Sistema modular para la conceptualización, diseño, codificación y renderizado de videos animados y motion graphics utilizando **Python** y **Manim Community Edition (Manim CE)**.

El proyecto está diseñado para desacoplar el proceso de creación en tres roles/skills especializados:
1. **`manim-director`**: Entrevista al usuario, define el estilo, resuelve dudas temáticas y produce el Storyboard escena por escena.
2. **`manim-animator`**: Convierte el Storyboard en código Python Manim modular, tipado, limpio y sin antipatrones.
3. **`manim-runner`**: Ejecuta el pipeline de renderizado en el entorno virtual (`.venv`), gestiona calidad/tiempos y diagnostica errores.

---

## 🚀 Requisitos y Configuración del Entorno Virtual (Python venv)

Para garantizar aislamiento, estabilidad y evitar contaminar el sistema operativo, **todo el ciclo de vida de ejecución e instalación de Manim se realiza dentro de un entorno virtual de Python (`.venv`)**.

### 1. Dependencias del Sistema Operativo

Manim depende de librerías del sistema para procesamiento gráfico (`cairo`, `pango`) y de video (`ffmpeg`).

#### En Arch Linux / CachyOS:
```bash
sudo pacman -S ffmpeg cairo pango pkgconf
```

> **Nota sobre LaTeX (Opcional):** Si vas a utilizar fórmulas matemáticas complejas con `MathTex`, instala TeXLive y dvisvgm:
> ```bash
> sudo pacman -S texlive-basic texlive-latexextra texlive-bin dvisvgm
> ```
> *Si no tienes LaTeX instalado, las animaciones usarán `Text` y `MarkupText` para títulos, etiquetas y diagramas sin ningún problema.*

---

### 2. Creación y Activación del Virtual Environment (`.venv`)

Crea y activa el entorno virtual en la raíz del proyecto:

```bash
# 1. Crear el entorno virtual
python3 -m venv .venv

# 2. Activar el entorno virtual
source .venv/bin/activate

# 3. Actualizar herramientas base
pip install --upgrade pip setuptools wheel
```

---

### 3. Instalación de Dependencias

Con el entorno virtual activado (`source .venv/bin/activate`):

```bash
pip install -r requirements.txt
```

Para verificar que Manim quedó correctamente instalado en tu entorno virtual:

```bash
manim --version
```

---

## 📁 Estructura del Proyecto

```text
animation/
├── .agents/
│   └── skills/
│       ├── manim-director/          # Skill 1: Cuestionario inteligente y Storyboarding
│       │   ├── SKILL.md
│       │   └── resources/
│       │       ├── presets.json     # Arquetipos visuales (colores, proporciones, fuentes)
│       │       └── storyboard_spec.md
│       ├── manim-animator/          # Skill 2: Arquitectura y código Manim CE
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── manim_ce_cheat_sheet.md
│       └── manim-runner/            # Skill 3: Renderizado, flags y QA
│           ├── SKILL.md
│           └── scripts/
│               └── render.sh        # Runner automatizado integrado con .venv
├── src/                             # Escenas y módulos Python
│   └── scenes/                      # Clases Scene de cada proyecto
├── output/                          # Videos finales renderizados (.mp4)
├── requirements.txt                 # Dependencias Python
├── README.md                        # Esta guía
└── .gitignore                       # Ignora venv, media cache y temporales
```

---

## 🔄 Flujo de Trabajo (Workflow)

```
[Usuario con una Idea o Prompt]
               │
               ▼
   [Skill: manim-director]
   - Preguntas estándar (Preset, Formato 16:9 vs 9:16, Duración)
   - 2 a 3 preguntas dinámicas según el tema específico
   - Generación de storyboard.md detallado
               │
               ▼
   [Skill: manim-animator]
   - Traducción del storyboard a código Python modular
   - Diseño de VGroups, composiciones y transiciones limpias
   - Ubicación en src/scenes/<video_name>.py
               │
               ▼
   [Skill: manim-runner]
   - Render rápido de prueba (-ql) en .venv
   - Detección / Corrección de errores
   - Render final en alta definición (-qh / 1080p60)
```

---

## ⚡ Comandos Rápidos de Render

Puedes usar el script helper provisto en `manim-runner`:

```bash
# Render rápido para vista previa (480p @ 15fps)
./.agents/skills/manim-runner/scripts/render.sh src/scenes/ejemplo.py MiEscena -ql

# Render de calidad estándar (720p @ 30fps)
./.agents/skills/manim-runner/scripts/render.sh src/scenes/ejemplo.py MiEscena -qm

# Render final de alta calidad (1080p @ 60fps)
./.agents/skills/manim-runner/scripts/render.sh src/scenes/ejemplo.py MiEscena -qh
```
