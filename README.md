# quantitative-economics-with-python
An open-source research platform for modeling stochastic dynamics in Python, with Markov chains, survival dynamics, Kalman filtering, Bayesian learning, and linear programming applied to economic models. These are the same state-transition methods used for customer retention and churn forecasting.

**Highlights**

- [Finite Markov chains](006_intro_to_dynamics/40_finite_markov_chains.ipynb): state transitions, stationary distributions, and long-run behavior.
- [Survival and long-run dynamics](004_stats_and_info/35_survival_long_run_dynamics_under_recursive_prefs.ipynb): which agents survive over time and why.
- Kalman filtering: [a first look](006_intro_to_dynamics/47_fist_look_kalman_filter.ipynb), [another look](006_intro_to_dynamics/48_another_look_kalman_filter.ipynb), and [with vector autoregressions](006_intro_to_dynamics/49_kalman_filter_vector_autoregress.ipynb).

**Repository structure**

- [001_tools_and_techniques](001_tools_and_techniques): numerical methods, linear algebra,
	QR and SVD, DMD, Newton methods, and applied modeling (e.g., COVID-19 dynamics).
- [002_elementary_statistics](002_elementary_statistics): probability, the law of large numbers,
	the central limit theorem, multivariate distributions, and randomized response surveys.
- [003_bayes_law](003_bayes_law): non-conjugate priors, posterior distributions for AR(1)
	parameters, and forecasting AR(1) processes.
- [004_stats_and_info](004_stats_and_info): likelihood ratio processes, Bayesian learning,
	comparing experiments, and survival dynamics.
- [005_linear_programming](005_linear_programming): optimal transport and the von Neumann growth model.
- [006_intro_to_dynamics](006_intro_to_dynamics): Markov chains, inventory dynamics, linear
	state space models, Kalman filters, and vector autoregressions.
- [qecon_platform](qecon_platform) and [examples](examples): reusable simulation helpers and an
	interactive demo (see below).

**Quick start**

Prerequisites: Python 3.8+ (3.10 recommended), `pip`, and `virtualenv` or
`venv`.

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start Jupyter Lab or Notebook and open the notebooks:

```bash
jupyter lab
# or
jupyter notebook
```

**Interactive research platform**

- Package: `qecon_platform` — contains simulation helpers in `qecon_platform/simulation.py`.
- Example notebook: `examples/interactive_demo.ipynb` demonstrates the Ornstein–Uhlenbeck
	simulator and a tiny agent-based microeconomic model. It uses `ipywidgets` for
	parameter sliders.

To run the demo after installing dependencies:

```bash
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Open `examples/interactive_demo.ipynb` and run the cells.

**Development notes**

- Dependencies are listed in [requirements.txt](requirements.txt). If you add
	packages, please update that file.
- The notebooks are intended for learning and demonstration; results may depend
	on package versions and the Python interpreter.

**Contributing**

Feel free to open issues or pull requests with improvements, corrections, or
additional notebooks. For reproducibility, include the `requirements.txt`
entry for any new dependencies.

**License & contact**

No license is specified in this repository. If you would like to add one,
include a `LICENSE` file. For questions or collaboration, open an issue.
