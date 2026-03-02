"""Runner script that pre-loads header.py before executing a solution file.

Usage: python run.py path/to/solution.py
"""
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python run.py <solution.py>")
    sys.exit(1)

header_path = Path(__file__).resolve().parent / "header.py"
solution_path = Path(sys.argv[1]).resolve()

namespace = {"__name__": "__main__", "__file__": str(solution_path)}

with open(header_path) as f:
    exec(compile(f.read(), str(header_path), "exec"), namespace)

sys.argv = sys.argv[1:]

with open(solution_path) as f:
    exec(compile(f.read(), str(solution_path), "exec"), namespace)
