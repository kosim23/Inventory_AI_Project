import pandas as pd
import numpy as np


def prepare_features(df):
    df = df.copy()

    # Индексни текшириш
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index)

    # 1. Вақт хусусиятлари (Модель сўраётганлари)
    df['weekday'] = df.index.weekday
    df['month'] = df.index.month
    df['is_month_start'] = df.index.is_month_start.astype(int)
    df['is_month_end'] = df.index.is_month_end.astype(int)
    df['is_weekend'] = df['weekday'].isin([5, 6]).astype(int)

    # 2. Лаглар (Lags)
    df['lag_1'] = df.groupby(['store_id', 'item_id'])['sales'].shift(1)
    df['lag_7'] = df.groupby(['store_id', 'item_id'])['sales'].shift(7)
    df['lag_30'] = df.groupby(['store_id', 'item_id'])['sales'].shift(30)

    # 3. Rolling статистик кўрсаткичлар
    df['rolling_mean_7'] = df.groupby(['store_id', 'item_id'])['sales'].transform(
        lambda x: x.shift(1).rolling(window=7).mean())
    df['rolling_std_7'] = df.groupby(['store_id', 'item_id'])['sales'].transform(
        lambda x: x.shift(1).rolling(window=7).std())

    # 4. Нарх ва Промо (Агар оригинал датасетда бўлса)
    # Агар бу устунлар бўлмаса, хато бермаслиги учун 0 ёки ўртача қиймат қўямиз
    if 'price' not in df.columns:
        df['price'] = 53.99  # Сиз топган ўртача нарх

    if 'promo' not in df.columns:
        df['promo'] = 0

    df['price_change'] = df.groupby(['store_id', 'item_id'])['price'].pct_change()

    # NaN қийматларни тўлдириш (бу жуда муҳим!)
    df = df.fillna(0)
    # pct_change дан чиққан инфинити қийматларни тузатиш
    df.replace([np.inf, -np.inf], 0, inplace=True)

    return df