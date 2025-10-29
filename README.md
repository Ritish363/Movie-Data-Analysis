# Movie Data Analysis


A reproducible, beginner-friendly repo for exploring movie metadata and doing simple analyses/visualizations.


## Contents
- `src/` — Python scripts for cleaning, exploring and visualizing data
- `data/` — place your dataset here (do not commit large datasets)
- `outputs/` — saved charts and summary CSVs


## Quickstart
1. Create a virtual environment and install requirements:
```bash
python -m venv venv
source venv/bin/activate # mac/linux
venv\Scripts\activate # windows
pip install -r requirements.txt
```
2. Place your movie CSV into `data/` (e.g. `data/movies_metadata.csv`).
3. Run data processing and exploratory analysis:
```bash
python src/data_processing.py --input data/movies_metadata.csv --output outputs/summary.csv
python src/exploratory_analysis.py --input outputs/summary.csv --outdir outputs/figures
```


## What to upload to GitHub
- `src/` code and `notebooks/` notebook(s)
- `README.md`, `requirements.txt`
- a small sample of `data/` (e.g. `movies_sample.csv`) or a download script (recommended)
- `outputs/` can be included for reproducibility but keep it small


## License
Choose a license (e.g. MIT). Put the text in `LICENSE`.
