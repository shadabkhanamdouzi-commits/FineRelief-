# Testing Guide

## Frontend Testing

### Unit Tests

```bash
cd frontend
npm test
```

Example test:

```javascript
import { render, screen } from '@testing-library/react';
import Login from '../pages/Login';

describe('Login Component', () => {
  test('renders login form', () => {
    render(<Login />);
    expect(screen.getByText(/email/i)).toBeInTheDocument();
  });
});
```

### E2E Tests (Playwright/Cypress)

```bash
# Install
npm install -D cypress

# Run tests
npm run cypress:open
```

## Backend Testing

### Unit Tests

```bash
cd backend
pytest -v
```

Example:

```python
import pytest
from app.financial_engine import calculate_health_score

def test_calculate_health_score():
    score = calculate_health_score(
        income=50000,
        expenses=25000,
        debt=100000
    )
    assert score > 0
    assert score <= 100
```

### Integration Tests

```bash
pytest -v -m integration
```

### API Tests

```bash
pytest tests/test_api.py -v

# Test with coverage
pytest --cov=app --cov-report=html
```

### Load Testing

```bash
pip install locust

# Create locustfile.py and run
locust -f locustfile.py
```

## Running All Tests

### Docker

```bash
docker-compose -f docker-compose.test.yml up
```

### Local

```bash
# Backend
cd backend
pytest --cov=app --cov-report=html

# Frontend
cd frontend
npm test -- --coverage
```

## Continuous Integration

Tests run automatically on:
- Pull requests
- Pushes to main/develop branches
- Scheduled daily runs

View results in GitHub Actions: `.github/workflows/ci-cd.yml`

## Test Coverage Goals

- Backend: Aim for >80% coverage
- Frontend: Aim for >70% coverage
- Critical paths: 100% coverage

Generate coverage reports:

```bash
# Backend
pytest --cov=app --cov-report=html

# Frontend
npm test -- --coverage
```

## Manual Testing

### Checklist

- [ ] User Registration
- [ ] User Login
- [ ] Profile Update
- [ ] Add Loan
- [ ] View Loans
- [ ] Financial Analysis
- [ ] Settlement Prediction
- [ ] AI Negotiation Email
- [ ] Logout

### Browser Testing

Test on:
- Chrome
- Firefox
- Safari
- Edge

### Device Testing

- Desktop
- Tablet
- Mobile

### API Testing

Use Postman/Insomnia:

1. Import API collection
2. Test each endpoint
3. Verify response codes
4. Check error handling

## Performance Testing

```bash
# Lighthouse (Frontend)
npm install -g lighthouse
lighthouse http://localhost:3000 --view

# Backend load test
locust -f locustfile.py --host=http://localhost:8000
```

---

**Run tests before submitting PR!**
