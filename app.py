import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, State
from openai_utils import get_ai_ideas

# Initialize app
app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.FLATLY]
)
app.title = "HackMate"

# Inject sidebar styles directly
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

# Sidebar
sidebar = dbc.Col(
    [
        html.Div("HackMate", style={
            "fontSize": "24px",
            "fontWeight": "bold",
            "marginBottom": "40px",
            "paddingLeft": "10px"
        }),
        html.Div([
            dcc.Link("◉ LaunchPad", href="/", className="sidebar-link"),
            dcc.Link("👤 Team Hub", href="/team-dynamics", className="sidebar-link"),
            dcc.Link("⏱ TimeMaster", href="/sprint-planner", className="sidebar-link"),
            dcc.Link("🧰 BuildBox", href="/buildbox", className="sidebar-link"),
            dcc.Link("🖥 PitchForge", href="/pitch-coach", className="sidebar-link"),
            dcc.Link("👥 Team Vibes", href="/team-vibes", className="sidebar-link"),
        ], style={
            "display": "flex",
            "flexDirection": "column",
            "gap": "20px",
            "paddingLeft": "10px"
        }),
    ],
    width=2,
    style={
        "backgroundColor": "#f8f9fa",
        "height": "100vh",
        "padding": "30px 10px",
        "boxShadow": "2px 0 12px rgba(0,0,0,0.05)"
    }
)

# Page container
main_content = dbc.Col(
    [
        dash.page_container
    ],
    width=10,
    style={"padding": "30px"}
)

# App layout
app.layout = dbc.Container([
    dbc.Row([
        sidebar,
        main_content
    ])
], fluid=True)

@app.callback(
    Output("idea-output", "children"),
    Input("generate-btn", "n_clicks"),
    State("idea-input", "value"),
    prevent_initial_call=True
)
def generate_ideas(n, user_input):
    if not user_input:
        return dbc.Alert("Please enter what you're building.", color="warning")

    try:
        ideas = get_ai_ideas(user_input)
        return html.Div([
            html.H5("Here are some AI-generated ideas:"),
            html.Pre(ideas, style={"whiteSpace": "pre-wrap"})
        ])
    except Exception as e:
        return dbc.Alert(f"Something went wrong: {str(e)}", color="danger")


if __name__ == "__main__":
    app.run(debug=True)