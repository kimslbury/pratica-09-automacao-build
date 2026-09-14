# Prática 09 - Automação de Build

Projeto desenvolvido para a prática de automação de build, com a adaptação do
pipeline originalmente descrito para GitLab CI para o GitHub Actions.

## O que foi implementado

- execução automática de testes Python;
- construção de imagem Docker;
- publicação da imagem no GitHub Container Registry (GHCR);
- versionamento por hash do commit e pela tag `latest`;
- cache do BuildKit entre as execuções do workflow.

## Execução local

```bash
python -m unittest discover -v
python app.py
```

Com Docker instalado:

```bash
docker build -t pratica09-automacao-build:local .
docker run --rm -p 8000:8000 pratica09-automacao-build:local
```

## Pipeline

O arquivo `.github/workflows/build.yml` possui dois jobs:

1. `quality`: executa os testes automatizados;
2. `build`: depende dos testes, cria a imagem e a publica no GHCR usando
   `cache-from: type=gha` e `cache-to: type=gha,mode=max`.

Em pull requests, apenas os testes são executados. Em pushes para `main`, o
workflow executa também o build e o push da imagem.

