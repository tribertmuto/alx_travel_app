# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=alx_travel_app_db
DB_USER=travel_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Redis Configuration
REDIS_URL=redis://127.0.0.1:6379/1

# Email Configuration (for production)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@alxtravelapp.com

# API Keys (add as needed)
# GOOGLE_MAPS_API_KEY=your-google-maps-api-key
# STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
# STRIPE_SECRET_KEY=your-stripe-secret-key