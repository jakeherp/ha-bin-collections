"""The Bin Collections integration."""
from __future__ import annotations

from pathlib import Path

from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import IMAGES_URL_PATH

PLATFORMS = ["sensor"]

IMAGES_DIR = Path(__file__).parent / "images"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Serve the integration's bundled bin images over HTTP."""
    await hass.http.async_register_static_paths(
        [StaticPathConfig(IMAGES_URL_PATH, str(IMAGES_DIR), True)]
    )
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Bin Collections from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
