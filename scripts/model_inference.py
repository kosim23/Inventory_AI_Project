import joblib
import pandas as pd
import numpy as np
import os
import sys

# Лойиҳа илдиз папкасини йўлга қўшиш (импортлар хато бермаслиги учун)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.data_ingestion import get_latest_data
from scripts.feature_engineering import prepare_features


def run_inference():
    # 1. Моделни юклаш
    model_path = 'models/demand_forecast_model.pkl'
    if not os.path.exists(model_path):
        print(f"Хато: {model_path} топилмади!")
        return

    model = joblib.load(model_path)

    # 2. Янги маълумотларни олиш
    raw_data = get_latest_data()
    if raw_data is None:
        print("Хато: Маълумотларни юклаб бўлмади.")
        return

    # 3. Хусусиятларни тайёрлаш (Feature Engineering)
    # Бу функция ичида барча 15 та устун (lag_1, price_change ва ҳ.к.) яратилади
    processed_data = prepare_features(raw_data)

    # 4. Башорат қилиш учун устунларни танлаш
    # МОДEЛЬ АЙНАН ШУ ТАРТИБДАГИ УСТУНЛАРНИ КУТМОҚДА:
    features_to_use = [
        'store_id', 'item_id', 'weekday', 'month', 'is_month_start',
        'is_month_end', 'is_weekend', 'lag_1', 'lag_7', 'lag_30',
        'rolling_mean_7', 'rolling_std_7', 'price', 'promo', 'price_change'
    ]

    # Моделга фақат керакли устунларни узатамиз
    try:
        X = processed_data[features_to_use]

        predictions = model.predict(X)
        processed_data['forecast'] = np.round(predictions)

        # 5. Бизнес мантиғи: Safety Stock ва Буюртма (RMSE: 3.43)
        rmse_val = 3.43
        z_score = 1.65  # 95% хизмат даражаси (Service Level) учун

        processed_data['safety_stock'] = np.ceil(z_score * rmse_val).astype(int)
        processed_data['order_recommendation'] = processed_data['forecast'] + processed_data['safety_stock']

        # 6. Натижани сақлаш
        output_path = 'data/processed/forecast_results.csv'
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        processed_data.to_csv(output_path)

        print(f"Башорат муваффақиятли якунланди!")
        print(f"Натижалар '{output_path}' файлига сақланди.")
        print(f"Жами башорат қилинган қаторлар сони: {len(processed_data)}")

    except KeyError as e:
        print(f"Хато: feature_engineering.py баъзи устунларни ярата олмади: {e}")
    except Exception as e:
        print(f"Башорат қилишда кутилмаган хато: {e}")


if __name__ == "__main__":
    run_inference()