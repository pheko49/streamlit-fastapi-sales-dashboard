import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "superstore.db"

# You need to query the following:
# -Database exists ✅  
# -Table exists ✅  
# -Data exists ✅  
# -Queries work ✅  

def get_connection():
    return sqlite3.connect(DB_PATH)

def preview_data():
    conn = get_connection()

    df = pd.read_sql("SELECT * FROM superstore LIMIT 5", conn)

    print(df)

    return df
    
    conn.close()

if __name__ == "__main__":
    preview_data()


# Check if tables exist

def show_tables():
    conn = get_connection()

    query = "SELECT name FROM sqlite_master WHERE type='table'"

    tables = pd.read_sql(query, conn)

    print(tables)


    conn.close()

if __name__ == '__main__':
    show_tables()

# Continue with step 3 before moving to API
def get_sales_by_region():
    conn = get_connection()

    query = """
    SELECT Region, SUM(Sales) as total_sales
    FROM superstore
    GROUP BY Region
    """

    df = pd.read_sql(
        sql=query,
        con=conn
    )

    print(df)

    conn.close()

    return df

if __name__ == '__main__':
    get_sales_by_region()


# get the full dataset
def get_superstore_data():
    conn = get_connection()

    query = "SELECT * FROM superstore"

    df = pd.read_sql(
        sql=query,
        con=conn
    )

    print(df)


    conn.close()

    return df

if __name__ == '__main__':
    get_superstore_data()

def get_profit_by_category():
    conn = get_connection()

    query = """
    SELECT Category, SUM(Sales) as total_profit
    FROM superstore
    GROUP BY Category"""

    df = pd.read_sql(
        sql=query,
        con=conn
    )

    print(df)

    conn.close()

    return df

if __name__ == '__main__':
    get_profit_by_category()


def get_profit_by_segment():
    conn = get_connection()

    query = """
    SELECT Segment, SUM(Profit) as total_profit
    FROM superstore
    GROUP BY Segment
    """

    df = pd.read_sql(
        sql=query,
        con=conn
    )

    conn.close()

    print(df)

    return df

if __name__ == '__main__':
    get_profit_by_segment()


def get_top_states_by_sales():
    conn = get_connection()

    query = """
    SELECT State, Sum(Sales) AS total_sales
    FROM superstore
    GROUP BY State
    ORDER BY total_sales DESC
    LIMIT 10
    """

    df = pd.read_sql(
        sql=query,
        con=conn
    )

    conn.close()

    print(df)

    return df

if __name__ == '__main__':
    get_top_states_by_sales()