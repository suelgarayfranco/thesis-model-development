import pandas as pd

COMPLETE_DATASET_PATH = 'complete-expressions.csv'
DATA_SPLITS_PATH = 'data-splits/'

class ExpressionsDataset():

    def __init__(self,dataset) -> None:
        DATA_SPLITS_PATH = f'data-splits/{dataset}/'
            
        self.train_data = self.read_csv_file(DATA_SPLITS_PATH + 'train_split.csv')
        self.validation_data = self.read_csv_file(DATA_SPLITS_PATH + 'validation_split.csv')
        self.test_data = self.read_csv_file(DATA_SPLITS_PATH + 'test_split.csv')

    def read_csv_file(self, path):
        df = pd.read_csv(path)
        df = df[['input','target']]
        return df