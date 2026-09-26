#!/usr/bin/env python
"""
Gradio application for Zero-Waste Mongolia Pilot System v1.
"""

import os
import gradio as gr
from dotenv import load_dotenv
from database.connection import test_connection, init_db

load_dotenv()


def create_app():
    """
    Create and configure the Gradio application.
    
    Returns:
        gr.Blocks interface
    """
    
    # Test and initialize database
    if not test_connection():
        print("Warning: Database connection failed. Attempting to initialize...")
        try:
            init_db()
        except Exception as e:
            print(f"Error: Could not initialize database: {e}")
    
    # Create the Gradio interface
    with gr.Blocks(
        title="Zero-Waste Mongolia Pilot System v1",
        theme=gr.themes.Soft()
    ) as demo:
        
        # Header
        gr.Markdown("""
        # 🌍 Zero-Waste Mongolia Pilot System v1
        
        A government-led circular waste management system for Mongolia.
        
        ---
        """)
        
        # Tabs for different functions
        with gr.Tabs():
            
            # Tab 1: Register Waste Batch
            with gr.TabItem("📝 Register Waste Batch"):
                gr.Markdown("""
                ### Register a New Waste Batch
                
                Provide information about your waste batch to generate a unique Waste ID and QR code.
                """)
                
                with gr.Row():
                    category = gr.Dropdown(
                        choices=["Battery", "E-waste", "Plastic", "Paper/Cardboard", "Glass", 
                                "Metal", "Textile", "Organic", "Used Tire", "Used Oil", "Other Hazardous Waste"],
                        label="Waste Category",
                        scale=1
                    )
                
                with gr.Row():
                    source_name = gr.Textbox(
                        label="Your Organization / Name",
                        placeholder="e.g., ABC Manufacturing",
                        scale=2
                    )
                    weight = gr.Number(
                        label="Weight (kg)",
                        value=1,
                        scale=1
                    )
                
                with gr.Row():
                    source_phone = gr.Textbox(
                        label="Contact Phone",
                        placeholder="+976 XX XXX XXXX",
                        scale=1
                    )
                    source_address = gr.Textbox(
                        label="Address",
                        placeholder="e.g., Ulaanbaatar, Mongolia",
                        scale=1
                    )
                
                notes = gr.Textbox(
                    label="Notes (optional)",
                    placeholder="Any additional information...",
                    lines=3
                )
                
                register_btn = gr.Button("🎫 Generate Waste ID & QR Code", variant="primary")
                
                # Output section
                gr.Markdown("---")
                with gr.Row():
                    waste_id_output = gr.Textbox(
                        label="Your Waste ID",
                        interactive=False,
                        visible=False
                    )
                    
                qr_output = gr.Image(
                    label="QR Code",
                    visible=False
                )
                
                # Placeholder for register function
                def register_waste_placeholder(category, source_name, weight, source_phone, source_address, notes):
                    waste_id = "WM-20260926-000001"  # Placeholder
                    return waste_id, None  # Return waste_id and QR code
                
                register_btn.click(
                    fn=register_waste_placeholder,
                    inputs=[category, source_name, weight, source_phone, source_address, notes],
                    outputs=[waste_id_output, qr_output]
                )
            
            # Tab 2: Public Lookup
            with gr.TabItem("🔍 Public Lookup"):
                gr.Markdown("""
                ### Track Your Waste
                
                Enter a Waste ID or scan the QR code to see where your waste is in its journey.
                """)
                
                with gr.Row():
                    lookup_input = gr.Textbox(
                        label="Waste ID or QR Code",
                        placeholder="e.g., WM-20260926-000001",
                        scale=4
                    )
                    lookup_btn = gr.Button("🔍 Search", scale=1, variant="primary")
                
                gr.Markdown("---")
                
                # Output section
                with gr.Group():
                    category_display = gr.Textbox(label="Category", interactive=False, visible=False)
                    reg_date_display = gr.Textbox(label="Registration Date", interactive=False, visible=False)
                    status_display = gr.Textbox(label="Current Status", interactive=False, visible=False)
                    weight_display = gr.Textbox(label="Weight (kg)", interactive=False, visible=False)
                    
                    history_display = gr.Dataframe(
                        label="Waste Journey Timeline",
                        visible=False
                    )
                
                # Placeholder for lookup function
                def lookup_waste_placeholder(waste_id):
                    return "Battery", "2026-09-26", "Registered", "5.0", None
                
                lookup_btn.click(
                    fn=lookup_waste_placeholder,
                    inputs=[lookup_input],
                    outputs=[category_display, reg_date_display, status_display, weight_display, history_display]
                )
            
            # Tab 3: Update Status
            with gr.TabItem("📊 Update Status"):
                gr.Markdown("""
                ### Update Waste Batch Status
                
                Log status updates as the waste moves through the system.
                """)
                
                with gr.Row():
                    status_waste_id = gr.Textbox(
                        label="Waste ID",
                        placeholder="e.g., WM-20260926-000001",
                        scale=2
                    )
                    status_lookup_btn = gr.Button("📋 Load", scale=1)
                
                with gr.Row():
                    current_status = gr.Textbox(
                        label="Current Status",
                        interactive=False
                    )
                    new_status = gr.Dropdown(
                        choices=["Awaiting Collection", "Collected", "In Transit", 
                                "Received", "Reused", "Repaired", "Recycled", "Disposed"],
                        label="New Status",
                        scale=1
                    )
                
                with gr.Row():
                    actor_name_input = gr.Textbox(
                        label="Your Name / Organization",
                        placeholder="e.g., Collection Team A",
                        scale=2
                    )
                    weight_update = gr.Number(
                        label="Weight (kg) - Optional",
                        scale=1
                    )
                
                status_notes = gr.Textbox(
                    label="Notes (optional)",
                    lines=3
                )
                
                update_btn = gr.Button("✅ Update Status", variant="primary")
                
                # Output
                update_output = gr.Textbox(
                    label="Result",
                    interactive=False,
                    visible=False
                )
                
                # Placeholder functions
                def load_waste_status(waste_id):
                    return "Registered"  # Placeholder
                
                def update_waste_status(waste_id, new_status, actor_name, weight, notes):
                    return "✓ Status updated successfully"  # Placeholder
                
                status_lookup_btn.click(
                    fn=load_waste_status,
                    inputs=[status_waste_id],
                    outputs=[current_status]
                )
                
                update_btn.click(
                    fn=update_waste_status,
                    inputs=[status_waste_id, new_status, actor_name_input, weight_update, status_notes],
                    outputs=[update_output]
                )
            
            # Tab 4: Admin Dashboard
            with gr.TabItem("⚙️ Admin Dashboard"):
                gr.Markdown("""
                ### Admin Dashboard (v1)
                
                **Note:** Full admin features coming soon.
                
                Currently available:
                - System status
                - Database connection test
                """)
                
                with gr.Row():
                    admin_test_btn = gr.Button("🔧 Test Database Connection", variant="primary")
                
                admin_output = gr.Textbox(
                    label="System Status",
                    interactive=False,
                    lines=5
                )
                
                def test_db_status():
                    from database.connection import test_connection
                    result = test_connection()
                    return "✓ Database connection: OK" if result else "✗ Database connection: FAILED"
                
                admin_test_btn.click(
                    fn=test_db_status,
                    outputs=[admin_output]
                )
        
        # Footer
        gr.Markdown("""
        ---
        **Zero-Waste Mongolia Pilot System v1**
        
        A government-led circular waste management system for Mongolia.
        """)
    
    return demo


if __name__ == "__main__":
    app = create_app()
    app.launch(server_name="0.0.0.0", server_port=7860)
