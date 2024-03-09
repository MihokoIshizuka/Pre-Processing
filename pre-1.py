import pandas as pd

def main():
    reserve_tb = pd.read_csv('./data/reserve.csv')
    # 配列に文字配列を指定
    print(reserve_tb[['reserve_id','hotel_id','customer_id','reserve_datetime']])

    # loc関数の二次元配列の二次元目に抽出したい列名を指定
    print(reserve_tb.loc[:,['reserve_id','hotel_id','customer_id','reserve_datetime']])

    # 不要な列をdropで削除する
    reserve_tb_drop = reserve_tb.drop(['people_num','total_price'], axis=1)
    print(reserve_tb_drop)
if __name__ == "__main__":
    main()