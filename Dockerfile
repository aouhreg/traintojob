# 使用官方 Python 3.13 slim image
FROM python:3.13-slim

# 設定工作目錄
WORKDIR /app

# 複製需求檔
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案
COPY ./app ./app

# 開放port
EXPOSE 8000

# 啓動API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]