import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/signup", name="Signup")

layout = dbc.Container([
    html.H3("📝 Sign Up", style={"marginBottom": "20px"}),
    dcc.Input(id="signup-username", type="text", placeholder="Username", className="form-control mb-2"),
    dcc.Input(id="signup-email", type="email", placeholder="Email", className="form-control mb-2"),
    dcc.Input(id="signup-password", type="password", placeholder="Password", className="form-control mb-2"),
    dbc.Button("Sign Up", id="signup-btn", color="success", className="mb-2 me-2"),
    html.A("Go to Login", href="/login"),
    html.Div(id="signup-message", style={"marginTop": "10px"})
])
