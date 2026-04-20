from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# ── Portfolio data ─────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Syed Asad Zaidi",
    "title": "Senior Data Analyst",
    "subtitle": "BI · SQL · Python · Power BI",
    "email": "syedaihzaidi@gmail.com",
    "phone": "+92 332 8211131",
    "linkedin": "linkedin": "linkedin.com/in/syedaihzaidi",
    "education": "MSc Business Intelligence & Analytics — University of Huddersfield, UK",
    "bio": [
        "Senior Data Analyst with 5 years turning complex datasets into actionable "
        "growth and product insights. Advanced SQL and BI with strong metrics design "
        "and data-quality discipline — delivering 98%+ data accuracy.",
        "I define north-star KPIs, design robust data models, and build self-serve "
        "dashboards that leadership actually use. My work spans customer segmentation, "
        "propensity modelling, impact measurement, and demand forecasting.",
        "I've presented data-driven research at international conferences in Leeds and "
        "Manchester, and hold an MSc in Business Intelligence & Analytics from the "
        "University of Huddersfield.",
    ],
    "stats": [
        {"value": "5+",  "unit": "",  "label": "Years experience",      "pct": 83},
        {"value": "98",  "unit": "%", "label": "Data accuracy",          "pct": 98},
        {"value": "40",  "unit": "%", "label": "Faster reporting",       "pct": 40},
        {"value": "30",  "unit": "%", "label": "Accuracy improvement",   "pct": 30},
    ],
}

EXPERTISE = [
    {
        "title": "Growth & monetization analytics",
        "desc":  "Funnel analysis, cohort analysis, activation, retention/churn, "
                 "opportunity sizing, trend & anomaly detection.",
    },
    {
        "title": "Impact measurement",
        "desc":  "Experiments & rollouts, incremental lift, controls for noise, "
                 "seasonality and external factors.",
    },
    {
        "title": "Segmentation & modelling",
        "desc":  "Customer segmentation, propensity modelling, and forecasting "
                 "for targeting and prioritization.",
    },
    {
        "title": "BI & data storytelling",
        "desc":  "Executive dashboards, KPI definitions, self-serve Power BI / "
                 "Tableau reporting.",
    },
]

SKILL_CATEGORIES = [
    {
        "title": "Analytics & BI",
        "cls":   "tag-blue",
        "tags":  ["SQL", "Power BI", "Tableau", "SPSS", "Excel (Adv.)"],
    },
    {
        "title": "Programming & ML",
        "cls":   "tag-green",
        "tags":  ["Python", "Propensity Models", "Forecasting", "Segmentation", "HTML"],
    },
    {
        "title": "Data & Systems",
        "cls":   "tag-amber",
        "tags":  ["Data Modelling", "ETL / Pipelines", "SAP S/4HANA",
                  "Arena Simulation", "Data Governance"],
    },
]

PROFICIENCY = [
    {"label": "SQL",            "pct": 96, "band": "Advanced"},
    {"label": "Power BI",       "pct": 92, "band": "Advanced"},
    {"label": "Data Modelling", "pct": 88, "band": "Strong"},
    {"label": "Python",         "pct": 85, "band": "Advanced"},
    {"label": "Tableau",        "pct": 80, "band": "Proficient"},
    {"label": "ML / Modelling", "pct": 78, "band": "Proficient"},
]

