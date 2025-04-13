from dash import html, dcc

sidebar = html.Div(
    [
        html.H2("HackMate", className="display-6", style={
            "fontWeight": "bold",
            "marginBottom": "40px",
            "fontSize": "28px"
        }),

        html.Div([
            dcc.Link("⚪ LaunchPad", href="/", className="sidebar-link"),
            dcc.Link("💡 Idea Generator", href="/idea-generator", className="sidebar-link"),
            dcc.Link("🧑‍💼 Team Hub", href="/team-dynamics", className="sidebar-link"),
            dcc.Link("⏱️ TimeMaster", href="/sprint-planner", className="sidebar-link"),
            dcc.Link("💼 BuildBox", href="/buildbox", className="sidebar-link"),
            dcc.Link("🖥️ PitchForge", href="/pitch-coach", className="sidebar-link"),
            dcc.Link("👥 Team Vibes", href="/team-vibes", className="sidebar-link"),
        ], style={
            "lineHeight": "2.5em",
            "fontSize": "1.05rem",
            "display": "flex",
            "flexDirection": "column",
            "gap": "6px"
        })
    ],
    style={
        "backgroundColor": "#f8f9fa",
        "height": "100vh",
        "padding": "30px 20px",
        "borderRight": "1px solid #ddd"
    }
)
