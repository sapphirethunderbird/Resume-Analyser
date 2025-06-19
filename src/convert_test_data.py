import os

import pandas as pd


def process_resumes(csv_path, output_dir):
    df = pd.read_csv(csv_path)

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

def 

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=str, required=True, help="Path to the resume CSV")
    parser.add_argument(
        "--outdir",
        type=str,
        default="data/processed",
        help="Output directory for text files",
    )
    args = parser.parse_args()

    save_resumes_from_csv(args.csv, args.outdir)
