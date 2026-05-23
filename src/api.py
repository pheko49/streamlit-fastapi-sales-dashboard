from fastapi import FastAPI
from src.queries import get_sales_by_region
from src.queries import preview_data
from src.queries import get_superstore_data
from src.queries import get_profit_by_category
from src.queries import get_profit_by_segment
from src.queries import get_top_states_by_sales

app = FastAPI()

@app.get('/sales_by_region')
async def get_sales():
    df = get_sales_by_region()
    return df.to_dict(orient='records')

@app.get('/preview_data')
async def data_preview():
    df = preview_data()
    return df.to_dict(orient='records')

@app.get('/superstore_data')
async def get_full_dataset():
    df = get_superstore_data()

    return df.to_dict(orient='records')


@app.get('/profit_by_category')
async def get_profit():
    df = get_profit_by_category()

    return df.to_dict(orient='records')

@app.get('/profit_by_segment')
async def get_segment_profit():
    df = get_profit_by_segment()

    return df.to_dict(orient='records')

@app.get('/top_state_sales')
async def get_top_sales_by_state():
    df = get_top_states_by_sales()

    return df.to_dict(orient='records')