from sdg.open_sdg import open_sdg_build
import pandas as pd
import numpy as np

all_meta_fields=['CONTACT_ORGANISATION', 'CONTACT_ORGANISATION__GLOBAL', 'CONTACT_NAME', 'CONTACT_NAME__GLOBAL', 'ORGANISATION_UNIT', 'ORGANISATION_UNIT__GLOBAL',
                'CONTACT_FUNCT', 'CONTACT_FUNCT__GLOBAL', 'CONTACT_PHONE', 'CONTACT_PHONE__GLOBAL', 'CONTACT_MAIL', 'CONTACT_MAIL__GLOBAL',
                'CONTACT_EMAIL', 'CONTACT_EMAIL__GLOBAL', 'STAT_CONC_DEF', 'STAT_CONC_DEF__GLOBAL', 'UNIT_MEASURE', 'UNIT_MEASURE__GLOBAL',
                'CLASS_SYSTEM', 'CLASS_SYSTEM__GLOBAL', 'SOURCE_TYPE', 'SOURCE_TYPE__GLOBAL', 'COLL_METHOD', 'COLL_METHOD__GLOBAL', 'FREQ_COLL', 'FREQ_COLL__GLOBAL',
                'REL_CAL_POLICY', 'REL_CAL_POLICY__GLOBAL', 'DATA_SOURCE', 'DATA_SOURCE__GLOBAL', 'COMPILING_ORG', 'COMPILING_ORG__GLOBAL',
                'INST_MANDATE', 'INST_MANDATE__GLOBAL', 'RATIONALE', 'RATIONALE__GLOBAL', 'REC_USE_LIM', 'REC_USE_LIM__GLOBAL', 'DATA_COMP', 'DATA_COMP__GLOBAL',
                'ADJUSTMENT', 'ADJUSTMENT__GLOBAL', 'IMPUTATION', 'IMPUTATION__GLOBAL', 'REG_AGG', 'REG_AGG__GLOBAL', 'DOC_METHOD', 'DOC_METHOD__GLOBAL',
                'QUALITY_MGMNT', 'QUALITY_MGMNT__GLOBAL', 'QUALITY_ASSURE', 'QUALITY_ASSURE__GLOBAL', 'QUALITY_ASSMNT', 'QUALITY_ASSMNT__GLOBAL',
                'COVERAGE', 'COVERAGE__GLOBAL', 'COMPARABILITY', 'COMPARABILITY__GLOBAL', 'OTHER_DOC', 'OTHER_DOC__GLOBAL']

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