DASHBOARDS = [
    {
        "num":      "01",
        "file":     "01_marketing_analytics.html",
        "category": "Marketing Analytics",
        "title":    "Campaign Performance Deep Dive",
        "desc":     "Multi-channel ROAS analysis, full-funnel drop-off, weekly revenue "
                    "trends, and budget reallocation recommendations across Paid Search, "
                    "Meta, Email and Affiliate.",
        "preview_bg":   "#1a1410",
        "stats": [
            {"val": "£4.2M", "label": "Revenue analysed"},
            {"val": "3.8×",  "label": "Avg ROAS"},
            {"val": "+24%",  "label": "CVR uplift found"},
        ],
        "preview_stats": [
            {"val": "£4.2M", "label": "Revenue", "color": "#d4922a"},
            {"val": "3.8×",  "label": "ROAS",    "color": "#4a7c59"},
            {"val": "+24%",  "label": "CVR",      "color": "#d4922a"},
        ],
        "tag_style": "background:#fff3e0;color:#9a6700",
    },
    {
        "num":      "02",
        "file":     "02_product_analytics.html",
        "category": "Product Analytics",
        "title":    "User Retention & Feature Adoption",
        "desc":     "Cohort retention curves, feature adoption heatmaps, NPS driver "
                    "analysis, and churn segmentation across a 12.4K MAU product "
                    "with D30/D60/D90 tracking.",
        "preview_bg":   "#080c12",
        "stats": [
            {"val": "12.4K", "label": "MAU"},
            {"val": "42%",   "label": "D30 Retention"},
            {"val": "4.6×",  "label": "NPS drivers"},
        ],
        "preview_stats": [
            {"val": "12.4K", "label": "MAU",       "color": "#00d4ff"},
            {"val": "42%",   "label": "D30 Ret.",   "color": "#a3e635"},
            {"val": "18.2%", "label": "Churn",      "color": "#fb923c"},
        ],
        "tag_style": "background:#ddf4ff;color:#0550ae",
    },
    {
        "num":      "03",
        "file":     "03_finance_analytics.html",
        "category": "Finance & BI Analytics",
        "title":    "P&L Variance & Revenue Forecast",
        "desc":     "Full P&L variance decomposition across FY 2024, revenue trend "
                    "forecasting with 96.2% accuracy, and a £1.4M cost-reduction "
                    "opportunity identified through SQL-driven analysis.",
        "preview_bg":   "#1a1916",
        "stats": [
            {"val": "£28.4M", "label": "Revenue analysed"},
            {"val": "−£1.4M", "label": "Cost opportunity"},
            {"val": "96.2%",  "label": "Forecast accuracy"},
        ],
        "preview_stats": [
            {"val": "£28.4M", "label": "Revenue",  "color": "#e8c54a"},
            {"val": "96.2%",  "label": "Forecast",  "color": "#a8d8a8"},
            {"val": "−£1.4M", "label": "Savings",   "color": "#e8c54a"},
        ],
        "tag_style": "background:#fafaf0;color:#7a6800;border:0.5px solid #d4c87a",
    },
    {
        "num":      "04",
        "file":     "04_data_science_analytics.html",
        "category": "Data Science Hybrid",
        "title":    "Churn Prediction & A/B Testing",
        "desc":     "Binary churn classification model (n=18,400) with SHAP "
                    "explainability, ROC curve analysis, and a full A/B testing "
                    "framework across 6 experiments protecting £2.1M in revenue.",
        "preview_bg":   "#0f0d0a",
        "stats": [
            {"val": "84.6%", "label": "Model accuracy"},
            {"val": "£2.1M", "label": "Revenue protected"},
            {"val": "0.79",  "label": "AUC-ROC"},
        ],
        "preview_stats": [
            {"val": "84.6%", "label": "Accuracy", "color": "#f5d800"},
            {"val": "£2.1M", "label": "Saved",    "color": "#f5d800"},
            {"val": "0.79",  "label": "AUC-ROC",  "color": "#f5d800"},
        ],
        "tag_style": "background:#fff9d6;color:#6b5a00",
    },
    {
        "num":      "05",
        "file":     "05_sales_crm_analytics.html",
        "category": "Sales & CRM Analytics",
        "title":    "Pipeline & Revenue Intelligence",
        "desc":     "Power BI–style pipeline dashboard for a 24-rep B2B SaaS team — "
                    "revenue trends, funnel drop-off, rep leaderboard, win/loss by "
                    "source, and deal velocity waterfall. Salesforce → BigQuery.",
        "preview_bg":   "#004578",
        "stats": [
            {"val": "£18.4M", "label": "Pipeline value"},
            {"val": "£11.2M", "label": "Revenue closed"},
            {"val": "38.4%",  "label": "Win rate"},
        ],
        "preview_stats": [
            {"val": "£18.4M", "label": "Pipeline", "color": "#0078d4"},
            {"val": "38.4%",  "label": "Win Rate",  "color": "#00b4d8"},
            {"val": "74d",    "label": "Cycle",     "color": "#ffb900"},
        ],
        "tag_style": "background:#e6f0fa;color:#003a6e",
    },
    {
        "num":      "06",
        "file":     "06_hr_people_analytics.html",
        "category": "HR & People Analytics",
        "title":    "Workforce Intelligence",
        "desc":     "Tableau-style HR dashboard for a 4,200-employee global retail "
                    "group — headcount waterfall, attrition by tenure & department, "
                    "gender representation by level, ethnicity breakdown. Workday → Redshift.",
        "preview_bg":   "#1a1712",
        "stats": [
            {"val": "4,218",  "label": "Headcount"},
            {"val": "14.2%",  "label": "Attrition rate"},
            {"val": "3.8 yrs","label": "Avg tenure"},
        ],
        "preview_stats": [
            {"val": "4,218",  "label": "Headcount", "color": "#c49a2a"},
            {"val": "14.2%",  "label": "Attrition",  "color": "#c25b3a"},
            {"val": "+34",    "label": "eNPS",        "color": "#5a7a5a"},
        ],
        "tag_style": "background:#fbf0ea;color:#7a2e15",
    },
    {
        "num":      "07",
        "file":     "07_supply_chain_analytics.html",
        "category": "Supply Chain & Ops",
        "title":    "Inventory & Fulfilment Intelligence",
        "desc":     "Live ops dashboard for an FMCG manufacturer — 840 SKUs across "
                    "3 warehouses and 14 suppliers. Stock-days by SKU, reorder alerts, "
                    "supplier OTIF, and lead-time variance. SAP → BigQuery.",
        "preview_bg":   "#0e1419",
        "stats": [
            {"val": "840",  "label": "Active SKUs"},
            {"val": "14",   "label": "Suppliers tracked"},
            {"val": "4",    "label": "Critical alerts"},
        ],
        "preview_stats": [
            {"val": "840",  "label": "SKUs",      "color": "#00c9b1"},
            {"val": "23",   "label": "Low Stock",  "color": "#f59e0b"},
            {"val": "4",    "label": "Critical",   "color": "#f87171"},
        ],
        "tag_style": "background:#e0f7f5;color:#065f56",
    },
    {
        "num":      "08",
        "file":     "08_saas_metrics_analytics.html",
        "category": "SaaS Metrics Analytics",
        "title":    "MRR, Churn & Unit Economics",
        "desc":     "Unit economics for a B2B SaaS business — MRR waterfall by motion, "
                    "cohort retention heatmap, LTV:CAC by tier, and Snowflake SQL. "
                    "Enterprise cohorts retain 130%+ NRR. Stripe + Segment.",
        "preview_bg":   "#06070d",
        "stats": [
            {"val": "£2.1M", "label": "ARR"},
            {"val": "840",   "label": "Accounts"},
            {"val": "130%+", "label": "Enterprise NRR"},
        ],
        "preview_stats": [
            {"val": "£2.1M", "label": "ARR",      "color": "#818cf8"},
            {"val": "840",   "label": "Accounts",  "color": "#a3e635"},
            {"val": "130%",  "label": "NRR",       "color": "#818cf8"},
        ],
        "tag_style": "background:#eef0fe;color:#3730a3",
    },
    {
        "num":      "09",
        "file":     "09_healthcare_analytics.html",
        "category": "Healthcare Analytics",
        "title":    "Patient Outcomes & Operational Efficiency",
        "desc":     "NHS district general hospital analytics — A&E wait times by "
                    "hour/day, readmission risk by specialty, 18-week RTT compliance "
                    "by department, and length-of-stay benchmarking. SQL Server + Power BI.",
        "preview_bg":   "#003087",
        "stats": [
            {"val": "620",   "label": "Bed capacity"},
            {"val": "180K",  "label": "A&E attendances/yr"},
            {"val": "4.8d",  "label": "Avg length of stay"},
        ],
        "preview_stats": [
            {"val": "620",   "label": "Beds",    "color": "#38bdf8"},
            {"val": "180K",  "label": "A&E/yr",  "color": "#34d399"},
            {"val": "4.8d",  "label": "Avg LoS", "color": "#38bdf8"},
        ],
        "tag_style": "background:#e0f2fe;color:#0c4a6e",
    },
]

