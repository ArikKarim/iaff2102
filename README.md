# Data Analysis with Python

Five freeCodeCamp projects expanded from their official starter repositories. Each folder keeps the starter entrypoint, tests, datasets, and example figures.

| Project folder | Implementation |
| --- | --- |
| [mean-variance-standard-deviation-calculator](mean-variance-standard-deviation-calculator) | NumPy statistics along columns, rows, and the entire 3 by 3 matrix; rejects inputs with a length other than nine. |
| [demographic-data-analyzer](demographic-data-analyzer) | Pandas calculations for race, age, education, income, working hours, country, and occupation; decimals rounded to one place. |
| [medical-data-visualizer](medical-data-visualizer) | BMI and health-marker normalization, cardiovascular categorical plots, and a cleaned correlation heatmap. |
| [page-view-time-series-visualizer](page-view-time-series-visualizer) | Percentile filtering, daily line plot, monthly averages by year, and annual/monthly box plots. |
| [sea-level-predictor](sea-level-predictor) | Historical scatter plot and two SciPy regression lines projected through 2050. |

## Setup

Use Python 3.11 and install the shared dependencies from the repository root:

```sh
python -m venv .venv
```

Activate the environment (PowerShell on Windows):

```powershell
.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```sh
source .venv/bin/activate
```

Then install and run all five official test suites:

```sh
python -m pip install -r requirements.txt
python run_tests.py
```

The runner uses a noninteractive Matplotlib backend and runs each suite from its own project directory. A failing suite makes the runner exit with a nonzero status. GitHub Actions runs the same command on pushes and pull requests.

## Run one project

Each folder is also self-contained. For example:

```sh
cd medical-data-visualizer
python -m pip install -r requirements.txt
python main.py
```

The original `main.py` entrypoints run the implementation and its tests. For tests with a reliable process exit status, use `python -m unittest test_module -v`.

The visualizers save these images in the current working directory:

- Medical: `catplot.png` and `heatmap.png`.
- Page views: `line_plot.png`, `bar_plot.png`, and `box_plot.png`.
- Sea level: `sea_level_plot.png`.

Generated charts and Python caches are ignored by Git. CSV input paths resolve relative to each implementation file, so importing from another working directory also works.

## Starter provenance

The datasets and `test_module.py` files are unchanged from these freeCodeCamp starters. Dependency versions are aligned so all five projects can share one environment; the implementations fill the starter placeholders.

| Official starter | Source commit |
| --- | --- |
| [Mean / variance / standard deviation](https://github.com/freeCodeCamp/boilerplate-mean-variance-standard-deviation-calculator) | `126bb94a8f8f4535ddcfe5452e188a4625062059` |
| [Demographic data analyzer](https://github.com/freeCodeCamp/boilerplate-demographic-data-analyzer) | `1fed7bb013559779ec8e23a0809644b1581df072` |
| [Medical data visualizer](https://github.com/freeCodeCamp/boilerplate-medical-data-visualizer) | `ffb0c5aabe599b4d6deb843e02cf18a8cd64c7a5` |
| [Page view time series visualizer](https://github.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer) | `10d2fe8058be34cdf47d730d03e5ee1500bf23cf` |
| [Sea level predictor](https://github.com/freeCodeCamp/boilerplate-sea-level-predictor) | `bcea802f0fd075d4bd7005f7892a3416f22cacc6` |

Project instructions are linked from each starter README. Submission to freeCodeCamp is a separate step: use each project's GitHub folder URL after merging the changes.
