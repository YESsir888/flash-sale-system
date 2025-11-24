### **【完整README.md内容】**

```markdown
# Flash Sale System

A high-performance flash sale system built with Flask, designed to handle high-concurrency seckill scenarios.

## Performance Benchmark

- **Current**: 100+ requests/second (single instance)
- **Future**: 10k+ requests/second (with Redis & MQ)

## Quick Start

```bash
pip install flask
python app.py
```

## API Endpoints

### Health Check
```http
GET /health
# Response: {"code":200,"status":"healthy"}
```

### Seckill
```http
POST /seckill
Content-Type: application/json

{
    "product_id": "iPhone15",
    "user_id": "user123"
}
```

## Architecture

```plaintext
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Flask API   │
│ (Rate Limiting) │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Redis     │  ← Cache & Counter
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Message Q   │  ← Async Processing
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   MySQL     │  ← Order Storage
└─────────────┘
```

## Tech Stack

- **Framework**: Flask
- **Language**: Python 3.8+
- **Extensions**: Flask-RESTful, Flask-Limiter
- **Database**: Redis, MySQL
- **Message Queue**: RabbitMQ

## Next Steps

- [x] Add Redis for rate limiting
- [ ] Implement database transactions
- [ ] Add unit tests with pytest
- [ ] Deploy to AWS/GCP

## Author

YESsir888 - Initial work
