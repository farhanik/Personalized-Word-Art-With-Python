# Unique Word Art Generator with Python

This project is a creative Python application designed to produce unique word art by combining text-based designs with a visually rich background. The word art takes the shape defined by a mask image and is seamlessly blended with a background image, allowing endless customization for creative, academic, or artistic purposes.

---

## Key Features

- **Custom Shape**: Generates a word cloud in the shape defined by the mask image (`ANIK.png`).
- **Background Blending**: Integrates the word cloud with a background image (`background.jpg`) using transparency for a smooth and professional finish.
- **Recolor Options**: Leverages the mask image's color scheme to enhance word cloud aesthetics.
- **Customizable Parameters**: Supports adjustments for word count, font size, and text layout.
- **Simple Text Input**: Reads input words from a text file (`word.txt`) for ease of use and flexibility.

---

## File Descriptions

### 1. `word_art.py`
- The Python script that executes the entire word art generation process.
- Functions include:
  - Reading input text.
  - Generating a word cloud based on the mask image.
  - Blending the word cloud with the background image.

### 2. `word.txt`
- A plain text file containing the words or phrases for the word cloud.
- Words are weighted based on frequency to control their prominence in the final design.

### 3. `ANIK.png`
- A mask image that defines the unique shape of the word cloud.
- The words align to this shape, creating an appealing and personalized design.

### 4. `background.jpg`
- The background image used to enhance the visual appeal of the word art.
- It serves as the canvas on which the word cloud is overlaid.

---

## Getting Started

### Prerequisites

Before running the script, ensure you have the following Python libraries installed:
- `wordcloud`
- `matplotlib`
- `numpy`
- `Pillow`

Install them using the command:
```bash
pip install wordcloud matplotlib numpy pillow
