# OpenCV Course — Example Scripts

This repository contains example Python scripts used while learning OpenCV (computer vision) concepts. The project is organized into phases with simple, focused scripts demonstrating basic image I/O, transformations, drawing, and text overlay.

## Contents

- `read.py` — (root) basic image read/display helper used during exercises.
- `phase-1/`
  - `Assignment-1.py` — assignment from phase 1
  - `dimensions.py` — prints image dimensions
  - `displaying.py` — demonstrates reading and showing images
  - `grayscale.py` — convert images to grayscale
  - `saving.py` — saving image files
  - `tempCodeRunnerFile.py` — temporary helper created by editor
- `phase-2/`
  - `cropped.py` — crop an image region
  - `flipped.py` — flip image horizontally/vertically
  - `resizing.py` — resize images while keeping aspect ratio
  - `rotation.py` — rotate images around center
- `phase-3/`
  - `add_text.py` — overlay text on images
  - `assignment-3.py` — assignment from phase 3
  - `draw_circle.py` — draw circles on images
  - `draw_line.py` — draw lines
  - `draw_rect.py` — draw rectangles

## Prerequisites

- Python 3.8+ recommended
- Install dependencies from `requirements.txt` (example below)

## Install

Create and activate a virtual environment, then install requirements:

```bash
# macOS / zsh example
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you're not using a virtualenv, you can run `pip install -r requirements.txt` directly, but virtual environments are recommended.

## Run examples

- Read and display an image (example):

```bash
python read.py
```

- Run a phase script, for example to convert an image to grayscale:

```bash
python phase-1/grayscale.py
```

Notes:
- Many scripts use `cv2.imshow()` which opens a GUI window. On headless systems (or some macOS setups), you may need to use an alternative display (like saving output images and opening them) or use `matplotlib` for inline displays in notebooks.
- If you see a window appear and scripts exit immediately, ensure the code calls `cv2.waitKey(0)` and `cv2.destroyAllWindows()` (many examples include those).

## Project notes & suggestions

- These scripts are compact learning examples. If you plan to reuse them as utilities, consider moving common operations (load/save/display) into a small helper module.
- Add tests or small sample images in a `data/` folder for reproducible runs.

## License

This repository does not currently include a license file. Add one if you plan to share or change the licensing.

---
Generated README for local OpenCV learning exercises.
