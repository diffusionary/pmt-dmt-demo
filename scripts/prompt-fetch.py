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
        
def load_prompt():
    with gr.Column():
        with gr.Row():
            pmt_loc = gr.inputs.Textbox(label="Load Prompt from URL:")
            pmt_rec = gr.inputs.Textbox(label="Results:")
            button = gr.Button("Load", variant='primary')
            button.click(parse_file, inputs=[pmt_loc], outputs=[ptm_rec])

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        load_prompt()
        return [(ui_component, "Prompt Loader", "extension_template_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)