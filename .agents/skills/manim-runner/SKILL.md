---
name: manim-runner
description: >-
  Executes, tests, and diagnoses Manim animation rendering using the local Python virtual environment (.venv).
  Use when running scene previews (-ql), rendering final high-resolution videos (-qh),
  or troubleshooting Manim compilation and runtime errors.
---

# Manim Runner & Render Orchestrator

Esta skill se encarga del ciclo de ejecución, verificación visual, depuración de errores y renderizado final de las animaciones generadas, garantizando que todo se ejecute de manera aislada dentro del entorno virtual de Python (`.venv`).

---

## 1. Script Helper de Renderizado

Para facilitar la ejecución sin necesidad de activar manualmente el entorno en cada comando, se proporciona el script:
[render.sh](./scripts/render.sh)

### Sintaxis Básica:
```bash
./.agents/skills/manim-runner/scripts/render.sh <ruta_archivo.py> <NombreClaseScene> [calidad] [flags]
```

### Niveles de Calidad:
* `-ql` : **480p @ 15fps** (Baja resolución). Usar SIEMPRE primero para comprobar que la escena corre sin errores en segundos.
* `-qm` : **720p @ 30fps** (Media resolución). Ideal para compartir avances o previews nítidos.
* `-qh` : **1080p @ 60fps** (Alta resolución). Calidad estándar de producción y entrega final.
* `-qk` : **2160p @ 60fps** (4K). Para exportaciones ultra-HD.

---

## 2. Flujo de Trabajo Recomendado (Iteración Rápida)

### Paso 1: Verificación de Frame Estático (Instantáneo)
Si solo quieres validar el layout visual sin esperar a que renderice todo el video:
```bash
.venv/bin/manim -s -ql --media_dir output src/scenes/mi_video.py MainScene
```
*(El flag `-s` guarda una imagen PNG del último cuadro de la animación).*

### Paso 2: Render de Prueba (Baja Calidad)
```bash
./.agents/skills/manim-runner/scripts/render.sh src/scenes/mi_video.py MainScene -ql
```

### Paso 3: Render Final de Producción
Solo una vez que el preview `-ql` corre sin errores de sintaxis, posicionamiento o tiempos:
```bash
./.agents/skills/manim-runner/scripts/render.sh src/scenes/mi_video.py MainScene -qh
```

Los videos generados se almacenan automáticamente en:
`output/videos/<nombre_archivo>/<resolución>/<NombreClaseScene>.mp4`

---

## 3. Matriz de Diagnóstico y Recuperación de Errores

Si el render falla, analiza el log de error e implementa la solución correspondiente:

### Error 1: `Latex error converting to dvi` o `dvisvgm not found`
* **Causa:** El código utiliza `MathTex` o `Tex` pero TeXLive no está instalado o falló la compilación de LaTeX.
* **Solución inmediata:** Reemplaza `MathTex` por `Text` o `MarkupText` con símbolos unicode directos (ej. `Text("E = mc²")`), o pide al usuario instalar `texlive-basic` y `dvisvgm`.

### Error 2: `AttributeError: 'Scene' object has no attribute 'X'` o mutaciones no animadas
* **Causa:** Se llamó a `self.play(obj.shift(UP))` en lugar de `self.play(obj.animate.shift(UP))`.
* **Solución:** Añadir `.animate` a las transformaciones o utilizar `obj.shift(UP)` fuera del `self.play(...)` si es un cambio instantáneo.

### Error 3: Elementos cortados o fuera de pantalla (Clipping)
* **Causa:** Coordenadas fuera del rango visible de la cámara (especialmente común en formato vertical 9:16).
* **Solución:**
  * En 16:9: Asegurar que los objetos se ubiquen dentro de $X \in [-6.0, 6.0]$ e $Y \in [-3.5, 3.5]$.
  * En 9:16: Asegurar que los objetos se ubiquen dentro de $X \in [-3.0, 3.0]$ e $Y \in [-6.0, 6.0]$, agrupando los mobjects en un `VGroup` y aplicando `.scale_to_fit_width(5.0)`.

### Error 4: `ModuleNotFoundError: No module named 'manim'`
* **Causa:** El script se ejecutó con el python del sistema en lugar del binario de `.venv`.
* **Solución:** Ejecutar siempre usando `./.agents/skills/manim-runner/scripts/render.sh` o llamando directamente a `.venv/bin/manim`.
