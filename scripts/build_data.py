from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
    if 'reporting_status' in meta:
        del meta['reporting_status']
    return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
