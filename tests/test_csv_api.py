from fastapi.testclient import TestClient

from csv_api_sender.app import app


def test_upload_csv_returns_summary():
    client = TestClient(app)

    csv_content = b"nome,idade\nAna,30\nJoao,25\n"

    response = client.post(
        "/upload-csv",
        files={"file": ("alunos.csv", csv_content, "text/csv")},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["filename"] == "alunos.csv"
    assert payload["rows_count"] == 2
    assert payload["columns"] == ["nome", "idade"]
