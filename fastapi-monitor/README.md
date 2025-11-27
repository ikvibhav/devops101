# FastAPI Monitor

A real-time monitoring solution for CPU and memory usage systems

## Features

- Real-time application metrics collection
- Dashboard integration ready

## Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-monitor
```

2. Create and activate a virtual environment
```bash
# Unix / macOS
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Using Docker Compose

If a docker-compose.yml is provided, build and start the service with:
```bash
# build and run in foreground
docker compose up --build

# build and run in detached mode
docker compose up --build -d

# stop and remove containers
docker compose down
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Future Work
[planned](./docs/future_work.md)
