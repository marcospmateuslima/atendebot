
# 🤖 AtendeBot

AtendeBot é um chatbot simples desenvolvido em Python com Flask. Ele responde a perguntas pré-definidas usando correspondência exata ou aproximação com difflib.

## 🚀 Funcionalidades

- Interface Web com Flask
- Respostas automáticas baseadas em um arquivo JSON de conhecimento
- Correspondência aproximada para perguntas semelhantes
- Fácil de personalizar

## 🛠️ Tecnologias

- Python 3.12
- Flask
- difflib
- HTML e CSS

## 📁 Estrutura do Projeto

```
projetochatboot/
│
├── app.py                # Inicia o servidor Flask
├── chatbot.py            # Lógica de resposta do chatbot
├── base_conhecimento.json # Base de perguntas e respostas
├── templates/
│   └── index.html        # Interface do usuário
├── static/
│   └── style.css         # Estilos da interface
└── README.md             # Documentação do projeto
```

## 📦 Como Executar

1. Instale as dependências:
```bash
pip install flask
```

2. Execute a aplicação:
```bash
python app.py
```

3. Acesse no navegador: `http://127.0.0.1:5000`

## 📄 Licença

Este projeto está sob a licença MIT.
