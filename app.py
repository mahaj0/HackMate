import dash
from dash import ctx, html, dcc
import dash_bootstrap_components as dbc
import json

# Register callbacks separately
import callbacks.idea_callbacks
import callbacks.sprint_callbacks
import callbacks.session_callbacks 
import callbacks.home_callbacks
import callbacks.team_callbacks
import callbacks.pitch_callbacks


app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.FLATLY]
)

app.title = "HackMate"

# HTML Template
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .sidebar-link {
                text-decoration: none;
                color: #212529;
                font-weight: 500;
                font-size: 16px;
            }
            .sidebar-link:hover {
                color: #0d6efd;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""

# Navbar generator function moved to reusable location (we’ll reuse this in callbacks too)
def create_navbar(user_data):
    if user_data:
        return dbc.Row([
            dbc.Col([
                html.Div(f"👋 Welcome, {user_data['username']}", style={"marginRight": "20px"}),
                dbc.Button("Logout", id="logout-btn", color="danger", size="sm")
            ], width="auto")
        ], justify="end", align="center", style={"padding": "20px", "marginRight": "30px"})
    else:
        return dbc.Row([
            dbc.Col([
                dcc.Link("Log in", href="/login", style={
                    "marginRight": "10px", "color": "#0d6efd", "fontWeight": "500", "textDecoration": "none"
                }),
                dcc.Link("Sign up", href="/signup", style={
                    "padding": "6px 12px", "backgroundColor": "#0d6efd", "color": "white",
                    "borderRadius": "6px", "textDecoration": "none", "fontWeight": "500"
                }),
            ], width="auto")
        ], justify="end", align="center", style={"padding": "20px", "marginRight": "30px"})

# Sidebar
sidebar = dbc.Col([
    html.Div("HackMate", style={"fontSize": "24px", "fontWeight": "bold", "marginBottom": "40px", "paddingLeft": "10px"}),
    html.Div([
        dcc.Link("◉ LaunchPad", href="/", className="sidebar-link"),
        dcc.Link("👤 Team Hub", href="/team-dynamics", className="sidebar-link"),
        dcc.Link("⏱ TimeMaster", href="/sprint-planner", className="sidebar-link"),
        dcc.Link("🧰 BuildBox", href="/buildbox", className="sidebar-link"),
        dcc.Link("🖥 PitchForge", href="/pitch-coach", className="sidebar-link"),
        dcc.Link("👥 Team Vibes", href="/team-vibes", className="sidebar-link"),
    ], style={"display": "flex", "flexDirection": "column", "gap": "20px", "paddingLeft": "10px"}),
], width=2, style={
    "backgroundColor": "#f8f9fa", "height": "100vh", "padding": "30px 10px", "boxShadow": "2px 0 12px rgba(0,0,0,0.05)"
})

# Main content
main_content = dbc.Col([
    html.Div(id="dynamic-navbar"),
    dash.page_container
], width=10, style={"padding": "30px"})

# Final layout
session_store = dcc.Store(id="session-store", storage_type="local")  # <-- change this


app.layout = dbc.Container([
    session_store,
    dcc.Location(id="url", refresh=False),          # For page routing
    dbc.Row([
        sidebar,
        dbc.Col([
            html.Div(id="top-navbar"),  # Dynamic navbar here
            dash.page_container
        ], width=10, style={"padding": "30px"})
    ])
], fluid=True)


if __name__ == "__main__":
    app.run(debug=True)
