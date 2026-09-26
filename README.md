# Zero-Waste-Mongolia-System v1

A government-led circular waste management system for Mongolia, designed as a scalable model for a waste-free world.

## Version 1: Minimal Pilot

This is the minimal pilot version using Python, Gradio, and PostgreSQL.

### Quick Start

#### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/Shirendev1/Zero-Waste-Mongolia-System.git
   cd Zero-Waste-Mongolia-System
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database URL and settings
   ```

5. Initialize the database:
   ```bash
   python -c "from database.connection import init_db; init_db()"
   ```

6. Run the application:
   ```bash
   python main.py
   ```

   The app will start at `http://localhost:7860`

#### Docker

```bash
docker build -t zero-waste-v1 .
docker run -p 7860:7860 --env-file .env zero-waste-v1
```

#### Render Deployment

1. Push to GitHub
2. Connect repository to Render
3. Set environment variables in Render dashboard
4. Deploy (auto on push)

### Project Structure

```
Zero-Waste-Mongolia-System/
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Docker configuration
├── render.yaml                # Render deployment config
├── main.py                    # Entry point
├── database/
│   ├── schema.sql            # Database schema
│   └── connection.py         # Database connection
└── ui/
    └── app.py                # Gradio application
```

### Features (v1 Skeleton)

- [x] Python 3.10+ environment
- [x] Gradio web interface
- [x] PostgreSQL database connection
- [x] Render-compatible deployment
- [ ] Waste batch registration
- [ ] QR code generation
- [ ] Public lookup
- [ ] Status updates
- [ ] Admin dashboard
- [ ] CSV export

### Environment Variables

See `.env.example` for required variables:
- `DATABASE_URL`: PostgreSQL connection string
- `DEBUG`: Enable debug mode (True/False)
- `PORT`: Port to run on (default: 7860)

### Database

The database schema is defined in `database/schema.sql`. Initialize with:

```bash
python -c "from database.connection import init_db; init_db()"
```

### License

MIT License
