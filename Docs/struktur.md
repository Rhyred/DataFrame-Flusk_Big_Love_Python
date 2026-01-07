project-name/                          ← ROOT
├── .gitignore
├── README.md                           ← Main documentation
├── docker-compose.yml                  ← Database setup (shared)
│
├── backend/                            ← BACKEND TEAM
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── users.py          # API: GET/POST/PUT/DELETE /api/users
│   │   ├── products.py       # API: GET/POST/PUT/DELETE /api/products
│   │   └── auth.py           # API: POST /api/auth/login
│   ├── models/               # DATABASE MODELS (shared dengan DB team)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── base.py
│   ├── services/             # Business logic
│   │   ├── user_service.py
│   │   └── product_service.py
│   ├── middleware/           # Auth, CORS, error handling
│   │   ├── auth.py
│   │   └── error_handler.py
│   ├── schemas/              # Request/Response validation
│   │   ├── user_schema.py
│   │   └── product_schema.py
│   └── tests/                # Backend unit tests
│
├── frontend/                           ← FRONTEND TEAM (Your domain)
│   ├── app.py                # Flask app hanya untuk serving template
│   ├── config.py
│   ├── requirements.txt
│   ├── templates/
│   │   ├── base.html         # Main layout
│   │   ├── index.html        # Dashboard
│   │   ├── users/
│   │   │   ├── list.html
│   │   │   ├── create.html
│   │   │   └── edit.html
│   │   ├── products/
│   │   │   ├── list.html
│   │   │   ├── create.html
│   │   │   └── edit.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── settings.html
│   │   ├── components/       # Reusable Jinja2 components
│   │   │   ├── navbar.html
│   │   │   ├── sidebar.html
│   │   │   ├── table.html
│   │   │   ├── modal.html
│   │   │   └── form.html
│   │   └── errors/
│   │       ├── 404.html
│   │       └── 500.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── flowbite.min.css
│   │   │   ├── tailwind.css
│   │   │   └── custom.css
│   │   ├── js/
│   │   │   ├── dark-mode.js
│   │   │   ├── sidebar.js
│   │   │   └── api-client.js  ← CRITICAL: Handle API calls ke backend
│   │   └── images/
│   ├── utils/
│   │   ├── api.py            # API client untuk call backend
│   │   └── helpers.py
│   └── tests/                # Frontend tests
│
├── database/                           ← DATABASE TEAM
│   ├── migrations/           # Alembic migrations
│   │   ├── versions/
│   │   ├── env.py
│   │   └── script.py.mako
│   ├── seeds/                # Initial data
│   │   ├── users.json
│   │   └── products.json
│   └── schema.sql            # SQL schema documentation
│
├── docs/                               ← SHARED DOCUMENTATION
│   ├── API.md                # API endpoints contract
│   ├── DATABASE.md           # Database schema
│   ├── SETUP.md              # How to run project
│   ├── GIT_WORKFLOW.md       # Git branching strategy
│   └── ARCHITECTURE.md       # Overall architecture
│
└── scripts/                            ← SHARED UTILITIES
    ├── setup.sh              # Setup project
    └── run.sh                # Run all services