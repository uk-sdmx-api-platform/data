from sdg.open_sdg import open_sdg_build
import pandas as pd

def alter_meta(meta, context):
    if 'reporting_status' in meta:
        del meta['reporting_status']
    if context['indicator_id']:
        print(context['indicator_id'])
    return meta

def alter_data(df):
    if 'Reference area' in df.columns:
        for row in df.intertuples():
            if row.Reference_area == 'United Kingdom of Great Britain and Northern Ireland':
                row.Reference_area = ''
        if df['Reference area'].replace(r'^\s*$', np.nan, regex=True).isna().all():
            df = df.drop('Reference area', 1)
    return df
    

open_sdg_build(config='config_data.yml', alter_meta=alter_meta, alter_data=alter_data)
