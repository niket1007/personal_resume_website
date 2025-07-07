# Personal Resume Website

A dynamic personal resume website built with Django that showcases your professional experience, education, projects, skills, and certifications. The website features a responsive design and is powered by a SQLite database for easy content management.

## Features

- **Dynamic Content Management**: All content is stored in a SQLite database and can be managed through Django's admin interface
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
- **Skill Categories**: Organized skills by categories (Programming Languages, Frameworks, Databases, Cloud, Tools)

## Technology Stack

- **Backend**: Django
- **Database**: SQLite3
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

## Database Schema Diagram

erDiagram
    PersonalInformation {
        int id PK
        varchar name
        varchar profile
        varchar github_profile_link
        varchar linkedin_link
        varchar email
        varchar short_description
    }
    
    Education {
        int id PK
        varchar institution_name
        varchar degree
        varchar place
        int start_year
        int end_year "nullable"
    }
    
    Experiences {
        int id PK
        varchar company_name
        varchar job_type "choices: intern, full-time"
        varchar position
        date start_date "MonthYearField"
        date end_date "MonthYearField, nullable"
        varchar description "semicolon separated"
    }
    
    Skills {
        int id PK
        varchar skill_name
        int skill_level "1-5 range"
        varchar skill_devicon_class
        varchar skill_category "choices: Programming Language, Framework, Database, Cloud, Tools"
    }
    
    Projects {
        int id PK
        varchar proj_name "unique"
        varchar proj_desc "unique, min 50 chars"
        varchar proj_code_link "unique URL"
        int proj_relates_to_exp_id FK "nullable"
    }
    
    Certifications {
        int id PK
        varchar cert_name "unique"
        date cert_start_date "MonthYearField"
        date cert_end_date "MonthYearField, nullable"
        varchar cert_link "nullable"
    }
    
    Projects_Skills {
        int id PK
        int project_id FK
        int skill_id FK
    }
    
    %% Relationships
    Experiences ||--o{ Projects : "relates_to"
    Projects }o--o{ Skills : "many_to_many"
    Projects ||--o{ Projects_Skills : "through"
    Skills ||--o{ Projects_Skills : "through"


## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

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
pip install django python-decouple
```

4. **Environment Configuration**
Create a `.env` file in the project root:
```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=
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

## Customization

### Styling
- Modify `portfolio/static/portfolio/css/resume.css` for custom styling
- Primary color can be changed by updating the `#BD5D38` color values

### Content Structure
- Template located at `portfolio/templates/portfolio/index.html`
- Uses Bootstrap 4 grid system for responsive layout

### Adding New Sections
1. Create new model in `models.py`
2. Add to admin in `admin.py`
3. Update view in `views.py`
4. Modify template to display new section

## Deployment

### Production Settings
1. Set `DEBUG=False` in your `.env` file
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up static files serving
4. Use a production database (PostgreSQL recommended)

### Static Files
```bash
python manage.py collectstatic
```

## Design Template Reference

This project uses a Bootstrap 4 CV template as a base:
- **Template Source**: [ThemeWagon Free Bootstrap CV Template](https://themewagon.com/themes/free-bootstrap-4-cv-template-download/)
- **License**: MIT License (included in project)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the Django documentation
2. Review the template reference
3. Create an issue in the repository

---

**Note**: This is a personal portfolio website template. Customize the content, styling, and features according to your needs.