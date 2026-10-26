import sys
from pathlib import Path

from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_name, output_name = sys.argv[1], sys.argv[2]
input_suffix, output_suffix = [
    Path(name).suffix.lower() for name in [input_name, output_name]
]

if input_suffix not in (".jpg", ".jpeg", ".png"):
    sys.exit(f"Wrong extension {input_name}")
if input_suffix != output_suffix:
    sys.exit("Input and output have different extensions")

try:
    with Image.open(input_name) as photo, Image.open("shirt.png") as shirt:
        photo_fitted = ImageOps.fit(photo, size=shirt.size)
        photo_fitted.paste(shirt, mask=shirt)
        photo_fitted.save(output_name)
except (FileNotFoundError, IsADirectoryError):
    sys.exit(f"Could not read {input_name}")
