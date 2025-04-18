import dash
from dash import Input, Output, State, html, dcc, ctx
import base64
import dash_bootstrap_components as dbc


# Add milestone
@dash.callback(
    Output("sprint-store", "data"),
    Output("milestone-input", "value"),
    Output("deadline-input", "date"),
    Input("add-milestone-btn", "n_clicks"),
    State("milestone-input", "value"),
    State("deadline-input", "date"),
    State("sprint-store", "data"),
    prevent_initial_call=True
)
def add_milestone(n_clicks, milestone, deadline, current_data):
    if not milestone or not deadline:
        return current_data, "", dash.no_update
    current_data.append({"milestone": milestone, "deadline": deadline, "done": False})
    return current_data, "", dash.no_update


# Display + Interactions
@dash.callback(
    Output("sprint-output", "children"),
    Output("progress-bar", "value"),
    Output("progress-bar", "label"),
    Output("sprint-download-link", "href"),
    Output("export-container", "style"),
    Input("sprint-store", "data"),
    Input({"type": "toggle-done", "index": dash.dependencies.ALL}, "n_clicks"),
    Input({"type": "delete-item", "index": dash.dependencies.ALL}, "n_clicks"),
    State("sprint-store", "data"),
    prevent_initial_call=True
)
def update_output(data_trigger, toggle_clicks, delete_clicks, data):
    triggered_id = ctx.triggered_id

    if not data:
        return html.I("No milestones added yet.", className="text-muted"), 0, "0% complete", "", {"display": "none"}

    # Handle toggle or delete
    if isinstance(triggered_id, dict):
        idx = triggered_id.get("index")
        if triggered_id.get("type") == "toggle-done":
            data[idx]["done"] = not data[idx]["done"]
        elif triggered_id.get("type") == "delete-item":
            data.pop(idx)

    # UI list
    milestone_list = []
    for i, item in enumerate(data):
        milestone_list.append(
            html.Li([
                dbc.Checkbox(id={"type": "toggle-done", "index": i}, value=item["done"], className="me-2"),
                html.Span([
                    html.Strong(item["milestone"]),
                    f" → ",
                    html.Em(item["deadline"])
                ], style={"textDecoration": "line-through" if item["done"] else "none"}),
                dbc.Button("🗑", id={"type": "delete-item", "index": i}, size="sm", color="danger", className="ms-2", n_clicks=0),
            ], style={"marginBottom": "10px"})
        )

    # Progress calc
    total = len(data)
    done = sum(1 for item in data if item.get("done"))
    percent = int((done / total) * 100) if total else 0

    # Export data
    markdown_lines = [f"- {'[x]' if item['done'] else '[ ]'} **{item['milestone']}** → _{item['deadline']}_\n" for item in data]
    sprint_text = "\n".join(markdown_lines)
    encoded = base64.b64encode(sprint_text.encode()).decode()
    href = f"data:text/plain;base64,{encoded}"

    return html.Ul(milestone_list), percent, f"{percent}% complete", href, {"display": "block"}
