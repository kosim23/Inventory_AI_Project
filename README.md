# 📦 AI-Powered Inventory Management System

Бу тизим чакана савдо (retail) соҳасида заҳираларни бошқариш ва сотувларни башорат қилиш учун мўлжалланган интеллектуал ечимдир.

## 🚀 Лойиҳа мақсади
Бизнесдаги иккита асосий муаммони ҳал қилиш:
1. **Stockout (Товар етишмовчилиги):** Сотувларни бой беришнинг олдини олиш.
2. **Overstock (Ортиқча заҳира):** Омборда пул "музлаб" қолишини камайтириш.

## 📊 Асосий кўрсаткичлар (KPI)
* **Аниқлик (Model Accuracy):** 88.52%
* **Stockout Risk:** 3.2% (минимал даражада)
* **Service Level:** 95% хизмат кўрсатиш кафолати

## 🛠 Технологик стек
- **ML Моделлар:** XGBoost, LightGBM (Stacking Regressor)
- **Dashboard:** Streamlit (Интерактив бошқарув панели)
- **Containerization:** Docker & Docker Compose
- **Data Engineering:** Python, Pandas, Scikit-learn

## 💻 Ишга тушириш
1. Лойиҳани клонлаш: `git clone https://github.com/kosim23/Inventory_AI_Project.git`
2. Кутубхоналарни ўрнатиш: `pip install -r requirements.txt`
3. Веб-интерфейсни юргизиш: `streamlit run web_app/app.py`

## 📈 Бизнес учун қиймат (Value)
Тизим шунчаки график чизмайди, балки ҳар бир товар учун **"Order Recommendation" (Қанча сотиб олиш керак?)** деган аниқ сонни тавсия қилади. Бу эса харид бўлими иш самарадорлигини 5 бараварга оширади.
