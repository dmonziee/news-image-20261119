"""news-image-20261119 entry: copy the front-page image to the output dir.

The image (entry.png, 1024x1024) was drawn by the agent in this session with
PIL from the day's news and is committed beside this file. Standard library
only; runs twice with identical bytes.
"""
import os
import shutil
import sys

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
shutil.copyfile(os.path.join(here, "entry.png"), os.path.join(out, "entry.png"))
print("wrote entry.png", file=sys.stderr)
