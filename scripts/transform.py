import pandas

def transform_orders(df: pandas.DataFrame) -> pandas.DataFrame:
    print('Transforming data')

    df["order_date"] = pandas.to_datetime(df["order_date"])
    df["total_amount"] = df["quantity"] * df["price"]

    return df[[
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "total_amount"
    ]]