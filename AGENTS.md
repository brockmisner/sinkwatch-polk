# AGENTS.md

## Mission

Build SinkWatch Polk: a human-in-the-loop geospatial ML system for detecting
localized subsidence candidates that may indicate sinkhole-related risk in Polk
County / Lakeland, Florida.

The system must never label an unverified location as a "confirmed sinkhole."
Use the terms:
- confirmed_karst_sinkhole
- probable_karst_subsidence
- possible_sinkhole_precursor
- non_karst_subsidence
- false_sar_anomaly
- unknown_needs_review

## Safety and language

- Never generate public-facing claims that a parcel, home, or road "has a sinkhole"
  unless a qualified professional has verified it.
- Dashboard language must say "candidate," "watch," "inspection priority," or
  "field verification required."
- Every prediction must include confidence, evidence, source data timestamps,
  and reason codes.
- All emergency guidance must say field hazards require local emergency/road
  authority response.

## Engineering standards

- Use Python 3.12.
- Use FastAPI for backend services.
- Use PostGIS for vector/geospatial storage.
- Use Parquet/Cloud-Optimized GeoTIFF/Zarr/HDF5-friendly utilities for raster and time series.
- Use pytest for unit tests.
- Use synthetic rasters/vectors in tests; do not require huge real datasets for CI.
- Every geospatial function must state its CRS assumptions.
- Distance/area calculations must be done in a projected CRS, not raw EPSG:4326.
- Add tests before or with new feature code.
- Run:
  - make lint
  - make test
  - make typecheck

## Modeling rules

- FDEP subsidence incidents are weak labels, not clean truth labels.
- Do not train a final model using weak positives only.
- Split model validation by geography and time, not random pixels.
- Report precision@K, recall of known events, false-alarm type, and lead time.
- Store all model runs, features, labels, and predictions with version hashes.

## Review guidelines

- Flag P0/P1 issues for unsafe public claims, broken CRS handling, leaking PII,
  missing data provenance, or predictions without confidence/explanation.
