
FROM python:3.12
LABEL authors="faati"

WORKDIR /

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . .
EXPOSE 5000

CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0", "--port=5000"]