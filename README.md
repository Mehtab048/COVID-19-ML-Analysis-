# COVID-19-ML-Analysis-
# COVID-19 Patient Condition Prediction using Machine Learning

This project analyzes a real-world COVID-19 dataset using various Machine Learning algorithms to predict patient infection risk and assess algorithm performance. The goal is to support decision-making in resource allocation and patient management during the pandemic.

## Problem Statement
The COVID-19 pandemic created a global health crisis with limited medical resources. Accurate early prediction of patient risk helps healthcare providers allocate resources effectively.

## Dataset
- **Source:** [Kaggle COVID-19 Dataset](https://www.kaggle.com/)
- **Records:** 1,048,576 patient records provided by the Mexican government
- **Features:** 21 patient features including age, gender, symptoms, and comorbidities
- **Target:** COVID-19 Status (Effected / Not Effected)

## Machine Learning Models Applied
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Naive Bayes

## Methodology
- Data Cleaning (handling missing values and invalid entries)
- Data Preprocessing (encoding categorical variables, feature scaling)
- Model Training on cleaned data
- Model Evaluation using Accuracy, Precision, Recall, and F1-score

## Key Results
- **Random Forest** showed the best balance between accuracy, precision, and recall, making it
  the most suitable model for this imbalanced dataset.
- **Naive Bayes** achieved high recall for COVID-19 positive cases but had poor precision,
  leading to a low F1-score due to the dataset's imbalance.
- **Logistic Regression** delivered fast training and high overall accuracy but performed poorly
  in detecting COVID-19 positive cases (low recall and F1-score).
- **K-Nearest Neighbors (KNN)** offered better precision than Logistic Regression but struggled
  with recall and had higher computational cost on the large dataset.
- **Support Vector Machine (SVM)** was not ideal for this dataset due to scalability issues and
  lower performance.
- Overall, **Random Forest** outperformed others in balancing prediction quality and handling
  data imbalance.

## Tools & Libraries
- Python
- Pandas
- Scikit-learn
- Matplotlib (for visualization)

## Conclusion
Random Forest was the most effective model for this dataset based on evaluation metrics. The project demonstrates the importance of model selection, data preprocessing, and metric evaluation for imbalanced classification problems.

## Author
Mehtab Mushtaq

## License
This project is for educational and research purposes.
