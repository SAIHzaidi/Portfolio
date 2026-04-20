# Syed Asad Zaidi — Portfolio (Flask)

A personal portfolio website built with Python + Flask.

## Project structure

```
portfolio/
├── app.py                      ← Routes & all portfolio data (edit this)
├── requirements.txt
├── templates/
│   ├── base.html               ← Nav, footer, shared HTML
│   └── index.html              ← Jinja2 template (loops over data from app.py)
└── static/
    ├── css/style.css           ← All styles
    ├── js/main.js              ← Scroll animations & nav highlight
    └── dashboards/             ← Dashboard HTML files (served at /dashboard/<file>)
        ├── 01_marketing_analytics.html
        ├── 02_product_analytics.html
        ├── 03_finance_analytics.html
        ├── 04_data_science_analytics.html
        ├── 05_sales_crm_analytics.html
        ├── 06_hr_people_analytics.html
        ├── 07_supply_chain_analytics.html
        ├── 08_saas_metrics_analytics.html
        └── 09_healthcare_analytics.html
```

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000

## How to update your content

All portfolio content lives in `app.py` as plain Python data structures —
no need to touch the HTML templates.

| Variable           | What it controls                        |
|--------------------|-----------------------------------------|
| `PROFILE`          | Name, title, contact details, bio, stats|
| `EXPERTISE`        | About section expertise cards           |
| `SKILL_CATEGORIES` | Skills section tags                     |
| `PROFICIENCY`      | Animated proficiency bars               |
| `DASHBOARDS`       | Dashboard cards (title, stats, colours) |
| `EXPERIENCE`       | Career timeline                         |
| `CERTIFICATIONS`   | Cert cards                              |
| `CONFERENCES`      | Conference presentations                |

## Add a new dashboard

1. Drop the HTML file into `static/dashboards/`
2. Add a new entry to the `DASHBOARDS` list in `app.py`

## Deploy to production

For production use gunicorn:

```bash
pip install gunicorn
gunicorn app:app
```

Or deploy to Railway / Render / Fly.io by pointing them at this folder.
