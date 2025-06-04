"""About section component for the AI Engineer portfolio."""

from nicegui import ui
from core.utils import get_professional_image
import asyncio


def create_about_section() -> None:
    """Create the about section with professional background."""
    
    with ui.element('div').classes('section').style('background: #f8fafc;'):
        ui.html('<h2 class="section-title" id="about">About Me</h2>')
        
        with ui.row().classes('w-full gap-8 items-center'):
            # About content
            with ui.column().classes('flex-1'):
                ui.markdown('''
                ## Passionate AI Engineer & Data Scientist
                
                With **5+ years of experience** in artificial intelligence and machine learning, 
                I specialize in developing intelligent systems that drive business value and 
                innovation. My expertise spans the entire AI development lifecycle, from 
                research and prototyping to production deployment and scaling.
                
                ### What I Do:
                - **Machine Learning Engineering**: Building robust ML pipelines and model deployment systems
                - **Deep Learning**: Developing neural networks for computer vision, NLP, and time series analysis
                - **Data Science**: Extracting insights from complex datasets using statistical analysis
                - **MLOps**: Implementing CI/CD for machine learning with monitoring and versioning
                - **AI Research**: Staying current with latest developments in AI and contributing to open source
                
                ### My Approach:
                I believe in **practical AI solutions** that solve real problems. Every project 
                starts with understanding the business need, followed by rigorous experimentation, 
                and ends with scalable, maintainable systems that deliver measurable impact.
                ''').classes('text-lg leading-relaxed')
            
            # Professional image
            with ui.column().classes('flex-none'):
                # This will be replaced with an actual professional image
                ui.image('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=500&fit=crop&crop=face').classes(
                    'w-80 h-96 rounded-2xl shadow-xl'
                ).style('object-fit: cover;')
        
        # Key achievements
        with ui.row().classes('w-full gap-6 mt-12'):
            achievements = [
                {"number": "50+", "label": "ML Models Deployed", "icon": "🚀"},
                {"number": "95%", "label": "Model Accuracy Average", "icon": "🎯"},
                {"number": "10M+", "label": "Data Points Processed", "icon": "📊"},
                {"number": "15+", "label": "AI Projects Completed", "icon": "✅"}
            ]
            
            for achievement in achievements:
                with ui.card().classes('flex-1 text-center p-6'):
                    ui.html(f'<div class="text-4xl mb-2">{achievement["icon"]}</div>')
                    ui.html(f'<div class="text-3xl font-bold text-purple-600 mb-1">{achievement["number"]}</div>')
                    ui.html(f'<div class="text-gray-600">{achievement["label"]}</div>')