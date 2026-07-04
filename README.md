# digital-stitch-pipeline

Author: Yen-Fen Chan

A computational-design pipeline built for Rhino + Grasshopper that turns embroidery/cable-stitch
curve designs into machine-ready `.DST` files — covering stitch pattern generation, path
optimization, and export in one workflow.

**Requires Rhino 8** — the pipeline runs inside Rhino's Grasshopper environment and won't run
standalone with just Python.

## Highlights

- **Pattern generation** — turns guide curves into stitch patterns (zigzag, cross, decorative,
  arrow, feather) automatically.
- **Fast path optimization** — a custom C++ engine (k-d tree + greedy/2-opt search) sorts the
  stitch path to minimize travel, handling 3000+ curves in real time — far beyond what the
  pure-Python fallback can do.
- **Machine-ready export** — one step to `.DST` (the industry-standard embroidery format), with
  tie-stitches, jump-thread handling, and cable color-change logic built in, plus a CSV log for QA.

## Installation

If you are developing or reviewing the code in an external IDE (like VSCode), install the dependencies via pip:

```
pip install -r requirements.txt
```

## Run (Rhino Grasshopper Environment)

For Rhino 8 Grasshopper Users (Native CPython 3)
You do not need to use the command line to install dependencies. The Grasshopper Python components in this project use Rhino 8's native package manager. 

Simply open the Grasshopper definition and run the script in the top left canvas "Check & Install Modules"; Rhino will automatically read the `# r: package_name` headers and install the required modules internally.


## Project Structure

This project follows a standardized folder layout for Rhino + Grasshopper Python workflows:

- `cad/`  
  Rhino `.3dm` files or exported geometry used as base design assets or simulation references.

- `data/`  
  Input data and machine constraints, as well as digital-to-machine outputs like `.csv`, `.dst`, and `.json`.

- `doc/`  
  Documentation, sketches, technical drawings, and visual references (`.png`, `.pdf`, etc.).

- `result/`  
  Outputs generated from scripts or Grasshopper definitions, such as renderings and log files.

- `src/`  
  Source code: Grasshopper Python components (`src/script/`), the Grasshopper definition
  (`src/gh/`), and a native C++ path-sorting engine (`src/script/native/`) for large designs.

- `.github/`  
  GitHub-specific automation (e.g., Actions, issue templates).  
  **Note:** If the project involves proprietary data or IP, do **not** make this repository public.

- `requirements.txt`  
  Lists Python dependencies for external IDE environment setup.

## License

See [LICENSE](LICENSE) for this project's license. This project also vendors
[nanoflann](https://github.com/jlblancoc/nanoflann) (BSD 2-Clause) in
`src/script/native/`; see [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) for its full license text.
