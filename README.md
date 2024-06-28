C Drive


Este é um projeto que replica funcionalidades básicas do Google Drive, permitindo uploads, downloads e manipulação de arquivos e pastas. O sistema possui dois tip


Funcionalidades Principais


-Autenticação de usuários com diferentes níveis de permissão (staff e usuários normais).
-Upload e download de arquivos.
-Criação, renomeação e exclusão de pastas.
-Interface amigável e responsiva para fácil navegação e interação.


Tecnologias Utilizadas


-Django: framework web em Python para o backend e Javascript para frontend-.
-Docker: para facilitar a configuração do ambiente de desenvolvimento.
-HTML, CSS, JavaScript: para o frontend e interações na interface do usuário.
-PostgreSQL: banco de dados para persistência dos dados.


Pré-requisitos
Certifique-se de ter instalado:


-Docker
-Docker Compose
-Django
-Poetry


Como Iniciar o Projeto


Clone o repositório:


git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio


Configure as variáveis de ambiente:
Construa as imagens Docker:


Execute o seguinte comando para construir as imagens Docker:




docker-compose build  ou docker-compose build --force-rm


Inicie os containers:


Após a construção das imagens, inicie os containers Docker:


docker-compose up -d


Execute as migrações do banco de dados:


Abra um novo terminal e execute as migrações do Django para configurar o banco de dados:




docker-compose run web python manage.py migrate e makemigrations


Crie um superusuário (admin):


Para acessar o painel de administração do Django, crie um superusuário:


docker-compose run web python manage.py createsuperuser


Siga as instruções no terminal para criar um superusuário com nome de usuário e senha.


Acesse a aplicação:


Após seguir os passos acima, você pode acessar a aplicação em seu navegador:


Aplicação principal: http://127.0.0.1:8000/
Painel de administração: http://127.0.0.1:8000/admin/
Funcionalidades de Usuário e Administração:


Faça login com o superusuário criado para acessar o painel de administração e gerenciar usuários.
Faça login com outros usuários para testar as funcionalidades de manipulação de arquivos e pastas.


Estrutura do Projeto


A estrutura de arquivos e pastas do projeto segue um padrão comum para aplicações Django, incluindo diretórios para templates, arquivos estáticos, e aplicação principal.


Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues para reportar problemas ou sugestões de melhorias.


Este README.md fornece uma visão geral do projeto, os passos necessários para configurar e iniciar o ambiente de desenvolvimento usando Docker, e informações básicas sobre as funcionalidades e estrutura do projeto. Certifique-se de personalizar e adaptar conforme necessário para refletir completamente seu projeto específico.










