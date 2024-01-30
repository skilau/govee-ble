"""Event constants for govee-ble."""
from __future__ import annotations

from sensor_state_data.enum import StrEnum


class EventDeviceKeys(StrEnum):
    """Keys for devices that send events."""

    # Button
    BUTTON = "button"

    # Dimmer
    DIMMER = "dimmer"

    # Motion
    MOTION = "motion"

    # Rocker switch
    SWITCH = "switch"


class EventTypeKeys(StrEnum):
    """Keys for event types."""

    # Single Press
    PRESS = "press"

    # Double Press
    DOUBLE_PRESS = "double_press"

    # Short Press
    SHORT_PRESS = "short_press"

    # Long Press
    LONG_PRESS = "long_press"
