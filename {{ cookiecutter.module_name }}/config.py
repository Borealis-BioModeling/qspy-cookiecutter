from pathlib import Path

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]

SUMMARY_DIR = PROJ_ROOT / "model-summary"
LOG_PATH = PROJ_ROOT / ".qspy/logs/qspy.log"

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
