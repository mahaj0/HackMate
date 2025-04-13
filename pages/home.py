import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", name="LaunchPad")

layout = html.Div([
    html.H1("AI-Powered Hackathon Co-Pilot", style={"marginBottom": "30px"}),

    dbc.Row([
        dbc.Col(
            dcc.Link(
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Idea Generator", className="card-title"),
                        html.P("Brainstorm and refine project ideas"),
                    ])
                ], className="mb-4", style={"textDecoration": "none", "color": "inherit"}),
                href="/idea-generator",
                style={"textDecoration": "none"}
            ),
            width=6
        ),
        dbc.Col(
            dcc.Link(
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Sprint Planner", className="card-title"),
                        html.P("Create a timeline with milestones"),
                    ])
                ], className="mb-4", style={"textDecoration": "none", "color": "inherit"}),
                href="/sprint-planner",
                style={"textDecoration": "none"}
            ),
            width=6
        ),
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Link(
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Team Dynamics", className="card-title"),
                        html.P("Optimize roles and collaboration"),
                    ])
                ], className="mb-4", style={"textDecoration": "none", "color": "inherit"}),
                href="/team-dynamics",
                style={"textDecoration": "none"}
            ),
            width=6
        ),
        dbc.Col(
            dcc.Link(
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Pitch Coach", className="card-title"),
                        html.P("Get help with your final pitch"),
                    ])
                ], className="mb-4", style={"textDecoration": "none", "color": "inherit"}),
                href="/pitch-coach",
                style={"textDecoration": "none"}
            ),
            width=6
        ),
    ])
])
