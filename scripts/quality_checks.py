def run_quality_checks(df):
    print('Running data quality checks')

    assert df["order_id"].isnull().sum() == 0
    assert df["order_date"].isnull().sum() == 0
    assert (df["quantity"] > 0).all()
    assert (df["total_amount"] >= 0).all()