import os
import json
import shutil
import random

folder = "profile"
json_file = "gifs.json"
latest_file = "latest.gif"

# Collect all GIFs
gifs = [f for f in os.listdir(folder) if f.endswith(".gif")]

# Save list to gifs.json
with open(json_file, "w") as f:
    json.dump(gifs, f, indent=2)

print("✅ gifs.json updated with:", gifs)

# Pick random gif for latest.gif
if gifs:
    src = os.path.join(folder, random.choice(gifs))
    shutil.copy(src, latest_file)
    print(f"✅ latest.gif updated -> {src}")
