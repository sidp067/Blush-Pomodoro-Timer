import project

def test_format_time():
    assert project.format_time(60) == "01:00"
    assert project.format_time(125) == "02:05"
    assert project.format_time(3600) == "60:00"
