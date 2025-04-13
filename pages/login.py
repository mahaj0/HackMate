# pages/login.py
import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from utils.db_utils import verify_user, register_user

dash.register_page(__name__, path="/login", name="Login")

layout = dbc.Container([
    html.H3("🔐 Log In", style={"marginBottom": "20px"}),
    dcc.Input(id="login-email", type="email", placeholder="Email", className="form-control mb-2"),
    dcc.Input(id="login-password", type="password", placeholder="Password", className="form-control mb-2"),
    dbc.Button("Log In", id="login-btn", color="primary", className="mb-2 me-2"),
    html.A("Go to Signup", href="/signup"),
    html.Div(id="login-message", style={"marginTop": "10px"})
])

@dash.callback(
    Output("login-message", "children"),
    Input("login-btn", "n_clicks"),
    State("login-email", "value"),
    State("login-password", "value"),
    prevent_initial_call=True
)
def handle_login(n, email, password):
    if verify_user(email, password):
        return dbc.Alert("Login successful!", color="success")
    return dbc.Alert("Invalid credentials. Please try again.", color="danger")
