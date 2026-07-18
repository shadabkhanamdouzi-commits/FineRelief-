# API Documentation

## Base URL

- **Development**: `http://localhost:8000`
- **Production**: `https://your-domain.com`

## Swagger UI

Interactive API documentation available at:
- `/docs` - Swagger UI
- `/redoc` - ReDoc

## Authentication

All endpoints requiring authentication use JWT Bearer tokens.

```bash
Authorization: Bearer <token>
```

## Response Format

### Success Response
```json
{
  "status": "success",
  "data": { ... },
  "message": "Operation successful"
}
```

### Error Response
```json
{
  "status": "error",
  "error": "Error code",
  "message": "Error description",
  "details": { ... }
}
```

## Endpoints

### Authentication

#### Register User
```
POST /api/register
```

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe"
}
```

**Response:** (201 Created)
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "John Doe"
}
```

#### Login
```
POST /api/login
```

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:** (200 OK)
```json
{
  "access_token": "eyJ0eXAi...",
  "token_type": "bearer",
  "user": { ... }
}
```

### Users

#### Get Current User
```
GET /api/users/me
```

**Headers:** `Authorization: Bearer <token>`

**Response:** (200 OK)
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "John Doe",
  "created_at": "2024-01-01T10:00:00Z"
}
```

#### Update Profile
```
PUT /api/users/profile
```

**Headers:** `Authorization: Bearer <token>`

**Request:**
```json
{
  "name": "Jane Doe",
  "phone": "+1234567890",
  "address": "123 Main St"
}
```

### Loans

#### Create Loan
```
POST /api/loans
```

**Headers:** `Authorization: Bearer <token>`

**Request:**
```json
{
  "loan_id": "LOAN123",
  "amount": 50000,
  "interest_rate": 12.5,
  "tenure_months": 60,
  "status": "active"
}
```

#### Get Loans
```
GET /api/loans
```

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `status` - active, closed, defaulted
- `limit` - max 100
- `offset` - pagination

#### Get Loan Details
```
GET /api/loans/{loan_id}
```

**Headers:** `Authorization: Bearer <token>`

### Financial Health

#### Analyze Financial Health
```
POST /api/financial/health
```

**Headers:** `Authorization: Bearer <token>`

**Request:**
```json
{
  "monthly_income": 50000,
  "monthly_expenses": 25000,
  "total_debt": 500000,
  "savings": 100000
}
```

**Response:**
```json
{
  "health_score": 65,
  "status": "moderate",
  "debt_to_income_ratio": 10,
  "recommendations": [...]
}
```

### Settlement Prediction

#### Predict Settlement
```
POST /api/settlement/predict
```

**Headers:** `Authorization: Bearer <token>`

**Request:**
```json
{
  "loan_amount": 50000,
  "current_balance": 45000,
  "monthly_payment": 1000,
  "payment_history": {
    "on_time": 45,
    "late": 5,
    "default": 0
  }
}
```

**Response:**
```json
{
  "settlement_probability": 0.75,
  "suggested_amount": 42000,
  "confidence": 0.85,
  "explanation": "..."
}
```

### AI Negotiation

#### Generate Negotiation Strategy
```
POST /api/ai/negotiate
```

**Headers:** `Authorization: Bearer <token>`

**Request:**
```json
{
  "loan_id": "LOAN123",
  "creditor_name": "Bank XYZ",
  "desired_settlement": 42000,
  "tone": "formal"
}
```

**Response:**
```json
{
  "email_draft": "...",
  "talking_points": [...],
  "alternative_offers": [...],
  "confidence_score": 0.82
}
```

## Error Codes

| Code | Meaning |
|------|---------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Unprocessable Entity |
| 500 | Internal Server Error |

## Rate Limiting

- **Default**: 100 requests per minute per user
- **Premium**: Unlimited

## Rate Limit Headers

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1704110400
```

## Testing

### Using cURL

```bash
# Register
curl -X POST http://localhost:8000/api/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123",
    "name": "Test User"
  }'

# Login
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123"
  }'

# Get user (with token)
curl -X GET http://localhost:8000/api/users/me \
  -H "Authorization: Bearer <token>"
```

### Using Postman

1. Import the Swagger JSON: `http://localhost:8000/openapi.json`
2. Set up environment variables for token
3. Use pre-configured requests

### Using Python

```python
import requests

BASE_URL = "http://localhost:8000"

# Login
response = requests.post(f"{BASE_URL}/api/login", json={
    "email": "test@example.com",
    "password": "test123"
})
token = response.json()["access_token"]

# Get user
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{BASE_URL}/api/users/me", headers=headers)
print(response.json())
```

## Webhooks (Future)

Webhooks for loan status updates coming soon:

```
POST https://your-webhook-url.com/webhook
```

Payload:
```json
{
  "event": "loan_status_changed",
  "loan_id": "LOAN123",
  "new_status": "settled",
  "timestamp": "2024-01-01T10:00:00Z"
}
```

## API Versioning

Current version: `v1`

Future versions will use `/api/v2/`, `/api/v3/`, etc.

---

**Last Updated:** 2024-01-01
**OpenAPI Spec:** `/openapi.json`
