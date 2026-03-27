from sqlalchemy import create_engine
from scripts.extract import extract_orders
from scripts.transform import transform_orders
from scripts.load import load_orders
from scripts.quality_checks import run_quality_checks
import os

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}"
)

def main():
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        df = extract_orders(os.path.join(base_path, "data/raw/orders.csv"))
        df = transform_orders(df)
        run_quality_checks(df)
        load_orders(df, engine)
        print("ETL completed successfully")

    except Exception as e:
        print(f"ETL failed: {e}")
        raise

if __name__ == "__main__":
    main()
