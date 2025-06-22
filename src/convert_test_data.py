import os
from pathlib import Path

from pypdf import PdfReader

# Ideally, we would analyze the pdf as opposed to the csv file.
# That's how most resume's would some anyways


def process_resumes(raw_data, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pdf_search = Path(raw_data).glob("*.pdf")
    pdf_files = [str(file.absolute()) for file in pdf_search]
    for pdf in pdf_files:
        reader = PdfReader(pdf)
        page = reader.pages[pdf_files]
        processed_resume = page.extrac_text()
        filename = f"resume_{pdf}.txt"
        file_path = os.path.join(output_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(processed_resume)

    print(f"Saved {len(pdf_search)} resumes to {output_dir}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str, required=True, help="Path to the resume PDF")
    parser.add_argument(
        "--outdir",
        type=str,
        default="../data/test_data/processed",
        help="Output directory for text files",
    )
    args = parser.parse_args()

    process_resumes(args.pdf, args.outdir)
