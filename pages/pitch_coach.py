import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/pitch-coach", name="Pitch Coach")

layout = dbc.Container([
    html.Div([
        html.H2("🖥️ Pitch Coach", className="mb-3"),
        html.P("Craft a compelling pitch for your project:"),

        dbc.Accordion([
            dbc.AccordionItem([
                dcc.Textarea(id="pitch-problem", placeholder="What problem are you solving?", className="form-control", style={"height": "100px"})
            ], title="🔍 Problem"),
            dbc.AccordionItem([
                dcc.Textarea(id="pitch-solution", placeholder="What is your solution?", className="form-control", style={"height": "100px"})
            ], title="💡 Solution"),
            dbc.AccordionItem([
                dcc.Textarea(id="pitch-audience", placeholder="Who is your target audience?", className="form-control", style={"height": "100px"})
            ], title="🎯 Target Audience"),
            dbc.AccordionItem([
                dcc.Textarea(id="pitch-uvp", placeholder="What is your unique value proposition?", className="form-control", style={"height": "100px"})
            ], title="✨ Unique Value Proposition"),
            dbc.AccordionItem([
                dcc.Textarea(id="pitch-tech", placeholder="Mention your tech stack.", className="form-control", style={"height": "100px"})
            ], title="⚙️ Tech Stack"),
            dbc.AccordionItem([
                dcc.Textarea(id="pitch-demo", placeholder="Describe your demo briefly.", className="form-control", style={"height": "100px"})
            ], title="📽️ Demo"),
        ], start_collapsed=True, className="mb-4"),

        dbc.Button("Generate Pitch Preview", id="generate-pitch-btn", color="primary", className="mb-3"),

        html.Hr(),

        html.Div(id="pitch-preview", className="mt-3"),

        html.Div(
            dbc.Button("Download Pitch", id="pitch-download-link", href="", target="_blank", download="pitch.txt", color="success"),
            id="export-pitch-container",
            style={"display": "none"},
            className="mt-3"
        )
    ], style={"maxWidth": "800px", "margin": "0 auto"})
])
