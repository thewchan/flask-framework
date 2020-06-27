"""Render the bokeh visualization of the stock time series.

Display a stock ticker visualization based on user input.

A Simple Stock Ticker Visualization Web App
Copyright (C) 2020 Matthew Chan

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import json
import pandas as pd
import requests
import sys
import bokeh.plotting as bkp
from bokeh.embed import json_item
from bokeh.models import HoverTool
from bokeh.models.tickers import DatetimeTicker


def ticker(symbol):
    """Build stock ticker plot, return it to outside module."""
    KEY = 'Q7JC95BEFD22FQDA'

    def get_data(symbol):
        """Get stock data given symbol from api, return json."""
        url = (f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&"
               f"symbol={symbol}&apikey={KEY}")
        response = requests.get(url)
        data = response.json()

        return data

    def get_df(data):
        """Return formatted dataframe from json data."""
        df = pd.DataFrame(data['Time Series (Daily)']).T
        df.index = pd.to_datetime(df.index)
        df = df.sort_index().copy()
        df.columns = df.columns.str.replace(r'\d+\.\s', '')
        df.columns = map(str.title, df.columns)
        df = df.drop('Volume', axis=1).astype(float).copy()

        return df

    def build_plot(symbol):
        """Render the boken html file."""
        data = get_data(symbol)
        df = get_df(data)

        monthago = df.index[-20]
        now = df.index[-1]
        high = df.loc[monthago:now].max().max() + 5
        low = df.loc[monthago:now].min().min() - 5

        p = bkp.figure(title=f'{symbol} Stock Price',
                       y_axis_label='Dollars',
                       x_axis_type='datetime',
                       plot_width=800,
                       plot_height=400,
                       x_range=(monthago, now),
                       y_range=(low, high),
                       toolbar_location="below",
                       tools="pan,box_zoom,wheel_zoom,reset,save",
                       active_drag="pan",
                       )
        p.circle(df.index,
                 df['Open'],
                 size=8,
                 color='olive',
                 alpha=0.6,
                 legend_label='Open',
                 name='Open',
                 )
        p.circle(df.index,
                 df['Close'],
                 size=8,
                 color='orange',
                 alpha=0.6,
                 legend_label='Close',
                 name='Close',
                 )
        p.line(df.index,
               df['High'],
               line_width=2,
               color='steelblue',
               legend_label='High',
               name='High',
               )
        p.line(df.index,
               df['Low'],
               line_width=2,
               color='firebrick',
               legend_label='Low',
               name='Low'
               )
        p.xaxis.ticker = DatetimeTicker(desired_num_ticks=20)
        hover = HoverTool(tooltips=[('Time Series', '$name'),
                                    ('Date', '@x{%F}'),
                                    ('Price', '$@y{0.00 a}'),
                                    ],
                          formatters={'@x': 'datetime'})
        p.add_tools(hover)
        p.toolbar.active_inspect = hover
        p.sizing_mode = 'stretch_width'

        return p

    p = build_plot(symbol)

    return p


def main():
    """Return raw json text from plot with given ticker symbol argument.

    Default ticker symbol is 'IBM'.
    """
    if len(sys.argv) == 1:
        symbol = 'IBM'

    else:
        symbol = sys.argv[1]

    p = ticker(symbol)
    print(json.dumps(json_item(p, f'{symbol}_stocks')))


if __name__ == '__main__':
    main()
