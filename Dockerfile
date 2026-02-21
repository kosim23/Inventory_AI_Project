# Python-нинг енгил версиясидан бошлаймиз
FROM python:3.9-slim

# Ишчи папкани белгилаймиз
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgomp1 \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Керакли кутубхоналарни нусхалаймиз ва ўрнатамиз
COPY requirements.txt .
# requirements.txt ни ўрнатишда тайм-аутни оширамиз
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

# Лойиҳа файлларни контейнер ичига кўчирамиз
COPY . .

# Streamlit учун портни очиб қўямиз
EXPOSE 8501

# Ҳозирча шунчаки контейнер ишлашини таъминлаймиз
CMD ["python", "scripts/model_inference.py"]