from pathlib import Path
from dotenv import find_dotenv, load_dotenv

# Make some of the basic directories globally available in your environment
base_dir = Path(__file__).resolve().parents[1]
data_dir = base_dir / 'data'
log_dir  = base_dir / 'logs'
plot_dir = base_dir / 'reports/figures'
jupyter_startup_script = base_dir / 'notebooks/jupyter_startup.ipy'

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()
# load up the entries as environment variables
load_dotenv(dotenv_path)