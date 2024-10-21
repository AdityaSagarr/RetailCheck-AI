from unstructured.partition.image import partition_image
from PIL import Image
import io

def merge_images(images, direction='vertical'):
    """Merge multiple images into one image."""
    if direction == 'vertical':
        total_height = sum(img.height for img in images)
        max_width = max(img.width for img in images)
        merged_image = Image.new('RGB', (max_width, total_height))
        y_offset = 0
        for img in images:
            merged_image.paste(img, (0, y_offset))
            y_offset += img.height
    elif direction == 'horizontal':
        total_width = sum(img.width for img in images)
        max_height = max(img.height for img in images)
        merged_image = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        for img in images:
            merged_image.paste(img, (x_offset, 0))
            x_offset += img.width

    return merged_image

def image_to_text(image):
    """Extracts text from the given image."""
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')  # Save image to a byte array
    img_byte_arr.seek(0)  # Reset buffer position
    elements = partition_image(file=img_byte_arr, languages=["eng", "kan"], strategy="auto")
    return elements
