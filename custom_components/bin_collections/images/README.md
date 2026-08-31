# Bin images

Drop the bin picture for each type into this folder using these exact
filenames (referenced by `image` in `const.py`):

| File | Bin |
| --- | --- |
| `rubbish.png` | Green-lidded rubbish bin |
| `recycling.png` | Blue-lidded recycling bin |
| `garden.png` | Brown-lidded garden waste bin |
| `food.png` | Food waste caddy |

They're served by the integration at `/api/bin_collections/images/<file>`
and exposed as each sensor's `entity_picture`, so cards like **Entities**,
**Glance**, and **Picture Entity** will render them automatically instead
of the fallback mdi icon.

PNG or JPG both work; a transparent-background PNG around 250–500px tall
looks best. No naming beyond the table above is required — any image
format Home Assistant's static file server can serve back works, just
update `image` in `const.py` if you use a different extension.
