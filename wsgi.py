import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.layout = html.Div([
    html.Div([dcc.Input(placeholder='Type your review here...',
                        id='input-box', 
                        type='text',
                        size = 50)], 
        # style={'margin': '20px',
        #        'align':'center'}
        ),

    html.Div([html.Button('Submit', id='button')], 
        style={'margin': '20px'}
        ),

    html.Div(id='output-container-button',
             children='Enter a value and press submit')

], style={'width': 500, 
          'margin': '100px',
          'text-align':'center'})


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])

def update_output(n_clicks, value):
    print (n_clicks)
    if n_clicks == None:
        return "Your submitted Review:\n (you haven't submitted one yet)".format(
            value
        )
    else: 
        return "Your submitted Review:\n {}".format(
            value
        )


app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0/superhero/bootstrap.min.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
