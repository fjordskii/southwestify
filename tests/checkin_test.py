import json
import pytest
import requests
import southwest
import checkin
from datetime import datetime, timedelta
from .my_vcr import custom_vcr
from pytz import timezone
from unittest.mock import Mock, patch

my_vcr = custom_vcr()
r = southwest.Reservation('XXXXXX', 'John', 'Smith')


@my_vcr.use_cassette()
def test_generate_headers():
    headers = southwest.Reservation.generate_headers()
    assert(headers['Content-Type'] == 'application/json')
    assert(headers['X-API-Key'] == 'l7xx0a43088fe6254712b10787646d1b298e')


@my_vcr.use_cassette()
def test_reservation_lookup():
    try:
        r.lookup_existing_reservation()
    except Exception:
        pytest.fail("Error looking up reservation")


@patch('southwest.Reservation.checkin')
@my_vcr.use_cassette()
def test_checkin(mock_get):
    mock_get.return_value.ok = True
    try:
        body = r.checkin()
        assert body
    except Exception:
        pytest.fail("Error checking in")


@my_vcr.use_cassette()
def test_openflights_api():
    assert southwest.timezone_for_airport('LAX').zone == "America/Los_Angeles"


@patch('checkin.auto_checkin')
@my_vcr.use_cassette()
def test_cli(mock_checkin):
    try:
        mock_checkin('XXXXXX', 'John', 'Smith', 'bobsaget@gmail.com')
        mock_checkin.assert_called()
        mock_checkin.assert_called_with('XXXXXX', 'John', 'Smith', 'bobsaget@gmail.com')
    except Exception:
        pytest.fail("cli error")
