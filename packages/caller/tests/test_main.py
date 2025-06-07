from caller import main


def test_main(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert len(captured.out) > 0