EXPERIENCE = [
    {
        "period":  "May 2025 – Sep 2025",
        "role":    "Consultant",
        "company": "Powersheds Ltd., United Kingdom",
        "badges":  [("UK", "blue")],
        "bullets": [
            "Defined objectives, success metrics and measurement frameworks for expansion initiatives.",
            "Assessed current-state operating model; defined to-be requirements with risks and dependencies for governance approval.",
            "Evaluated SaaS vendor solutions; built comparative scorecards and ROI/cost-benefit cases.",
        ],
    },
    {
        "period":  "Sep 2023 – Dec 2024",
        "role":    "Senior Data Analyst",
        "company": "Newports Institute of Communications and Economics",
        "badges":  [("+30% accuracy", "green")],
        "bullets": [
            "Defined north-star KPIs with cross-functional teams; converted into BI backlogs, user stories and acceptance criteria.",
            "Designed metric definitions and data models; authored Power BI dashboard specs and validated data quality.",
            "Ran customer segmentation and journey analysis; surfaced drivers, anomalies and growth opportunities.",
            "Built impact measurement frameworks with baseline + seasonality-aware trend analysis.",
            "Developed propensity models to forecast demand/service uptake and prioritize interventions.",
            "Sustained 98%+ data accuracy through validation rules and reconciliations.",
        ],
    },
    {
        "period":  "Aug 2020 – Sep 2023",
        "role":    "Data Analyst",
        "company": "Newports Institute of Communications and Economics",
        "badges":  [("−40% turnaround", "green")],
        "bullets": [
            "Analysed large volumes of survey and operational data; created reliable datasets for KPI tracking.",
            "Built and automated SQL/Python transformations and recurring extracts; cut reporting turnaround by 40%.",
            "Delivered dashboards and insight reports highlighting trends and anomalies.",
        ],
    },
    {
        "period":  "2025",
        "role":    "MSc Business Intelligence & Analytics",
        "company": "University of Huddersfield, United Kingdom",
        "badges":  [],
        "bullets": [
            "Postgraduate study in BI systems, data analytics, and applied machine learning.",
        ],
    },
]

