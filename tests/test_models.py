import pytest

from models import DialogModel


def test_dialog_model_summary():
    dialog = DialogModel(question="What is the capital of Israel?", answer="Jerusalem")
    summary = dialog.summary()
    assert summary == "Q: What is the capital of Israel? - A: Jerusalem"
