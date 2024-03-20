import pandas as pd
import numpy as np

def main():
    # 3-2
    reserve_tb = pd.read_csv('./data/reserve.csv')
    result = reserve_tb.groupby(['hotel_id','people_num'])['total_price'].sum().reset_index()
    result.rename(columns={'total_price':'price_sum'},inplace=True)
    print(result)

    # 3-3
    result2 = reserve_tb\
        .groupby('hotel_id')\
        .agg({'total_price': ['max','min','mean','median',
                              lambda x: np.percentile(x, q=20)]}).reset_index()
    result2.columns = ['hotel_id','price_max','price_min','proce_mean','price_median','price_20per']
    print(result2)

    #3-4
    result3 = reserve_tb.groupby('hotel_id').agg({'total_price':['var','std']}).reset_index()
    result3.columns = ['hotel_id','var_price','std_price']
    result3.fillna(0,inplace=True)
    print(result3)

    #3-5
    result4 = reserve_tb['total_price'].round(-3).mode()
    print(result4)

    #3-6
    result5 = reserve_tb
    result5['log_no'] = reserve_tb.groupby('customer_id')['reserve_datetime'].rank(ascending=True, method='first')
    print(result5)

    #3-7
    result6 = reserve_tb.groupby('hotel_id').size().reset_index()
    result6.columns = ['hotel_id','rsv_cnt']
    result6['rsv_cnt_rank'] = result6['rsv_cnt'].rank(ascending=False,method='min')
    result6.drop('rsv_cnt',axis=1,inplace=True)
    print(result6)

if __name__ == "__main__":
    main()