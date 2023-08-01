import os
import boto3
import tarfile

def fazer_backup(diretorio_local, nome_arquivo_backup, bucket_nome, chave_acesso, chave_secreta):
    # Criar arquivo de backup local (tar.gz)
    arquivo_backup = f"{nome_arquivo_backup}.tar.gz"
    with tarfile.open(arquivo_backup, "w:gz") as tar:
        tar.add(diretorio_local, arcname=os.path.basename(diretorio_local))

    # Configurar o cliente do Amazon S3
    s3 = boto3.client('s3', aws_access_key_id=chave_acesso, aws_secret_access_key=chave_secreta)

    # Enviar o arquivo de backup para o Amazon S3
    try:
        s3.upload_file(arquivo_backup, bucket_nome, nome_arquivo_backup)
        print(f"Backup realizado com sucesso! Arquivo '{nome_arquivo_backup}' enviado para o bucket '{bucket_nome}'.")
    except Exception as e:
        print(f"Erro ao enviar o backup para o Amazon S3: {str(e)}")
    finally:
        # Remover o arquivo de backup local
        os.remove(arquivo_backup)

# Exemplo de uso
if __name__ == '__main__':
    # Configurações do backup
    DIRETORIO_LOCAL = "/caminho/do/diretorio/local"
    NOME_ARQUIVO_BACKUP = "meu_backup"
    BUCKET_NOME = "nome_do_bucket_no_s3"
    CHAVE_ACESSO = "sua_access_key"
    CHAVE_SECRETA = "sua_secret_key"

    fazer_backup(DIRETORIO_LOCAL, NOME_ARQUIVO_BACKUP, BUCKET_NOME, CHAVE_ACESSO, CHAVE_SECRETA)
