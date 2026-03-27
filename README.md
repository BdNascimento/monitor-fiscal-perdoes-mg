# monitor-fiscal-perdoes-mg
Plataforma de Auditoria Analítica e Eficiência Fiscal (2017-2026) - Modern Data Stack

Documento de Especificação Funcional (DEF)
Projeto: Monitor de Eficiência Fiscal e Transparência – Perdões/MG

Versão: 2.0
Data: Março/2026
Responsável: Bruno Pereira – Data Engineer

1. Apresentação do Projeto

O projeto Monitor de Eficiência Fiscal e Transparência – Perdões/MG tem como finalidade construir uma plataforma de análise de dados públicos capaz de consolidar, padronizar e interpretar informações fiscais e orçamentárias do município de Perdões, Minas Gerais, no período de 2017 a 2026.

A proposta é transformar relatórios públicos dispersos e de difícil leitura em uma base analítica estruturada, auditável e de fácil interpretação, permitindo acompanhar a evolução fiscal do município, verificar conformidade com limites legais e comparar o perfil de alocação de recursos entre diferentes períodos administrativos.

O projeto terá caráter técnico, apartidário, transparente e reprodutível, com foco em indicadores objetivos e rastreáveis.

2. Objetivo Geral

Desenvolver uma plataforma de monitoramento fiscal e execução orçamentária baseada em dados públicos, capaz de analisar a evolução histórica da gestão municipal de Perdões/MG, com foco em:

conformidade com exigências legais e constitucionais;
capacidade de investimento do município;
dependência de transferências externas;
evolução da arrecadação própria;
perfil de composição dos gastos públicos;
geração de informação acessível para cidadãos, analistas e portfólio técnico.

3. Objetivos Específicos

Consolidar dados fiscais municipais oriundos de diferentes fontes públicas.
Estruturar uma base histórica padronizada entre 2017 e 2026.
Automatizar o cálculo de indicadores fiscais e constitucionais.
Permitir comparações entre mandatos e exercícios financeiros.
Fornecer painéis e relatórios com memória de cálculo clara.
Garantir rastreabilidade entre dado bruto, transformação e indicador final.
Criar um ativo técnico de portfólio com alto valor demonstrativo em engenharia de dados.

4. Contexto e Justificativa

As informações fiscais dos municípios brasileiros, apesar de públicas, normalmente se encontram distribuídas em portais, relatórios PDF e bases governamentais distintas, muitas vezes com nomenclaturas inconsistentes e baixa usabilidade para o cidadão comum.

Esse cenário dificulta análises históricas, comparações entre períodos administrativos e acompanhamento do cumprimento de limites legais relevantes, como os previstos na Lei de Responsabilidade Fiscal (LRF) e nas regras constitucionais de aplicação mínima em saúde e educação.

O projeto busca atacar esse problema ao criar uma camada analítica confiável que permita leitura técnica e pública da realidade fiscal do município de Perdões/MG.

Valor gerado para o portfólio técnico

O projeto demonstrará, de forma prática:

extração e tratamento de dados públicos não estruturados;
ingestão de PDFs, páginas web e APIs;
modelagem analítica em camadas Bronze, Silver e Gold;
uso de BigQuery, dbt Core e GCP;
governança, documentação e linhagem de dados;
construção de produtos analíticos de interesse público.
Valor gerado para a comunidade
ampliação da transparência pública;
facilitação do entendimento dos relatórios fiscais;
apoio a análises técnicas apartidárias;
incentivo ao controle social baseado em evidências.

5. Escopo do Projeto

5.1 Escopo incluído

O projeto contemplará:

coleta de dados fiscais e orçamentários públicos do município de Perdões/MG;
consolidação histórica do período de 2017 a 2026;
extração de relatórios RREO e RGF;
coleta de dados complementares do IBGE;
validação cruzada com dados do Siconfi/Tesouro Nacional;
cálculo de indicadores fiscais e constitucionais;
produção de dashboards comparativos e relatórios técnicos;
documentação metodológica e repositório versionado.

5.2 Escopo não incluído nesta fase

Não fazem parte do escopo inicial:

avaliação político-partidária;
análise subjetiva de qualidade de governo;
inferências causais complexas sobre desempenho da gestão;
benchmarking amplo com todos os municípios do estado;
previsões econométricas avançadas;
publicação oficial institucional vinculada ao poder público.

6. Pergunta Central de Negócio

A partir de dados públicos oficiais, o projeto deve responder, de forma objetiva:

Como evoluiu a estrutura fiscal, o cumprimento de limites legais e a capacidade de investimento do município de Perdões/MG entre 2017 e 2026, e quais padrões de alocação de recursos caracterizam cada período administrativo?

7. Fontes de Dados

7.1 Portal da Transparência de Perdões/MG

Fonte primária municipal para obtenção de relatórios oficiais, especialmente:

RREO – Relatório Resumido da Execução Orçamentária;
RGF – Relatório de Gestão Fiscal;
relatórios complementares eventualmente disponibilizados no portal.

Possíveis formatos:

