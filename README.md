# AI-Powered Inventory Management System 📦🚀

Бу тизим чакана савдо дўконлари учун талабни башорат қилиш ва заҳираларни оптималлаштириш мақсадида яратилган.

## ✨ Асосий хусусиятлар
* **ML Model:** XGBoost ва LightGBM асосидаги Stacking Regressor (88.52% аниқлик).
* **Feature Engineering:** Вақт динамикаси (Lags, Rolling windows), байрамлар ва нарх ўзгариши таҳлили.
* **Inference Engine:** Ҳар кунлик башорат ва "Safety Stock" (Хавфсиз заҳира) ҳисоби.
* **Web Interface:** Streamlit асосидаги интерактив бошқарув панели.
* **Automation:** Docker ва Apache Airflow орқали тўлиқ автоматик ETL жараёни (Концепт).

## 📊 Бизнес учун самарадорлик
- **Stockout Risk:** 3.2% (Товар тугаб қолиш хавфи пасайтирилган).
- **Service Level:** 95% хизмат кўрсатиш даражаси.
- **Lost Sales Reduction:** Савдо бой берилишининг олдини олиш.

## 🚀 Ишга тушириш
1. Кутубхоналарни ўрнатиш: `pip install -r requirements.txt`
2. Веб-интерфейсни очиш: `streamlit run web_app/app.py`
3. Docker орқали ишга тушириш (Инфратузилма): `docker-compose up --build`

---
*Developed as a Data Engineering Solution for Retail Business.*