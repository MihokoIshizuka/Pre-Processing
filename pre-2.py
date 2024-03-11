import pandas as pd

def main():
    # not awesome
    reserve_tb = pd.read_csv('./data/reserve.csv')
    rsv_cnt = reserve_tb.groupby('hotel_id').size().reset_index()
    rsv_cnt.columns = ['hotel_id','rsv_cnt']
    cus_cnt = \
        reserve_tb.groupby('hotel_id')['customer_id'].nunique().reset_index()
    cus_cnt.columns = ['hotel_id','cus_cnt']
    merge = pd.merge(rsv_cnt, cus_cnt, on='hotel_id')
    print(merge)

    # awesome
    result = reserve_tb.groupby('hotel_id').agg({'reserve_id': 'count','customer_id': 'nunique'})
    result.reset_index(inplace=True)
    result.columns = ['hotel_id','rsv_id','cus_cnt']
    print(result)
if __name__ == "__main__":
    main()