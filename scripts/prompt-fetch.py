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
    url_input = gr.inputs.Textbox(label="Enter the URL of the .pmt file")
    with gr.Blocks(analytics_enabled=False) as ui_component:
        url = url_input()
        json_data = fetch_json_data(url)
        gr.json(json_data)
    return [(ui_component, "Prompt Fetcher", "promtp_fetcher")]

script_callbacks.on_ui_tabs(on_ui_tabs)