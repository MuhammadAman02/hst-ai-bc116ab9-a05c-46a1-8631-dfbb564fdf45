#!/usr/bin/env python3
"""
AI Engineer Portfolio - Entry Point
Professional portfolio showcasing AI engineering expertise
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import and run the application
if __name__ == "__main__":
    from app.main import main
    main()