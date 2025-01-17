from dash import Dash, dcc, html, Input, Output
import dash_player

app = Dash(__name__)

app.scripts.config.serve_locally = True


app.layout = html.Div(
    [
        dash_player.DashPlayer(
            id="video-player",
            url="https://media.w3.org/2010/05/bunny/movie.ogv",
            controls=True,
        ),
        dcc.Checklist(
            id="radio-bool-props",
            options=[
                {"label": val.capitalize(), "value": val}
                for val in ["playing", "loop", "controls", "muted", "seekTo"]
            ],
            value=["controls"],
        ),
    ]
)


@app.callback(Output("video-player", "playing"), Input("radio-bool-props", "value"))
def update_prop_playing(values):
    return "playing" in values


@app.callback(Output("video-player", "loop"), Input("radio-bool-props", "value"))
def update_prop_loop(values):
    return "loop" in values


@app.callback(Output("video-player", "controls"), Input("radio-bool-props", "value"))
def update_prop_controls(values):
    return "controls" in values


@app.callback(Output("video-player", "muted"), Input("radio-bool-props", "value"))
def update_prop_muted(values):
    return "muted" in values


@app.callback(Output("video-player", "seekTo"), Input("radio-bool-props", "value"))
def update_prop_seekTo(values):
    if "seekTo" in values:
        return 5


if __name__ == "__main__":
    app.run(debug=True)
