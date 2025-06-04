"""Skills section component for the AI Engineer portfolio."""

from nicegui import ui
from typing import Dict, List


def create_skills_section() -> None:
    """Create the skills section with technical expertise."""
    
    with ui.element('div').classes('section'):
        ui.html('<h2 class="section-title" id="skills">Technical Skills</h2>')
        
        # Skills categories
        skills_data = {
            "Machine Learning & AI": {
                "skills": [
                    "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "XGBoost",
                    "LightGBM", "Hugging Face", "OpenAI API", "LangChain"
                ],
                "icon": "🤖",
                "color": "bg-blue-500"
            },
            "Programming Languages": {
                "skills": [
                    "Python", "R", "SQL", "JavaScript", "Java", "C++", "Scala", "Go"
                ],
                "icon": "💻",
                "color": "bg-green-500"
            },
            "Data Engineering": {
                "skills": [
                    "Apache Spark", "Kafka", "Airflow", "Pandas", "NumPy",
                    "Dask", "Polars", "Apache Beam", "ETL Pipelines"
                ],
                "icon": "🔧",
                "color": "bg-orange-500"
            },
            "Cloud & DevOps": {
                "skills": [
                    "AWS", "Google Cloud", "Azure", "Docker", "Kubernetes",
                    "MLflow", "Weights & Biases", "GitHub Actions", "Terraform"
                ],
                "icon": "☁️",
                "color": "bg-purple-500"
            },
            "Databases": {
                "skills": [
                    "PostgreSQL", "MongoDB", "Redis", "Elasticsearch",
                    "ClickHouse", "Snowflake", "BigQuery", "DynamoDB"
                ],
                "icon": "🗄️",
                "color": "bg-red-500"
            },
            "Visualization & BI": {
                "skills": [
                    "Matplotlib", "Seaborn", "Plotly", "Tableau", "Power BI",
                    "Streamlit", "Dash", "D3.js", "Observable"
                ],
                "icon": "📊",
                "color": "bg-indigo-500"
            }
        }
        
        with ui.grid(columns=2).classes('w-full gap-6'):
            for category, data in skills_data.items():
                with ui.card().classes('p-6'):
                    # Category header
                    with ui.row().classes('items-center mb-4'):
                        ui.html(f'<div class="text-3xl mr-3">{data["icon"]}</div>')
                        ui.html(f'<h3 class="text-xl font-bold text-gray-800">{category}</h3>')
                    
                    # Skills tags
                    with ui.element('div').classes('flex flex-wrap gap-2'):
                        for skill in data["skills"]:
                            ui.html(f'<span class="skill-tag">{skill}</span>')
        
        # Proficiency levels
        with ui.card().classes('mt-8 p-6'):
            ui.html('<h3 class="text-xl font-bold text-gray-800 mb-6 text-center">Core Competencies</h3>')
            
            competencies = [
                {"skill": "Machine Learning Engineering", "level": 95},
                {"skill": "Deep Learning & Neural Networks", "level": 90},
                {"skill": "Data Science & Analytics", "level": 92},
                {"skill": "Python Programming", "level": 98},
                {"skill": "Cloud Architecture (AWS/GCP)", "level": 85},
                {"skill": "MLOps & Model Deployment", "level": 88}
            ]
            
            for comp in competencies:
                with ui.row().classes('w-full items-center mb-4'):
                    ui.label(comp["skill"]).classes('w-64 font-medium')
                    with ui.element('div').classes('flex-1 bg-gray-200 rounded-full h-3 mx-4'):
                        ui.element('div').classes(f'bg-gradient-to-r from-blue-500 to-purple-600 h-3 rounded-full').style(f'width: {comp["level"]}%')
                    ui.label(f'{comp["level"]}%').classes('w-12 text-right font-bold text-purple-600')