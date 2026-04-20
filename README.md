# Duplicate Code Finder

A simple Python script to detect exact duplicate code in TypeScript/JavaScript projects.

## Features

- Scans `.ts`, `.tsx`, `.js`, `.jsx` files
- Normalizes code by removing comments and whitespace
- Finds exact duplicates after normalization
- Generates human-readable reports
- Skips common directories (node_modules, .git, dist, etc.)

## Installation

Clone this repository:

```bash
git clone https://github.com/cenbonlon-poolside/duplicate-finder-.git
cd duplicate-finder-
```

## Usage

Run the script on any project directory:

```bash
python3 duplicate_finder.py
```

The script will:
1. Scan for TypeScript/JavaScript files
2. Normalize code content
3. Detect duplicates
4. Print a formatted report

## Customization

To scan a different project, edit the `project_path` variable in `duplicate_finder.py`:

```python
project_path = "/path/to/your/project"
```

## What It Detects

- Exact duplicates after removing comments and normalizing whitespace
- Files with identical logic but different formatting
- Accidental file copies or duplicates

## Limitations

- Only detects exact duplicates (not semantic similarities)
- Requires Python 3
- Designed for TypeScript/JavaScript projects

## Example Output

```
🔍 Starting duplicate code analysis...

📁 Scanning for TypeScript/JavaScript files...
   Found 42 files

🔎 Analyzing code for duplicates...
   Found 2 duplicates

📊 Generating report...

============================================================
🔍 DUPLICATE CODE REPORT
============================================================

Found 2 duplicate(s)

--- Duplicate #1 ---
📄 Original: src/utils/helpers.ts
📄 Copy:     src/components/Button.tsx

📝 Code Preview:
export const formatDate = (date: Date): string => { return date.toISOString().split('T')[0]; };
```

## Contributing

Feel free to submit issues or pull requests!

## License

MIT License
   cd sptinder
   ```

2. **Set up Spotify App**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app
   - Add `http://localhost:3000/auth/callback` to redirect URIs
   - Copy Client ID and Client Secret

3. **Environment Setup**
   ```bash
   # Copy environment files
   cp services/api/.env.example services/api/.env
   cp services/realtime/.env.example services/realtime/.env
   cp services/worker/.env.example services/worker/.env
   cp services/frontend/.env.example services/frontend/.env

   # Edit .env files with your Spotify credentials and database URLs
   ```

4. **Start Development Environment**
   ```bash
   # Start all services
   docker-compose up -d

   # Or use the development script
   ./scripts/dev.sh
   ```

5. **Access the Application**
   - Frontend: http://localhost:3000
   - API: http://localhost:4000
   - Real-time: ws://localhost:3001

### Production Deployment

1. **Build and Push Images**
   ```bash
   # Build all services
   docker build -t your-registry/sptinder-api:latest services/api/
   docker build -t your-registry/sptinder-realtime:latest services/realtime/
   docker build -t your-registry/sptinder-worker:latest services/worker/
   docker build -t your-registry/sptinder-frontend:latest services/frontend/

   # Push to registry
   docker push your-registry/sptinder-api:latest
   # ... push other images
   ```

2. **Deploy to Kubernetes**
   ```bash
   # Using Helm
   helm install sptinder ./infrastructure/helm \
     --set image.registry=your-registry \
     --set database.password=your-db-password \
     --set redis.password=your-redis-password \
     --set spotify.clientId=your-spotify-client-id \
     --set spotify.clientSecret=your-spotify-client-secret \
     --set jwt.secret=your-jwt-secret
   ```

3. **Configure Ingress**
   ```bash
   # Update ingress values
   helm upgrade sptinder ./infrastructure/helm \
     --set ingress.enabled=true \
     --set ingress.hosts[0].host=your-domain.com
   ```

## 📁 Project Structure

```
sptinder/
├── services/
│   ├── api/                 # REST API service
│   ├── realtime/           # WebSocket service
│   ├── worker/             # Background worker
│   └── frontend/           # React application
├── infrastructure/
│   ├── helm/               # Kubernetes Helm charts
│   ├── kubernetes/         # Raw Kubernetes manifests
│   └── monitoring/         # Prometheus/Grafana configs
├── scripts/                # Development and deployment scripts
├── docker-compose.yml      # Local development setup
├── .github/workflows/      # CI/CD pipelines
└── README.md
```

## 🔧 Configuration

### Environment Variables

#### API Service
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `SPOTIFY_CLIENT_ID`: Spotify app client ID
- `SPOTIFY_CLIENT_SECRET`: Spotify app client secret
- `JWT_SECRET`: JWT signing secret
- `PORT`: Service port (default: 4000)

