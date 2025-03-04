import project

def test_format_time():
    """Tests the format_time function."""
    assert project.format_time(0) == "00:00"
    assert project.format_time(60) == "01:00"
    assert project.format_time(125) == "02:05"
    assert project.format_time(3600) == "60:00"
    assert project.format_time(3661) == "61:01"

def test_start_timer():
    try:
        project.start_timer(0.1)  # Test with a very short time
    except Exception as e:
        assert False, f"start_timer raised an exception: {e}"

def test_start_pomodoro():
    try:
        project.start_pomodoro(work_minutes=0.1, break_minutes=0.1)  # Short times
    except Exception as e:
        assert False, f"start_pomodoro raised an exception: {e}"