CERTIFICATIONS = [
    {"icon": "SQL",  "name": "Advanced SQL"},
    {"icon": "PY",   "name": "Python"},
    {"icon": "XLS",  "name": "Advanced Excel"},
    {"icon": "HTML", "name": "HTML"},
]

CONFERENCES = [
    {
        "year":  "2026",
        "title": "Housing Affordability in the United Kingdom: A Data-Driven Analysis "
                 "of Regional Housing Prices and Earnings",
        "event": "Leeds Sustainability Conference, Leeds, UK — March 2026",
    },
    {
        "year":  "2024",
        "title": "Integrating Artificial Intelligence in HR Systems: An Approach to "
                 "Employee Management",
        "event": "MPP Conference, Manchester, UK — May 2024",
    },
]


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        expertise=EXPERTISE,
        skill_categories=SKILL_CATEGORIES,
        proficiency=PROFICIENCY,
        dashboards=DASHBOARDS,
        experience=EXPERIENCE,
        certifications=CERTIFICATIONS,
        conferences=CONFERENCES,
    )


@app.route("/dashboard/<filename>")
def dashboard(filename):
    """Serve a dashboard HTML file from static/dashboards/."""
    safe_files = {d["file"] for d in DASHBOARDS}
    if filename not in safe_files:
        abort(404)
    return app.send_static_file(f"dashboards/{filename}")


if __name__ == "__main__":
    print("Portfolio running at http://localhost:5000")
    app.run(debug=True, port=5000)
