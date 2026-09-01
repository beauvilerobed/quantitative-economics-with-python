# quantitative-economics-with-python

A collection of Jupyter notebooks and supporting materials for learning quantitative
economics and applied statistics using Python. The notebooks cover elementary
probability and statistics concepts, numerical methods, and practical tools and
techniques used in quantitative research.

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
