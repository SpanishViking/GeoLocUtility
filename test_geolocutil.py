import geolocutil


def test_mixed_single_inputs(capsys):
    geolocutil.main(["geolocutil.py", "--locations", "Maryville, TN", "78550"])
    out, err = capsys.readouterr()
    assert "Maryville" in out
    assert  "78550" in out
    assert err == ""


def test_mixed_multiple_inputs(capsys):
    geolocutil.main(["geolocutil.py", "Maryville, TN", "78550", "Madison, WI", "12345", "Chicago, IL", "10001"])
    out, err = capsys.readouterr()
    assert "Maryville" in out
    assert  "78550" in out
    assert "Madison" in out
    assert  "12345" in out
    assert "Chicago" in out
    assert  "10001" in out
    assert err == ""


def test_single_location_name_input(capsys):
    geolocutil.main(["geolocutil.py", "Maryville, TN"])
    out, err = capsys.readouterr()
    assert "Maryville" in out
    assert err == ""


def test_single_zip_code_input(capsys):
    geolocutil.main(["geolocutil.py", "--locations", "12345"])
    out, err = capsys.readouterr()
    assert  "12345" in out
    assert err == ""


def test_multiple_location_name_inputs(capsys):
    geolocutil.main(["geolocutil.py", "Maryville, TN", "Knoxville, TN", "Madison, WI", "Dallas, TX", "Chicago, IL"])
    out, err = capsys.readouterr()
    assert "Maryville" in out
    assert  "Knoxville" in out
    assert "Madison" in out
    assert  "Dallas" in out
    assert "Chicago" in out
    assert err == ""


def test_multiple_zip_code_inputs(capsys):
    geolocutil.main(["geolocutil.py", "78550", "37901", "12345", "75001", "10001"])
    out, err = capsys.readouterr()
    assert  "78550" in out
    assert "37901" in out
    assert  "12345" in out
    assert "75001" in out
    assert  "10001" in out
    assert err == ""