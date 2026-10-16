# 🐍 Repositório de Estudos — `uv` com Python

Repositório criado para testar e aprender a utilizar o [`uv`](https://docs.astral.sh/uv/), uma ferramenta moderna para gerenciamento de dependências, ambientes virtuais e projetos Python.

O objetivo é praticar o fluxo de desenvolvimento utilizando **Python, uv e Git**, incluindo o versionamento do código e a sincronização do projeto entre diferentes máquinas.

## 📋 Pré-requisitos

Antes de começar, verifique se você possui as seguintes ferramentas instaladas:

- [Python](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Git](https://git-scm.com/downloads/)
- Uma conta no [GitHub](https://github.com/)

## 🚀 1. Criar e configurar o repositório Git

No terminal, acesse a pasta do projeto e execute os comandos abaixo.

### Inicializar o repositório

```bash
git init
git branch -M main
git status
```

### Adicionar e registrar os arquivos

```bash
git add .
git commit -m "Initial commit"
```

### Conectar ao GitHub

Substitua a URL de exemplo pelo endereço do seu repositório remoto.

```bash
git remote add origin https://github.com/USER/REPO.git
git remote -v
```

### Enviar o projeto para o GitHub

```bash
git push -u origin main
```

O parâmetro `-u` configura o vínculo entre a branch local `main` e a branch remota `main`, facilitando os próximos envios.

## 🔄 2. Fluxo de trabalho diário

Sempre que realizar alterações no código ou adicionar arquivos ao projeto, utilize a sequência abaixo para registrar e enviar as mudanças.

### Adicionar as alterações

```bash
git add .
```

### Criar um commit

```bash
git commit -m "Describe your changes"
```

Utilize uma mensagem curta e descritiva, indicando o que foi alterado.

Exemplos:

```bash
git commit -m "Add Python application"
git commit -m "Update project dependencies"
git commit -m "Improve README documentation"
```

### Enviar as alterações ao GitHub

```bash
git push
```

**Fluxo resumido:**

`git add` → `git commit` → `git push`

## 🔃 3. Atualizar o projeto a partir do GitHub

Se você realizou alterações diretamente no GitHub ou se existem novos commits no repositório remoto, execute:

```bash
git pull
```

Esse comando busca e integra as alterações remotas à branch local atual.

> **Atenção:** se você tiver alterações locais ainda não registradas, verifique o estado do repositório com `git status` antes de executar o `git pull`. Se houver conflitos, será necessário resolvê-los.

## 💻 4. Configurar o projeto em outra máquina

Para continuar o desenvolvimento em outro computador, siga estas etapas.

### Clonar o repositório

```bash
git clone https://github.com/USER/REPO.git
```

### Entrar na pasta do projeto

```bash
cd REPO
```

### Instalar e sincronizar as dependências

```bash
uv sync
```

O comando `uv sync` cria ou atualiza o ambiente virtual do projeto e sincroniza as dependências declaradas nos arquivos de configuração, especialmente no `pyproject.toml` e, quando aplicável, no `uv.lock`.

### Executar a aplicação

```bash
uv run app
```

Esse comando pressupõe que `app` seja um executável ou script reconhecido pelo ambiente do projeto. Se a aplicação estiver em um arquivo chamado `app.py`, por exemplo, utilize:

```bash
uv run python app.py
```

O `uv run` executa o comando no ambiente do projeto, gerenciando as dependências necessárias conforme a configuração existente.

## 📦 5. Comandos úteis do uv

| Comando | Finalidade |
|---|---|
| `uv init` | Inicializa um projeto Python |
| `uv add requests` | Adiciona uma dependência ao projeto |
| `uv remove requests` | Remove uma dependência |
| `uv sync` | Sincroniza o ambiente com as dependências declaradas |
| `uv run python app.py` | Executa um script Python no ambiente do projeto |
| `uv run pytest` | Executa os testes, caso o pytest esteja configurado |
| `uv lock` | Atualiza o arquivo de resolução de dependências |
| `uv tree` | Exibe a árvore de dependências do projeto |

## 📁 6. Arquivos importantes do projeto

Ao utilizar o `uv`, você poderá encontrar os seguintes arquivos e diretórios:

| Arquivo ou diretório | Descrição |
|---|---|
| `pyproject.toml` | Contém os metadados e as configurações do projeto, incluindo dependências |
| `uv.lock` | Registra as versões resolvidas das dependências |
| `.python-version` | Pode definir a versão do Python utilizada pelo projeto |
| `.venv/` | Ambiente virtual local, normalmente não versionado no Git |
| `.gitignore` | Define arquivos e diretórios que o Git deve ignorar |
| `README.md` | Documentação principal do repositório |

## ⚠️ Boas práticas

- **Versione o `pyproject.toml` e o `uv.lock`** para facilitar a reprodução do ambiente em outras máquinas.
- **Não versione a pasta `.venv/`**, pois ela contém um ambiente virtual local.
- Utilize o `.gitignore` para evitar o envio de arquivos temporários, caches e informações sensíveis.
- Prefira mensagens de commit objetivas e descritivas.
- Execute `git status` antes de registrar alterações para conferir quais arquivos serão incluídos.
- Após adicionar ou modificar dependências, verifique as alterações nos arquivos de configuração antes de realizar o commit.

## 📚 Referências

- [Documentação oficial do uv](https://docs.astral.sh/uv/)
- [Guia de início rápido do uv](https://docs.astral.sh/uv/getting-started/)
- [Documentação oficial do Git](https://git-scm.com/doc)
- [Documentação do GitHub](https://docs.github.com/)

---

**Objetivo do repositório:** explorar o ecossistema `uv` e praticar um fluxo de desenvolvimento Python com gerenciamento de dependências e versionamento utilizando Git e GitHub.
