from unittest.mock import MagicMock, patch
from hydroponics import hydroponics_schedule_run


def test_hydroponics_schedule_run():
    mock_lamp = MagicMock()

    mock_lamp.on.side_effect = lambda: print("Running")
    mock_lamp.off.side_effect = lambda: print("Shutting")

    hydroponics_schedule_run(mock_lamp, max_duration=1200)


test_hydroponics_schedule_run()
