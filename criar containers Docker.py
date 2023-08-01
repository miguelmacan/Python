import docker

# Crie um cliente Docker
client = docker.from_env()

# Crie e execute um container
container = client.containers.run('ubuntu', 'echo Hello, Docker!', detach=True)

# Exiba a saída do container
print(container.logs())

# Pare e remova o container após a execução
container.stop()
container.remove()
