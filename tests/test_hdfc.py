"""Tests for HDFC statement balance extraction.

All statement text here is invented.
"""

from bank_statement_parser.parsers.hdfc import _CLOSING_BAL_RE, _OPENING_BAL_RE


def test_opening_balance_accepts_minus_sign():
    m = _OPENING_BAL_RE.search("Opening Balance : -1,234.56")
    assert m is not None
    assert m.group(1) == "-1,234.56"


def test_opening_balance_positive_still_read():
    m = _OPENING_BAL_RE.search("Opening Balance : 1,234.56")
    assert m is not None
    assert m.group(1) == "1,234.56"


def test_closing_balance_summary_accepts_minus_signs():
    text = (
        "Opening Balance Debit Amount Credit Amount Closing Balance\n"
        "-100.00 500.00 300.00 -300.00"
    )
    m = _CLOSING_BAL_RE.search(text)
    assert m is not None
    assert m.group(1) == "-100.00"
    assert m.group(4) == "-300.00"


def test_closing_balance_summary_positive_still_read():
    text = (
        "Opening Balance Debit Amount Credit Amount Closing Balance\n"
        "1,000.00 500.00 300.00 800.00"
    )
    m = _CLOSING_BAL_RE.search(text)
    assert m is not None
    assert m.group(4) == "800.00"
