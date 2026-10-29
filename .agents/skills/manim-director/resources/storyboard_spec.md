# Especificación de Storyboard para Manim

Este documento define el formato estructurado y obligatorio en el que `manim-director` debe entregar el Storyboard antes de que `manim-animator` comience a programar.

---

## Estructura del Documento Storyboard

```markdown
# Storyboard: [Título del Video]

## Metadatos Globales
- **Tema / Objetivo:** [Breve descripción conceptual del mensaje]
- **Preset Visual:** [Nombre del Preset de presets.json, ej: Modern Tech / Dark Neon]
- **Fondo:** [Color hex o descripción]
- **Relación de Aspecto:** [16:9 | 9:16 | 1:1]
- **Duración Estimada Total:** [ej: 45 segundos]
- **Paleta de Colores Activa:**
  - Primario: `#HEX`
  - Secundario: `#HEX`
  - Acento: `#HEX`
  - Texto: `#HEX`

---

## Escena 1: [Nombre de la Escena / Gancho Inicial]
- **Duración estimada:** [ej: 8s]
- **Objetivo visual:** [Qué debe entender el espectador aquí]
- **Elementos en pantalla:**
  - `E1_Title`: Título principal arriba (`Text`).
  - `E1_Diagram`: Caja o icono central representando el concepto.
- **Acciones y Animaciones (Timeline):**
  1. `[0.0s - 1.5s]`: FadeIn + Write del título superior.
  2. `[1.5s - 3.5s]`: Creación del diagrama central (`Create` con `run_time=2.0`).
  3. `[3.5s - 6.0s]`: Destacar elemento clave con `Indicate` o `Circumscribe`.
  4. `[6.0s - 8.0s]`: Transición hacia la Escena 2 (FadeOut / Transform).
- **Notas de Layout y Espacio:**
  - Dejar 1.5 unidades de margen superior para evitar colisiones.
  - El diagrama debe mantenerse centrado dentro de [-3, 3] en X y [-2, 2] en Y.

---

## Escena 2: [Desarrollo / Transformación Principal]
- **Duración estimada:** [ej: 15s]
...
```