#### Real-time Service
- `REDIS_URL`: Redis connection string
- `PORT`: Service port (default: 3001)

#### Worker Service
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `SPOTIFY_CLIENT_ID`: Spotify app client ID
- `SPOTIFY_CLIENT_SECRET`: Spotify app client secret

#### Frontend Service
- `REACT_APP_API_URL`: API service URL
- `REACT_APP_REALTIME_URL`: Real-time service WebSocket URL

## 🧪 Testing

```bash
# Run all tests
npm run test

# Run tests with coverage
npm run test:coverage

# Run e2e tests
npm run test:e2e

# Run specific service tests
cd services/api && npm test
```

## 📊 Monitoring

The application includes comprehensive monitoring with Prometheus and Grafana:

- **Metrics**: Request latency, error rates, connection counts
- **Dashboards**: Pre-configured Grafana dashboard for application metrics
- **Alerts**: Configurable alerts for service health and performance

Access Grafana at: http://your-domain.com/grafana

## 🔒 Security

- JWT-based authentication
- OAuth 2.0 with Spotify
- HTTPS everywhere in production
- Secrets management with Kubernetes secrets
- Rate limiting and input validation
- CORS configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow TypeScript strict mode
- Write tests for new features
- Update documentation
- Use conventional commits
- Ensure all CI checks pass

## 📝 API Documentation

### Authentication Endpoints

```
POST /auth/login          # Spotify OAuth login
POST /auth/callback       # OAuth callback
POST /auth/refresh        # Refresh access token
GET  /auth/me            # Get current user
```

### Songs Endpoints

```
GET  /songs              # Get songs for swiping
POST /songs/:id/swipe    # Record a swipe
GET  /songs/recommendations  # Get personalized recommendations
```

### Matches Endpoints

```
GET  /matches            # Get user matches
GET  /matches/:id        # Get specific match details
POST /matches/:id/chat   # Send chat message
```

## 🧩 Duplicate Finder Script

This repository includes a simple duplicate code finder script at `duplicate_finder.py`.

It is designed to:

- Scan the Sptinder project for TypeScript/JavaScript files
- Normalize code by removing comments and whitespace
- Detect exact duplicate files across the project
- Generate a readable duplicate report

### How to run

```bash
cd /Users/ben.conlon/Projects/Sptinder
python3 duplicate_finder.py
```

### What it checks

- `.ts`, `.tsx`, `.js`, `.jsx` files
- Skips common directories like `node_modules`, `.git`, `dist`, `build`, and `.next`
- Treats files as duplicates when the normalized code text is identical

### Why it is useful

This script helps identify duplicated file content in the repository quickly, so you can:

- Catch accidental duplicate files
- Find duplicate copies from nested directories or copies of generated code
- Keep the codebase cleaner before refactoring or deployment

### Notes

- The current implementation does not perform semantic matching, so it only finds exact content duplicates after normalization.
- If you want to scan a different project, update the `project_path` in `duplicate_finder.py`.

```

### Users Endpoints

```
GET  /users/profile      # Get user profile
PUT  /users/profile      # Update user profile
GET  /users/:id          # Get public user info
```

## 🚀 Deployment Options

### Local Development
- Docker Compose for quick setup
- Hot reloading for all services
- Local database and cache

### Staging Environment
- Automated deployment via GitHub Actions
- Separate namespace in Kubernetes
- Full monitoring stack

### Production Environment
- High availability setup
- Horizontal Pod Autoscaling
- External load balancer
- Database backups and replication

## 📈 Performance

- **API Response Time**: <100ms for most endpoints
- **Real-time Latency**: <50ms for WebSocket messages
- **Concurrent Users**: Supports 10k+ simultaneous connections
- **Database Queries**: Optimized with proper indexing
- **Caching**: Redis for session and frequently accessed data

## 🔄 CI/CD Pipeline

The project includes a complete CI/CD pipeline with:

- **Automated Testing**: Unit and integration tests on every PR
- **Security Scanning**: Dependency and container image scanning
- **Build & Push**: Automated Docker image building and registry push
- **Deployment**: Automatic deployment to staging and production
- **Rollback**: Easy rollback capabilities for failed deployments

## 📚 Additional Resources

- [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Charts Guide](https://helm.sh/docs/)
- [Prometheus Monitoring](https://prometheus.io/docs/)
- [Grafana Dashboards](https://grafana.com/docs/grafana/latest/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Spotify for providing the Web API
- The open-source community for amazing tools and libraries
- Contributors who help improve this project

---

Made with ❤️ for music lovers everywhere