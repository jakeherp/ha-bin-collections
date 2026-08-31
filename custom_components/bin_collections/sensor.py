"""Sensor platform for the Bin Collections integration."""
from __future__ import annotations

from datetime import date, datetime, timedelta

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_time
from homeassistant.util import dt as dt_util

from .const import BIN_TYPES, DOMAIN


def calculate_next_collection(anchor: date, frequency_days: int, today: date) -> date:
    """Roll an anchor collection date forward to the next occurrence on or after today."""
    if anchor >= today:
        return anchor
    days_since = (today - anchor).days
    cycles_needed = -(-days_since // frequency_days)  # ceil division
    return anchor + timedelta(days=cycles_needed * frequency_days)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Bin Collections sensors from a config entry."""
    async_add_entities(
        BinCollectionSensor(entry, bin_key, bin_info)
        for bin_key, bin_info in BIN_TYPES.items()
    )


class BinCollectionSensor(SensorEntity):
    """Sensor showing the next collection date for a single bin."""

    _attr_device_class = SensorDeviceClass.DATE
    _attr_has_entity_name = True
    _attr_should_poll = False

    def __init__(self, entry: ConfigEntry, bin_key: str, bin_info: dict) -> None:
        """Initialize the sensor."""
        self._bin_key = bin_key
        self._bin_info = bin_info
        self._attr_name = bin_info["name"]
        self._attr_icon = bin_info["icon"]
        self._attr_unique_id = f"{entry.entry_id}_{bin_key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="Bin Collections",
            entry_type=DeviceEntryType.SERVICE,
        )
        self._unsub_midnight_update = None

    @property
    def native_value(self) -> date:
        """Return the next collection date for this bin."""
        return calculate_next_collection(
            self._bin_info["first_collection"],
            self._bin_info["frequency_days"],
            dt_util.now().date(),
        )

    @property
    def extra_state_attributes(self) -> dict:
        """Return additional attributes about this bin's schedule."""
        days_until = (self.native_value - dt_util.now().date()).days
        return {
            "bin_color": self._bin_info["color"],
            "frequency_days": self._bin_info["frequency_days"],
            "days_until_collection": days_until,
        }

    async def async_added_to_hass(self) -> None:
        """Schedule a daily refresh at midnight once added to hass."""
        self._schedule_midnight_update()

    async def async_will_remove_from_hass(self) -> None:
        """Cancel the scheduled midnight refresh."""
        if self._unsub_midnight_update is not None:
            self._unsub_midnight_update()
            self._unsub_midnight_update = None

    def _schedule_midnight_update(self) -> None:
        """Schedule the state to refresh just after the next local midnight."""
        now = dt_util.now()
        next_midnight = dt_util.start_of_local_day(now + timedelta(days=1))

        def _handle_midnight(_now: datetime) -> None:
            self.async_write_ha_state()
            self._schedule_midnight_update()

        self._unsub_midnight_update = async_track_point_in_time(
            self.hass, _handle_midnight, next_midnight
        )
