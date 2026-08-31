"""Constants for the Bin Collections integration."""
from datetime import date

DOMAIN = "bin_collections"

# URL prefix the integration's bin images are served under (see __init__.py).
IMAGES_URL_PATH = f"/api/{DOMAIN}/images"

# Hard-coded collection schedule.
# Each entry's "first_collection" is any known past or future collection date
# for that bin (an anchor point) — the integration rolls forward from it in
# steps of "frequency_days" to find the next upcoming collection date.
# "image" is the filename of the bin's picture under the integration's
# images/ directory, served at IMAGES_URL_PATH and exposed as entity_picture.
BIN_TYPES = {
    "rubbish": {
        "name": "Rubbish",
        "icon": "mdi:trash-can",
        "color": "green",
        "frequency_days": 14,
        "first_collection": date(2026, 9, 2),
        "image": "rubbish.png",
    },
    "recycling": {
        "name": "Recycling",
        "icon": "mdi:recycle",
        "color": "blue",
        "frequency_days": 14,
        "first_collection": date(2026, 9, 9),
        "image": "recycling.png",
    },
    "garden": {
        "name": "Garden Waste",
        "icon": "mdi:leaf",
        "color": "brown",
        "frequency_days": 14,
        "first_collection": date(2026, 9, 9),
        "image": "garden.png",
    },
    "food": {
        "name": "Food Waste",
        "icon": "mdi:food-apple",
        "color": "dark green",
        "frequency_days": 7,
        "first_collection": date(2026, 9, 9),
        "image": "food.png",
    },
}
