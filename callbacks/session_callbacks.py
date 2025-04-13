from dash import Input, Output, State, callback, html, dcc
import dash_bootstrap_components as dbc
from utils.db_utils import verify_user, register_user
import dash

# Renders the dynamic navbar based on login session
@callback(
    Output("top-navbar", "children"),
    Input("session-store", "data")
)
def render_navbar(session_data):
    logged_in = session_data and session_data.get("logged_in", False)
    username = session_data.get("username") if logged_in else None

    if logged_in:
        return dbc.Row([
            dbc.Col(),
            dbc.Col([
                html.Span(f"Welcome, {username}", style={"marginRight": "20px", "fontWeight": "500"}),
                dbc.Button("Logout", id="logout-btn", color="danger", size="sm")
            ], width="auto")
        ], justify="end", align="center", style={"padding": "20px", "marginRight": "30px"})
    else:
        return dbc.Row([
            dbc.Col(),
            dbc.Col([
                dcc.Link("Log in", href="/login", style={
                    "marginRight": "10px", "color": "#0d6efd",
                    "fontWeight": "500", "textDecoration": "none"
                }),
                dcc.Link("Sign up", href="/signup", style={
                    "padding": "6px 12px", "backgroundColor": "#0d6efd",
                    "color": "white", "borderRadius": "6px", "textDecoration": "none",
                    "fontWeight": "500"
                }),
            ], width="auto")
        ], justify="end", align="center", style={"padding": "20px", "marginRight": "30px"})


# Handles login
@callback(
    Output("login-message", "children"),
    Output("session-store", "data"),
    Input("login-btn", "n_clicks"),
    State("login-email", "value"),
    State("login-password", "value"),
    prevent_initial_call=True
)
def handle_login(n_clicks, email, password):
    if not email or not password:
        return dbc.Alert("Please enter email and password.", color="warning"), dash.no_update

    if verify_user(email, password):
        return dbc.Alert("Login successful!", color="success"), {"email": email}

    return dbc.Alert("Invalid credentials. Please try again.", color="danger"), dash.no_update


# Handles signup
@callback(
    Output("signup-message", "children"),
    Input("signup-btn", "n_clicks"),
    State("signup-username", "value"),
    State("signup-email", "value"),
    State("signup-password", "value"),
    prevent_initial_call=True
)
def handle_signup(n, username, email, password):
    success, message = register_user(username, email, password)
    alert_type = "success" if success else "danger"
    return dbc.Alert(message, color=alert_type)


# Logout button clears the session
@callback(
    Output("session-store", "clear_data"),
    Input("logout-btn", "n_clicks"),
    prevent_initial_call=True
)
def logout_user(n):
    return True
