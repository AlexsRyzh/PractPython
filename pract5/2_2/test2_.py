from main import binary_search


def test_binary_search(monkeypatch):
    inputs = [3]

    def my_input():
        return inputs.pop()

    monkeypatch.setattr('builtins.input', my_input)
    assert binary_search() == 2
