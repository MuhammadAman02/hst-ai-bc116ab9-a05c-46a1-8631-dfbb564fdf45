"""
AI Engineer Portfolio - Main Application
Professional portfolio with interactive components and modern design
"""

from nicegui import ui, app
from typing import Dict, List, Any
import asyncio
from app.config import settings
from app.components.hero import create_hero_section
from app.components.about import create_about_section
from app.components.skills import create_skills_section
from app.components.projects import create_projects_section
from app.components.experience import create_experience_section
from app.components.contact import create_contact_section
from app.components.footer import create_footer
from core.utils import setup_page_meta, get_professional_image


def setup_global_styles() -> None:
    """Setup global CSS styles for the portfolio."""
    ui.add_head_html('''
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #2d3748;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .portfolio-container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 20px 60px rgba(0,0,0,0.1);
            border-radius: 20px;
            overflow: hidden;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        
        .section {
            padding: 4rem 2rem;
        }
        
        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 3rem;
            color: #1a365d;
            position: relative;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 2px;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid #e2e8f0;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
        }
        
        .skill-tag {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            margin: 4px;
            display: inline-block;
        }
        
        .project-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        
        .hero-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .hero-subtitle {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        .contact-form {
            max-width: 600px;
            margin: 0 auto;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #2d3748;
        }
        
        .form-input {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e2e8f0;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }
        
        .form-input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        .footer {
            background: #1a365d;
            color: white;
            text-align: center;
            padding: 2rem;
        }
        
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.5rem;
            }
            
            .section {
                padding: 2rem 1rem;
            }
            
            .portfolio-container {
                margin: 10px;
                border-radius: 10px;
            }
        }
    </style>
    ''')


@ui.page('/')
async def index():
    """Main portfolio page with all sections."""
    
    # Setup page metadata
    setup_page_meta(
        title="AI Engineer Portfolio - Machine Learning & Data Science Expert",
        description="Professional AI Engineer specializing in machine learning, deep learning, and data science solutions.",
        keywords="AI Engineer, Machine Learning, Deep Learning, Data Science, Python, TensorFlow, PyTorch"
    )
    
    # Setup global styles
    setup_global_styles()
    
    # Main portfolio container
    with ui.column().classes('portfolio-container'):
        # Hero Section
        await create_hero_section()
        
        # About Section
        create_about_section()
        
        # Skills Section
        create_skills_section()
        
        # Projects Section
        await create_projects_section()
        
        # Experience Section
        create_experience_section()
        
        # Contact Section
        create_contact_section()
        
        # Footer
        create_footer()


@ui.page('/health')
async def health_check():
    """Health check endpoint for deployment monitoring."""
    return {"status": "healthy", "service": "ai-portfolio"}


def main():
    """Main application entry point."""
    
    # Configure the app
    app.add_static_files('/static', 'static')
    
    # Run the application
    ui.run(
        host=settings.host,
        port=settings.port,
        title=settings.app_title,
        favicon='🤖',
        dark=False,
        show=False,
        reload=settings.debug
    )


if __name__ in {"__main__", "__mp_main__"}:
    main()