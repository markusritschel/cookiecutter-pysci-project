---
icon: material/flask
---

# Research Project

Enable `is_research_project` during setup to get a data science project structure for:

- Data analysis, processing, visualization
- Machine learning model development
- Scientific computing or simulations
- Experimental workflows

## Directory Structure

```yaml
project/
├── data/
│   ├── raw/           # Original, immutable data
│   ├── interim/       # Intermediate processing stages
│   └── processed/     # Final, analysis-ready data
├── notebooks/
│   ├── exploratory/   # Experimental analysis
│   └── reports/       # Polished notebooks for sharing
├── references/        # Papers, documentation, links
├── reports/
│   ├── figures/       # Generated plots/visualizations
│   └── README.md
├── scripts/           # Analysis and processing scripts
├── src/mypackage/     # Reusable package code
├── tests/             # Test suite
└── docs/              # Documentation
```

### High-level & low-level Code

All **high-level** code (that is, code the user directly interacts with) should reside in the `scripts/` and the `notebooks/` directory.
High-level code is, for example, code that produces a figure, a report, or similar.


!!! TIP "Best practice"
    Name scripts and notebooks in a way that indicates their order of execution (examples can be found in the respective directories).
    In addition, document the proceedure of execution and what each script does.
    Have *one* script for each task, i.e. the creation of *one* figure or *one* table. <br />

Code residing in `src/` is *exclusively* source code or **low-level** code and **is not meant to be actively run** but rather used in your scripts and notebooks.



## Path variables

The package's `__init__.py` pre-defines a set of path variables that are available as soon as you import the package:

| Variable   | Points to              | Available when          |
| ---------- | ---------------------- | ----------------------- |
| `BASE_DIR` | project root directory | always                  |
| `DATA_DIR` | `data/`                | `is_research_project`   |
| `PLOT_DIR` | `reports/figures/`     | `is_research_project`   |

Use them in notebooks and scripts without hard-coding paths:

```python
from mypackage import DATA_DIR, PLOT_DIR

df = pd.read_csv(DATA_DIR / "raw" / "input.csv")
fig.savefig(PLOT_DIR / "result.png")
```

## Data Management

**`data/raw/`** - Original data (never modify)
```bash
# Document source and date
# Downloaded from: https://...
# Date: 2024-02-25
```

**`data/interim/`** - Intermediate processing results
- Use for expensive computations
- Can be regenerated from raw data

**`data/processed/`** - Final analysis-ready data
- Use directly in notebooks/analysis
- For large files (>100MB), use [DVC](https://dvc.org/)

**`.gitignore` data files:**
```
data/raw/**/*.csv
data/interim/**/*.pkl
```

## Notebooks

- `notebooks/exploratory/` - Quick experimentation
- `notebooks/reports/` - Publication-ready notebooks

Typical notebook structure:

```python
# 1. IMPORTS
import pandas as pd
from mypackage.analysis import process

# 2. CONFIGURATION
DATA_PATH = "../data/raw/input.csv"
SEED = 42

# 3. LOAD DATA
df = pd.read_csv(DATA_PATH)

# 4. ANALYSIS
results = process(df)

# 5. SAVE
results.to_csv("../reports/output.csv")
```

## Scripts

Reusable analysis and processing scripts in `scripts/`:

```python
# scripts/01-clean-data.py
import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")
df = df.dropna()
df.to_csv("data/processed/cleaned.csv")
```

Run with:
```bash
uv run python scripts/01-clean-data.py
```

## Typical Workflow

1. **Collect data** → `data/raw/`
2. **Explore** → `notebooks/exploratory/01-data-overview.ipynb`
3. **Process** → `scripts/01-clean-data.py`
4. **Analyze** → `notebooks/exploratory/02-analysis.ipynb`
5. **Visualize** → `notebooks/reports/01-results.ipynb`
6. **Package code** → Move reusable functions to `src/mypackage/`

## Package Reusable Code

Move proven analysis functions to your package:

```python
# src/mypackage/analysis.py
def statistical_test(data):
    """Reusable analysis function."""
    # Implementation
    return results

# notebooks/reports/01-results.ipynb
from mypackage.analysis import statistical_test
results = statistical_test(df)
```

## Managing Large Data

**Small datasets (<100MB)** - Version control in Git:
```bash
git add data/processed/
git commit -m "Add processed dataset"
```

**Large datasets** - Use [DVC](https://dvc.org/):
```bash
uv add --group dev dvc
dvc add data/raw/large-dataset.csv
git add data/raw/large-dataset.csv.dvc
```

## Data Validation

Validate results make sense:

```python
assert len(results) > 0, "No results"
assert results['value'].isna().sum() == 0, "NaN values"
assert (results['value'] > 0).all(), "Unexpected negatives"
```

## References

Document data sources in `references/`:

```markdown
# data-sources.md

## Main Dataset
- **Source**: https://example.com/dataset
- **License**: CC-BY-4.0
- **Last accessed**: 2024-02-25
```

## See Also

- [Development](./development.md) - Full development workflow
- [Code Quality](./code-quality.md) - Testing and validation

## Further Reading

- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
- [Jupyter Best Practices](https://docs.jupyter.org/en/latest/)
- [Pandas Docs](https://pandas.pydata.org/)
- [DVC - Data Version Control](https://dvc.org/)
