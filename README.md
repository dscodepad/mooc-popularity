# mooc-popularity-prediction: case study on Udemy
- This repository includes the data and code used to predict the MOOC popularity based on Udemy
- Under the data folder
  - ``udemy-data.csv`` under data folder includes the all the features we used to make prediction. 
  - ``course-text-data.csv`` is used to extract text embeddings by extract_text_embedding.py.
- The file extract_text_embedding.py extracted the embeddings of five content features, i.e., title-headline, objective, prerequisite, description and target audience.
- The notebook experiment.ipynb provides the code we used to obtain the results, including parameter tuning steps of the four machine learning models used in the paper. 
