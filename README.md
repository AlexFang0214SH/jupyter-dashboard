# Jupyter Dashboard - Voila

## Introduction
This notebook is a dashboard publication tool via Jupyter-Voila. It is developed based on this [tutorial](https://github.com/duarteocarmo/interactive-dashboard-post) by Duarte O. Carmo.

He has also published an article to outline his tutorial [here](https://pbpython.com/interactive-dashboards.html).

This notebook is organized into modules to complete the following tasks:

1. Data Analysis
2. Data Visualization
3. Dashboard Publication

## VTA Open Data

This dashboard visualizes cumulative monthly ridership from the VTA Open Data [Portal](http://data.vta.org/). The Portal is described as "central location for access to VTA's open data, including transit, active transportation, congestion management and more."

The [monthly ridership data](http://data.vta.org/datasets/ridership-by-route-cumulative-monthly) includes fields for train route, line type, ridership and cumulative monthly period. It consists of data from 2013 to 2018; chart below shows monthly cumulative passenger boarding count by VTA train line type.

![Plot](https://github.com/walteryu/jupyter-dashboard/blob/master/posts/cplot_linetype.png)

## Original README

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/duarteocarmo/interactive-dashboard-post/master?urlpath=%2Fvoila%2Frender%2Fnotebooks%2FDashboard.ipynb)  [![Python](https://img.shields.io/badge/python-v3.7-blue)](https://www.python.org/)  [![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://duarteocarmo.com)

# From notebook to web application 📔​+🔮=💥

[Visit the original blog post!](https://duarteocarmo.com)

* [What is this? 🤔](#what-is-this-thinking)
* [Screenshots](#screenshots)
* [How do I run the notebook? 📔](#how-do-i-run-the-notebook-notebook_with_decorative_cover)
* [How do I run the dashboard? 📊](#how-do-i-run-the-dashboard-bar_chart)


## What is this? :thinking:

A blog post/tutorial for the [Practical Business Python](https://pbpython.com/) blog that teaches how to create web applications from jupyter notebooks and then deploy them.

[Visit the live dashboard](https://mybinder.org/v2/gh/duarteocarmo/interactive-dashboard-post/master?urlpath=%2Fvoila%2Frender%2Fnotebooks%2FDashboard.ipynb) (might take a bit to load because of binder)




## Screenshots

[![](posts/readme_figure.png)](https://mybinder.org/v2/gh/duarteocarmo/interactive-dashboard-post/master?urlpath=%2Fvoila%2Frender%2Fnotebooks%2FDashboard.ipynb)

[![](posts/readme_figure_1.png)](https://mybinder.org/v2/gh/duarteocarmo/interactive-dashboard-post/master?urlpath=%2Fvoila%2Frender%2Fnotebooks%2FDashboard.ipynb)


## How do I run the notebook? :notebook_with_decorative_cover:

Clone the repo:

```bash
$ git clone https://github.com/duarteocarmo/interactive-dashboard-post.git
```

Navigate to it:

```bash
$ cd interactive-dashboard-post
```

Create a [virtual environment](https://virtualenv.pypa.io/en/latest/):

```bash
$ virtualenv env
```

Activate the environment:

```bash
$ . env/bin/activate
```

Install the requirements:

```bash
(env) $ pip install -r requirements.txt
```

Launch [jupyter lab](https://jupyterlab.readthedocs.io/en/stable/):

```bash
(env) $ jupyter lab
```

It should launch automatically. If not, [check this](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html).

🚨 **troubleshooting** 🚨

If the plotly express plots are not showing then try:

```bash
(env) $ jupyter labextension install @jupyterlab/plotly-extension
```

If you still have problems, follow [these instructions](https://plot.ly/python/getting-started/#jupyterlab-support-python-35).



## How do I run the dashboard? :bar_chart:

Follow the instructions above until you have the requirements installed, and then:

```bash
(env) $ voila notebooks/Dashboard.ipynb
```

This should launch the dashboard in http://localhost:8866/
