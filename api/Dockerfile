FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:0.12.22 /uv /usr/local/bin/uv

WORKDIR /srv

# Avval faqat bog'liqliklar: kod o'zgarsa ham bu qatlam keshdan olinadi.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY app ./app

ENV PATH="/srv/.venv/bin:$PATH"

# root emas, oddiy foydalanuvchi bilan ishlaymiz.
RUN useradd --system --no-create-home appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
