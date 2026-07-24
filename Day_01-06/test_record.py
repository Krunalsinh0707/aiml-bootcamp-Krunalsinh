from parse import load_records


def test_empty_file():
    result = load_records("empty.csv")
    assert result["records"] == []


def test_missing_marks():
    result = load_records("missing_marks.csv")
    assert result["records"][0]["exam2"] is None


def test_bad_email():
    result = load_records("bad_email.csv")
    assert len(result["malformed_emails"]) == 1
