# CRL - Connect, Request, Locate

A platform that connects users to verified local service providers: water suppliers, electricians, plumbers, hospitals, schools, and more.

## What You Can Find

### 🏥 Healthcare Services
- Hospitals and clinics
- Medical practitioners
- Emergency services
- Pharmacy locations

### 🔧 Home & Maintenance Services
- Electricians
- Plumbers
- Carpenters
- General contractors

### 🏫 Educational Services
- Schools and universities
- Tutoring centers
- Training institutes
- Educational consultants

### 🛡️ Emergency Services
- Police stations
- Fire departments
- Ambulance services
- Security companies

### 🏠 Utility Services
- Water suppliers
- Electricity providers
- Gas companies
- Internet/cable providers

### 🛒 Other Essential Services
- Grocery stores
- Pharmacies
- Banks and ATMs
- Post offices
- Government offices

## Features

- 🔐 User authentication (register/login/logout)
- 👥 Provider management system
- 🛠️ Service catalog with detailed information
- 📱 Responsive Bootstrap interface
- 🛡️ Admin panel for management
- 🌐 Modern web application
- 📍 Location-based service discovery
- ⭐ Provider ratings and reviews (future feature)

## Tech Stack

- **Backend**: Django 5.0
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Authentication**: Django Auth

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Rocky-bot-byte/ctrl.project.git
cd ctrl.project
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the server:
```bash
python manage.py runserver
```

7. Open http://127.0.0.1:8000/ in your browser

## Usage

- **Home**: Overview of the platform
- **Providers**: Browse and add service providers
- **Services**: View available services
- **Admin**: Manage all data at /admin/

## Models

- **User Profile**: Extended user information
- **Provider**: Service provider details
- **Service**: Services offered by providers
- **Request**: Service requests (future feature)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

---

**CRL** - Connecting you to trusted local services</content>
<parameter name="filePath">c:\Users\PC\OneDrive\Desktop\crl_project\README.md