FROM python:3.11-slim

ENV PROJECT_DIR="/app" \
    # python:
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # poetry:
    POETRY_HOME="/opt/poetry" \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Prepend poetry and venv to path
ENV PATH="${POETRY_HOME}/bin:${VENV_PATH}/bin:${PATH}"

# System deps:
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential \
    curl \
    libpq-dev \
    # cache cleaning:
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* 

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set work directory
WORKDIR ${PROJECT_DIR}
COPY pyproject.toml poetry.lock ${PROJECT_DIR}

# Install dependencies
RUN poetry install --no-root --without dev

# Expose port
EXPOSE 8000

# Copy project
COPY . .

# Install project:
RUN poetry install --only-root

# Make scripts executable
RUN chmod +x ./scripts/*

# Start Application
CMD [ "./scripts/run-server.sh"]
