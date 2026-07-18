# Contributing Guidelines

Thank you for contributing to FineRelief! We appreciate your help in improving this project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/FineRelief-.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Push to your fork
6. Create a Pull Request

## Development Setup

### Using Docker (Recommended)

```bash
docker-compose up --build
```

### Local Setup

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

## Code Style

### Python (Backend)

We use PEP 8 style guide:

```bash
# Format code
pip install black
black app/

# Check style
pip install flake8
flake8 app/
```

### JavaScript (Frontend)

We use Airbnb style guide:

```bash
# Check style
npm run lint
```

## Commit Messages

Follow conventional commits:

```
type(scope): subject

body (optional)

footer (optional)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code refactoring
- `test`: Tests
- `ci`: CI/CD changes
- `chore`: Dependencies/maintenance

**Examples:**
```
feat(auth): add Google OAuth login
fix(settlement): correct calculation algorithm
docs(api): update endpoint documentation
```

## Testing

### Backend Tests

```bash
cd backend
pytest -v
pytest --cov=app  # with coverage
```

Write tests in `tests/` directory:

```python
import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Pull Request Process

1. **Update tests** - Add tests for new features
2. **Update docs** - Update relevant documentation
3. **Describe changes** - Clear PR description
4. **Wait for review** - Address review comments
5. **Pass CI/CD** - All checks must pass

**PR Template:**

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation

## Testing
How was this tested?

## Checklist
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Issues

### Reporting Bugs

Include:
- Clear description
- Steps to reproduce
- Expected behavior
- Actual behavior
- System info (OS, Python/Node version, etc.)

### Feature Requests

Include:
- Clear description
- Use case
- Example implementation (optional)

## Code Review

We appreciate your patience during code review. Reviewers may ask for:
- Changes to coding style
- Additional tests
- Documentation updates
- Performance improvements

## Recognition

Contributors will be recognized in:
- README.md
- Release notes
- GitHub contributors page

## Questions?

- Open an issue with the `question` label
- Check existing issues/discussions first
- Ask in pull request comments

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Respect diverse opinions
- Report inappropriate behavior

---

**Thank you for contributing to FineRelief! 🎉**
