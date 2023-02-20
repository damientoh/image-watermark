from PIL import Image, ImageDraw, ImageFont
import os

# Get the current working directory
directory = os.getcwd()

# Define the watermark text and font to use
watermark_text = '100% Asli | Tersedia'
min_padding = 10
font = ImageFont.truetype('arial.ttf', size=1)

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an image file
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Open the image file
        image = Image.open(os.path.join(directory, filename))
        # Crop the image to a square
        size = min(image.size)
        left = (image.size[0] - size) / 2
        top = (image.size[1] - size) / 2
        right = (image.size[0] + size) / 2
        bottom = (image.size[1] + size) / 2
        image = image.crop((left, top, right, bottom))
        # Create a drawing context
        draw = ImageDraw.Draw(image)
        # Determine the maximum font size that fits within the image width with a small padding
        font_size = 1
        while True:
            font_size += 1
            font = ImageFont.truetype('arial.ttf', size=font_size)
            text_width, text_height = draw.textsize(watermark_text, font=font)
            if text_width >= image.width - 2 * min_padding:
                break
        # Determine the position to place the watermark text
        x = (image.width - text_width) / 2
        y = 0
        # Draw the watermark text on the image
        draw.rectangle((0, y, image.width, y + text_height + min_padding), fill=(0, 0, 139, 128))
        draw.text((x, y + min_padding), watermark_text, font=font, fill=(255, 255, 255, 128))
        # Save the watermarked image in the same directory with the same filename
        watermarked_path = os.path.join(directory, filename)
        image.save(watermarked_path)
        # Print a message indicating that the image has been watermarked
        print(f'Watermarked {filename}')