PDF;
HTML;
planilhas;
documentos digitalizados.

Uso no projeto:

base principal para apuração municipal;
identificação de receitas, despesas, aplicação mínima e limites fiscais.

7.2 Siconfi / Tesouro Nacional

Fonte complementar federal para validação e reconciliação de dados fiscais.

Uso no projeto:

validação cruzada de indicadores;
conferência de valores consolidados;
apoio à padronização de nomenclaturas.

7.3 API do IBGE

Fonte de dados contextuais e demográficos.

Uso no projeto:

população estimada por ano;
dados econômicos complementares, como PIB municipal;
normalização de indicadores per capita.

7.4 Fontes complementares futuras

Podem ser consideradas em fases posteriores:

bases do TCE/MG;
dados de convênios e transferências específicas;
bases abertas estaduais ou federais adicionais.

8. Premissas do Projeto

Para garantir consistência metodológica, o projeto adotará as seguintes premissas:

os dados analisados serão exclusivamente oriundos de fontes públicas;
toda métrica final deverá possuir memória de cálculo documentada;
sempre que possível, os indicadores serão validados em mais de uma fonte;
valores monetários poderão ser apresentados em termos nominais e reais;
comparações entre anos e mandatos devem considerar contexto temporal e dados incompletos;
o projeto terá postura técnica, sem atribuição de juízo político.

9. Eixos Analíticos

A análise será estruturada em quatro eixos principais.

9.1 Conformidade Fiscal e Legal

Avaliará o cumprimento de limites previstos em lei e na Constituição, incluindo:

despesa total com pessoal em relação à Receita Corrente Líquida;
aplicação mínima em saúde;
aplicação mínima em educação;
consistência entre demonstrativos publicados.

9.2 Capacidade de Investimento

Avaliará o quanto o município converte receita em expansão de ativos, infraestrutura e melhorias permanentes, considerando:

despesas de capital;
investimento em relação à Receita Corrente Líquida;
investimento em relação à despesa total;
investimento per capita.

9.3 Autonomia e Dependência Fiscal

Avaliará o nível de dependência do município em relação a transferências intergovernamentais e sua capacidade de arrecadação própria, considerando:

arrecadação própria em relação à receita total;
arrecadação de IPTU e ISS;
participação do FPM e demais repasses;
dependência de transferências correntes.

9.4 Perfil de Alocação de Recursos

Avaliará a composição do gasto público para identificar o perfil administrativo de cada período, incluindo:

peso de pessoal;
peso de custeio;
peso de investimento;
distribuição funcional das despesas;
composição relativa por áreas prioritárias.

Esse eixo servirá de base para caracterizar o chamado “DNA fiscal/administrativo” de cada gestão, entendido como o padrão objetivo de alocação orçamentária ao longo do tempo.


10. Indicadores e KPIs

O sistema deverá calcular e exibir, no mínimo, os seguintes indicadores.

10.1 Indicadores fiscais principais

Receita Corrente Líquida (RCL)
Receita total arrecadada
Despesa total executada
Resultado orçamentário
Despesa com pessoal
Despesa com pessoal / RCL

10.2 Indicadores constitucionais

Aplicação em saúde (%)
Aplicação em educação (%)
Alerta de descumprimento do mínimo constitucional

10.3 Indicadores de investimento

Despesa de capital
Índice de Investimento Real = Despesas de Capital / RCL
Investimento per capita
Investimento / despesa total

10.4 Indicadores de autonomia fiscal

Arrecadação própria / receita total
IPTU / receita total
ISS / receita total
IPTU + ISS / receita corrente
FPM / receita total
Transferências correntes / receita total

10.5 Indicadores comparativos

variação anual da arrecadação própria;
variação anual dos repasses;
crescimento percentual por mandato;
comparação entre períodos administrativos;
variação nominal e variação real.

11. Regras de Negócio

O sistema deverá obedecer às seguintes regras funcionais:

Os dados deverão ser carregados com identificação clara de:
fonte;
período de referência;
tipo de relatório;
data de coleta.
Toda métrica calculada deverá possuir:
fórmula definida;
tabela de origem;
período de referência;
rastreabilidade até o dado bruto.
Quando houver divergência entre fontes:
o sistema deverá registrar a inconsistência;
priorizar a fonte definida como principal;
manter evidência para auditoria posterior.
Os indicadores monetários deverão, sempre que viável, ser apresentados em:
valor nominal;
valor corrigido por inflação;
valor per capita.
O sistema deverá sinalizar automaticamente:
gasto com pessoal acima do limite legal;
saúde abaixo do mínimo constitucional;
educação abaixo do mínimo constitucional.
A comparação entre gestões deve utilizar períodos claramente delimitados, evitando inferências fora da janela temporal disponível.

12. Regras de Comparabilidade

Para garantir comparações tecnicamente válidas, o projeto adotará:

padronização de nomenclaturas fiscais ao longo da série histórica;
marcação explícita de anos com dados incompletos;
separação entre valores nominais e valores reais;
uso de população estimada do IBGE para normalização per capita;
documentação de eventuais mudanças metodológicas entre anos.

