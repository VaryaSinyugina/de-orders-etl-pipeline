from sqlalchemy import text

def load_orders(df, engine):
    print('Loading data')

    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE fact_orders"))

    df.to_sql("fact_orders", engine, if_exists="append", index=False)