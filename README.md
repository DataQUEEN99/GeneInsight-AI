# GeneInsight AI – Intelligent Genomic Variant Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18.0+-61DAFB.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-20.10+-2496ED.svg)](https://www.docker.com/)

GeneInsight AI is a production-grade, AI-powered genomics platform that combines Retrieval-Augmented Generation (RAG), genomic variant interpretation, biomedical literature retrieval, ACMG evidence reasoning, and an interactive dashboard for genomic research and clinical decision support.

## 🚀 Features

### Core Capabilities
- **Variant Upload & Parsing** - VCF, CSV, TSV, HGVS notation support
- **AI-Powered Variant Interpretation** - Clinical significance, pathogenicity prediction
- **RAG Pipeline** - Semantic retrieval from ClinVar, PubMed, UniProt, OMIM, Gene Ontology
- **Biomedical AI Chat** - Context-aware Q&A with grounded citations
- **ACMG Classification** - Automated ACMG evidence reasoning and classification
- **Interactive Dashboard** - Gene frequency, variant type, disease distribution analytics
- **Report Generation** - PDF, Markdown, JSON, CSV export formats
- **Admin Panel** - User management, knowledge base control, embeddings management

### Technical Excellence
- **Modern UI** - React with Tailwind CSS, ShadCN UI, glassmorphism design
- **Secure Authentication** - JWT with refresh tokens, role-based access control
- **Vector Database** - ChromaDB with Sentence Transformers embeddings
- **LLM Flexibility** - Easy switching between OpenAI GPT and Claude
- **Docker Ready** - Complete containerization with docker-compose
- **CI/CD Pipeline** - GitHub Actions for automated testing and deployment
- **Comprehensive Testing** - Unit and integration tests with >80% coverage

## 📋 Quick Start

### Prerequisites
- Docker & Docker Compose (recommended)
- Or Python 3.10+, Node.js 18+, PostgreSQL 15+
- OpenAI API key or Anthropic API key

### Docker Compose (Fastest)

```bash
git clone https://github.com/DataQUEEN99/GeneInsight-AI.git
cd GeneInsight-AI
cp .env.example .env
# Edit .env with your API keys
docker-compose up --build
```

Access at `http://localhost:3000`

### Local Development

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

## 📚 Documentation

- [Architecture & Design](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Installation Guide](docs/INSTALLATION.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [Database Schema](docs/DATABASE_SCHEMA.md)
- [RAG Pipeline Details](docs/RAG_PIPELINE.md)

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (React/TypeScript)              │
│  Dashboard | Upload | Analysis | Chat | Reports | Admin     │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                 API Gateway (FastAPI)                       │
│  Auth | Upload | Variants | RAG | Chat | Reports | Admin    │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
    PostgreSQL         ChromaDB           LLM API
    (Metadata)      (Embeddings)     (OpenAI/Claude)
```

## 🛠️ Tech Stack

**Backend:** FastAPI, SQLAlchemy, PostgreSQL, Alembic, LangChain, ChromaDB
**Frontend:** React 18, TypeScript, Vite, Tailwind CSS, ShadCN UI, React Query
**AI/ML:** OpenAI GPT-4, Claude 3, Sentence Transformers, Cross-Encoder
**Infrastructure:** Docker, PostgreSQL, ChromaDB, Redis (optional)

## 📁 Project Structure

```
GeneInsight-AI/
├── backend/                 # FastAPI application
├── frontend/                # React application
├── docker/                  # Docker configuration
├── .github/workflows/       # CI/CD pipelines
├── docs/                    # Documentation
├── scripts/                 # Utility scripts
├── docker-compose.yml       # Docker compose config
└── .env.example             # Environment template
```

## 🧪 Testing

```bash
# Backend tests
cd backend && pytest tests/ -v --cov

# Frontend tests
cd frontend && npm run test
```

## 📊 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user
- `POST /api/v1/auth/refresh` - Refresh token

### Variants
- `POST /api/v1/variants/upload` - Upload variant file
- `GET /api/v1/variants/{id}` - Get variant details
- `GET /api/v1/variants/stats` - Get statistics

### Chat & RAG
- `POST /api/v1/chat/message` - Send chat message
- `GET /api/v1/chat/history` - Get chat history

### ACMG
- `POST /api/v1/acmg/classify` - Classify variant

### Reports
- `POST /api/v1/reports/generate` - Generate report
- `GET /api/v1/reports/{id}` - Get report

### Dashboard
- `GET /api/v1/dashboard/summary` - Dashboard data

### Admin
- `GET /api/v1/admin/users` - Manage users
- `GET /api/v1/admin/knowledge-base/stats` - KB statistics

## 🔐 Security

- JWT authentication with refresh tokens
- Role-based access control (RBAC)
- Rate limiting on all endpoints
- Input validation with Pydantic
- SQL injection prevention with SQLAlchemy ORM
- CORS configuration
- Secure password hashing (bcrypt)

## 📈 Performance

- Vector database caching
- Redis support for session management
- Database query optimization
- Async/await for concurrent operations
- Frontend code splitting and lazy loading
- CDN-ready static assets

## 🚀 Deployment

### Docker Compose
```bash
docker-compose up --build
```

### Production Checklist
- [ ] Update `SECRET_KEY` in `.env`
- [ ] Set `DEBUG=false`
- [ ] Configure PostgreSQL credentials
- [ ] Add LLM API keys
- [ ] Set up CORS origins
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Enable HTTPS
- [ ] Configure backups

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazing`)
5. Open Pull Request

Please ensure:
- Code passes linting and tests
- Documentation is updated
- Commits are descriptive

## 📝 License

MIT License - see LICENSE file for details

## 🙋 Support

- GitHub Issues for bug reports
- Check `/docs` for documentation
- Review API docs at `/api/docs`

---

**GeneInsight AI** - Advancing Genomic Discovery with Artificial Intelligence ❤️
