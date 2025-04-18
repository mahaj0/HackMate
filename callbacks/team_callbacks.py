import dash
from dash import Input, Output, State, html, ctx
import dash_bootstrap_components as dbc
import base64

# Add member callback
@dash.callback(
    Output("team-store", "data"),
    Output("member-name", "value"),
    Output("member-role", "value"),
    Input("add-member-btn", "n_clicks"),
    State("member-name", "value"),
    State("member-role", "value"),
    State("team-store", "data"),
    prevent_initial_call=True
)
def add_member(n_clicks, name, role, data):
    if not name or not role:
        return data, "", ""
    data.append({"name": name, "role": role})
    return data, "", ""


# Display, delete, and export logic
@dash.callback(
    Output("team-output", "children"),
    Output("team-download-link", "href"),
    Output("export-container-team", "style"),
    Input("team-store", "data"),
    Input({"type": "delete-member", "index": dash.ALL}, "n_clicks"),
    State("team-store", "data"),
    prevent_initial_call=True
)
def update_team(_, delete_clicks, data):
    triggered_id = ctx.triggered_id

    if not data:
        return html.I("No members added yet.", className="text-muted"), "", {"display": "none"}

    if isinstance(triggered_id, dict) and triggered_id.get("type") == "delete-member":
        idx = triggered_id.get("index")
        if 0 <= idx < len(data):
            data.pop(idx)

    member_list = []
    for i, member in enumerate(data):
        member_list.append(
            html.Div([
                html.Strong(member["name"]),
                html.Span(f" – {member['role']}", className="ms-2"),
                dbc.Button("🗑", id={"type": "delete-member", "index": i}, size="sm", color="danger", className="ms-2", n_clicks=0),
            ], className="mb-2 d-flex align-items-center")
        )

    # Export logic
    export_text = "\n".join(f"- {member['name']} – {member['role']}" for member in data)
    encoded = base64.b64encode(export_text.encode()).decode()
    href = f"data:text/plain;base64,{encoded}"

    return member_list, href, {"display": "block"}
