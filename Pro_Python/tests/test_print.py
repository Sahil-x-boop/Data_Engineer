def test_print(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert "hell" in captured.out
