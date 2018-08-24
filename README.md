# Flask on Heroku

This project is intended to help you tie together some important concepts and
technologies from the 12-day course, including Git, Flask, JSON, Pandas,
Requests, Heroku, and Bokeh for visualization.

The repository contains a basic template for a Flask configuration that will
work on Heroku.

We will use docker to create a container which allows us to use a wider variety of packages than a bare heroku install and get around the heroku slug limit (useful for deploying scikit-learn models).  This is motivated by [python-miniconda](https://github.com/heroku-examples/python-miniconda)

A [finished example](https://lemurian.herokuapp.com) that demonstrates some basic functionality.

## Step 1: Setup and deploy
- You will probably want to do this on your DO box where Docker is easy to install. Look up how to install docker here [Docker Documentation](https://docs.docker.com/engine/installation/)
- Git clone the existing template repository.
`app/requirements.txt` and `app/conda-requirements.txt`  contain some default settings which will be installed by `pip` and `conda` respectively.
- There is some boilerplate HTML in `app/templates/`
- Create Heroku application with `heroku create <app_name>` or leave blank to auto-generate a name.
- Login to container with `heroku container:login`
- Deploy to Heroku: `heroku container:push web`
- Release image on Heroku: `heroku container:release web`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 3: Use Bokeh to plot pandas data
- Create a Bokeh plot from the dataframe.
- Consult the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Make the plot visible on your website through embedded HTML or other methods - this is where Flask comes in to manage the interactivity and display the desired content.
- Some good references for Flask: [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off", and [this tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
