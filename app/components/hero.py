"""Hero section component for the AI Engineer portfolio."""

from nicegui import ui
from core.utils import get_professional_image
import asyncio


async def create_hero_section() -> None:
    """Create the hero section with professional introduction."""
    
    with ui.element('div').classes('hero-section'):
        with ui.column().classes('w-full items-center'):
            # Profile image
            profile_image = await get_professional_image(
                keywords=["professional", "technology", "workspace"],
                width=200,
                height=200
            )
            
            ui.image(profile_image).classes(
                'w-48 h-48 rounded-full border-4 border-white shadow-lg mb-6'
            ).style('object-fit: cover;')
            
            # Main title
            ui.html('<h1 class="hero-title">AI Engineer</h1>')
            
            # Subtitle
            ui.html('<p class="hero-subtitle">Machine Learning • Deep Learning • Data Science</p>')
            
            # Description
            with ui.column().classes('max-w-3xl text-center'):
                ui.markdown('''
                **Transforming data into intelligent solutions** with cutting-edge AI technologies.
                Specialized in building scalable machine learning systems, neural networks, 
                and data-driven applications that solve real-world problems.
                ''').classes('text-lg mb-8 opacity-90')
            
            # CTA buttons
            with ui.row().classes('gap-4 mt-4'):
                ui.button('View Projects', on_click=lambda: ui.run_javascript(
                    'document.querySelector("#projects").scrollIntoView({behavior: "smooth"})'
                )).classes('btn-primary text-lg px-8 py-3')
                
                ui.button('Contact Me', on_click=lambda: ui.run_javascript(
                    'document.querySelector("#contact").scrollIntoView({behavior: "smooth"})'
                )).classes('bg-transparent border-2 border-white text-white px-8 py-3 rounded-full hover:bg-white hover:text-purple-600 transition-all')