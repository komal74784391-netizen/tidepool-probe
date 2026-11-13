# tidepool-probe data schema

Each capture is written as a CSV table with one header row.

| column | type | description |
| --- | --- | --- |
| sample_id | string | stable sample identifier |
| channel | string | measurement channel name |
| value_si | float | calibrated value in SI units |
| quality | float | 0..1 acquisition confidence |
