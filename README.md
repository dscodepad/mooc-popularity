# Mooc Popularity Prediction: A Case Study on Udemy
- This repository iprovide the code used to predict the MOOC popularity based on Udemy.
- As the file size is large, we offer the google drive links to acess the data we used in the paper, including two files, i.e.,
  - ``udemy-data.csv`` (https://drive.google.com/file/d/1R9_mUWfWlPRiCgzWw_Qqhu0iiHQMIXkx/view?usp=sharing) includes the all the features we used to make prediction. 
  - ``course-text-data.csv`` (https://drive.google.com/file/d/1T2qLL3_68Br8YXjFIz2pgeL8__j1lWxk/view?usp=sharing) is used to extract text embeddings by extract_text_embedding.py.
- The python file ``extract_text_embedding.py`` extracted the embeddings of five content features, i.e., title-headline, objective, prerequisite, description and target audience.
- The notebook ``experiment.ipynb`` provides the code we used to obtain the results, including parameter tuning steps of the four machine learning models used in the paper.   
\*: The parameter tunning guidence for XGBoost and Random Forest can also refer to the tutorials offered in <https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/> and <https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74>.
