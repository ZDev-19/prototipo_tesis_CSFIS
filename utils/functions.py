from surprise.dataset import Dataset
from surprise.reader import Reader
from surprise.model_selection import train_test_split
import pandas as pd


def recover_all_data(path,inputs):

    data_rating = pd.read_csv(path)

    last_user_id = data_rating['user_id'].max()

    new_user_ids = [last_user_id + 1] * len(inputs)
    new_items_ids = [1,2,3,4,5,6,7,8,9,10]

    df_new_user = pd.DataFrame({'user_id': new_user_ids , 'factor_id': new_items_ids , 'rating': inputs})

    data_rating = pd.concat([data_rating,df_new_user],ignore_index=True)

    reader = Reader()
    surprise_data = Dataset.load_from_df(data_rating,reader)
    
    trainset, testset = train_test_split(surprise_data, test_size=.3, random_state=42)

    return surprise_data , trainset , testset