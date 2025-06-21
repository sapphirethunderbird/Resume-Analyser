import os

import pandas as pd

# Ideally, we would analyze the pdf as opposed to the csv file.
# That's how most resume's would some anyways


def process_resumes(pdf_path, output_dir):
    df = pd.read_csv(pdf_path)

    os.makedirs(output_dir, exist_ok=True)

    for i, row in df.iterrows():
        resume_text = row["Resume"]
        category = row.get("Category", "Unknown")
        category = category.replace(" ", "_")
        filename = f"resume_{i}_{category}.txt"
        file_path = os.path.join(output_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(resume_text)

    print(f"Saved {len(df)} resumes to {output_dir}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str, required=True, help="Path to the resume PDF")
    parser.add_argument(
        "--outdir",
        type=str,
        default="data/test_data/processed",
        help="Output directory for text files",
    )
    args = parser.parse_args()

    process_resumes(args.csv, args.outdir)
