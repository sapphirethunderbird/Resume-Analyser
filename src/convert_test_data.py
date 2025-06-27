import os
from pathlib import Path

from pypdf import PdfReader


def process_resumes(raw_data_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # 🔍 Recursively find all PDFs in subfolders
    pdf_files = list(
        Path(raw_data_dir).rglob("*.pdf")
    )  # Use rglob here instead of glob

    for i, pdf_path in enumerate(pdf_files):
        try:
            reader = PdfReader(str(pdf_path))
            all_text = ""

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_text += text + "\n"

            # 📁 Extract job title from parent folder
            job_title = pdf_path.parent.name.replace(" ", "_")
            filename = f"resume_{i}_{job_title}.txt"
            file_path = os.path.join(output_dir, filename)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(all_text.strip())

        except Exception as e:
            print(f"❌ Failed to process {pdf_path.name}: {e}")

    print(f"✅ Saved {len(pdf_files)} resumes to {output_dir}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pdfdir", type=str, required=True, help="Path to folder with PDFs"
    )
    parser.add_argument(
        "--outdir",
        type=str,
        default="data/test_data/processed",
        help="Output directory for text files",
    )
    args = parser.parse_args()

    process_resumes(args.pdfdir, args.outdir)
