import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from datetime import date

dash.register_page(__name__, path="/sprint-planner", name="Sprint Planner")

layout = dbc.Container([
    html.Div([
        html.H2("📅 Sprint Planner", className="mb-3"),

        html.P("Add milestones with deadlines:", className="text-muted"),

        dbc.InputGroup([
            dbc.Input(id="milestone-input", placeholder="Milestone", type="text"),
            dcc.DatePickerSingle(
                id="deadline-input",
                date=date.today(),
                display_format="YYYY-MM-DD",
                className="form-control",
                style={"maxWidth": "180px"}
            ),
            dbc.Button("Add", id="add-milestone-btn", color="primary", className="ms-2")
        ], className="mb-4", style={"gap": "8px"}),

        dbc.Progress(id="progress-bar", value=0, label="0% complete", className="mb-3", striped=True, animated=True),

        dcc.Store(id="sprint-store", data=[]),

        html.Div(id="sprint-output"),

        html.Div(
            dbc.Button("Export Sprint Plan", id="sprint-download-link", download="sprint_plan.txt", href="", target="_blank", color="success"),
            className="mt-4", id="export-container", style={"display": "none"}
        )
    ], style={"maxWidth": "800px", "margin": "0 auto"})
])
