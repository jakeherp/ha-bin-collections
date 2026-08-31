"""Config flow for the Bin Collections integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class BinCollectionsConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Bin Collections.

    The collection schedule is hard-coded, so setup only needs a single
    confirmation step and one instance is allowed.
    """

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the single setup step."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        if user_input is not None:
            return self.async_create_entry(title="Bin Collections", data={})

        return self.async_show_form(step_id="user", data_schema=vol.Schema({}))
