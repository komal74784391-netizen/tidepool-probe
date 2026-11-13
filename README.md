# tidepool-probe

Reference implementation of the Tidepool Probe intertidal sonde

## What is in this repository

- `src/` - acquisition, scheduling and calibration services
- `data/` - sample measurement tables and the data schema
- `experiments/` - field notes and analysis code used for the released results

## Quick start

Install the runtime dependencies and start a capture session:

```bash
pip install -r requirements.txt
python src/acquire.py --config configs/default.json
```

Calibration coefficients are rebuilt with `python src/calibrate.py`. The data
schema is documented in `data/schema.md`. This release is tagged `v1.4.0`.
