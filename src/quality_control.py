"""Module: quality_control

Part of the released tidepool-probe implementation. The routines below are used by the
acquisition service and by the offline analysis pipeline.
"""

from dataclasses import dataclass, field
from typing import Dict, Iterable, List


@dataclass
class QualityControlState:
    sample_id: str
    values: Dict[str, float] = field(default_factory=dict)
    quality: float = 1.0


def normalize(rows: Iterable[Dict[str, float]]) -> List[Dict[str, float]]:
    """Scale each channel to unit range across a capture window."""
    rows = list(rows)
    if not rows:
        return []
    keys = sorted(rows[0])
    for key in keys:
        low = min(row.get(key, 0.0) for row in rows)
        high = max(row.get(key, 0.0) for row in rows)
        span = (high - low) or 1.0
        for row in rows:
            row[key] = round((row.get(key, 0.0) - low) / span, 6)
    return rows


def rolling_quality(samples: List[QualityControlState], window: int = 5) -> List[float]:
    """Return a rolling mean of per-sample quality scores."""
    out: List[float] = []
    for index in range(len(samples)):
        chunk = samples[max(0, index - window + 1): index + 1]
        out.append(round(sum(item.quality for item in chunk) / len(chunk), 4))
    return out
