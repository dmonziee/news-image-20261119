"""news-image-20261119 entry: copy the front-page image to the output dir.

The image (entry.png, 1024x1024) was drawn by the agent in this session with
PIL from the day's news and is committed beside this file. Standard library
only; runs twice with identical bytes.
"""
import hashlib
import os
import shutil
import sys

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
src = os.path.join(here, "entry.png")
dst = os.path.join(out, "entry.png")
shutil.copyfile(src, dst)
# Determinism guard: the copy must be byte-identical to the committed image.
src_hash = hashlib.sha256(open(src, "rb").read()).hexdigest()
dst_hash = hashlib.sha256(open(dst, "rb").read()).hexdigest()
assert src_hash == dst_hash, "entry.png copy differs from source"
print(f"wrote entry.png ({os.path.getsize(dst)} bytes, sha256 {dst_hash[:12]}…)",
      file=sys.stderr)
