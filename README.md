# Algosoft II Website

This is the official website for Algosoft II, a software engineering company specializing in software development and data services.

## Features

- Multi-language support (English and German)
- Contact form with email delivery
- Responsive design for all devices
- Service descriptions and portfolio showcase

## Technologies Used

- Django 3.2
- HTML5/CSS3
- Python 3.8+
- SQLite (Development) / PostgreSQL (Production)
- WhiteNoise for static files

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository
   ```
   git clone https://github.com/yourusername/algosoft-website.git
   cd algosoft-website
   ```

2. Create a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Create an environment file
   ```
   cp .env.example .env
   ```
   
5. Edit the `.env` file with your specific configuration values

6. Compile translations
   ```
   python compile_translations.py
   ```

7. Run the development server
   ```
   python manage.py runserver
   ```

## Environment Variables

The following environment variables need to be set in the `.env` file:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to "True" for development, "False" for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `EMAIL_HOST_USER`: Gmail address for sending emails
- `EMAIL_HOST_PASSWORD`: Gmail app password
- `DEFAULT_FROM_EMAIL`: Default sender email address
- `CONTACT_EMAIL`: Email address where contact form submissions are sent

## Contact

For more information, contact us at [contact@algosoftii.com](mailto:contact@algosoftii.com)