---
name: manim-director
description: >-
  Directs the conceptualization, interview process, and storyboarding for Manim animations.
  Use when the user proposes a video idea, requests an animation script, needs to establish
  visual style, duration, aspect ratio, or wants a scene-by-scene storyboard before coding.
---

# Manim Director & Storyboard Architect

Esta skill guía el proceso creativo y editorial previo a la escritura de código. Su misión es transformar una idea abstracta en un **Storyboard estructurado y ejecutable**, evitando la fatiga de cuestionarios excesivos mediante un modelo ágil de preguntas estándar y dinámicas.

---

## 1. Protocolo de Entrevista Ágil ("Smart Presets + Dynamic Delta")

Cuando el usuario propone una idea o prompt para un video, **no formules una lista interminable de preguntas**. Aplica el siguiente flujo estructurado en una única interacción clara:

### Paso 1: Preguntas Estándar (Con Recomendaciones por Defecto)
Presenta opciones claras y sugiere una opción recomendada basada en el prompt:
1. **Preset Visual:**
   - Referencia: [presets.json](./resources/presets.json)
   - Opciones: `Modern Tech Dark`, `Minimalist Explainer (3b1b)`, `Infographic Motion`, `Social Reel (9:16)`, o `Clean Light`.
   - *(Indicar cuál recomiendas y por qué).*
2. **Formato / Relación de Aspecto:**
   - `16:9` Horizontal (YouTube, Presentaciones) **(Recomendado por defecto)**.
   - `9:16` Vertical (Shorts, TikTok, Reels).
3. **Duración Objetivo:**
   - Corto / Punchy: `15 - 30 segundos`.
   - Explainer Medio: `45 - 90 segundos` **(Recomendado por defecto)**.
   - Profundo / Detallado: `2 - 3 minutos`.

### Paso 2: Preguntas Dinámicas del Tema (Máximo 2 a 3)
Formula de 2 a 3 preguntas **específicas y exclusivas del tema del usuario** para resolver decisiones visuales clave.
* *Ejemplo si el tema es un algoritmo:* "¿Quieres ver la animación con datos aleatorios interactuando paso a paso o una metáfora visual primero?"
* *Ejemplo si el tema es arquitectura cloud:* "¿Representamos microservicios con cajas y flechas dinámicas de paquetes o con metáforas de edificios/redes?"
* *Ejemplo si incluye matemáticas:* "¿Requiere ecuaciones formales LaTeX o solo gráficos geométricos y números explicativos?"

### Paso 3: Cláusula "Defaults & Go"
Siempre ofrece al usuario la opción de responder: *"Usa los valores recomendados por defecto"* si desea pasar directamente al guión sin responder una a una.

---

## 2. Generación del Storyboard Formal

Una vez consensuadas las respuestas (o aceptados los defaults), genera el documento de Storyboard siguiendo estrictamente la especificación en:
[storyboard_spec.md](./resources/storyboard_spec.md)

### Reglas para un Buen Storyboard Manim:
1. **Modularidad por Escenas:** Cada escena debe tener una duración acotada (típicamente de 6 a 20 segundos) y un objetivo conceptual único.
2. **Limpieza Visual (No saturación):** Manim se vuelve ilegible si hay más de 5-7 elementos compitiendo por atención simultáneamente. Define claramente qué elementos desaparecen (`FadeOut`) antes de que entren los nuevos.
3. **Continuidad de Objetos (Morphing / Transformations):** Siempre que sea posible, prefiere transformar un objeto existente en el siguiente (`ReplacementTransform`) en lugar de borrar y crear todo de cero. Esto aprovecha la fortaleza visual de Manim.
4. **Respeto a Márgenes de Cámara:**
   - En 16:9: El ancho visible seguro va de $X \in [-6, 6]$ y alto $Y \in [-3.5, 3.5]$.
   - En 9:16: El ancho visible seguro va de $X \in [-3, 3]$ y alto $Y \in [-6, 6]$.

---

## 3. Entrega y Transición al Animador

Al finalizar el Storyboard:
1. Presenta el resumen estructurado al usuario.
2. Guarda el archivo resultante en `src/scenes/<nombre_video>/storyboard.md` (o en la raíz del proyecto si es una escena única).
3. Indica que el storyboard está listo para ser consumido por la skill `manim-animator`.
