"""
Example Motion Graphics Scene for Manim Video Studio.
Demonstrates:
- Clean styling with Modern Tech Dark palette
- Relative positioning and VGroups
- Safe Text elements (No LaTeX dependency)
- Modular phase execution
"""

from manim import *

# ==========================================
# CONSTANTES DE DISEÑO Y PALETA
# ==========================================
BG_COLOR = "#0D1117"
PRIMARY = "#58A6FF"
SECONDARY = "#3FB950"
ACCENT = "#F0883E"
TEXT_COLOR = "#F0F6FC"
MUTED_COLOR = "#8B949E"


def create_pipeline_card(step_num: str, title: str, subtitle: str, stroke_color: str) -> VGroup:
    """Crea una tarjeta estilizada para motion graphics con bordes redondeados."""
    box = RoundedRectangle(
        corner_radius=0.18,
        width=3.2,
        height=2.0,
        fill_color="#161B22",
        fill_opacity=0.9,
        stroke_color=stroke_color,
        stroke_width=2.5,
    )

    badge = RoundedRectangle(
        corner_radius=0.08,
        width=0.7,
        height=0.35,
        fill_color=stroke_color,
        fill_opacity=0.2,
        stroke_color=stroke_color,
        stroke_width=1.5,
    )
    badge_text = Text(step_num, font_size=14, weight=BOLD, color=stroke_color)
    badge_group = VGroup(badge, badge_text)
    badge_group.next_to(box.get_top(), DOWN, buff=0.25).align_to(box.get_left(), LEFT).shift(RIGHT * 0.25)

    title_text = Text(title, font_size=18, weight=BOLD, color=TEXT_COLOR)
    title_text.next_to(badge_group, DOWN, buff=0.2).align_to(badge_group, LEFT)

    desc_text = Text(subtitle, font_size=12, color=MUTED_COLOR)
    desc_text.next_to(title_text, DOWN, buff=0.15).align_to(title_text, LEFT)

    return VGroup(box, badge_group, title_text, desc_text)


class PipelineMotionScene(Scene):
    """Escena demostrativa de un pipeline de datos animado."""

    def construct(self):
        # 1. Configuración de fondo
        self.camera.background_color = BG_COLOR

        # 2. Ejecución secuencial de fases narrativas
        self.phase_intro()
        self.phase_cards_pipeline()
        self.phase_data_flow()
        self.phase_outro()

    def phase_intro(self):
        # Título superior y subtítulo
        title = Text("Pipeline de Animación", font_size=36, weight=BOLD, color=PRIMARY)
        title.to_edge(UP, buff=0.8)

        subtitle = Text("De Prompt a Video con Manim CE", font_size=18, color=MUTED_COLOR)
        subtitle.next_to(title, DOWN, buff=0.25)

        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(0.8)

        self.header_group = VGroup(title, subtitle)

    def phase_cards_pipeline(self):
        card1 = create_pipeline_card("01", "Director", "Guion y Presets", PRIMARY)
        card2 = create_pipeline_card("02", "Animator", "Código Python CE", SECONDARY)
        card3 = create_pipeline_card("03", "Runner", "Render en .venv", ACCENT)

        cards = VGroup(card1, card2, card3).arrange(RIGHT, buff=0.6)
        cards.move_to(ORIGIN)

        # Flechas de conexión
        arrow1 = Arrow(card1.get_right(), card2.get_left(), buff=0.12, color=MUTED_COLOR, stroke_width=2.5)
        arrow2 = Arrow(card2.get_right(), card3.get_left(), buff=0.12, color=MUTED_COLOR, stroke_width=2.5)

        # Animación de entrada
        self.play(FadeIn(card1, shift=UP * 0.4), run_time=0.7)
        self.play(Create(arrow1), FadeIn(card2, shift=UP * 0.4), run_time=0.7)
        self.play(Create(arrow2), FadeIn(card3, shift=UP * 0.4), run_time=0.7)
        self.wait(1.0)

        self.pipeline_elements = VGroup(cards, arrow1, arrow2)

    def phase_data_flow(self):
        # Pulso de datos que viaja por el pipeline
        pulse = Dot(radius=0.12, color=PRIMARY).move_to(self.pipeline_elements[0][0].get_center())

        self.play(FadeIn(pulse, scale=1.5), run_time=0.4)
        self.play(pulse.animate.move_to(self.pipeline_elements[0][1].get_center()), run_time=0.9, rate_func=smooth)
        self.play(pulse.animate.set_color(SECONDARY).move_to(self.pipeline_elements[0][2].get_center()), run_time=0.9, rate_func=smooth)
        self.play(Circumscribe(self.pipeline_elements[0][2], color=ACCENT), run_time=1.0)
        self.play(FadeOut(pulse), run_time=0.3)
        self.wait(0.8)

    def phase_outro(self):
        # Limpieza suave
        self.play(
            FadeOut(self.pipeline_elements, shift=DOWN * 0.4),
            FadeOut(self.header_group, shift=UP * 0.4),
            run_time=0.8,
        )

        badge = RoundedRectangle(
            corner_radius=0.2,
            width=5.0,
            height=1.2,
            fill_color="#1F242C",
            fill_opacity=0.95,
            stroke_color=SECONDARY,
            stroke_width=2.0,
        )
        success_text = Text("¡Sistema Listo para Crear!", font_size=24, weight=BOLD, color=SECONDARY)
        success_text.move_to(badge.get_center())

        final_group = VGroup(badge, success_text)
        self.play(FadeIn(final_group, scale=1.1), run_time=1.0)
        self.wait(1.5)
