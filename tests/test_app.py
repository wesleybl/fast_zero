from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem três etapas:
    - A Arrange - Arranjo
    - A Act     - Executa a coisa (o SUT)
    - A Assert  - Garanta que A é A
    """
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.json() == {'message': 'Olá mundo!'}  # Assert
    assert response.status_code == HTTPStatus.OK  # Assert


def test_html_deve_retornar_html():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/html')

    # Assert
    assert (
        response.text
        == """
    <html>
        <head>
            <title>Olá mundo!</title>
        </head>
        <body>
            <h1>Olá mundo!</h1>
        </body>
    </html>
    """
    )
