# Resume-Analyser

A Machine Learning powered resume analyzer that runs locally.

This project was inspired by [SpicychieF05's AI Powered Resume Screening System](https://github.com/SpicychieF05/Ai-Resume-Screening-System).

## Data

The training data is from [here](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset?select=UpdatedResumeDataSet.csv)<br>
The test data is from [here](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)

Install requirements with `pip install -r requirements.txt`. Then, do `pip install numpy==1.26.0 --force-reinstall` for compatibility. <br>

## Converting resume data to text data

### CSV

To convert the csv data to text data, run the following: <br>
`python src/convert_dataset.py --csv data/raw/UpdatedResumeDataSet.csv --outdir data/processed/converted`<br>

### PDF

To convert pdf data to text data, run the following: <br>
`python src/convert_test_data.py --pdfdir <data directory> --outdir <desired output directory>
`
<br>

> For the time being, you can ignore the bad naming scheme, that will be fixed later to clarity

## train_classifier.py

Initial training with Logistic Regression. Run with `python src/train_classifier.py`. <br>
Example output: <br>
![./assets/Logistic_Regression_Test.png](./assets/Logistic_Regression_Test.png)

> Will experiment with other algorithms as well

## predict.py

For testing predicted category based on processed resume. <br>

> Also works on test data

## advice.py

This is an MVP version of the Resume-Analyser (more like pre-beta). The test was done on a data science resume, and the criterea was the following:

1. **Length**: Is the resume too short?
2. **Missing keywords**: Are key terms like "Python", "machine learning", etc., missing?
3. **Missing sections**: Are "Experience", "Projects", "Education", or "Skills" missing?
4. **Soft skills**: Check for mentions of soft skills (e.g., communication, leadership).
5. **Role match**: Check how close the resume is to a target career path (e.g., Data Science).

> I can't stress enough, this is not the final version
