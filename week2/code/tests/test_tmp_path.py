# content of test_tmp_path.py
CONTENT = "This is wrote in python programming language"


def test_create_file(tmp_path):
    d = tmp_path / "my_python_folder"
    d.mkdir()
    p = d / "python.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    assert 1

