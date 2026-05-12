import sqlite3

def get_user_by_email(email):
    """
    VULNERABILIDADE: SQL Injection
    Este código é vulnerável porque concatena diretamente a entrada do usuário
    na query SQL sem usar parameterized queries.
    """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Entrada do usuário sem sanitização
    query = "SELECT * FROM users WHERE email = '" + email + "'"
    
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    
    return result


def search_users(search_term):
    """
    Outro exemplo de SQL Injection usando format string
    """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Vulnerável a SQL injection
    query = "SELECT * FROM users WHERE name LIKE '%{}%'".format(search_term)
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    
    return results


# Teste da função
if __name__ == "__main__":
    # Um atacante poderia passar algo como: admin' --
    result = get_user_by_email("user@example.com")
    print(result)
