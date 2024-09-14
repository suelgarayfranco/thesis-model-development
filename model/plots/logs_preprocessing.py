import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

BASE_PATH = "model/training-logs"

models = ['latex', 'latex-ner', 'latex-trees', 'complete']

for model in models:
    logs_df = pd.read_json(f"{BASE_PATH}/train-{model}-log.json")

    loss_logs = logs_df.loc[logs_df['loss'].notnull()]
    eval_loss_logs = logs_df.loc[logs_df['eval_loss'].notnull()]

    loss_logs = loss_logs[['epoch', 'loss']]
    loss_logs['type'] = 'training'

    eval_loss_logs = eval_loss_logs[['epoch', 'eval_loss']].rename(columns={'eval_loss':'loss'})
    eval_loss_logs['type'] = 'evaluation'

    df = pd.concat([loss_logs, eval_loss_logs])

    df.to_csv(f"{model}-loss.csv")
