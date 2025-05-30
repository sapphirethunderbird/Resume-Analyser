import argparse

from advice import generate_advice
from preprocess import clean_text

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', type=str, required=True,
                        help='<pathtoresumefile>')
    args = parser.parse_args()

    with open(args.resume, 'r', encoding='utf-8') as f:
        text = f.read()

    cleaned = clean_text(text)
    suggestions = generate_advice(cleaned)

    print("\nResume Advice:")
    for s in suggestions:
        print(f"- {s}")
