import pandas as pd

def get_metrics(df):
    '''
    return DataFrames:
    metrics_node, metrics_relation 
    '''
    df['time_stamp_start'] = pd.to_datetime(df.time_stamp_start)
    df['time_stamp_end']   = pd.to_datetime(df.time_stamp_end)

    metrics_relation = df.groupby(['url_start','url_end']).agg({'diff':['mean','max','min','sum','count'],'reload':['mean'], 'process_flag_num':['mean']})
    metrics_relation.columns = [ '_'.join(col) for col in metrics_relation.columns]
    metrics_relation = metrics_relation.rename(columns={'diff_count':'qty_rel_all','process_flag_num_mean':'process_order_mean','reload_mean':'is_reload'})
    metrics_relation = metrics_relation.reset_index()

    qty_all = df.groupby('url_start').count().rename(columns={'clientcode':'qty_all'})[['qty_all']]
    qty_unique_user = df[['clientcode','url_start']].drop_duplicates().groupby('url_start').count().rename(columns={'clientcode':'qty_unique_user'})
    qty_in = metrics_relation.reset_index().groupby('url_start').sum().rename(columns = {'qty_rel_all':'qty'})
    qty_in.columns = qty_in.columns+'_in'
    qty_out = metrics_relation.reset_index().groupby('url_end').sum().rename(columns = {'qty_rel_all':'qty'})
    qty_out.columns = qty_out.columns+'_out'

    metrics_node = pd.merge(qty_all,qty_unique_user,left_index=True, right_index=True, how = 'left')
    metrics_node = pd.merge(metrics_node,qty_in,left_index=True, right_index=True, how = 'left')
    metrics_node = pd.merge(metrics_node,qty_out,left_index=True, right_index=True, how = 'left')
    metrics_node['qty_in_out_ratio'] = metrics_node.qty_in/metrics_node.qty_out
    metrics_node = metrics_node.reset_index()

    return metrics_node, metrics_relation