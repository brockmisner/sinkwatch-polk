# SinkWatch Polk

SinkWatch Polk is a **human-in-the-loop geospatial ML platform** for localized subsidence and sinkhole-precursor screening in Polk County, Florida.

## Safety-first product scope

- Output **candidates for review**, not public sinkhole determinations.
- Ground truth comes from qualified human reviewers and field inspections.
- Weak public records (e.g., incident reports) are tracked as weak labels.

## Monorepo layout

```text
sinkwatch-polk/
  AGENTS.md
  README.md
  docker-compose.yml
  pyproject.toml
  Makefile

  apps/
    api/
    web/
    worker/

  src/sinkwatch/
    ingest/
    features/
    candidates/
    labels/
    models/
    evals/
    geo/

  db/
    migrations/
    seed/

  tests/
    unit/
    integration/
    fixtures/
```

## Architecture (MVP)

1. Ingest OPERA/ASF InSAR displacement observations.
2. Ingest LiDAR terrain-derived depressions.
3. Ingest FDEP incidents as weak labels.
4. Ingest roads/assets exposure layers.
5. Generate localized subsidence candidates.
6. Human labeling and inspection workflow.
7. Baseline model training and inspection-priority queue.

## Local development

### Prerequisites

- Python 3.12
- Docker + Docker Compose

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,geo]"
```

### Run checks

```bash
make lint
make test
make typecheck
```

### Start local stack

```bash
make db-up
```

## Notes

- Use synthetic fixtures in CI tests (no large real datasets).
- CRS-aware geospatial processing is mandatory.
