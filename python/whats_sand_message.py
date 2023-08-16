import requests

# Substitua os valores abaixo pelos seus próprios
instance_id = 123456
client_id = "your-client-id"
client_secret = "your-client-secret"
access_token = "your-access-token"
to_number = "5511987654321"
message = "Hello, World!"

url = f

# Envie a mensagem
response = requests.post(
    url,
    json={
        "number": to_number,
        "message": message,
    },
    headers={
        "Content-Type": "application/json",
        "X-WM-CLIENT-ID": client_id,
        "X-WM-CLIENT-SECRET": client_secret,
    },
)

# Verifique se a mensagem foi enviada com sucesso
if response.status_code == 200:
    print("Mensagem enviada com sucesso!")
else:
    print("Falha ao enviar mensagem")
