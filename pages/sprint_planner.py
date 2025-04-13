import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/sprint-planner", name="Sprint Planner")

layout = dbc.Container([
    html.H2("📅 Sprint Planner", style={"fontWeight": "bold", "marginBottom": "20px"}),

    html.Div("Add milestones with deadlines:", style={"marginBottom": "10px"}),

    dbc.Row([
        dbc.Col(dcc.Input(id="milestone-input", placeholder="Milestone", type="text", className="form-control"), width=6),
        dbc.Col(dcc.Input(id="deadline-input", placeholder="Deadline (e.g. 2025-04-20)", type="text", className="form-control"), width=4),
        dbc.Col(dbc.Button("Add", id="add-milestone-btn", color="primary"), width=2),
    ], className="mb-3"),

    dcc.Store(id="sprint-store", data=[]),

    html.Hr(),

    html.Div(id="sprint-output"),

    html.Div([
        html.A("Export Sprint Plan", id="sprint-download-link", download="sprint_plan.txt", href="", target="_blank", style={"display": "none"})
    ], className="mt-3")
])
