import dash
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/idea-generator", name="Idea Generator")

layout = dbc.Container([
    html.H2("💡 Idea Generator", style={"fontWeight": "bold", "marginBottom": "20px"}),

    html.Div("Describe what you want to build:", style={"marginBottom": "10px"}),

    dcc.Textarea(
        id="idea-input",
        placeholder="What are you building? 🚀",
        style={"width": "100%", "height": "100px", "marginBottom": "15px"},
    ),

    dbc.Button("Generate Ideas", id="generate-btn", color="primary", className="mb-4"),

    html.Div(id="idea-output", style={"marginTop": "30px"})
])
