# Personal Resume Website

A dynamic personal resume website built with Django that showcases your professional experience, education, projects, skills, and certifications. The website features a responsive design and is powered by a SQLite database for easy content management.

### Website Link: https://personal-resume-website-psi.vercel.app/

## Features

- **Dynamic Content Management**: All content is stored in a database and can be managed through Django's admin interface
- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Professional Sections**:
  - Personal Information & About
  - Work Experience
  - Education
  - Projects with GitHub links
  - Skills with visual icons
  - Certifications
- **Modern UI**: Clean, professional Bootstrap-based design
- **Admin Interface**: Easy content management through Django admin
- **Custom Date Fields**: Special month/year fields for dates
- **Skill Categories**: Organised skills by categories (Programming Languages, Frameworks, Databases, Cloud, Tools)
- **Production Ready**: Configured for deployment on Vercel with PostgreSQL

## Technology Stack

- **Backend**: Django
- **Database**: 
  - **Development**: SQLite3
  - **Production**: PostgreSQL
- **Deployment**: Vercel
- **Icons**: Font Awesome, Devicons, Simple Line Icons
- **Fonts**: Google Fonts (Saira Extra Condensed, Open Sans)

## Project Structure

```
portfolio_website/
├── portfolio/                    # Main Django app
│   ├── migrations/              # Database migrations
│   ├── static/portfolio/        # Static files (CSS, JS)
│   ├── templates/portfolio/     # HTML templates
│   ├── templatetags/           # Custom template tags
│   ├── admin.py                # Admin interface configuration
│   ├── models.py               # Database models
│   ├── views.py                # View logic
│   ├── urls.py                 # URL routing
│   └── custom_field.py         # Custom form fields
├── portfolio_website/          # Project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
├── manage.py                   # Django management script
├── vercel.json                 # Vercel deployment configuration
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## Database Models

The website uses the following Django models:

### PersonalInformation
- Name, profile title, email
- GitHub and LinkedIn profile links
- Short description/bio

### Experiences
- Company name, position, job type (intern/full-time)
- Start and end dates (custom month/year fields)
- Job description (semicolon-separated bullet points)

### Education
- Institution name, degree, location
- Start and end years
- Automatic ordering by date

### Skills
- Skill name, proficiency level (1-5)
- Category (Programming Language, Framework, Database, Cloud, Tools)
- Devicon class for visual representation

### Projects
- Project name and description
- Associated skills (many-to-many relationship)
- GitHub repository link
- Related work experience

### Certifications
- Certification name and dates
- Certificate link
- Expiration handling

# Database Schema

```mermaid
erDiagram
    PersonalInformation {
        int id PK
        varchar name "User's full name"
        varchar profile "Professional title/profile"
        varchar github_profile_link "GitHub profile URL"
        varchar linkedin_link "LinkedIn profile URL"
        varchar email "Email address"
        varchar short_description "Brief bio/description"
    }
    
    Education {
        int id PK
        varchar institution_name "Name of educational institution"
        varchar degree "Degree/qualification obtained"
        varchar place "Location of institution"
        int start_year "Year started (2013-current year)"
        int end_year "Year ended (nullable)"
    }
    
    Experiences {
        int id PK
        varchar company_name "Name of company/organization"
        varchar job_type "Type: intern or full-time"
        varchar position "Job title/position"
        date start_date "Start date (MonthYearField)"
        date end_date "End date (MonthYearField, nullable)"
        varchar description "Semicolon-separated job responsibilities (nullable)"
    }
    
    Skills {
        int id PK
        varchar skill_name "Name of the skill"
        int skill_level "Proficiency level (1-5)"
        varchar skill_devicon_class "CSS class for skill icon"
        varchar skill_category "Category: Programming Language, Framework, Database, Cloud, Tools"
    }
    
    Projects {
        int id PK
        varchar proj_name "Project name (unique)"
        varchar proj_desc "Project description (unique, min 50 chars)"
        varchar proj_code_link "GitHub repository URL (nullable)"
        int proj_relates_to_exp_id FK "Foreign key to Experiences (nullable)"
    }
    
    Certifications {
        int id PK
        varchar cert_name "Certification name (unique)"
        date cert_start_date "Certification start date (MonthYearField)"
        date cert_end_date "Certification end date (MonthYearField, nullable)"
        varchar cert_link "Certificate URL (nullable)"
    }
    
    Projects_Skills {
        int id PK
        int project_id FK "Foreign key to Projects"
        int skill_id FK "Foreign key to Skills"
    }
    
    %% Relationships
    Experiences ||--o{ Projects : "relates_to_exp (one experience can have many projects)"
    Projects }o--o{ Skills : "many_to_many (projects use multiple skills)"
    Projects ||--o{ Projects_Skills : "through table"
    Skills ||--o{ Projects_Skills : "through table"
    
    %% Additional Notes
    %% PersonalInformation: Single record per user - all fields required
    %% Education: Ordered by -start_year, -end_year; end_year validation
    %% Experiences: Ordered by -start_date, -end_date; end_date validation
    %% Skills: Ordered by skill_category, -skill_level; skill_level range 1-5
    %% Projects: No specific ordering; unique constraints on name and description
    %% Certifications: Ordered by -cert_end_date, -cert_start_date; end_date validation
```

## Database Schema Overview

This entity-relationship diagram represents a portfolio/resume database with the following key entities:

- **PersonalInformation**: Stores user profile data
- **Education**: Academic background and qualifications
- **Experiences**: Professional work history
- **Skills**: Technical and professional skills with proficiency levels
- **Projects**: Portfolio projects linked to experiences
- **Certifications**: Professional certifications and credentials
- **Projects_Skills**: Junction table for many-to-many relationship between projects and skills

### Key Relationships

1. **Experiences → Projects**: One-to-many (an experience can relate to multiple projects)
2. **Projects ↔ Skills**: Many-to-many (projects use multiple skills, skills are used in multiple projects)

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- PostgreSQL (for production deployment)

### Local Development Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd portfolio_website
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Configuration**
Create a `.env` file in the project root:
```env
# Django Configuration
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Configuration (for local development, SQLite3 will be used automatically)
ENV=DEV

# CSRF Configuration (for production)
CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

5. **Database Setup**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create Superuser**
```bash
python manage.py createsuperuser
```

7. **Run the Development Server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view your website and `http://127.0.0.1:8000/admin/` to manage content.

## Deployment

### Vercel Deployment

This project is configured for deployment on Vercel, with support for PostgreSQL databases.

#### Prerequisites for Production
- Vercel account
- PostgreSQL database (can be provided by Neon etc.)

#### Production Environment Variables
Set the following environment variables in your Vercel dashboard:

```env
# Django Configuration
DJANGO_SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.vercel.app,yourdomain.com

# Environment
ENV=PROD

# PostgreSQL Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=5432

# CSRF Configuration
CSRF_TRUSTED_ORIGINS=https://yourdomain.vercel.app,https://yourdomain.com
```

#### Deployment Steps

1. **Connect to Vercel**: Connect your GitHub repository to Vercel

2. **Configure Build Settings**: Vercel will automatically detect the Django configuration from `vercel.json`

3. **Set Environment Variables**: Add all the production environment variables listed above

4. **Deploy**: Vercel will automatically build and deploy your application

5. **Database Migration**: After deployment, run migrations using Vercel's serverless function or your database provider's tools

#### Database Configuration

The project automatically switches between databases based on the `ENV` environment variable:

- **Development (`ENV=DEV` or not set)**: Uses SQLite3 database (`db.sqlite3`)
- **Production (`ENV=PROD`)**: Uses PostgreSQL with credentials from environment variables

### Static Files

The project uses WhiteNoise for static file serving in production. Static files are automatically collected and served.

```bash
# For local static file collection (if needed)
python manage.py collectstatic
```

## Configuration

### Adding Content

1. **Access Admin Interface**: Navigate to `/admin/` and log in with your superuser credentials

2. **Add Personal Information**: 
   - Add your basic information, profile title, and social links
   - Use space-separated format for name/title to enable color splitting

3. **Add Skills**:
   - Include devicon class names for visual icons
   - Set proficiency levels (1-5)
   - Categorize skills appropriately

4. **Add Experience**:
   - Use semicolon-separated descriptions for bullet points
   - Dates are automatically formatted as month/year

5. **Add Projects**:
   - Link projects to related experiences
   - Associate relevant skills
   - Include GitHub repository links

6. **Add Education & Certifications**:
   - Fill in all relevant academic and professional credentials

### Custom Features

- **Date Formatting**: The website uses custom month/year fields for professional date display
- **Skill Icons**: Uses Devicon for technology skill visualization
- **Responsive Navigation**: Auto-hides sections with no content
- **Text Splitting**: Custom template filter for name/title color formatting
- **Database Flexibility**: Automatic switching between SQLite3 (development) and PostgreSQL (production)

## Environment-Specific Features

### Development Environment
- **Database**: SQLite3 (file-based, no setup required)
- **Debug Mode**: Enabled for development convenience
- **Static Files**: Served directly by Django

### Production Environment
- **Database**: PostgreSQL (scalable, robust)
- **Debug Mode**: Disabled for security
- **Static Files**: Served by WhiteNoise middleware
- **Security**: CSRF protection, secure headers
- **Platform**: Optimized for Vercel serverless deployment

## Template Attribution

This project is built upon the **"Resume - A Bootstrap 4, Simple Yet Exquisite CV Template"** with extensive modifications including:

- **Complete Django Backend Integration**: Converted static template to dynamic Django application
- **Database-Driven Content**: All content now managed through database with custom models
- **Admin Interface**: Added Django admin for easy content management
- **Custom Fields**: Implemented specialized form fields like month/year date pickers
- **Dynamic Relationships**: Created many-to-many relationships between projects and skills
- **Enhanced Functionality**: Added features like skill categorization, project linking, and certification management
- **Responsive Improvements**: Enhanced mobile responsiveness and user experience
- **Production Deployment**: Configured for Vercel deployment with PostgreSQL support

**Template Source**: [ThemeWagon Free Bootstrap CV Template](https://themewagon.com/themes/free-bootstrap-4-cv-template-download/)

---
