# 📚 Projeto de API RESTful com Django REST Framework

Este projeto consiste no desenvolvimento de uma API para gerenciamento de livros, utilizando o **Django REST Framework**. O objetivo foi aplicar conhecimentos práticos de criação de endpoints, consumo e manipulação de dados em formato JSON, além de explorar ferramentas de testes e automação.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Python 3.10+**
- **Django**
- **Django REST Framework**
- **SQLite** (como banco de dados local)
- **Faker** (geração de dados fictícios em português)
- **Selenium** (automação web para testes simples)
- **Pytest** (testes automatizados)
- **HTML/CSS** (interface básica de administração)
- **Postman** (testes de API)

---

## 🚀 Funcionalidades da API

- 📖 **Listagem de livros**
- ➕ **Cadastro de novos livros**
- ✏️ **Atualização de informações**
- ❌ **Exclusão de livros**
- 🔍 **Consulta de livros por ID**

---

## 🤖 Automação de Testes com Selenium

Para validar o funcionamento da interface e do endpoint de cadastro de livros, foi criada uma automação simples utilizando **Selenium WebDriver**, que:

1. Abre a interface do Django REST.
2. Clica no botão `POST`.
3. Preenche os campos obrigatórios com dados aleatórios (gerados com `Faker` em português).
4. Envia a requisição e verifica o resultado.

Essa automação auxilia em testes manuais repetitivos, garantindo que o endpoint está ativo e funcionando corretamente.

---

## 📚 Conhecimentos Aplicados

- Criação e configuração de projeto Django
- Modelagem de dados com `models.py`
- Serialização com `serializers.py`
- Criação de `ViewSets` e rotas com `routers`
- Integração com ferramentas de testes automatizados
- Uso de bibliotecas externas para geração de dados realistas
- Manipulação de elementos com XPath e CSS Selectors via Selenium

---

## ✅ Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repo.git
   cd nome-do-repo
