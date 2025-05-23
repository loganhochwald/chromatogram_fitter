# Chromatographic Peak Deconvolution Tool

This Python script performs deconvolution of chromatographic data from Excel files using Gaussian curve fitting. It detects multiple overlapping peaks in a chromatogram, fits them with Gaussian functions, and visualizes the original data alongside the fitted peaks with annotated area percentages.

For a deeper look into how this script works and the reasoning behind the approach, check out the full article:
[Deconvolution of Chromatographic Peaks Using Python](https://medium.com/@loganhochwald/deconvolution-of-chromatographic-peaks-using-python-9a3efedaa054)


## Features

- Load chromatographic data (`x` and `y` values) from an Excel file and sheet selected via a GUI.
- Automatically detect peaks in the data using signal processing techniques.
- Fit multiple Gaussian curves simultaneously to model overlapping chromatographic peaks.
- Calculate and annotate each peak's relative area percentage.
- Visualize original data, fitted overall curve, and individual Gaussian peaks.

## Requirements

- Python 3.7+
- Libraries listed in `requirements.txt`:
  - pandas
  - numpy
  - matplotlib
  - scipy

## Installation

Install all required dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```