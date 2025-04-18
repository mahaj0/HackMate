import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/team-dynamics", name="Team Dynamics")

layout = dbc.Container([
    html.Div([
        html.H2("👥 Team Dynamics", className="mb-3"),
        html.P("Add team members with their roles:", className="text-muted"),

        dbc.InputGroup([
            dbc.Input(id="member-name", placeholder="Name", type="text"),
            dbc.Input(id="member-role", placeholder="Role", type="text"),
            dbc.Button("Add", id="add-member-btn", color="primary", className="ms-2"),
        ], className="mb-4", style={"gap": "8px"}),

        dcc.Store(id="team-store", data=[]),

        html.Div(id="team-output", className="mt-3"),
        html.Div(
            dbc.Button("Export Team List", id="team-download-link", download="team_list.txt", href="", target="_blank", color="success"),
            id="export-container-team",
            style={"display": "none"},
            className="mt-4"
        )
    ], style={"maxWidth": "800px", "margin": "0 auto"})
])
