import sys
from pathlib import Path
sys.dont_write_bytecode=True
ARCH=Path(__file__).resolve().parents[1]
ROOT=ARCH.parents[1]
sys.path.insert(0,str(ARCH))
ART=ARCH/'.artifacts/tests'
ART.mkdir(parents=True,exist_ok=True)
