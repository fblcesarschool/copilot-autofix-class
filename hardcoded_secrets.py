import requests

def authenticate_to_api():
    """
    VULNERABILIDADE: Hardcoded Credentials/Secrets
    Credenciais e tokens armazenados diretamente no código são uma falha de segurança grave.
    Isso expõe as credenciais em repositórios públicos e histórico do Git.
    """
    # NUNCA faça isso! Credenciais hardcoded
    api_key = "sk_live_51234567890abcdefghijklmnop"
    database_password = "MySecurePassword123!@#"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(
        "https://api.example.com/users",
        headers=headers
    )
    
    return response.json()


def connect_to_database():
    """
    Outro exemplo com credenciais do banco de dados hardcoded
    """
    # VULNERÁVEL: Credenciais expostas
    db_connection_string = "postgresql://admin:SuperSecret123@db.example.com:5432/mydb"
    
    # Simular conexão
    print(f"Conectando com: {db_connection_string}")
    
    return db_connection_string


def send_email(recipient):
    """
    Exemplo com SMTP credentials hardcoded
    """
    # VULNERÁVEL: Credenciais SMTP expostas
    smtp_server = "smtp.gmail.com"
    smtp_user = "myemail@gmail.com"
    smtp_password = "gapp_1234567890abcdef"
    
    print(f"Sending email to {recipient} via {smtp_user}")
    
    return True


# Teste das funções
if __name__ == "__main__":
    authenticate_to_api()
    connect_to_database()
    send_email("user@example.com")
