FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit uses 8501 by default, but we respect OpenShift PORT env
ENV PORT=8501

# Expose the port for OpenShift
EXPOSE 8501

# Run Streamlit with env-port support
CMD streamlit run app.py --server.port $PORT --server.enableCORS false --server.headless true