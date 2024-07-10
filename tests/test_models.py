import pytest

from models import DialogModel

class TestDialogModel:
    def test_dialog_model_summary(self):
        dialog = DialogModel(question="What is the capital of Israel?", answer="Jerusalem")
        summary = dialog.summary()
        assert summary == "Q: What is the capital of Israel? - A: Jerusalem"
