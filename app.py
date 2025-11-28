from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alisson Ponce Chevere</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #6a0572, #120078);
            color: #fff;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            font-size: 3rem;
            text-shadow: 0 0 20px rgba(255,255,255,0.2);
            margin-bottom: 0.5rem;
        }
        p {
            font-size: 1.2rem;
            opacity: 0.8;
        }
        a {
            margin-top: 1.5rem;
            display: inline-block;
            background: #ff6f91;
            color: #fff;
            padding: 0.8rem 1.6rem;
            border-radius: 30px;
            text-decoration: none;
            transition: 0.3s ease;
            font-weight: bold;
        }
        a:hover {
            background: #ff8fab;
            transform: translateY(-3px);
            box-shadow: 0 8px 15px rgba(255, 143, 171, 0.3);
        }
        footer {
            position: absolute;
            bottom: 15px;
            font-size: 0.9rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <h1>Bienvenida 🚀</h1>
    <p>Aplicación Flask creada por <strong>Alisson Ponce</strong></p>
    <a href="/saludo/alisson.ponce">Ver saludo personalizado</a>
    <footer>Powered by Flask & Traefik · 2025</footer>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_TEMPLATE

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"""
    <html>
        <head>
            <meta charset='UTF-8'>
            <title>Saludo de Alisson Ponce</title>
            <style>
                body {{
                    background: radial-gradient(circle at top left, #120078, #6a0572);
                    color: #fff;
                    font-family: 'Segoe UI', sans-serif;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                h2 {{
                    font-size: 2.5rem;
                    margin-bottom: 1rem;
                }}
                p {{
                    font-size: 1.2rem;
                    opacity: 0.9;
                    margin-bottom: 1.5rem;
                }}
                a {{
                    color: #ff8fab;
                    text-decoration: none;
                    font-weight: bold;
                    transition: 0.3s ease;
                }}
                a:hover {{
                    text-shadow: 0 0 10px #ff8fab;
                }}
            </style>
        </head>
        <body>
            <h2>Hola {nombre}, <strong>Alisson Ponce</strong> 🌟</h2>
            <p>Bienvenida a tu app Flask con estilo 😎🚀</p>
            <a href="/">Volver al inicio</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1003)
