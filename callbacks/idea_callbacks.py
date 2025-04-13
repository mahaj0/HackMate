from dash import Output, Input, State, dcc, html, ctx
import dash
import dash_bootstrap_components as dbc
from utils.gemini_utils import get_gemini_ideas  # or your correct import path
import base64

@dash.callback(
    Output("idea-output", "children"),
    Output("last-prompt-store", "data"),
    Output("last-ideas-store", "data"),
    Output("download-link", "href"),
    Output("download-link", "style"),
    Input("generate-btn", "n_clicks"),
    Input("regenerate-btn", "n_clicks"),
    State("idea-input", "value"),
    State("last-prompt-store", "data"),
    prevent_initial_call=True
)
def generate_or_regenerate(n_clicks, n_regen, current_input, last_input):
    triggered_id = ctx.triggered_id
    prompt = current_input if triggered_id == "generate-btn" else last_input

    if not prompt:
        return dbc.Alert("Please enter a prompt.", color="warning"), dash.no_update, dash.no_update, "", {"display": "none"}

    try:
        ideas = get_gemini_ideas(prompt)
        markdown_output = dcc.Markdown(ideas, style={"whiteSpace": "pre-wrap", "fontFamily": "monospace"})

        download_text = base64.b64encode(ideas.encode()).decode()
        href_link = f"data:text/plain;base64,{download_text}"

        return (
            html.Div([
                html.H5("Here are some AI-generated ideas:"),
                markdown_output
            ]),
            prompt,
            ideas,
            href_link,
            {"display": "inline-block"}
        )

    except Exception as e:
        return dbc.Alert(f"Something went wrong: {str(e)}", color="danger"), dash.no_update, dash.no_update, "", {"display": "none"}
