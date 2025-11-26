from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")

    # Código 200 OK
    assert res.status_code == 200

    # El HTML incluye "Bienvenido 🚀"
    assert b"Bienvenido" in res.data
    assert b"Jorge Escobar" in res.data

def test_saludo():
    client = app.test_client()
    nombre = "jorge.escobar"
    res = client.get(f"/saludo/{nombre}")

    # Código 200 OK
    assert res.status_code == 200

    # Validar contenido dinámico
    assert b"Hola jorge.escobar" in res.data
    assert b"Messi" in res.data  # Está en tu HTML
    assert b"Volver al inicio" in res.data
