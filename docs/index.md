<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12">
<center>

Concepção de sistema de automação industrial

</center>
</font>

> _Observação 1: A estrutura inicial deste documento é só um exemplo. O seu grupo deverá alterar esta estrutura de acordo com o que está sendo solicitado nos artefatos._

> _Observação 2: O índice abaixo não precisa ser editado se você utilizar o Visual Studio Code com a extensão **Markdown All in One**. Essa extensão atualiza o índice automaticamente quando o arquivo é salvo._

**Conteúdo**

- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Empresa](#empresa)
  - [O Problema](#o-problema)
  - [Objetivos](#objetivos)
    - [Objetivos gerais](#objetivos-gerais)
    - [Objetivos específicos](#objetivos-específicos)
  - [Partes interessadas](#partes-interessadas)
- [Análise do Problema](#análise-do-problema)
  - [Dados levantados e analisados relativos ao problema](#dados-levantados-e-analisados-relativos-ao-problema)
  - [Análise financeira do projeto](#análise-financeira-do-projeto)
  - [Análise das 5 forças de Porter](#análise-das-5-forças-de-porter)
    - [Fornecedores:](#fornecedores)
    - [Consumidores:](#consumidores)
    - [Entraves de de entrada](#entraves-de-de-entrada)
    - [Concorrentes diretos:](#concorrentes-diretos)
    - [Substitutos:](#substitutos)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
    - [Produto:](#produto)
    - [Cliente](#cliente)
  - [Matriz de Risco](#matriz-de-risco)
  - [Matriz de avaliação de valor Oceano Azul](#matriz-de-avaliação-de-valor-oceano-azul)
- [Requisitos do Sistema](#requisitos-do-sistema)
  - [Personas](#personas)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
    - [Técnico do laboratório IPT](#técnico-do-laboratório-ipt)
    - [Engenheiro responsável pelo laboratório](#engenheiro-responsável-pelo-laboratório)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Croqui](#croqui)
  - [Documentação dos componentes](#documentação-dos-componentes)
    - [Esquema Geral dos Componentes](#esquema-geral-dos-componentes)
    - [Componentes](#componentes)
      - [Raspberry Pi Pico W:](#raspberry-pi-pico-w)
      - [Especificações do Raspberry Pi Pico W:](#especificações-do-raspberry-pi-pico-w)
      - [Braço Robótico Dobot Magician Lite](#braço-robótico-dobot-magician-lite)
      - [Especificações do Braço Robótico Dobot Magician Lite:](#especificações-do-braço-robótico-dobot-magician-lite)
      - [Teclado Matricial de Membrana:](#teclado-matricial-de-membrana)
      - [Especificações do Teclado Matricial de Membrana:](#especificações-do-teclado-matricial-de-membrana)
      - [Display LCD:](#display-lcd)
      - [Especificações do Display LCD:](#especificações-do-display-lcd)
      - [Eletroímã:](#eletroímã)
      - [Especificações do Eletroímã:](#especificações-do-eletroímã)
      - [Ponte H:](#ponte-h)
      - [Especificações da Ponte H:](#especificações-da-ponte-h)
      - [Célula de Peso e Módulo Hx711 Sensor de Peso:](#célula-de-peso-e-módulo-hx711-sensor-de-peso)
      - [Especificações do Célula de Peso e Módulo Hx711 Sensor de Peso:](#especificações-do-célula-de-peso-e-módulo-hx711-sensor-de-peso)
    - [Módulos funcionais do sistema](#módulos-funcionais-do-sistema)
      - [Projeto dos dispositivos mecânicos](#projeto-dos-dispositivos-mecânicos)
      - [Projeto dos dispositivos Eletrônicos](#projeto-dos-dispositivos-eletrônicos)
      - [Pinagem Magic Box:](#pinagem-magic-box)
      - [Esquemático célula de peso:](#esquemático-célula-de-peso)
- [Planejamento e método de fabricação:](#planejamento-e-método-de-fabricação)
      - [Descrição do Hardware](#descrição-do-hardware)
    - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [UX e UI Design](#ux-e-ui-design)
  - [Wireframe + Storyboard](#wireframe--storyboard)
  - [Design de Interface](#design-de-interface)
- [Projeto de Banco de Dados](#projeto-de-banco-de-dados)
  - [Modelo Conceitual](#modelo-conceitual)
  - [Modelo Lógico](#modelo-lógico)
- [Teste de Software](#teste-de-software)
  - [Testes Unitários](#testes-unitários)
    - [Sprint 2](#sprint-2)
      - [Braço mecanico](#braço-mecanico)
      - [Eletroímã](#eletroímã-1)
      - [Módulo de peso](#módulo-de-peso)
  - [Teste de Usabilidade](#teste-de-usabilidade)
- [Análise de Dados](#análise-de-dados)
- [Manuais](#manuais)
  - [Manual de Implantação](#manual-de-implantação)
  - [Manual do Usuário](#manual-do-usuário)
  - [Manual do Administrador](#manual-do-administrador)
- [Referências](#referências)

# Autores

- Jean Lucas Rothstein Machado
- Antonio Angelo Teixeira
- Rafael Nissim Katalan
- Vinicios Venâncio Lugli
- Felipe Henrique Moreira Leão
- Pablo Ruan Lana Viana
- Gustavo Ferreira de Oliveira

# Visão Geral do Projeto

## Empresa

O IPT (Instituto de Pesquisas Tecnológicas) é uma organização de pesquisa, desenvolvimento e inovação, vinculada ao Governo do Estado de São Paulo. As áreas de atuação do IPT são bastante diversificadas, produzindo soluções de engenharia, materiais, meio ambiente, energia, e saúde. O instituto é reconhecido nacional e internacionalmente pela excelência técnica e qualidade de seus serviços, e principalmente, pela capacidade de inovação.

No setor de mineração, o IPT desenvolve pesquisas e desenvolvimento de tecnologias para essa indústria, e utiliza seus laboratórios e equipamentos principalmente para a realização de ensaios e análises de amostras de minérios, separação de minerais e estudos de solos com potencial de extração mineral.

## O Problema

No início do módulo, foi nos apresentado, durante o processo de exposição do projeto para a turma de Engenharia da Computação do Inteli, o Instituto de Pesquisa Tecnológicas - IPT . Tal projeto traz como principal foco o processo de separação de minérios (imagem 1), ao qual ainda é realizado manualmente por um operador (técnico de laboratório do IPT) que leva em média de 20 – 30 minutos dependendo do tamanho de amostra e concentração de minérios de ferro encontrados na amostra.

## Objetivos

### Objetivos gerais

Com o intuito de aliviar os problemas e as dores apresentadas, produziremos uma solução que emprega um braço robótico (Magician Lite) para a automação da tarefa de separação de materiais magnéticos. O técnico precisará apenas inserir a amostra nas bandejas, configurar o campo magnético desejado e supervisionar o procedimento, que será executado automaticamente.

### Objetivos específicos

Para cumprir com o objetivo citado, os seguintes objetivos específicos devem ser concluídos:

- O braço robótico fará a tarefa de executar a varredura da bandeja inicial da amostra com um eletroímã, que deverá ser ajustado conforme o metal que deseja-se obter;
- O braço robótico também deverá começar a varrer a amostra, mantendo uma distância e o campo magnético fixos;
- Após a conclusão da varredura, o robô irá submergir em água o que foi coletado, com o intuito de retirar as impurezas que ficaram retidas;
- Posteriormente, o braço irá se direcionar para a bandeja de coleta, onde o ímã será desativado e a amostra será depositada;
- O processo será repetido até que toda a amostra seja coletada.

## Partes interessadas

- IPT - Instituto de Pesquisas Tecnológicas.
- INTELI - Instituto de Tecnologia e Liderança.

# Análise do Problema

No início do módulo, foi nos apresentado, durante o processo de exposição do projeto para a turma de Engenharia da Computação do Inteli, o Instituto de Pesquisa Tecnológicas - IPT . Tal projeto traz como principal foco o processo de separação de minérios (imagem 1), ao qual ainda é realizado manualmente por um operador (técnico de laboratório do IPT) que leva em média de 20 – 30 minutos dependendo do tamanho de amostra e concentração de minérios de ferro encontrados na amostra.

<p align="center">
<img src="img/relatorio/processo-separacao-minerios.png">

<p align="center"> 1 — Demonstração do processo manual de separação de amostras realizado pelo IPT.</p>

</p>
  
<br>
O processo de separação de amostras atualmente ocorre da seguinte forma: sobre uma mesa são dispostos 3 ímãs de diferentes potenciais (medidos em Gauss); 3 bandejas; 1 saco plástico; 1 recipiente com a amostra (imagem 2). Em todas as 3 bandejas são colocados água para facilitar a manipulação da amostra - na primeira bandeja é despejado a amostra e as outras 2 bandejas irão ser utilizadas como apoio durante o processo de separação manual. Após estas etapas, é escolhido o ímã que mais atrai minérios magnéticos, o qual é envolvido em um plástico (para facilitar a retirada dos materiais de ferros recolhidos pelo ímã).

Após esta fase, o ímã é mergulhado e passa pela bandeja que se encontra com água e a amostra, posteriormente na segunda bandeja só com água e por último solto e armazenado na última bandeja. Este processo é feito várias vezes com o ímã de maior potência e depois com os outros dois ímãs de menor potência, sendo realizado as etapas da mesma forma.

<p align="center">

<img src="img/relatorio/processo-separacao-minerios-etapas.png">

<p align="center"> 2 - Processo manual de separação de amostras realizado pelo IPT.</p>
</p>

<br>

A necessidade de atualizar este processo vem das grandes demandas de empresas procurando o IPT para realizar testes de separação de minérios em amostra de perfurações realizadas em alguns terrenos. Essas amostras, por sua vez, têm a intenção de analisar a viabilidade do investimento em mineração desses terrenos por meio de algumas métricas pré-estabelecidas, que procuram informações acerca de presença, quantidade e qualidade dos minérios de ferro para extração ponderando viabilidade financeira e ambiental. Algumas das informações almejadas para tal análise são:

1. Concentração de ferro na amostra;
2. Qualidade do minério para determinar a pureza desse;
3. Características geológicas do minério;
4. Quantidade de recursos disponíveis para mineração no local;
5. Riscos ambientais envolvidos com o projeto.

Com a separação magnética feita de forma automática com o braço robótico (Magician Lite), a medição dos minérios poderá ser mais efetiva, e assim, será possível analisar mais facilmente esses parâmetros para viabilização do projeto de mineração do ambiente pretendido.

## Dados levantados e analisados relativos ao problema

Após uma análise da realização da separação pelo técnico de laboratório, é possível perceber que a cada passagem, é gasto aproximadamente 1 minuto. A partir disso, poderemos quantificar se a automação estará trazendo economia de tempo e aumento da produtividade.

Atualmente, o ímã que apresenta o melhor resultado para a separação metálica é de 3000 Gauss, conforme os testes que já foram realizados. No laboratório, há também ímãs de 1500 e 6000 Gauss, que podem ser utilizados de acordo com a amostra que estiver sendo testada.

Existem diferentes tipos de separadores magnéticos, sendo normalmente usados ímãs permanentes, que incluem: ímãs de barra, disco, pulso, rolo, tambor e correia, e dentre esses, os ímãs de barra são utilizados atualmente na separação. Para otimização do processo, esses materiais serão substituídos por eletroímãs que variam o campo magnético para melhor separação dos minérios.
Em relação à taxa de eficiência da separação magnética em minérios, no entanto, pode haver uma variação dependendo de diversos fatores, incluindo a composição mineral do minério, a granulometria, a concentração de minério, a intensidade do campo magnético e o tipo de separador magnético utilizado.

Os metais que despertam o maior interesse da indústria atualmente são o ferro e o cobre. Entretanto, esses metais apresentam uma grande diferença de atração magnética, o que permite que a separação magnética seja bastante efetiva. Como o ferro apresenta um potencial de atração muito alto, um campo magnético muito baixo é o suficiente para atrair as amostras desse tipo de minério. Após a separação desse minério, poderá ser utilizado um campo magnético de intensidade maior, para que o cobre seja atraído com maior facilidade.

## Análise financeira do projeto

O cenário financeiro do parceiro, laboratório de mineração do IPT, atualmente é de 8 análises de solo por mês com cada uma custando na faixa de 3 mil reais. Ainda nesse sentido, podemos considerar o técnico que realiza o processo manual como único custo que deve ser considerado, pois esse será o único custo que, efetivamente, mudará, porque com a automação, o técnico ficará livre para realizar outros trabalhos gerando um valor apenas dependente de suas qualificações.

Por outro lado, com o processo de automatização realizado, o rendimento aumentaria em 25%, passando para 10 amostras analisadas por mês, mantendo-se em 3 mil reais. Dessa maneira, para realizar esse processo, o robô custaria 20 mil reais somado a um kit de 600 reais, que seriam custos únicos, além dos custos por mês de operação, sendo dividido em estruturação e implementação. Os custos de estruturação são de operação com 2,5 mil reais, 4 mil por ano de manutenção e um engenheiro robótico com salário de 20 mil reais. Já no processo de implementação, os custos são: 2,5 mil reais e uma equipe com o engenheiro e três funcionários, totalizando pouco mais de 42 mil reais.

Em última análise, realizando-se os cálculos, chega-se à conclusão que o valor da automação deve custar algo próximo a 90 mil reais, com dois meses de operação. Assim, esse processo se pagaria em torno de 10 meses, pois o aumento de desempenho irá gerar nove mil reais a mais por mês, somando com o que o técnico, que terá mais tempo livre, conseguirá realizar com esse tempo de sobra.

## Análise das 5 forças de Porter

- As 5 forças de Porter é uma análise feita em relação a como a empresa se encontra no ecossistema empresarial, levantando pontos relacionados aos seus principais stakeholder e como eles influenciam no desenvolvimento dela. Entre eles estão:

### Fornecedores:

- Eles possuem a influência na distribuição de insumos ou serviços necessários para as operações da empresa, sendos eles no contexto do IPT fornecedores de peças e materiais para construção de circuitos eletronicos, microprocessadores e materias gerais para a realização dos teste.

### Consumidores:

- Eles possuem a influência na receita da empresa pela escolha de adquirir ou não o produto, para o IPT as empresas e instituições que fecham contratatos com eles são importantes não só pelo funcionamento e mantimento das operações da empresa, mas para o incentivo de constante melhoria tendo em vista o grande aumento de tecnologia e na area de análise e pesquisas para diversas áreas.

### Entraves de de entrada

- São os desafios das empresas que pretendem entrar nesse setor, analisando o setor do IPT um dos principais entraves é o auto investimento em infraestrutura para realizar as pesquisas, além da necessidade de mão de obra qualificada que aumenta a demanda de uma relação próxima com universidades e o valor a ser investido nos serviços desses profissionais.

### Concorrentes diretos:

- São empresas que possuem produtos ou serviços do mesmo setor e com a mesma finalidade. A princípio, os concorrentes diretos do IPT são outros intituos como ITA e IME, mas algumas empresas privadas também fornecem os mesmo produtos de testes e pesquisas podendo elas serem comcorrentes diretos.

### Substitutos:

- São empresas que possuem produtos que não são do mesmo setor mas possuem soluções que se aplicam para as dores do setor. Algumas empresas privadas que encontramos em uma pesquisa sobre produtos similares a análise do solo para mineração fornecem esse tipo de serviços mas de maneira diferente e não só para esse propósito podendo atuar como produtos substitutos.

<p align="center">

<img src="img/relatorio/cinco-forcas-porter.png">
</p>
<br>

## Proposta de Valor: Value Proposition Canvas

- O canvas proposition é uma ferramenta que auxilia na criação do produto em relação as espectativa e demandas do cliente, ele é fundamental para o entendimento de como a solução será relevante e validar algumas hipótese sobre o produto. Essa ferreamenta é divido em dois pontos sobre o produto e sobre o cliente. Esses pontos servem para nortear os tópicos relevantes ao produto e quais são relevantes ao cliente.

### Produto:

1. Aliviador de dores: Os aliviadores de dores tem correspondência com as dores e explicitam a forma como o produto resolve as dores de maneira direta do cliente.
2. Produtos e serviços: Essa área são as especifações gerais do produto, o que ele é de fato.
3. Criadores de ganhos: Eles são os ganhos indiretos que a solução propõe para o cliente e agrega valor intriseco a ele.

### Cliente

1. Dores: São os problemas do cliente diretamente exemplificado o que ele precisa que seja solucionado.
2. Tarefas do cliente: São instruções que o cliente precisa fazer ou para a solução funcionar ou para que ela auxilie ele na resolução das dores.
3. Ganhos: Valor agregado do produto que irá impactar diretamente o cliente.

<p align="center">

<img src="img/relatorio/value-proposition-canvas.png">
</p>
<br>

## Matriz de Risco

A partir da análise que realizamos sobre o contexto do projeto, percebemos que os aspectos que gerariam maiores riscos foram relacionados com um funcionamento impreciso da solução, gerado por algum erro durante o processo de desenvolvimento.

Em contrapartida, os aspectos que gerariam maiores oportunidades seriam relacionados com a possibilidade de se obter uma separação mais precisa e com a capacidade de variação do campo magnético.

<p align="center">
<img src="img/relatorio/matriz-risco.png">
</p>

## Matriz de avaliação de valor Oceano Azul

A matriz de oceano Azul é uma análise feita sobre a empresa e a solução proposta, em relação a outras empresas e soluções parecidas. A matriz leva em consideração alguns atributos como: Preço, qualidade, tecnologia, conforto, comodidade e praticidade. Assim, através desses atributos é classificado de 0 a 10 o valor desses atributos em relação as empresas e a solução.

<p align="center">

 <img src="img/relatorio/matriz-avaliacao-valor-oceano-azul.png">
 </p>

# Requisitos do Sistema

1. Um braço robótico capaz de posicionar um manipulador em posição e distância
   controladas sobre a bandeja de amostras;
2. Eletroímã montado no manipulador do braço robótico com campo magnético ajustável
   na faixa de 800 a 12.000 Gauss;
3. Estrutura para calibração de posicionamento do braço;
4. Estrutura para calibração de eletroímã;
5. Automação da bandeja de amostra para promover a agitação das partículas;
6. Recipiente com automatização de pesagem para receber material coletado (opcional);
7. Relatório apresentando todos os dados pertinentes do ensaio (opcional).

## Personas

<p  align="center">

<img src="img/relatorio/personas-1.png">
</p>
<p align="center">

<img src="img/relatorio/personas-2.png">
</p>
<br>

## Histórias dos usuários (user stories)

### Técnico do laboratório IPT

1. Eu, como técnico de laboratório do IPT, desejo poder variar o campo magnético sem mover a distância do ímã para coletar minérios mais ou menos atrativos.
2. Eu, como técnico de laboratório do IPT, desejo que a bandeja vibre e misture a amostra para melhor qualidade do experimento.
3. Eu, como técnico de laboratório do IPT, desejo que a estrutura de bandejas seja removível para maior facilidade de lavagem e remoção de amostras.
4. Eu, como técnico de laboratório do IPT, desejo automatizar o processo de varredura e separação de amostras.
5. Eu, como técnico de laboratório do IPT, desejo dedicar mais meu tempo para pesagem e análise química das amostras.
6. Eu, como técnico de laboratório do IPT, desejo uma interface para uso do robô que seja de fácil utilização e simples manutenção.

### Engenheiro responsável pelo laboratório

1. Eu, como engenheiro responsável pelo laboratório do IPT, desejo que a amostra analisada seja de maior confiabilidade do que possui hoje em dia.
2. Eu, como engenheiro responsável pelo laboratório do IPT, desejo que a amostra seja analisada de maneira mais rápida para maior satisfação dos clientes.
3. Eu, como engenheiro responsável pelo laboratório do IPT, desejo que a aplicação seja de fácil manutenção para não parar por muito tempo o atendimento dos clientes do laboratório.
4. Eu, como engenheiro responsável pelo laboratório do IPT, desejo que a interface da aplicação seja simples e que eu consiga fazer todas as alterações possíveis por meio de uma tela LCD.

# Arquitetura do Sistema

## Croqui

Um croqui trata-se de um método de representação gráfica, utilizado principalmente por arquitetos, engenheiros e designers para esboçar ideias e conceitos visualmente. O objetivo do croqui é transmitir uma ideia de forma rápida e intuitiva, permitindo que o criador possa explorar diferentes possibilidades e testar soluções de forma prática. Neste sentido, o croqui foi uma ferramenta fundamental para o processo criativo da solução proposta pelo grupo. O projeto consisti na criação de um sistema automatizado de ensaio para análise de amostras de metal retiradas do solo, utilizando o braço robótico Dobot Magician Lite. Para otimizar a movimentação do braço, serão utilizadas três bandejas dispostas radialmente, permitindo maior velocidade de execução e reduzindo travamentos. A primeira bandeja será destinada à amostra bruta, a segunda será uma bandeja com água para limpar possíveis resíduos não magnéticos que foram puxados acidentalmente pelo eletroímã, e a terceira será para a amostra limpa. Para controle dos componentes, será utilizado o Raspberry Pi Pico W, eliminando a necessidade de um servidor externo e permitindo ao cliente acesso às configurações do ensaio através de um display de membrana e LCD. Além disso, será adicionado um sensor de peso à terceira bandeja, responsável pela amostra limpa, que, a cada rodada, realizará a pesagem e finalizará o ensaio quando não houver alteração de peso. Para acoplar as amostras ao braço robótico, será adicionado um eletroímã, que será regulado pelo Raspberry Pi Pico através de uma ponte H, permitindo a regulagem da força magnética. Espera-se obter, com a implementação dessas características, um sistema de ensaio automatizado eficiente e de fácil utilização. Um croqui deste sistema pode ser visto na figura abaixo:

<p align="center">

<img src="img/relatorio/croqui.png">
</p>

## Documentação dos componentes

### Esquema Geral dos Componentes

<p align="center">

<img src="img/relatorio/documentacao-componentes.png">
</p>

### Componentes

#### Braço Robótico Dobot Magician Lite

- O braço robótico Dobot Magician lite é um robo que apresenta uma interface em software que dá suporte para a programação do hardware, possibilitando a utilização da garra para tarefas diversas tanto em protótipos reais como no estudo de interação entre inteligência artificial e hardware.
<p align="center">
<img src="img/relatorio/magician-lite.png" width="400px">
</p>
<br>

#### Especificações do Braço Robótico Dobot Magician Lite:

- Capacidade de Carga: 250 gramas
- Potência: 60W máx
- Número de eixos: 4
- Alcance Máximo: 340mm
- Posição da Repetibilidade (controle): 0.2mm
- Fonte de Alimentação: 100V~240V, 50/60 Hz.
- Alimentação: 12V/7A DC
- Controle por USB virtual porta serial / Porta serial

#### Eletroímã:

O Eletroimã é um componente eletrônico moderno com funcionalidade básica semelhante a de um imã, porém com a diferença de possuir maior capacidade de atração graças a presença de solenóides. Que através deles, quando expostos a uma tensão é capaz de gerar um campo magnético no seu interior e exterior, podendo controlar este campo a medida que se controla a intesidade da tensão.

<p align="center">
 <img src="img/relatorio/Eletroima.jpg" width="400px">
</p>
<br>

#### Especificações do Eletroímã:

- Eletroimã / Solenóide 20mm;
- Capacidade de atração elevada;
- Princípo básico de funcionamento semelhante a imã;
- Constituído por solenóides (bobinas cilíndricas);
- Ideal para projetos robóticos e automação residendial.
- Tensão de entrada: 12VDC;
- Capacidade: 2,5Kg;
- Corrente: 0,25A;
- Comprimento do fio: 28cm;
- Diâmetro: 20mm;
- Altura: 15mm;
- Peso: 24g.

#### Célula de Peso e Módulo Hx711 Sensor de Peso:

O Sensor de Peso trata-se de um acessório eletrônico capaz de detectar diferentes cargas que estejam sobre sua meia-ponte, entretanto para funcionamento deve atuar em conjunto com uma plataforma de prototipagem, entre elas, Arduino, PIC, ARM, AVR, entre outros. Como as Células de Carga instalados nas balanças não oferecem dados com grande precisão é necessário o Módulo Conversor HX711 que também funciona como um amplificador de sinal para oferecer dados mais precisos. O Módulo Conversor Amplificador Hx711 de 24bits se comunica através do padrão de comunicação TTL 232, possuindo estrutura simples, fácil de usar e com desempenho estável, além é claro, da elevada sensibilidade e velocidade de medida.

<p align="center">
<img src="img/relatorio/celula-peso.png" width="400px">
</p>
<br>

#### Especificações do Célula de Peso e Módulo Hx711 Sensor de Peso:

- Carga nominal: 1 kg
- Potência nominal de saída: 1.0mv/v ± 0.15mv/v
- Tensão de funcionamento recomendada: 3 ~ 12 VDC
- Tensão máxima de operação: 15 VDC
- Impedância de entrada: 410 +/-30 ohm
- Impedância de saída: 350 +/-3 ohm
- Isolamento: > 2000 megaohm/50 VDC
- Faixa de compensação de temperatura: -10C ~ 40C
- Faixa de temperatura de operação: -20C ~ 60C
- Sobrecarga permitida: <120% da carga nominal
- Carga de ruptura: >150% da carga nominal
- Classe de proteção: IP65
- Material: liga de alumínio
- Dimensões(CxLxA):80mm,12,7mm,12,7mm
- Peso: 31g
- Ligação do fios: Vermelho(+),Preto(-),Verde(Sinal +),Branco(Sinal -)

### Módulos funcionais do sistema

#### Projeto dos dispositivos mecânicos

#### Projeto dos dispositivos Eletrônicos


- As placas que serão utilizadas será apena a placa de circuito integrada para o módulo de peso e a célula de carga.
- O esquemático da célula de peso, os cabos serão todos conectados em uma porta do Magic box sendo eles apresentados no esquemático abaixo. O cabo de cor preta será ligado na porta do GND, o cabo de cor vermelha será ligado na entrada de 5V, o cabo verde será ligado na porta EIO16, o cabo azul será ligado na entrada EIO15.
  
- Para a construção da balança será usada uma célula de carga que é um sensor de peso com capacidade de 5kg que será utilizado para fazer a pesagem da amostragem na última bandeja. Esse sensor trata-se de um acessório eletrônico capaz de detectar diferentes cargas que estejam sobre ele, mas que para seu funcionamento deve atuar em conjunto com uma plataforma de prototipagem, que no caso será o microcontrolador embutido na MagicBox, e ligado a um Módulo Conversor Amplificador HX711 com a finalidade de converter alterações da resistência do sensor da balança em dados digitais por meio de um circuito ADC de 24-bits.
- No centro do sensor de peso 5kg existe uma área sensível responsável por detectar a carga. Dessa forma, será acoplada uma base ao sensor para fazer melhor detecção da carga na última bandeja. Mecanicamente o sensor é composto por uma ponte resistiva que tem a resistência alterada ao ter um peso aplicado sobre ele. Eletricamente, quando o sensor de peso entra em operação, ou seja, quando uma força Peso é aplicada, ele envia uma tensão ao microcontrolador e conforme o peso essa tensão será oscilada. No entanto, a tensão que o sensor envia é tão fraca que é necessário utilizar um amplificador de sinal para a comunicação com o microcontrolador, comunicação esta que não deve ser feita por meio de pinos digitais.
- O amplificador de sinal usado, então, será o Módulo Conversor Amplificador HX711 que converte as mudanças medidas em alteração do valor da resistência, através do circuito de conversão em potência elétrica.

#### Pinagem Magic Box:
<p align="center">
<img src="img/relatorio/pinosmagicbox.png" width="400">
</p>
<br> 

#### Esquemático célula de peso: 
<p align="center">
<img src="img/relatorio/céluladepeso.png" width="400">
</p>
<br> 


- MagicBox
  - Interface: Port1
  - Pinos: Gnd - Ground
  - 5V - Power
  - EIO16 - Interface geral I/O
  - EIO15 - Interface geral I/O
  - Level Output: 5V - 5V/1A
  - EIO16 - 3.3V_10m output
  - EIO15 - 3.3V_10m output
  - PWM: EIO16;
  - Level input: EIO16 - 3.3V_10mA input
  - EIO15 - 3.3V_10mA input
  - Padrão de resistência:
  - EIO16 - 3.3V com resistência de 51K
  - EIO15 - 3.3V com resistência de 51K

<p align="center">
<img src="img/relatorio/Magic%20box.png">
</p>
<br>



- Explicação das entradas:

  1. Portas de interface PWM para utilização dos sensores.

  2. interface de motor DC/ Motor de passo
  3. Saída 12V
  4. Botão retorno/resetar
  5. Botão de power
  6. Oled display
  7. Botão de controle superior
  8. Botão para confirmar ou deletar arquivos
  9. Botão de controle inferior  
  10. Porta de comunicação com Magician  
  11. Alimentação de 12V provinda do magician Lite
  12. Porta de comunicação para conectar com módulo joystick
  13. Interface para alimentação de energia.
  14. Entrada e saída de 12V
  15. Porta USB
  16. Porta tipo C


- Lista de materias: 
  
  1. Magician box
  2. Eletroímã 
  3. Módulo de peso e célula de peso.

# Planejamento e método de fabricação: 
- A fabricação da placa de uso será através de uma placa de circuito integrado genérica com os componentes soldados e os cabos de alimentação serão ligados em uma porta do Magic Box.

#### Descrição do Hardware

Para o projeto, serão utilizados alguns componentes eletrônicos que têm a finalidade de cumprir com o objetivo da automação do processo de separação magnética de minérios e entre esses temos o braço robótico Magician Lite, que é conectado com um controlador externo que será o Magic Box através da porta de interface de comunicação com o Magician Lite (item 10 na imagem do campo de projeto de dispositivos eletrônicos). Além desses componentes serão usados, também, um eletroímã que será conectado ao Magic Box pela saída de 12 Volts e um módulo de peso que acompanha uma célula de carga que será conectada também ao Magic Box.

O Magic Box atua como um microcontrolador capaz de rodar scripts que são iniciados e selecionados pela própria interface de display que ele possui, além disso ele também possui uma Ponte H integrado a ele que será utilizado para inverter o campo e desligar o eletroímã através de um comando efetuado no script. O Magician Lite é o braço robótico utilizado com estrutura física para realizar a separação de misturas efetuando o processo operacional dividido em 3 fases como proposto no TAPI, e assim o eletroímã é responsável por coletar o material ferromagnético, e com a ajuda do braço, depositá-lo no recipiente de amostra. Já o módulo de peso e a célula de carga serão utilizados como método de verificar o momento de encerrar o ciclo de separação de misturas através da checagem após o final da separação, em que haverá a verificação para saber se houve ou não alteração no peso da amostra. Assim, quando não houver mais alteração será indicado que não há mais conteúdo ferromagnético na amostra e o processo poderá ser encerrado.


### Requisitos de software

## Tecnologias Utilizadas

# UX e UI Design

## Wireframe + Storyboard

## Design de Interface

A conexão homem máquina da solução do grupo será realizada por meio do Magic Box, controle que faz parte do kit do Dobot Magician Lite, de modo que a interface se mantenha simples e prática, sem a necessidade de outros dispositivos ou acesso à internet para a visualização do status da aplicação. A entrada de dados será feita por meio de um script pré definido, esse que o usuário poderá carregar no Magic Box para iniciar a atuação do robô. Além disso, para ajuste da intensidade de corrente elétrica de acionamento do ímã, distância do braço do robô, assim como sua velocidade, somente será necessário o usuário carregar o script que melhor supra sua necessidade, tendo variações nesses três parâmetros.

Dessa forma, a arquitetura da solução foi idealizada com o intuito de dar maior praticidade ao operador, com a interface completa acoplada ao robô, tendo apenas o cabo de conexão como única distância entre eles. Somado a isso, o grupo decidiu usar o controle como forma de alimentação do(s) ímã(s), além de servir como controlador e alimentação da célula de carga, responsável por realizar o cálculo que conclui a varredura do robô.

- Forma de uso da interface de usuário:
  
  O controle Magic Box é ligado segurando o botão redondo no centro por um tempo. Após isso, as opções citadas abaixo aparecerão e, para selecioná-las, o usuário deve usar o botão com um círculo como forma de confirmação. Por outro lado, a seta presente no botão esquerdo serve como retorno, cancelando ou voltando a operação realizada ou até mesmo para reiniciar o Magic Box.

  Seleção do método de uso: Nessa parte do processo, o usário poderá decidir entre as opções de uso do Magic Box, a primeira para rodar o script, contida na imagem abaixo. Vale ressaltar que para usar o controle, o usário deve ter conhecimento da função dos botões do controlador.
  <p align="center">
  <img src="img/relatorio/selecao_script.jpeg" width="400px">
  </p>
  <br>

  Seleção de arquivos de script python(.py) em ambos os métodos de uso: Nessa parte do processo, o usuário poderá decidir entre os arquivos já carregados para o Magic Box. Dessa maneira, o grupo pensa em alterar os parâmetros em diferentes scripts para atender a todas as necessidades que o usuário possa ter.
Opção para carregar do zero script enviado ao controlador.

  <p align="center">
  <img src="img/relatorio/iniciar_ensaio.jpeg" width="400px">
  </p>
  <br>

  Já no método playback, o usuário apenas poderá escolher reexecutar o último arquivo de script executado.

  <p align="center">
  <img src="img/relatorio/selecao_novamente.jpeg" width="400px">
  </p>
  <br>


  Status da operação: Nessa etapa do processo, o usuário acompanha pelo display em qual etapa está o processo, recebendo feedback se algo está fora dos conformes. Além disso, vale ressaltar que ele poderá cancelar o processo a qualquer momento que quiser, bastando apertar o botão de voltar e confirmar o cancelamento.

  Primeira bandeja, na qual o braço com o ímã ligado recolhe materiais magnéticos que vêm acompanhados de materiais não magnéticos da amostra.

  <p align="center">
  <img src="img/relatorio/primeira_bandeja.jpeg" width="400px">
  </p>
  <br>

  Segunda bandeja, na qual o braço com o ímã ligado passa em uma bandeja só com água para limpar o excesso de materiais, visando a limpeza de tudo que não seja magnético.


  <p align="center">
  <img src="img/relatorio/segunda_bandeja.jpeg" width="400px">
  </p>
  <br>

  Terceira bandeja, na qual o braço quando se aproxima da bandeja com água, desliga o(s) ímã(s) a fim de soltar todo o material magnético na bandeja.

  <p align="center">
  <img src="img/relatorio/terceira_bandeja.jpeg" width="400px">
  </p>
  <br>


  Pronto, após a repetição dessa sequência algumas vezes, o ensaio é finalizado. Posteriormente, o grupo pensa em utilizar uma balança para ser a condição de parada do ensaio, terminando a operação quando a diferença entre duas varreduras completas for muito pequena.

  <p align="center">
  <img src="img/relatorio/ensaio_finalizado.jpeg" width="400px">
  </p>
  <br>


  <b>Nota: as especificações dos componentes acima, podem ser encontrado de forma detalha na seção de "Documentação dos componentes."</b>


# Projeto de Banco de Dados

## Modelo Conceitual

## Modelo Lógico

# Teste de Software

## Testes Unitários

### Sprint 2

#### Braço mecanico

Para a primeira versão do protótipo do braço robótico (Magician Lite), foi construído um código-fonte que permitisse a comunicação entre o braço robótico e um computador atraves do controle de seus eixos X, Y e Z por meio de um controle de Xbox. A escolha do controle de Xbox foi feita, inicialmente, pelo fato de ser o que chega ao mais próximo de nosso interface proposta, já que ambos se comunicarem por meio de um cabo a um receptor de entrada/saída (computador). Sendo assim, realizamos teste de movimentação ao qual notamos os seguintes problemas/ delimitações do Dobot Magician:

1. Limites máximo de movimentação:

- Ao atingirmos o limite máximo do braço robótico, nos ângulos -135° e 135°, o Dobot Magician acaba travando e sendo necessário realizar o desligamento e ligamento do braço robótico para voltar a utilizar novamente.

1. Movimentação forçada do braço robótico (batidas ou movimentações manuais):

- O mesmo travamento acontece quando está ocorrendo a execução de um determinado código-fonte no braço robótico, por algum evento acabe ocorrendo uma movimentação forçada (batida ou reajuste no braço robótico manualmente). Sendo assim, para a construção de códigos-fonte de execução de processos mais complexo há a necessidade de tratamento para estes possíveis acontecimentos.
<center>

[![Foo](img/relatorio/teste-robo.png)](https://drive.google.com/file/d/1z_-WjqqmEGV3r7EgLiq7NLJw4R8_bzBm/view?usp=sharing)

</center>

#### Eletroímã

Para fim de primeira versão do protótipo do eletroímã, realizamos por meio da ligação de um eletroímã a uma ponte H, por meio disto podemos testar três níveis inicias de intercidades do campo magnético passado energia manualmente pela fonte digital. Durante os teste, encontramos algumas possíveis delimitações dos componentes, aos quais pode afetar a construção do protótipo:

1. Delimitações do Eletroímã:

- Como o tamanho do eletroímã é relativamente pequeno, dado a quantidade de amostra que iremos processar e o objetivo de tornar este processo de execução fosse realizado de forma mais rápido. Notamos que apenas um eletroímã ligado a uma ponte H, não nos ajudaria, desta forma partimos do pressuposto de utilizar dois eletroímãs ligados a uma ponte h. Em consequência, o peso de nosso eletroímã por completo aumenta, nos fazendo pensar alternativas que no auxiliem diminuir o peso e também talvez da necessidade de dividirmos o processo de varredura da separação de amostras por quadrantes, já que devemos considerar o peso dos eletroímãs com o coletado da amostra.

2. Delimitações da Ponte H:

- Foi disponibilizado para nós a Ponte H L298n Driver Motor Dc ao qual tem a capacidade de aguentar té 2A e 30v, mas para o projeto e protótipo desenvolvido. A necessidade desse modelo tão poderoso talvez não seja necessário e sim alguma de potência mais baixa. Desta forma, seria possível reduzir consideravelmente o peso do protótipo do eletroímã produzido. Por exemplo, um modelo adequado seria o L9110S, que tem tensão máxima de 12v ( que é o que utilizamos ) e corrente de 800mah por motor, sendo que o imã tem consumo de corrente de até 250mah
<center>

[![Foo](img/relatorio/teste-eletroima.png)](https://drive.google.com/file/d/1Zvlc5oBxqtvwXt64XTNt2HBSVcuGdnnM/view?usp=share_link)

</center>

#### Módulo de peso

Também durante está sprint 2, realizamos a construção do módulo de peso que serviram como uma das peças principais do nosso protótipo, atuando como um mecanismo de forma de parada do processo de separação da amostra. Após a construção da primeira versão, realizamos testes para ver as possibilidades e possíveis delimitações (sendo encontrado mais delimitações para a ideia principal de uso do módulo):

1. Delimitações do módulo de peso:

- Durante a contrição, notamos a dificuldade de achar exemplos de construção do mesmo por meio da linguagem de programação Python. Apenas encontrado, exemplos de construções realizadas em C, por meio deste, notamos que talvez para a nossa solução, teremos que mudar a linguagem de programação, sendo adotada a linguagem C.

- Também, notamos que inicialmente, para pesos maiores, o modulo de peso conseguem capturar os valores, mas para valores menores não consegue capturar com tanta precisão (este processo de teste foi realizado com parafusos e porcas). Desta forma, não podemos distinguir se esta limitação ocorre devido ao módulo ou pelo código-fonte, necessitando realizar teste com a amostra disponibilizada recentemente.

<center>

[![Foo](img/relatorio/teste-modulo-peso.png)](https://drive.google.com/file/d/1Z5szDusptTmaxcjM55xNJIMFCwcP95F8/view?usp=share_link)

</center>

## Teste de Usabilidade

Como citado anteriormente, o modelo de interface escolhido para o protótipo desenvolvido pelo grupo foi o próprio Magic Box do Dobot, ao qual é fornecido pelo kit. Essa escolha foi feita pelo fato de ser um microcontrolador, ponte-H, ter uma interface intuitiva e amigável, além de ter uma comunicação rápida e direta por meio de dois cabos: um de alimentação e outro de comunicação com o braço robótico. 

O Magic Box já possui uma interface em inglês, totalmente criada para facilitar o processo de utilização. Entretanto, o Magic Box não permite a customização de sua interface, pois ainda não foi disponibilizado para open source. Além disso, são identificados apenas arquivos .py, mesmo que uma pasta seja criada em um dos seus menus: Scripts ou Playback, no que lhe concerne, não serão exibidos no display.

Sendo assim, durante essa sprint, decidimos criar códigos em arquivos .py, aos quais foram nomeados de acordo com suas funcionalidades, para que assim fosse possível que os usuários identificassem de maneira rápida, sendo acrescentado uma numeração na frente, como mostra a imagem abaixo:


 <p align="center">
  <img src="img/relatorio/iniciar_ensaio.jpeg" width="400px">
  </p>
  <br>

   <p align="center">
  <img src="img/relatorio/reiniciar-ensaio.jpg" width="400px">
  </p>
  <br>

Sendo assim, os próprios arquivos salvos no Magic Box serviram como um menu, aos quais os usuários poderão utilizar e navegar entre eles. Além de possibilitar que ao longo do desenvolvimento do protótipo e posteriormente, seja possível alterar e customizar de forma mais rápida e fácil. Após essa construção, foi realizado alguns testes com usuários, obtendo os seguintes resultados:

- Positivos: O menu funciona conforme o pensado, além de ter uma interface mais limpa. Também é intuitivo para aqueles que não utilizaram a solução anteriormente.

- Negativos: O botão de OK, sinalizado em um formato esférico (localizado à direita do teclado), não apresenta um formato intuitivo em relação à sua função. Adicionalmente,  em algumas situações, é necessário pressionar os botões com força para realizar a ação desejada, já que o teclado apresenta baixa sensibilidade.

Embora alguns resultados negativos, foi possível validar a ideia principal do que foi desenvolvido, além de ter algumas percepções do que talvez possa ser melhorado.

# Análise de Dados

# Manuais

## Manual de Implantação

## Manual do Usuário

## Manual do Administrador

# Referências
