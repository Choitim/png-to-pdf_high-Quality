from PIL import Image
import os

def convert_png_to_pdf(output_pdf_name):
    """
    Converts all PNG files in the current folder to a single high-quality PDF.

    Args:
    - output_pdf_name (str): Name of the resulting PDF file.

    Returns:
    - None
    """
    try:
        current_folder = os.getcwd()
        png_files = [os.path.join(current_folder, file) for file in os.listdir(current_folder) if file.lower().endswith('.png')]

        if not png_files:
            print("No PNG files found in the current folder.")
            return

        images = [Image.open(file).convert('RGB') for file in sorted(png_files)]
        output_pdf_path = os.path.join(current_folder, output_pdf_name)
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:], quality=95)

        print(f"High-quality PDF successfully saved as: {output_pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

convert_png_to_pdf("output.pdf")
