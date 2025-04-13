import dash
from dash import Input, Output, State, html, dcc
import base64

@dash.callback(
    Output("sprint-store", "data"),
    Output("milestone-input", "value"),
    Output("deadline-input", "value"),
    Input("add-milestone-btn", "n_clicks"),
    State("milestone-input", "value"),
    State("deadline-input", "value"),
    State("sprint-store", "data"),
    prevent_initial_call=True
)
def add_milestone(n, milestone, deadline, current_data):
    if milestone and deadline:
        current_data.append({"milestone": milestone, "deadline": deadline})
    return current_data, "", ""


@dash.callback(
    Output("sprint-output", "children"),
    Output("sprint-download-link", "href"),
    Output("sprint-download-link", "style"),
    Input("sprint-store", "data"),
)
def display_sprint_plan(data):
    if not data:
        return html.I("No milestones added yet."), "", {"display": "none"}

    markdown_lines = [f"- **{item['milestone']}** → _{item['deadline']}_\n" for item in data]
    sprint_text = "\n".join(markdown_lines)

    download_href = f"data:text/plain;base64,{base64.b64encode(sprint_text.encode()).decode()}"

    return dcc.Markdown(sprint_text, style={"whiteSpace": "pre-wrap"}), download_href, {"display": "inline-block"}
