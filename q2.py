"""
Questão:

Você foi contratado para desenvolver um sistema de gerenciamento de filmes de uma locadora. Para esta tarefa, você tem duas opções na escolha da estrutura de dados a ser utilizada para manipular os dados em memória:

Opção 1: Estrutura Estática: Você decide utilizar um array de tamanho fixo para armazenar os filmes da locadora.

Qual seria a principal vantagem de utilizar um array neste caso?
Quais seriam os desafios que você enfrentaria se a locadora recebesse muitos filmes novos?
Opção 2: Estrutura Dinâmica: Você opta por utilizar uma lista encadeada para representar os filmes.

Quais são as principais vantagens de usar uma lista encadeada nesse contexto?
Em quais situações uma lista encadeada seria menos eficiente do que um array?
Por fim, considerando as duas opções, qual das duas opções você escolheria e por quê? Justifique sua resposta levando em conta as características do problema e as vantagens e desvantagens de cada tipo de estrutura.

Resposta esperada:

Opção 1: Array (estático)

Vantagem: Acesso rápido aos elementos por meio do índice, o que facilita consultas diretas sobre os filmes da locadora.
Desafio: Tamanho fixo limita a quantidade de filmes, podendo causar overflow se a locadora crescer muito, ou desperdício de espaço se o array for criado muito maior que o necessário.
Opção 2: Lista encadeada (dinâmica)

Vantagem: Tamanho variável, permitindo adicionar ou remover filmes facilmente conforme a demanda muda.
Desvantagem: Acesso a elementos específicos é mais lento, pois é necessário percorrer a lista para localizar o filme desejado.
Qual escolher?

A escolha ideal depende da frequência de cada operação:

Se a locadora tiver um número fixo de filmes e a ordem não for importante: um array pode ser suficiente.
Se a locadora crescer constantemente e a ordem dos filmes não for crucial: uma lista encadeada é mais flexível.

"""