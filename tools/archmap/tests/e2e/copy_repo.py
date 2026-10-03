"""Isolated live-test copy. No write or git operation touches the real inputs."""
from pathlib import Path
import shutil
import sys
ROOT=Path(__file__).resolve().parents[4]
ART=ROOT/'tools/archmap/.artifacts'
DEST=ART/'live-repo'
if DEST.exists():shutil.rmtree(DEST)
# All authored repository files + Git metadata. Dependency/build caches are not inputs.
shutil.copytree(ROOT,DEST,ignore=shutil.ignore_patterns('node_modules','.artifacts','target','.venv','__pycache__'),symlinks=True)
print(DEST)
