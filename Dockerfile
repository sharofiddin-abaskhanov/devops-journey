# Base image — Python 3.11, Alpine (yengil, ~50MB)
FROM python:3.11-alpine

# Konteyner ichida ishchi papka
WORKDIR /app

# Avval faqat requirements copy qilamiz (cache uchun)
COPY requirements.txt .

# Dependencylarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Qolgan fayllarni copy qilamiz
COPY . .

# Flask port
EXPOSE 5000

# App ishga tushirish
CMD ["python", "app.py"]
