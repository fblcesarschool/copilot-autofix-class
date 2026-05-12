import sqlite3

def authenticate_user(username, password):
    """
    Autentica um usuário verificando credenciais no banco de dados.
    VULNERÁVEL: SQL Injection
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILIDADE: Concatenação direta de entrada do usuário na query SQL
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    
    cursor.execute(query)
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        return True, "Autenticação bem-sucedida"
    else:
        return False, "Usuário ou senha inválidos"


def get_user_data(user_id):
    """
    Recupera dados do usuário pelo ID.
    VULNERÁVEL: SQL Injection
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILIDADE: Entrada do usuário incorporada diretamente na query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    
    cursor.execute(query)
    user_data = cursor.fetchall()
    
    conn.close()
    
    return user_data


def search_products(search_term):
    """
    Busca produtos no banco de dados.
    VULNERÁVEL: SQL Injection
    """
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # VULNERABILIDADE: Formato string com entrada não sanitizada
    query = f"SELECT name, price FROM products WHERE description LIKE '%{search_term}%'"
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    conn.close()
    
    return results
