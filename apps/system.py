import streamlit as st
from utils.functions import *
from utils.model_functions import *
from utils.cf_model_class import collab_filtering_based_recommender_model
from surprise import KNNWithMeans

sim_options = {
    "name": ["msd", "cosine", "pearson", "pearson_baseline"],
    "min_support": [3, 4, 5],
    "user_based": [True],
}
params = { 'k': range(5,50,5), 'sim_options': sim_options}

@st.cache
def exec_system(inputs=None):

    surprise_data , trainset , testset = recover_all_data("data/factors_ratings.csv" , inputs)

    clf = find_best_model(KNNWithMeans, params, surprise_data)

    knnwithmeans = clf.best_estimator['rmse']
    
    col_fil_knnwithmeans = collab_filtering_based_recommender_model(knnwithmeans, trainset, testset, surprise_data)

    knnwithmeans_rmse = col_fil_knnwithmeans.fit_and_predict()

    knnwithmeans_cv_rmse = col_fil_knnwithmeans.cross_validate()

    result_knn_user = col_fil_knnwithmeans.recommend()

    return result_knn_user
    