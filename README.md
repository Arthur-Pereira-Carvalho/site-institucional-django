# DevSync - Site Institucional

Projeto desenvolvido como parte de um desafio técnico para criação de um site institucional com formulário funcional.

---

## 📌 Descrição

O **DevSync** é um site institucional fictício para uma empresa de tecnologia focada em desenvolvimento de software.

O projeto possui as seguintes páginas:

* Home
* Sobre
* Serviços
* Contato

A página de contato conta com um formulário funcional que permite o envio de mensagens, armazenando os dados em um banco de dados utilizando Django.

---

## 🖼️ Preview do Projeto

### 🏠 Home

![Home](images/DevSync Home.png)

### 🧾 Serviços

![Serviços](images/DevSync Servicos.png)

### 📬 Contato

![Contato](images/DevSync  Contato.png)

> 📁 Crie uma pasta chamada `images` na raiz do projeto e adicione os prints do sistema.

---

## 🚀 Tecnologias utilizadas

* Python
* Django
* HTML
* CSS
* Bootstrap

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/devsync.git
```

---

### 2. Acesse a pasta do projeto

```bash
cd devsync
```

---

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

---

### 4. Ative o ambiente virtual

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

---

### 5. Instale as dependências

```bash
pip install django
```

---

### 6. Execute as migrações

```bash
python manage.py migrate
```

---

### 7. Inicie o servidor

```bash
python manage.py runserver
```

---

### 8. Acesse no navegador

```
http://127.0.0.1:8000/
```

---

## 📬 Funcionalidade de Contato

O formulário da página de contato permite que usuários enviem:

* Nome
* Email
* Mensagem

Esses dados são armazenados no banco de dados SQLite e podem ser acessados pelo painel administrativo do Django.

---

## 🔐 Acesso ao painel administrativo

Para acessar o admin:

```
http://127.0.0.1:8000/admin/
```

> ⚠️ É necessário criar um superusuário antes:

```bash
python manage.py createsuperuser
```

---

## 📁 Estrutura do projeto

```
site-institucional-django/
├── config/
├── mainapp/
├── templates/
├── images/
├── manage.py
└── README.md
```

---

## 👨‍💻 Autor

Arthur Pereira

---
