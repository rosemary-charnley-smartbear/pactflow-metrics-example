# pactflow-metrics-example

A metrics dashboard for visualizing PactFlow contract testing data, branded for Swagger Contract Testing.

## Running locally

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

### Start the dashboard

```bash
docker compose up --build
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

The `--build` flag is only needed the first time, or after changing files in `dashboard/`. For subsequent starts you can use:

```bash
docker compose up
```

### Stop the dashboard

```bash
docker compose down
```

## Dashboard views

**Latest** — snapshot of the current state of your PactFlow instance, including pacticipants, integrations, pact publications, verification results, deployed versions, users, webhooks, tags, and provider contracts.

**History** — time-series line charts showing how each metric has changed across all recorded snapshots.

## Data

The dashboard reads from two JSON files in the `data/` directory:

| File | Description |
|------|-------------|
| `data/pactflow_metrics_latest.json` | Most recent metrics snapshot |
| `data/pactflow_metrics_history.json` | All historical snapshots (array, sorted by timestamp) |

These files are mounted read-only into the container, so the dashboard always reflects the latest data without requiring a rebuild.
