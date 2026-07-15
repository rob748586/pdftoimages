from pdf2image import convert_from_path
from pathlib import Path

poppler_path = r"./poppler-26.02.0/library/bin"


def list_pdf_files(input_folder: str = "input") -> list[str]:
    folder = Path(input_folder)
    if not folder.exists() or not folder.is_dir():
        return []

    return [str(path) for path in folder.iterdir() if path.is_file() and path.suffix.lower() == ".pdf"]

input_folder = Path("input")
if not input_folder.exists():
    input_folder.mkdir()

output_folder = Path("output")
if not output_folder.exists():
    output_folder.mkdir()

files = list_pdf_files("input")

for file in files:
    images = convert_from_path(file, poppler_path=poppler_path)
    for i, image in enumerate(images):
        output_path = output_folder / f'{Path(file).stem}_page_{i + 1}.jpg'
        image.save(output_path, 'JPEG')
