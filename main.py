#!/usr/bin/env python
"""
Zero-Waste Mongolia Pilot System v1
Entry point for Gradio application.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the Gradio app
from ui.app import create_app

if __name__ == "__main__":
    debug = os.getenv("DEBUG", "False").lower() == "true"
    port = int(os.getenv("PORT", 7860))
    
    app = create_app()
    app.launch(
        server_name="0.0.0.0",
        server_port=port,
        debug=debug,
        share=False
    )
