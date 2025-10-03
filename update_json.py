import os
import json

# GIFs ka folder path
gif_folder = "profile"  # aapke folder ka naam
json_file = "gifs.json"  # output JSON file

# GIF files read karna aur sort karna
gif_files = sorted([f for f in os.listdir(gif_folder) if f.lower().endswith(".gif")])

# JSON me likhna
with open(json_file, "w") as f:
    json.dump(gif_files, f, indent=2)

print(f"{json_file} updated with {len(gif_files)} GIFs!")
