from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the text
text = open('word.txt', encoding='utf-8').read()

# Load the mask for the word shape
word_mask = np.array(Image.open('ANIK.png'))

# Load the background image and convert it to RGBA
background_image = Image.open('background.jpg').convert("RGBA")


# Generate the word cloud
wc = WordCloud(
    stopwords=STOPWORDS,
    mask=word_mask,
    background_color=None,  # Set to None for a transparent background
    mode='RGBA',  # Use RGBA mode for transparency support
    min_font_size=2,
    max_words=500
).generate(text)

# Recolor the word cloud using the color scheme of the mask
colormap = ImageColorGenerator(word_mask)
wc = wc.recolor(color_func=colormap)

# Convert the word cloud to an RGBA image
wc_image = wc.to_image()

# Resize the word cloud to match the background image dimensions if necessary
wc_image = wc_image.resize(background_image.size)

# Convert both images to NumPy arrays (ensure they have 4 channels - RGBA)
background_array = np.array(background_image)
wc_array = np.array(wc_image)

# Ensure wc_array has four channels by converting if needed
if wc_array.ndim == 2:  # If wc_array is grayscale (2D)
    wc_array = np.stack((wc_array,) * 3 + (np.full_like(wc_array, 255),), axis=-1)
elif wc_array.shape[2] == 3:  # If wc_array has only RGB channels
    alpha_channel = np.full((wc_array.shape[0], wc_array.shape[1]), 255, dtype=wc_array.dtype)
    wc_array = np.dstack((wc_array, alpha_channel))

# Blend the two images manually using NumPy
blended_array = np.where(wc_array[:, :, 3:4] > 0, wc_array, background_array)

# Convert the result back to an image
blended_image = Image.fromarray(blended_array, 'RGBA')

# Display the final image
plt.figure(figsize=(10, 6))
plt.imshow(blended_image)
plt.axis("off")
plt.show()
