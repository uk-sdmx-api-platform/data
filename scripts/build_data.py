from sdg.open_sdg import open_sdg_build
import pandas as pd
import numpy as np

def alter_meta(meta, context):
    if 'reporting_status' in meta:
        del meta['reporting_status']
    if context['indicator_id']:
        print(context['indicator_id'])
    meta["data_start_values"]=[{"field":"Reporting type","value":"National"}]
    for meta_field in all_meta_fields:
       if meta_field not in meta or meta[meta_field] is None:
          meta[meta_field]='Not available for this indicator'
    return meta

def alter_data(df, context):
    if context['indicator_id'] == '1-1-1':
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(df)
    if 'Reference area' in df.columns:
        df["Reference area"].replace({"United Kingdom of Great Britain and Northern Ireland":""}, inplace=True)
        if df['Reference area'].replace(r'^\s*$', np.nan, regex=True).isna().all():
            df = df.drop('Reference area', 1)
        if context['indicator_id'] == '1-1-1':
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(df)
    if 'REF_AREA' in df.columns:
        df["REF_AREA"].replace({"826":""}, inplace=True)
        if df['REF_AREA'].replace(r'^\s*$', np.nan, regex=True).isna().all():
            df = df.drop('REF_AREA', 1)
        if context['indicator_id'] == '1-1-1':
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(df)
    special_cols = ['Year', 'Value', 'Reporting type', 'REPORTING_TYPE', 'Units', 'UNIT_MEASURE', 'UNIT_MULT', 'Unit multiplier', 'Series', 'SERIES', 'OBS_STATUS', 'Observation status']
    for col in df.columns:
        if col in special_cols:
            continue
        if len(df[col].unique()) == 1:
            df.drop(col, inplace=True, axis=1)
    return df
    

open_sdg_build(config='config_data.yml', alter_meta=alter_meta, alter_data=alter_data)
