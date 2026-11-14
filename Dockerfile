
# Red Hat UBI 9 with Python 3.12
FROM registry.access.redhat.com/ubi9/python-312:latest

# Python environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install operating system dependencies
USER 0

RUN dnf install -y \
    curl \
    ca-certificates \
    gcc \
    gcc-c++ \
    unixODBC \
    unixODBC-devel \
    && dnf clean all

# Configure Microsoft SQL Server repository
RUN curl -fsSL \
    https://packages.microsoft.com/config/rhel/9/prod.repo \
    -o /etc/yum.repos.d/mssql-release.repo

# Install Microsoft ODBC Driver 18
RUN ACCEPT_EULA=Y dnf install -y msodbcsql18 \
    && dnf clean all

# Application directory
WORKDIR /opt/app-root/src

# Copy Python dependencies
COPY requirements.txt .

# Install Python dependencies
RUN python3.12 -m venv /opt/app-root/venv \
    && /opt/app-root/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/app-root/venv/bin/pip install --no-cache-dir -r requirements.txt

# Configure Python path
ENV PATH="/opt/app-root/venv/bin:$PATH"

# Copy application
COPY --chown=1001:0 app/ ./app/

# Run as non-root user
USER 1001

# Application port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
