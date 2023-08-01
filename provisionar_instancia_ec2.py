import boto3

def provisionar_instancia_ec2(cliente_id):
    # Configurar as credenciais da AWS (substitua pelas suas credenciais)
    ACCESS_KEY = 'sua_access_key'
    SECRET_KEY = 'sua_secret_key'
    REGION = 'us-east-1'  # Região da AWS onde a instância será criada

    # Iniciar o cliente EC2
    ec2 = boto3.client('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

    # Definir as configurações da instância
    AMI_ID = 'ami-0c55b159cbfafe1f0'  # ID da imagem AMI (Amazon Machine Image) a ser usada
    INSTANCIA_TIPO = 't2.micro'  # Tipo da instância (pode ser alterado conforme suas necessidades)
    KEY_PAIR = 'nome_da_sua_chave'  # Nome da chave de acesso SSH

    # Criar a instância EC2
    response = ec2.run_instances(ImageId=AMI_ID, InstanceType=INSTANCIA_TIPO, KeyName=KEY_PAIR, MinCount=1, MaxCount=1)

    # Obter o ID da instância criada
    instancia_id = response['Instances'][0]['InstanceId']

    # Associar o cliente_id à tag "ClienteID" da instância
    ec2.create_tags(Resources=[instancia_id], Tags=[{'Key': 'ClienteID', 'Value': cliente_id}])

    print(f'Instância EC2 criada para o cliente {cliente_id}. ID da instância: {instancia_id}')

# Exemplo de uso
if __name__ == '__main__':
    novo_cliente_id = '12345'
    provisionar_instancia_ec2(novo_cliente_id)
