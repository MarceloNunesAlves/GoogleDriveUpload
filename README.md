# Projeto para enviar arquivos ao Google Drive

> Os seguintes passos podem ser seguidos para habilitar o Google Drive API no GCP:

 - Acesse o Console do Google Cloud Platform (GCP) e selecione sua conta de projeto.
 - Vá para a página de APIs e Serviços e selecione "Biblioteca de APIs".
 - Procure por "Google Drive API" na biblioteca de APIs e clique em "Habilitar".

Após seguir esses passos, você poderá usar a API do Google Drive em suas aplicações, basta escolher apenas a formar de acessar.

> Para obter os dados de credenciais (OAuth2) da sua conta do Google siga os seguintes passos:

 - Vá para o Console do Google Cloud Platform: https://console.developers.google.com/
 - Selecione o projeto que você deseja usar ou crie um novo projeto.
 - Na barra de navegação à esquerda, clique em "APIs & Serviços" e, em seguida, clique em "Credenciais".
 - Clique no botão "Criar credenciais" e selecione "Credencial de cliente OAuth".
 - Preencha as informações necessárias para criar a credencial e clique em "Criar".
 - Em seguida, clique no botão "Fazer download" para baixar o arquivo credentials.json com as suas credenciais.

> Para criar uma conta de serviço no Google Cloud Platform (GCP), você precisa seguir os seguintes passos:

 - Entre na Console do GCP: Acesse o console do GCP em https://console.cloud.google.com/ e faça o login com sua conta do Google.
 - Crie um projeto: No console do GCP, clique no botão "Selecionar projeto" e, em seguida, clique em "Criar projeto". Selecione um nome e ID para seu projeto e clique em "Criar".
 - Acesse o Console de Segurança do IAM: No console do GCP, vá até a seção "Segurança, identidade e conformidade" e clique em "Contas de serviço".
 - Crie uma conta de serviço: Clique no botão "Criar conta de serviço" e preencha as informações solicitadas, como o nome da conta, a descrição da conta e a função da conta.
 - Conceda as permissões necessárias: Escolha as permissões necessárias para a conta de serviço, que podem incluir acesso ao armazenamento de dados, acesso à rede e acesso aos serviços do GCP.
 - Crie as chaves de autenticação: Clique no botão "Criar chave" e selecione o formato da chave (por exemplo, JSON). Salve a chave em um local seguro, pois ela será necessária para autenticar a conta de serviço.
 - Conclua a criação da conta de serviço: Clique no botão "Concluir" para criar a conta de serviço. A conta de serviço estará pronta para ser utilizada em suas aplicações.