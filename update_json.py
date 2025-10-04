import os
import json
import shutil

# Profile folder
folder = "profile"
json_file = "gifs.json"
latest_file = "latest.gif"

# Collect all GIFs
gifs = sorted([f for f in os.listdir(folder) if f.endswith(".gif")])

# Save list to gifs.json
with open(json_file, "w") as f:
    json.dump(gifs, f, indent=2)

print("✅ gifs.json updated with:", gifs)

# Update latest.gif -> point to first gif (or you can rotate)
if gifs:
    src = os.path.join(folder, gifs[0])
    shutil.copy(src, latest_file)
    print(f"✅ latest.gif updated -> {src}")
