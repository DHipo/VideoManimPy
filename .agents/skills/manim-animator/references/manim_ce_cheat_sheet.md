# Cheat Sheet & Buenas Prácticas de Manim Community Edition (v0.18+)

Guía técnica de referencia obligatoria para `manim-animator` al generar scripts de animación limpios y libres de errores.

---

## 1. Importación Canónica
```python
from manim import *
```

---

## 2. Sintaxis Moderna vs APIs Obsoletas (EVITAR ERRORES)

| ❌ Obsoleto / Prohibido | ✅ Moderno Manim CE | Motivo / Contexto |
| :--- | :--- | :--- |
| `ShowCreation(mobj)` | `Create(mobj)` | `ShowCreation` fue eliminado en ManimCE v0.2+ |
| `self.play(mobj.shift(UP))` | `self.play(mobj.animate.shift(UP))` | `.animate` es la sintaxis oficial para mutaciones |
| `TextMobject(...)` | `Tex(...)` o `Text(...)` | `TextMobject` pertenecía a Cairo antiguo |
| `mobj.set_color(color="red")` | `mobj.set_color(RED)` o `#HEX` | Paletas de Manim o constantes directas |
| `FadeInFrom(mobj, UP)` | `FadeIn(mobj, shift=DOWN)` | La dirección en `FadeIn` moderno usa `shift` |
| `FadeOutAndShift(mobj, UP)` | `FadeOut(mobj, shift=UP)` | La dirección en `FadeOut` moderno usa `shift` |

---

## 3. Primitivas Gráficas Clave (Motion Graphics)

### Formas Geométricas y Bloques
```python
# Cajas de diagramas / Tarjetas de contenido
card = RoundedRectangle(
    corner_radius=0.2, 
    width=4.0, 
    height=2.5, 
    fill_color="#1E222A", 
    fill_opacity=0.9, 
    stroke_color="#58A6FF", 
    stroke_width=2.5
)

# Círculos y Nodos
node = Dot(radius=0.15, color="#3FB950")
ring = Circle(radius=1.2, color="#F0883E", stroke_width=3)
```

### Flechas y Conectores Dinámicos
```python
arrow = Arrow(
    start=card1.get_right(),
    end=card2.get_left(),
    buff=0.2,
    color="#ECEEDF",
    stroke_width=3,
    max_tip_length_to_length_ratio=0.15
)

curved_arrow = CurvedArrow(
    start_point=card1.get_top(),
    end_point=card2.get_top(),
    angle=-TAU / 4,
    color="#58C4DD"
)
```

---

## 4. Textos y Tipografía (Seguro contra fallos de LaTeX)

Cuando no se requiera fórmulas matemáticas formales o LaTeX no esté configurado en el sistema, **usar siempre `Text` o `MarkupText`**:

```python
# Título claro y robusto
title = Text("Arquitectura del Sistema", font_size=36, weight=BOLD, color="#FFFFFF")

# Texto enriquecido con Markup (colores y formato inline)
detail = MarkupText(
    "El servicio procesa <span fgcolor='#3FB950'>eventos en tiempo real</span>",
    font_size=24,
    color="#ECEEDF"
)
```

Si se usan ecuaciones matemáticas y TeXLive está disponible:
```python
equation = MathTex(r"E = mc^2", font_size=40, color="#FFFF00")
```

---

## 5. Posicionamiento Relativo (Prohibidas las Coordenadas Mágicas)

❌ **Antipatrón:**
```python
box.move_to(np.array([3.42, -1.85, 0])) # Frágil, se rompe si cambia la resolución
```

✅ **Patrón Limpio:**
```python
title.to_edge(UP, buff=0.8)
subtitle.next_to(title, DOWN, buff=0.3)

# Agrupación y alineación automática
cards = VGroup(card1, card2, card3)
cards.arrange(RIGHT, buff=0.6)
cards.move_to(ORIGIN)

# Alinear bordes entre elementos
label.align_to(card1, LEFT)
```

---

## 6. Animaciones Esenciales y Duraciones (`run_time`)

```python
# Creación fluida
self.play(Create(box), Write(label), run_time=1.2)

# Destacar elemento sin interrumpir el flujo
self.play(Indicate(box, color="#FFFF00", scale_factor=1.1), run_time=1.0)
self.play(Circumscribe(box, color="#3FB950"), run_time=1.2)

# Transformación de concepto (Morphing)
self.play(ReplacementTransform(old_group, new_group), run_time=1.5)

# Fades limpios con desplazamiento suave
self.play(
    FadeOut(box, shift=UP * 0.5),
    FadeIn(new_box, shift=UP * 0.5),
    run_time=0.8
)

# Pausa visual para permitir lectura humana
self.wait(1.5)
```

---

## 7. Composición de Escenas Grandes (SRP)

Para evitar clases `Scene` gigantes de 500 líneas, descompón la lógica en métodos constructores o clases auxiliares:

```python
class MyFeatureVideo(Scene):
    def construct(self):
        # 1. Setup global
        self.camera.background_color = "#0D1117"
        
        # 2. Pipeline de escenas
        self.play_intro()
        self.play_core_mechanism()
        self.play_outro()

    def play_intro(self):
        ...
```
