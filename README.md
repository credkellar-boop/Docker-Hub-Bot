# Docker-Hub-Bot

Docker-Hub-Bot is an AI Triad (Asset, Security, Brain) unifying official Docker Library repositories. Powered by Gemini, it autonomously searches Docker Hub, executes Scout vulnerability audits, and dynamically generates optimized, layer-cached container environments for high-throughput smart contract execution and robust CI/CD automation pipelines.

## Architecture

* **Asset Module:** Automatically clones and syncs the scattered Docker official library repositories (`docs`, `faq`, `repo-info`).
* **Security Module:** Intercepts environments and runs automated vulnerability audits using Docker Scout.
* **Brain Module:** Utilizes Gemini AI to interpret conceptual queries and generate optimized `Dockerfile` and `docker-compose.yml` files.

## Deployment

1. Clone the repository.
2. Duplicate `.env.example` to `.env` and input your `GEMINI_API_KEY`.
3. Launch the bot using Docker Compose:
   ```bash
   docker compose up --build -d
