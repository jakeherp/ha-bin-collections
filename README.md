# Bin Collections for Home Assistant

A minimal, hard-coded Home Assistant integration for tracking personal bin
(rubbish) collection days. No scraping, no API, no council website — just a
known collection date and a repeat frequency per bin, rolled forward to give
you the next collection date at all times.

## Bins

| Bin | Frequency | Next collection (anchor date) |
| --- | --- | --- |
| Rubbish (green lid) | Every 14 days | Wednesday, 2 September 2026 |
| Recycling (blue lid) | Every 14 days | Wednesday, 9 September 2026 |
| Garden waste (brown lid) | Every 14 days | Wednesday, 9 September 2026 |
| Food waste | Every 7 days | Wednesday, 9 September 2026 |

Each bin's next collection date is calculated by rolling forward from its
anchor date in steps of its frequency, so the sensors stay correct
indefinitely without any maintenance.

## Installation

### HACS (custom repository)

1. In HACS, go to **Integrations** → the **⋮** menu → **Custom repositories**.
2. Add this repository's URL with category **Integration**.
3. Install **Bin Collections**, then restart Home Assistant.

### Manual

1. Copy `custom_components/bin_collections` into your Home Assistant
   `config/custom_components/` directory.
2. Restart Home Assistant.

## Setup

Go to **Settings → Devices & Services → Add Integration**, search for
**Bin Collections**, and confirm. Only one instance is needed.

This creates four sensors, one per bin:

- `sensor.rubbish`
- `sensor.recycling`
- `sensor.garden_waste`
- `sensor.food_waste`

Each sensor's state is the next collection date, with `bin_color`,
`frequency_days`, and `days_until_collection` attributes.

## Bin pictures

Each sensor also exposes an `entity_picture` — a photo of the actual bin —
served directly by the integration, so cards like **Entities**, **Glance**,
and **Picture Entity** show the real bin instead of a generic mdi icon.
See `custom_components/bin_collections/images/README.md` for the filenames
to drop in.

## Customizing the schedule

Since the schedule is hard-coded (there is no council API), edit the
`BIN_TYPES` dictionary in
`custom_components/bin_collections/const.py` to match your own bins,
colors, frequencies, and a known collection date for each.
