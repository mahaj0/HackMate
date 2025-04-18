import dash
from dash import Input, Output, State, html, dcc
import dash_bootstrap_components as dbc
import base64
from utils.gemini_utils import get_gemini_ideas


# Manual pitch preview generation
@dash.callback(
    Output("pitch-preview", "children"),
    Output("pitch-download-link", "href"),
    Output("export-pitch-container", "style"),
    Input("generate-pitch-btn", "n_clicks"),
    State("pitch-problem", "value"),
    State("pitch-solution", "value"),
    State("pitch-audience", "value"),
    State("pitch-uvp", "value"),
    State("pitch-tech", "value"),
    State("pitch-demo", "value"),
    prevent_initial_call=True
)
def generate_pitch(n_clicks, problem, solution, audience, uvp, tech, demo):
    print("🔧 DEBUG: Generate Pitch button clicked.")
    print(f"  • Problem: {problem}")
    print(f"  • Solution: {solution}")
    print(f"  • Audience: {audience}")
    print(f"  • UVP: {uvp}")
    print(f"  • Tech: {tech}")
    print(f"  • Demo: {demo}")

    sections = [
        ("🔍 Problem", problem),
        ("💡 Solution", solution),
        ("🎯 Target Audience", audience),
        ("✨ Unique Value Proposition", uvp),
        ("⚙️ Tech Stack", tech),
        ("📽️ Demo", demo),
    ]

    markdown = "\n\n".join(f"### {title}\n{content}" for title, content in sections if content)
    encoded = base64.b64encode(markdown.encode()).decode()
    href = f"data:text/plain;base64,{encoded}"

    return dcc.Markdown(markdown), href, {"display": "block"}


# AI generation
@dash.callback(
    Output("pitch-problem", "value"),
    Output("pitch-solution", "value"),
    Output("pitch-audience", "value"),
    Output("pitch-uvp", "value"),
    Output("pitch-tech", "value"),
    Output("pitch-demo", "value"),
    Output("ai-status", "children"),
    Input("ai-generate-btn", "n_clicks"),
    prevent_initial_call=True
)
def generate_ai_pitch(n_clicks):
    print("⚡ Gemini AI button clicked")

    response = get_gemini_ideas("Generate a pitch structure including problem, solution, audience, UVP, tech stack, and demo.")

    if not response or not isinstance(response, dict):
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, "⚠️ Failed to generate pitch."

    return (
        response.get("problem", ""),
        response.get("solution", ""),
        response.get("audience", ""),
        response.get("uvp", ""),
        response.get("tech", ""),
        response.get("demo", ""),
        "✅ AI pitch generated!"
    )
