# quantitative-economics-with-python
Built an open-source interactive research platform executing computational microeconomics and macroeconomic stochastic data modeling. 

**Repository structure**

- [elementary_statistics](elementary_statistics): Notebooks on probability, the
	law of large numbers, central limit theorem, multivariate distributions, and
	introductory topics in applied statistics.
- [tools_and_techniques](tools_and_techniques): Notebooks demonstrating
	numerical methods, linear algebra techniques, SVD, DMD, Newton methods, and
	applied modeling examples (e.g., simple COVID-19 modeling).

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

Open notebooks from the [elementary_statistics](elementary_statistics) and
[tools_and_techniques](tools_and_techniques) folders.

**Interactive research platform**

This repository now includes a minimal interactive research package: `qecon_platform`.

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
