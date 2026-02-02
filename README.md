# FinTech Payment API 

A cloud-native payment transaction API demonstrating modern DevOps practices, Infrastructure as Code, and containerized application deployment on AWS.

> **Status:** Work in Progress - Actively developing production ready infrastructure and CI/CD automation

## Project Overview

This repo showcases end to end implementation of a production grade payment API with complete infrastructure automation. Built to demonstrate proficiency in cloud infrastructure, containerization, database management, and CI/CD pipeline design.

**Key Achievement:** Full Infrastructure as Code (IaC) approach with zero manual AWS console configuration.

## Tech Stack

**Backend & API:**
- Python 3.14 with FastAPI framework
- PostgreSQL 16 for transactional data persistence
- SQLModel for ORM and data validation
- Pydantic for request/response schemas

**Infrastructure & DevOps:**
- **Terraform** - Full IaC for AWS resource provisioning
- **Docker** - Multi-stage containerization with optimized image builds
- **AWS Services** - VPC, ECS Fargate, RDS, ALB, ECR, NAT Gateway
- **GitHub Actions** - Automated testing, building, and deployment pipeline

**Local Development:**
- Docker Compose for local development environment
- Hot-reload enabled API container
- Containerized PostgreSQL with health checks

## Architecture Highlights

### Network Design
- Custom VPC with public/private subnet architecture
- Internet Gateway for public subnet internet access
- NAT Gateway enabling private subnet outbound connectivity
- Route tables configured for proper traffic flow

### Security & Best Practices
- Database isolated in private subnet (no direct internet exposure)
- Application containers deployed in ECS with private subnet placement
- ALB handling external traffic in public subnet
- Environment-based configuration management
- Health check endpoints for monitoring and orchestration

### API Endpoints
```
POST /transactions        - Create new payment transaction
GET  /transactions/{id}   - Retrieve transaction by ID
GET  /health             - Health check endpoint
```

## Infrastructure as Code

The Terraform configuration provisions:
- **VPC Module**: Custom networking with public/private subnets, IGW, NAT Gateway
- **ECS Cluster**: Fargate-based container orchestration (In Progress)
- **RDS PostgreSQL**: Managed database in private subnet (In Progress)
- **Application Load Balancer**: Traffic distribution and SSL termination (In Progress)
- **ECR Repository**: Container image registry (In Progress)

## CI/CD Pipeline (In Progress)

GitHub Actions workflow implementing:
1. Automated test execution on pull requests
2. Docker image building with layer caching
3. Image pushing to Amazon ECR
4. ECS service deployment with rolling updates

## Local Development

Run the complete stack locally:

```bash
# Start PostgreSQL and API containers
docker-compose up

# API available at http://localhost:8000
# PostgreSQL accessible on port 5432
```

The local setup includes:
- PostgreSQL 16 with persistent volume storage
- API container with hot-reload for development
- Health check monitoring for service readiness
- Isolated Docker network for service communication

## Engineering Decisions

**Why Terraform over CloudFormation?**
- Cloud agnostic skillset demonstration
- Superior state management and module reusability
- Industry standard for multi-cloud infrastructure

**Why FastAPI?**
- High performance async capabilities for payment processing
- Automatic OpenAPI documentation generation
- Built-in request validation reducing error handling code

**Why ECS Fargate over EC2?**
- Serverless container management reduces operational overhead
- Automatic scaling without cluster management
- Pay-per-use pricing model suitable for variable workloads

**Why SQLModel over raw SQLAlchemy?**
- Combined ORM and validation in single model definition
- Type safety with Pydantic integration
- Reduced boilerplate and improved developer experience

## Project Roadmap

- [x] FastAPI application with transaction endpoints
- [x] PostgreSQL integration with SQLModel ORM
- [x] Docker containerization with multi-stage builds
- [x] Local development environment with Docker Compose
- [x] Terraform VPC module with networking components
- [ ] Complete Terraform modules (ECS, RDS, ALB, ECR)
- [ ] GitHub Actions CI/CD pipeline implementation
- [ ] AWS deployment and infrastructure provisioning
- [ ] API documentation with OpenAPI/Swagger
- [ ] Monitoring and logging integration (CloudWatch)
- [ ] Unit and integration test suite expansion

## Current Focus

Working on completing the Terraform infrastructure modules for ECS, RDS, and ALB. Next I'll be implementing the GitHub Actions pipeline for automated deployments.

---

**Note:** This is an active development project built to demonstrate DevOps engineering capabilities while applying for positions. The infrastructure design reflects production-ready practices and security considerations.
