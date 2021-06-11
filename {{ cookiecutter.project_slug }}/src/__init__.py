from pathlib import Path

# Make some of the basic directories globally available in your environment
base_dir = Path(__file__).resolve().parents[1]
data_dir = base_dir / 'data'
log_dir  = base_dir / 'logs'
plot_dir = base_dir / 'reports/figures'
jupyter_startup_script = base_dir / 'notebooks/jupyter_startup.ipy'