13. Qualidade, Auditoria e Governança de Dados

O projeto deverá contemplar uma camada mínima de governança analítica, incluindo:

armazenamento do arquivo bruto original;
registro da URL de origem;
data e hora da coleta;
hash do arquivo quando aplicável;
versionamento de evidências brutas;
testes de completude e consistência;
controle de duplicidade;
documentação dos modelos;
linhagem Bronze → Silver → Gold;
memória de cálculo dos indicadores.
Níveis de confiança dos dados

Os indicadores poderão receber classificação de confiabilidade:

Alta confiança: confirmado em fonte primária e validado com fonte secundária;
Média confiança: disponível em uma única fonte consistente;
Baixa confiança: extraído com necessidade de OCR ou com inconsistência detectada.

14. Arquitetura Técnica

A solução será estruturada em camadas analíticas.

14.1 Camada de Ingestão

desenvolvimento em Python;
crawler/scraper para coleta de relatórios e arquivos públicos;
armazenamento inicial em Google Cloud Storage (GCS).

14.2 Camada Bronze
arquivos brutos preservados;
tabelas com dados extraídos sem grande transformação;
armazenamento da evidência original para auditoria.

14.3 Camada Silver

limpeza, padronização e estruturação dos dados;
consolidação temporal;
harmonização de campos fiscais;
deduplicação e tratamento de inconsistências.

14.4 Camada Gold

geração de indicadores finais;
tabelas analíticas por ano, mandato e eixo temático;
views consumíveis por dashboard e relatório.

14.5 Tecnologias previstas

Python para ingestão e parsing;
Google Cloud Storage para armazenamento bruto;
BigQuery para processamento analítico;
dbt Core para transformação, testes e documentação;
GitHub Actions para CI/CD;
Evidence.dev para publicação de relatórios e dashboards estáticos.

15. Produto Final Esperado

O projeto deverá gerar os seguintes artefatos.

15.1 Dashboard Comparativo

Painel analítico com visão comparativa entre períodos administrativos, incluindo:

visão por mandato;
visão por ano;
alertas de conformidade;
indicadores fiscais principais;
métricas per capita e percentuais;
comparações históricas.

15.2 Relatório Técnico de Auditoria Analítica

Documento em Markdown ou formato publicado contendo:

metodologia;
descrição das fontes;
memória de cálculo;
principais achados;
inconsistências encontradas;
limitações do projeto.

15.3 Repositório GitHub

Repositório modular, documentado e reprodutível, com:

código de ingestão;
modelos dbt;
documentação;
estrutura de pastas padronizada;
instruções de execução.

15.4 Glossário Cidadão

Material explicativo simplificado com definição de termos como:

RCL;
despesa com pessoal;
mínimo constitucional;
investimento per capita;
arrecadação própria;
transferências.

16. Critérios de Sucesso

O projeto será considerado bem-sucedido se atender aos seguintes critérios:

consolidar o histórico fiscal previsto no escopo;
automatizar a carga e transformação dos dados principais;
gerar KPIs documentados e rastreáveis;
disponibilizar painel comparativo funcional;
validar indicadores relevantes com pelo menos uma fonte complementar;
manter documentação técnica suficiente para reprodutibilidade;
apresentar narrativa técnica clara, compreensível e auditável.

17. Riscos e Limitações

Os principais riscos previstos são:

indisponibilidade de relatórios históricos em algumas janelas;
mudanças de layout nos PDFs e páginas do portal;
baixa qualidade de documentos digitalizados;
divergência entre bases municipais e federais;
ausência de granularidade em determinados anos;
necessidade de OCR em arquivos antigos;
alteração de nomenclaturas contábeis ao longo do período.

Esses riscos deverão ser documentados e tratados sempre que possível por regras de validação, logs e classificação de confiança.

18. Roadmap Proposto

Fase 1 – MVP
levantamento das fontes;
coleta inicial dos relatórios;
ingestão dos dados do IBGE;
construção da camada Bronze;
definição dos primeiros KPIs.
Fase 2 – Modelagem Analítica
estruturação Silver e Gold;
padronização histórica;
criação dos indicadores fiscais e legais;
validação cruzada com Siconfi.
Fase 3 – Produto Analítico
construção do dashboard;
elaboração do relatório técnico;
documentação da memória de cálculo;
publicação do repositório.
Fase 4 – Evolução
correção inflacionária;
expansão para comparativos regionais;
inclusão de novas fontes;
possível replicação da arquitetura para outros municípios.

19. Considerações Finais

O projeto Monitor de Eficiência Fiscal e Transparência – Perdões/MG possui potencial para se tornar ao mesmo tempo:

um produto de alto valor para portfólio técnico em engenharia de dados;
uma prova prática de capacidade de modelagem analítica em dados públicos;
uma iniciativa de transparência baseada em evidências;
uma base reutilizável para monitoramento fiscal de outros municípios.

Sua força está na combinação entre engenharia de dados, governança, análise fiscal e impacto público, com uma abordagem técnica, neutra e auditável.
