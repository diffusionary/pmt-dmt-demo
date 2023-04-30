import modules.scripts as scripts
import requests
import gradio as gr
import os

from modules import script_callbacks

def parse_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            content = response.json()
            return content
        except:
            return "Error: file is not in valid JSON format"
    else:
        return "Error: could not download file from provided URL"

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            angle = gr.Slider(
                minimum=0.0,
                maximum=360.0,
                step=1,
                value=0,
                label="Angle"
            )
            checkbox = gr.Checkbox(
                False,
                label="Checkbox"
            )
        return [(ui_component, "Prompt Fetcher", "extension_template_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)