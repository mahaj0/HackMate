import dash
from dash import html, dcc, Output, Input, State, ctx
import dash_bootstrap_components as dbc
from utils.gemini_utils import get_gemini_ideas

dash.register_page(__name__, path="/idea-generator", name="Idea Generator")

layout = dbc.Container([
    html.H2("💡 Idea Generator", style={"fontWeight": "bold", "marginBottom": "20px"}),

    html.Div("Describe what you want to build:", style={"marginBottom": "10px"}),

    dcc.Textarea(
        id="idea-input",
        placeholder="What are you building? 🚀",
        style={"width": "100%", "height": "100px", "marginBottom": "15px"},
    ),

    dbc.Button("Generate Ideas", id="generate-btn", color="primary", className="me-2"),
    dbc.Button("Regenerate", id="regenerate-btn", color="secondary", outline=True, className="me-2"),
    html.A("Export Ideas", id="download-link", download="ai_ideas.txt", href="", target="_blank", style={"display": "none"}),

    dcc.Store(id="last-prompt-store"),
    dcc.Store(id="last-ideas-store"),

    html.Div(id="idea-output", style={"marginTop": "30px"})
])
