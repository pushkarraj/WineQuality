"""read params
process
return dataframe
"""

import os
import yaml
import pandas as pd
import numpy as np
import json
import pickle
import argparse

def read_params(config_path):
    with open (config_path) as f:
        params =yaml.safe_load(f)
        return  params

def get_data(config_path):
    config= read_params(config_path)
    data_path=config['data_source']['s3_source']
    df=pd.read_csv(data_path,sep=',',encoding='utf8')
    return df

#extra comment

if __name__ == "__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config", type=str, default="params.yaml",)
    args.add_argument("--data_path", type=str, default="./data")
    parsed_args=args.parse_args()
    data=get_data(parsed_args.config)


