# 🧾 BARCODE_PARSING

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A compact, easy-to-read **Python decoder for Code-39 barcodes**.  
This repository contains a single-file implementation (`Code.py`) that demonstrates the algorithmic steps needed to convert a barcode's bar/space pattern into human-readable characters. It's ideal for learning, testing custom scanning setups, or plugging into a simple inventory/demo pipeline.

---

## What this project does

`BARCODE_PARSING` implements the decoding logic for the **Code-39** symbology:

- Converts narrow/wide bar and space patterns (or bitstrings derived from a scan) into the corresponding alphanumeric characters.
- Performs basic validation and will report decoding errors when patterns don't match valid symbols.
- Designed to be readable and modifiable — good for learning or as a minimal decoding engine for prototypes.
- Checks and accounts for the False Positives and False Negatives.
---

## Supported input formats

The decoder expects one of the following simplified representations (preprocessed from an image or sensor):

1. **Bit string** — a raw sequence like `"1011001110..."` where `1` represents a bar and `0` a space (you may need to normalize widths first).  
2. **Width sequence** — a list of integers representing consecutive stripe widths, e.g. `[1,1,3,1,1,3,...]` where small numbers mean "narrow" and larger numbers mean "wide".  
3. **Pre-parsed symbol patterns** — a list/sequence of narrow/wide flags already mapped per character.

> Note: `Code.py` focuses on decoding logic. Preprocessing (image-to-pattern conversion) is out of scope but easy to add (OpenCV edge detection → run-length widths → normalization).

---

## Installation

```bash
git clone https://github.com/STARSHIP2006/BARCODE_PARSING.git
cd BARCODE_PARSING
# Use your system Python 3 interpreter
python3 --version
