FROM python:3.10-slim AS builder
WORKDIR /app
COPY app.py requirements.txt /app/
RUN pip install --no-cache-dir --target=/app/libs -r requirements.txt

FROM gcr.io/distroless/python3
WORKDIR /app
COPY --from=builder /app /app
ENV PYTHONPATH=/app/libs
CMD ["app.py"]