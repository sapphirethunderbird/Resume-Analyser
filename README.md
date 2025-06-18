# Resume-Analyser

A Machine Learning powered resume analyzer that runs locally.

This project was inspired by [SpicychieF05's AI Powered Resume Screening System](https://github.com/SpicychieF05/Ai-Resume-Screening-System).

The data is from [here](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset?select=UpdatedResumeDataSet.csv)

Install requirements with `pip install -r requirements.txt`. Then, do `pip install numpy==1.26.0 --force-reinstall` for compatibility. <br>

## Converting csv data to text data

To convert the csv data to text data, run the following: <br>
`python src/convert_dataset.py --csv data/raw/UpdatedResumeDataSet.csv --outdir data/processed/converted`
