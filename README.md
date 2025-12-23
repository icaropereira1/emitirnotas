# 🧾 Automação de Emissão de Notas (NFCe) - Vuca Solution

Este projeto é um script de automação desenvolvido em Python utilizando **Selenium**. Seu objetivo é automatizar o processo de emissão de Notas Fiscais de Consumidor Eletrônica (NFCe) no painel administrativo, navegando dia a dia e emitindo as notas pendentes.

## 📂 Estrutura dos Arquivos

* `abrirlinks.py`: O código principal da automação.
* `ANTES DE EXECUTAR PELA 1 VEZ.bat`: Script facilitador para instalação das dependências.
* `.env`: Arquivo de configuração onde ficam seu login e senha (seguro).
* `chrome.exe`: Executável/Driver do navegador necessário para a automação.

## 📋 Pré-requisitos

Certifique-se de que você possui o **Python** instalado em sua máquina. O script `.bat` utilizará o Python para baixar as bibliotecas necessárias.

## 🚀 Instalação (Primeiro Uso)

Para preparar o ambiente, você não precisa digitar comandos complexos.

1.  Na pasta do projeto, localize o arquivo chamado:
    **`ANTES DE EXECUTAR PELA 1 VEZ.bat`**
2.  Dê um **duplo clique** nele.
3.  Uma janela preta (terminal) se abrirá e instalará automaticamente as bibliotecas `selenium` e `python-dotenv`.
4.  Aguarde a janela fechar ou exibir uma mensagem de conclusão.

---

## 🔐 Configurando seu Login e Senha (.env)

Para garantir a segurança dos seus dados, o robô lê as credenciais de um arquivo separado. Como o arquivo `.env` já existe na sua pasta (conforme visto na estrutura), siga estes passos:

1.  Clique com o botão direito no arquivo **`.env`**.
2.  Escolha **"Abrir com"** e selecione o **Bloco de Notas** (ou VS Code, se tiver).
3.  Substitua o conteúdo ou preencha seguindo exatamente este modelo (sem espaços e sem aspas):

```env
login=SEU_USUARIO_AQUI
senha=SUA_SENHA_AQUI
```

## ⚙️ Ajustando Datas e Instância

Antes de rodar a automação, se precisar mudar o período ou a loja, edite o arquivo **`abrirlinks.py`**. Vá até o final do código, na seção `if __name__ == "__main__":`:

```python
    nome_da_instancia = ''                # Instância
    mes_do_relatorio = 12                 # Mês
    ano_do_relatorio = 2025               # Ano
    primeirodia = 1                       # Dia inicial
    ultimodia = 22                        # Dia final
```

## ▶️ Como Rodar a Automação

Com as bibliotecas instaladas (via `.bat`) e o `.env` configurado:

1. Abra o terminal na pasta do arquivo (ou use seu editor de código).
2. Execute o comando:

```bash
python abrirlinks.py
```

## ⚠️ Observações Importantes

* **Não apague o `.env`**: Sem ele, o robô não conseguirá fazer login.
* **Conflito de Drivers**: O arquivo `chrome.exe` na pasta sugere uma versão específica do navegador/driver. Se o script der erro ao abrir o Chrome, verifique se a versão instalada no seu PC é compatível com este arquivo.