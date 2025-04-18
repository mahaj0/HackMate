from dash import Input, Output, callback, html
import dash_bootstrap_components as dbc

@callback(
    Output("welcome-banner", "children"),
    Input("session-store", "data"),
    Input("dummy-home-refresh", "data")
)
def show_login_status(session_data, _):
    if session_data and session_data.get("logged_in"):
        username = session_data.get("username")
        return dbc.Alert(f"👋 Welcome back, {username}!", color="info")
    return ""
