import subprocess
import os

def process_file(filename):
    """
    VULNERABILIDADE: Command Injection
    Usar entrada do usuário diretamente em comandos shell é perigoso.
    Um atacante pode injetar comandos maliciosos.
    """
    # VULNERÁVEL: filename não é sanitizado
    command = f"cat {filename}"
    result = os.system(command)
    
    return result


def compress_backup(file_path):
    """
    Outro exemplo de command injection com subprocess
    """
    # VULNERÁVEL: file_path não é escapado
    command = f"tar -czf backup.tar.gz {file_path}"
    
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    stdout, stderr = process.communicate()
    
    return stdout.decode()


def scan_directory(directory_path):
    """
    Exemplo com comando de busca vulnerável
    """
    # VULNERÁVEL: directory_path pode conter caracteres especiais maliciosos
    search_command = f"find {directory_path} -name '*.txt' | head -20"
    
    result = subprocess.check_output(search_command, shell=True)
    
    return result.decode().split('\n')


# Teste das funções
if __name__ == "__main__":
    # Um atacante poderia passar algo como: "; rm -rf /" ou "file.txt; cat /etc/passwd"
    process_file("user_input.txt")
    compress_backup("/home/user/documents")
    scan_directory("/var/log")
