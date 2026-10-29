#!/usr/bin/env bash
# ==============================================================================
# Helper Script: Manim Runner (Ejecución dentro de .venv)
# ==============================================================================
set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
VENV_DIR="$PROJECT_ROOT/.venv"
MANIM_BIN="$VENV_DIR/bin/manim"
OUTPUT_DIR="$PROJECT_ROOT/output"

# Colores para salida de terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

if [ "$#" -lt 2 ]; then
    echo -e "${YELLOW}Uso:${NC} $0 <archivo_python> <nombre_escena> [calidad: -ql|-qm|-qh|-qk] [opciones_adicionales]"
    echo ""
    echo "Opciones de calidad:"
    echo "  -ql : Calidad baja (480p, 15fps)  -> Ideal para previsualización ultra rápida"
    echo "  -qm : Calidad media (720p, 30fps) -> Calidad balanceada"
    echo "  -qh : Calidad alta (1080p, 60fps) -> Render final para producción (por defecto)"
    echo "  -qk : Calidad 4K (2160p, 60fps)   -> Ultra alta resolución"
    echo ""
    echo "Ejemplo:"
    echo "  $0 src/scenes/demo.py MainScene -ql"
    exit 1
fi

SCRIPT_PATH="$1"
SCENE_NAME="$2"
QUALITY="${3:--qh}"
shift 3 2>/dev/null || shift $#
EXTRA_ARGS="$@"

# 1. Verificar existencia del entorno virtual
if [ ! -d "$VENV_DIR" ] || [ ! -f "$MANIM_BIN" ]; then
    echo -e "${RED}[ERROR]${NC} No se encontró el entorno virtual en $VENV_DIR o no está instalado Manim."
    echo -e "Por favor, crea el entorno virtual e instala las dependencias primero:"
    echo -e "  python3 -m venv .venv"
    echo -e "  source .venv/bin/activate"
    echo -e "  pip install -r requirements.txt"
    exit 1
fi

# 2. Asegurar directorio de salida
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}=== Iniciando Render con Manim CE en .venv ===${NC}"
echo -e "Script:  ${GREEN}$SCRIPT_PATH${NC}"
echo -e "Escena:  ${GREEN}$SCENE_NAME${NC}"
echo -e "Calidad: ${GREEN}$QUALITY${NC}"
echo -e "Salida:  ${GREEN}$OUTPUT_DIR${NC}"
echo ""

# 3. Ejecución de Manim con el binario del entorno virtual
"$MANIM_BIN" render \
    "$QUALITY" \
    --media_dir "$OUTPUT_DIR" \
    "$SCRIPT_PATH" \
    "$SCENE_NAME" \
    $EXTRA_ARGS

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo -e "${GREEN}[ÉXITO] Render finalizado correctamente.${NC}"
    echo -e "Los archivos de video se encuentran en: ${BLUE}$OUTPUT_DIR/videos/${NC}"
else
    echo ""
    echo -e "${RED}[ERROR] El render falló con código $EXIT_CODE.${NC}"
    exit $EXIT_CODE
fi
