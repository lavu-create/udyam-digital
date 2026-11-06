import os
import sys

# Ensure repository root is on sys.path for backend imports
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Set VERCEL environment flag
os.environ["VERCEL"] = "1"

from backend.main import app
