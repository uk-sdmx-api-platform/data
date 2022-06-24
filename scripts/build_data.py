from sdg.open_sdg import open_sdg_build
import pandas as pd

def alter_meta(meta, context):
    if 'reporting_status' in meta:
        del meta['reporting_status']
    if context['indicator_id']:
        print(context['indicator_id'])
    return meta

def alter_data(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
    return df
    

open_sdg_build(config='config_data.yml', alter_meta=alter_meta, alter_data=alter_data)
