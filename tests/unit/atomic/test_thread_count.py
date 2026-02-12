import logging

from debriddo import main


def test_resolve_thread_count_env_auto(monkeypatch):
    monkeypatch.setenv("N_THREADS", "auto")
    monkeypatch.setattr(main, "calculate_optimal_thread_count", lambda: 7)

    assert main.resolve_thread_count() == 7


def test_resolve_thread_count_env_integer(monkeypatch):
    monkeypatch.setenv("N_THREADS", "4")

    assert main.resolve_thread_count() == 4


def test_resolve_thread_count_invalid_value(monkeypatch, caplog):
    monkeypatch.setenv("N_THREADS", "not-a-number")

    with caplog.at_level(logging.ERROR):
        assert main.resolve_thread_count() == 1

    assert "N_THREADS non valido" in caplog.text


def test_resolve_thread_count_auto_failure(monkeypatch, caplog):
    monkeypatch.delenv("N_THREADS", raising=False)

    def raise_error():
        raise RuntimeError("boom")

    monkeypatch.setattr(main, "calculate_optimal_thread_count", raise_error)

    with caplog.at_level(logging.ERROR):
        assert main.resolve_thread_count() == 1

    assert "Errore nel calcolo dei numero dei threads" in caplog.text
