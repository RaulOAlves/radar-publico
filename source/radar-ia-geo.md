# Radar IA, GeoIA e Setores

> Base relacional de notícias para projetos. Atualizado: 2026-11-26 10:36 (BRT).

## Critério de sinal

- Prioridade: anúncio oficial, release, mudança de API/produto, paper primário, vulnerabilidade, ciclo de vida ou caso de uso operacional.
- Janela padrão: últimas 24 h. Sem item de alto sinal, registrar `sem_novidade` e não preencher com notícia genérica.
- Relevância: primeiro `ArcGIS`, automação geoespacial, agentes, Claude Code e Codex; depois impacto nos setores-alvo.

## Registros

### 2026-11-26 10:36 BRT — AWS Lambda passa a orquestrar MicroVMs em fluxos duráveis

- Fonte: [AWS — Lambda durable functions e MicroVMs](https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-microvm/)
- Publicado: 2026-11-25 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A AWS lançou em *developer preview* uma extensão que permite a Lambda durable functions executar tarefas em Lambda MicroVMs e gerenciar seu ciclo de vida. O fluxo pode manter checkpoints, tentar novamente tarefas que falharam e orquestrar múltiplas MicroVMs em paralelo; sessões de MicroVM compartilham arquivos e memória entre tarefas. A proposta cobre, entre outros usos, código não confiável ou gerado por agentes em ambientes isolados. Há SDKs de prévia para TypeScript e Python. A AWS alerta que o recurso ainda pode mudar e não deve ser usado em produção.
- Por que importa: Oferece arquitetura experimental para executar código de agentes com isolamento de VM e retomada de trabalhos longos. Antes de adoção operacional, esperar maturidade e validar custos, limites e controles de segurança.
- Tags: #aws #lambda #microvm #agentes-ia #sandbox #orquestracao #developer-preview
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-26 10:36 BRT — BigQuery habilita conexões analíticas multicloud em todas as regiões

- Fonte: [Google Cloud — release notes do BigQuery](https://docs.cloud.google.com/bigquery/docs/release-notes#november_25_2026)
- Publicado: 2026-11-25 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: O Google Cloud disponibilizou, em caráter geral, conexões *cross-cloud* para consultar dados de AWS, Azure e Salesforce Data 360 a partir de todas as regiões do BigQuery. A nota informa que essas conexões oferecem mais recursos que as conexões padrão baseadas em BigQuery Omni, mas não detalha nessa entrada os custos nem o desempenho de cada origem.
- Por que importa: Pode simplificar análises que cruzam dados operacionais e geoespaciais distribuídos entre nuvens. Ganho real depende de arquitetura, controles de acesso, transferência de dados e custo de consulta.
- Tags: #google-cloud #bigquery #multicloud #aws #azure #integracao-de-dados #ga
- Relações: [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-26 10:36 BRT — BigQuery Storage API v1beta1 tem data de desligamento

- Fonte: [Google Cloud — ciclo de vida da BigQuery Storage API](https://docs.cloud.google.com/bigquery/docs/release-notes#november_25_2026)
- Publicado: 2026-11-25 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A API `v1beta1` do BigQuery Storage foi depreciada e será desligada em 31 de agosto de 2027; chamadas ao endpoint antigo passarão a retornar `NOT_FOUND`. Desde 20 de novembro de 2026, o acesso já está restrito a projetos com uso registrado no período indicado pela nota. O Google orienta migrar para a API `v1`, compatível com a `v1beta1`, e atualizar conectores, SDKs ou chamadas gRPC diretas que ainda apontem para a versão beta.
- Por que importa: Pipelines de extração e integração que fixaram `v1beta1` podem falhar no prazo de desligamento. Convém inventariar dependências e testar a migração sem presumir que todos os clientes já usam `v1`.
- Tags: #google-cloud #bigquery #storage-api #api #migracao #ciclo-de-vida #pipeline-de-dados
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-11-26 10:36 BRT — Google Managed Airflow adiciona verificação de upgrade por agente

- Fonte: [Google Cloud — release notes do Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/release-notes#november_26_2026)
- Publicado: 2026-11-26 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: O Google Cloud disponibilizou no console uma verificação de upgrade conduzida pelo Managed Airflow Agent. Antes de selecionar nova versão de build ou imagem do ambiente, a ferramenta analisa quais mudanças as DAGs exigem para funcionar com a versão escolhida. A nota de lançamento não afirma que o agente aplica as alterações automaticamente nem que elimina a necessidade de testes de execução.
- Por que importa: Pode antecipar incompatibilidades em pipelines orquestrados por Airflow e reduzir risco de atualização. Relevância para projetos depende de usarem Managed Airflow no Google Cloud.
- Tags: #google-cloud #managed-airflow #agentes-ia #dags #upgrade #automacao #release
- Relações: [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-11-25 07:31 BRT — Google disponibiliza MCP do Workspace e define migração de agentes

- Fonte: [Google Cloud — interfaces e controles para agentes no Workspace](https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise)
- Publicado: 2026-11-24 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: O Google anunciou disponibilidade geral de servidores MCP remotos para Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat e Tasks, além do Workspace CLI para agentes locais e automações. Também apresentou o Cloud Agent Gateway para tráfego LLM, MCP e A2A, com verificação de identidades e políticas IAM. O adendo de ferramentas de IA do Workspace exige que agentes usem os servidores MCP ou o CLI, em vez das APIs REST tradicionais; a aplicação técnica começa em 1º de fevereiro de 2027. Agentes precisarão de IDs OAuth dedicados; a cobrança por cotas anunciadas começa em 1º de abril de 2027. Alguns controles adicionais, como aprovações temporárias e restrições ampliadas de acesso a dados, ainda são futuros.
- Por que importa: Integrações de agentes com arquivos, e-mail ou planilhas do Workspace precisam revisar interface, identidade, permissões e custos antes do prazo. A exigência não implica migração de aplicações tradicionais que usam REST sem atuar como agentes.
- Tags: #google-workspace #google-cloud #mcp #agentes-ia #oauth #governanca #api #ciclo-de-vida
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-25 07:31 BRT — Claude Code 2.1.332 aceita skills MCP e reforça controle de shell

- Fonte: [Anthropic — release Claude Code v2.1.332](https://github.com/anthropics/claude-code/releases/tag/v2.1.332)
- Publicado: 2026-11-25 01:32, conforme página do GitHub (fuso não exibido; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A versão adiciona, em beta, skills servidas por servidores MCP, identificadas como `server:skill` no menu de comandos. O novo evento de hook `PreSkillShellCommand` pode recusar comandos shell embutidos em uma skill ou comando durante seu carregamento. A release também corrige casos de servidores MCP por SSE que travavam após interrupção e reconexão do fluxo de eventos, além de congelamento quando um servidor local produzia saída excessiva.
- Por que importa: Amplia distribuição de capacidades de agentes por MCP, mas aumenta a importância de revisar permissões e comandos de skills remotas. As correções reduzem falhas em integrações persistentes.
- Tags: #anthropic #claude-code #mcp #skills #hooks #seguranca #agentes-ia #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-25 07:31 BRT — ArcGIS Pro 3.8 acessa Databricks SQL Warehouse diretamente

- Fonte: [Esri — suporte a Databricks SQL Warehouse no ArcGIS Pro 3.8](https://www.esri.com/arcgis-blog/products/arcgis-pro/announcements/introducing-databricks-sql-warehouse-support-in-arcgis-pro-3-8)
- Publicado: 2026-11-24 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada). A versão 3.8 do ArcGIS Pro foi lançada anteriormente.
- Resumo: A Esri detalhou a conexão direta do ArcGIS Pro 3.8 a Databricks SQL Warehouse para dados espaciais e não espaciais. O fluxo requer driver ODBC de 64 bits e aceita OAuth de usuário ou de serviço. Permite criar camadas de consulta, trabalhar com visões materializadas e usar agregação espacial de pontos (*feature binning*) sem copiar previamente os dados para outro banco. Cada conexão aponta a um catálogo e esquema por vez. O suporte equivalente no ArcGIS Enterprise é plano para 2027, não capacidade atual.
- Por que importa: Pode reduzir cópias e latência entre lakehouse e análise GIS em projetos com grandes volumes de dados. Desempenho, permissões e custo de consultas precisam ser medidos no ambiente real.
- Tags: #esri #arcgis-pro #databricks #lakehouse #sql-warehouse #feature-binning #integracao-de-dados
- Relações: [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-11-25 07:31 BRT — ArcGIS Server 12.1 recebe correções para serviços de mapa e feição

- Fonte: [Esri — Map, Feature and Print Service Patch para ArcGIS Server 12.1](https://support.esri.com/en-us/patches-updates/2026/arcgis-server-12-1-map-feature-and-print-service-patch)
- Publicado: 2026-11-24 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A Esri publicou um patch para ArcGIS Server 12.1 que corrige operações de serviços de mapa, feição e impressão. Entre os defeitos listados estão falhas de edição com anotações, resultados incorretos em consultas espaciais e crescimento contínuo de memória em processos ArcSOC durante solicitações `Identify` a serviços com mosaicos. A instalação interrompe e reinicia o serviço ArcGIS Server; a Esri recomenda plano de reversão e aplicação em todos os nós pertinentes.
- Por que importa: Ambientes que dependem de serviços de feições ou mosaicos devem avaliar o patch para reduzir erros e consumo de memória. Testar em homologação antes de interromper produção.
- Tags: #esri #arcgis-server #arcgis-enterprise #patch #feature-service #mosaic-dataset #confiabilidade
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-11-25 07:31 BRT — ArcGIS Pro 3.8 protege edição de arquivos GIS no OneDrive

- Fonte: [Esri — acesso protegido a arquivos OneDrive no ArcGIS Pro](https://www.esri.com/arcgis-blog/products/arcgis-pro/sharing-collaboration/protect-your-onedrive-files-in-arcgis-pro)
- Publicado: 2026-11-24 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada). A versão 3.8 do ArcGIS Pro foi lançada anteriormente.
- Resumo: O ArcGIS Pro 3.8 adiciona check-out e check-in de acesso exclusivo para arquivos GIS em OneDrive e atalhos do SharePoint, incluindo projetos `.aprx`, geodatabases `.gdb`, toolboxes, shapefiles e rasters suportados. Outros usuários abrem o arquivo em modo somente leitura enquanto ele estiver reservado. O administrador precisa habilitar o recurso e todos os computadores que compartilham os dados devem usar Pro 3.8 ou posterior com a proteção ativada; edições fora desse ambiente não são protegidas.
- Por que importa: Reduz risco de conflitos e corrupção em equipes que armazenam projetos GIS no OneDrive. Não substitui colaboração multiusuário nem dispensa política de sincronização e versão.
- Tags: #esri #arcgis-pro #onedrive #sharepoint #geodatabase #colaboracao #integridade-de-dados
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-11-25 07:31 BRT — AWS CloudFormation adiciona recursos de infraestrutura de agentes

- Fonte: [AWS — expansão de cobertura do CloudFormation e Cloud Control API](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-coverage-expansion/)
- Publicado: 2026-11-24 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A AWS anunciou suporte a 206 novos tipos de recurso em 88 serviços no CloudFormation, entre eles Amazon Bedrock AgentCore PolicyEngine e Amazon SageMaker Hub. A Cloud Control API passa a suportar esses novos tipos e mais 224 tipos somente leitura em 99 serviços. A disponibilidade acompanha as regiões dos serviços subjacentes; o comunicado não detalha mudanças de preço.
- Por que importa: Amplia a possibilidade de provisionar e auditar componentes de agentes por infraestrutura como código, em vez de configurar manualmente cada recurso. Relevância prática depende dos serviços AWS usados por cada projeto.
- Tags: #aws #cloudformation #cloud-control-api #bedrock-agentcore #agentes-ia #infraestrutura-como-codigo #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-25 07:31 BRT — INPE tornará autenticação obrigatória no Brazil Data Cube

- Fonte: [INPE — Autenticação BIG/BDC](https://data.inpe.br/autenticacao-big-bdc/)
- Publicado: 2026-11-24 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: O INPE disponibilizou autenticação para acesso aos dados da plataforma Brazil Data Cube no novo portal de dados geoespaciais BIG. Códigos, scripts e aplicações que hoje acessam os dados sem credenciais precisarão ser adaptados. O acesso anônimo continua permitido durante a transição até 4 de janeiro de 2027; depois, a autenticação será obrigatória. A documentação oficial descreve a geração e o uso das credenciais. O portal e seus serviços web ainda são apresentados como experimentais.
- Por que importa: Pipelines automatizados de imagens e cubos de dados do INPE podem parar após o prazo se não incorporarem credenciais. Convém inventariar integrações, testar autenticação e proteger segredos; relação com projetos depende de uso efetivo do Brazil Data Cube.
- Tags: #inpe #brazil-data-cube #big #autenticacao #api #sensoriamento-remoto #automacao #ciclo-de-vida
- Relações: [[NAVIS / GeoFramework]], [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]]
- Confiança: alta

### 2026-11-24 07:31 BRT — Codex CLI 0.172.0 inicia MCP sob demanda e refina aprovações

- Fonte: [OpenAI — release Codex CLI 0.172.0](https://github.com/openai/codex/releases/tag/rust-v0.172.0)
- Publicado: 2026-11-24 00:03, conforme página do GitHub (fuso não exibido; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A versão passa a iniciar servidores MCP `stdio` opcionais, com listas de ferramentas em cache, na primeira chamada de ferramenta. Também permite definir um revisor de aprovação para cada ferramenta de aplicativo conectado em `config.toml`. A correção de `codex exec resume` restaura as permissões de sandbox, o diretório de trabalho e as raízes do workspace salvos, salvo substituição explícita.
- Por que importa: Reduz inicializações desnecessárias de integrações MCP e permite controles de aprovação mais específicos. A correção de retomada ajuda a evitar que automações continuem com contexto de execução diferente do esperado.
- Tags: #openai #codex #mcp #agentes-ia #aprovacao #sandbox #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-24 07:31 BRT — Claude Code 2.1.331 amplia Code Mode e corrige travamento MCP

- Fonte: [Anthropic — release Claude Code v2.1.331](https://github.com/anthropics/claude-code/releases/tag/v2.1.331)
- Publicado: 2026-11-23 21:34, conforme página do GitHub (fuso não exibido; inclusão na janela exata de 24 horas não confirmada).
- Resumo: O Claude Code adiciona Code Mode em sessões de terminal com Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry e Claude Platform on AWS. Seus rastros OpenTelemetry passam a incluir atributos de uso de tokens, modelo e operação. A versão corrige chamadas de ferramentas MCP que podiam ficar pendentes por até 30 minutos após respostas malformadas de servidores locais ou WebSocket.
- Por que importa: Expande opções de execução em nuvem e melhora observabilidade e confiabilidade de agentes que dependem de MCP. A aplicação a projetos concretos depende da infraestrutura adotada.
- Tags: #anthropic #claude-code #mcp #code-mode #opentelemetry #agentes-ia #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-24 07:31 BRT — ArcGIS Pro 3.8 migra esquema de datasets em geodatabase SQL Server

- Fonte: [Esri — ferramenta Change Dataset Schema no ArcGIS Pro 3.8](https://www.esri.com/arcgis-blog/products/arcgis-pro/announcements/introducing-the-change-dataset-schema-tool-in-arcgis-pro-3-8)
- Publicado: 2026-11-23 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada). A versão 3.8 do ArcGIS Pro foi lançada anteriormente.
- Resumo: A Esri detalhou a ferramenta `Change Dataset Schema`, que permite a um administrador mover tabelas, classes de feição e feature datasets registrados em geodatabases corporativas SQL Server para outro esquema. Ela atualiza os metadados da geodatabase e preserva, por exemplo, o histórico de arquivamento da tabela. A operação exige permissões adequadas no banco; serviços, consultas SQL, scripts e outros consumidores que referenciem o dataset podem precisar de ajustes, e o novo proprietário deve conceder novamente as permissões necessárias.
- Por que importa: Ajuda a transferir responsabilidade por bases GIS sem copiar e recriar datasets, preservando histórico relevante para auditoria. Antes de usar, é preciso mapear dependências e testar a migração.
- Tags: #esri #arcgis-pro #geodatabase #sql-server #esquema #governanca-de-dados #release
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-11-24 07:31 BRT — AWS lança descoberta e proteção de APIs, MCP e endpoints de IA

- Fonte: [AWS — lançamento de API Portal, API Security e AI Security](https://aws.amazon.com/blogs/security/introducing-api-and-ai-security-on-aws-from-discovery-to-protection/)
- Publicado: 2026-11-23 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A AWS anunciou disponibilidade geral do API Portal no Amazon API Gateway e de dois grupos de regras gerenciadas no AWS WAF: API Security e AI Security. O portal inventaria APIs e endpoints de inferência, MCP e A2A a partir de configurações e tráfego em CloudFront, Application Load Balancer e API Gateway. As regras de WAF cobrem abusos de API, validam solicitações MCP/A2A conforme protocolo e podem verificar prompts e respostas por meio de Bedrock Guardrails; precisam ser associadas aos recursos protegidos via web ACL.
- Por que importa: Dá visibilidade a servidores MCP e APIs expostos fora dos inventários formais e oferece controles na borda. Não substitui autenticação, autorização nem testes de segurança da aplicação.
- Tags: #aws #api-gateway #waf #mcp #a2a #agentes-ia #seguranca #lancamento
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-24 07:31 BRT — Google Navigation Connect passa a receber viagens do Maps no iOS

- Fonte: [Google Maps Platform — release notes do Navigation Connect](https://developers.google.com/maps/documentation/navigation/connect/release-notes)
- Publicado: 2026-11-23 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A API Navigation Connect, ainda em preview, passou a aceitar viagens iniciadas no Google Maps para iOS, além de Waze, enviando dados de viagem em tempo real ao backend. O motorista precisa da versão 26.45 ou posterior do Maps; o mesmo URL de lançamento usado no Android pode ser aberto como Universal Link. No iOS, os relatos de rota restante e desvio de rota ainda não estão disponíveis.
- Por que importa: Pode simplificar integração de localização e ETA de frota com aplicativos de navegação já usados pelos motoristas. É preciso avaliar lacunas de telemetria no iOS antes de depender dessa API para operação logística.
- Tags: #google-maps #navigation-connect #ios #api #logistica #frotas #preview
- Relações: [[Suzano — Rotas e logística]]
- Confiança: alta

### 2026-11-24 07:31 BRT — Planet trocará MODIS por VIIRS na reflectância de superfície

- Fonte: [Planet — continuidade dos produtos Surface Reflectance](https://support.planet.com/hc/en-us/articles/40893230900253-Ensuring-Long-Term-Data-Continuity-for-Planet-s-Surface-Reflectance-Products)
- Publicado: 2026-11-23 22:35 (fuso não informado na página; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A Planet anunciou que, em 30 de novembro, passará a usar dados VIIRS no lugar de MODIS como entrada da correção atmosférica dos produtos de reflectância de superfície de PlanetScope, SkySat e Pelican. Novos GeoTIFFs indicarão a origem dos parâmetros atmosféricos nos campos `aot_source`, `water_vapor_source` e `ozone_source`, com valores `viirs` ou `viirs_nrt`. A empresa não planeja reprocessar o histórico produzido com MODIS.

  A Planet espera manter a latência de entrega, mas alerta que, em alguns casos, a diferença de horário entre passagens VIIRS e imagens PlanetScope pode causar pequena alteração ou escurecimento artificial dos valores de reflectância.
- Por que importa: Séries de vegetação, vigor e desmatamento que misturam cenas anteriores e posteriores à mudança devem registrar a origem da correção e validar limiares e tendências. O impacto em projetos específicos depende do uso desses produtos Planet.
- Tags: #planet #viirs #modis #reflectancia-de-superficie #correcao-atmosferica #planet-scope #qualidade-de-dados #sensoriamento-remoto
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]], [[São Martinho — Planejamento agrícola]]
- Confiança: alta

### 2026-11-23 14:40 BRT — sem_novidade

### 2026-11-20 07:37 BRT — Codex CLI 0.171.0 amplia workspace e execução remota

- Fonte: [OpenAI — release Codex 0.171.0](https://github.com/openai/codex/releases/tag/rust-v0.171.0)
- Publicado: 2026-11-20 00:44, conforme página do GitHub (fuso não exibido; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A versão torna padrão o workspace da interface de terminal, com prévias pesquisáveis de documentos, imagens e transcrições de subagentes ao lado da conversa. Adiciona `codex exec --remote` para iniciar ou retomar sessões não interativas em um app server existente, além de comandos de controle remoto e linha de status MCP configurável. Corrige preservação de perfis de permissão ao mudar diretórios e login MCP com alguns provedores corporativos.
- Por que importa: Facilita acompanhar trabalho paralelo e operar sessões remotas em fluxos de desenvolvimento com agentes. Quem depende de permissões por diretório ou MCP corporativo deve validar a atualização.
- Tags: #openai #codex #agentes-ia #mcp #execucao-remota #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-20 07:37 BRT — Claude Code 2.1.329 reúne tarefas e reforça diagnóstico MCP

- Fonte: [Anthropic — release Claude Code v2.1.329](https://github.com/anthropics/claude-code/releases/tag/v2.1.329)
- Publicado: 2026-11-19 22:14, conforme página do GitHub (fuso não exibido; inclusão na janela exata de 24 horas não confirmada).
- Resumo: O comando `/tasks` passa a mostrar tarefas agendadas da sessão, ativações de `/loop`, objetivo e forks da conversa. A tela `/mcp` mostra a mensagem de erro JSON-RPC quando um servidor HTTP remoto recusa conexão. A versão também alerta sobre a origem de hooks de uma pasta e corrige casos de perda de configurações locais, tarefas MCP paradas após reconexão e revisões de código feitas sobre o branch errado.
- Por que importa: Dá mais visibilidade à execução de agentes e reduz diagnósticos ambíguos em integrações MCP. É especialmente útil para rotinas agendadas e revisão assistida de código.
- Tags: #anthropic #claude-code #mcp #tarefas-agendadas #agentes-ia #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-20 07:37 BRT — ArcGIS Pro amplia integração BIM/CAD para infraestrutura linear

- Fonte: [Esri — novidades de BIM e CAD no ArcGIS Pro](https://www.esri.com/arcgis-blog/products/arcgis-pro/announcements/whats-new-for-bim-and-cad-in-arcgis-pro-november-2026)
- Publicado: 2026-11-19 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A atualização de novembro do ArcGIS Pro permite acessar alinhamentos, perfis, equações de estaca e superfícies TIN do OpenRoads Designer e combiná-los com conteúdo de Revit, Civil 3D e outros formatos. Também permite propagar propriedades de camadas de edifícios e escolher níveis de detalhe Fine, Medium ou Coarse para modelos Revit.
- Por que importa: Pode reduzir conversão manual de dados de projeto viário para GIS e apoiar análise conjunta de traçado, terreno e ativos. A adoção depende dos formatos efetivamente usados nos projetos.
- Tags: #esri #arcgis-pro #bim #cad #openroads #infraestrutura-linear #release
- Relações: [[GeoNext — LiDAR e rodovias]], [[Bracell — GeoIA Estradas]]
- Confiança: alta

### 2026-11-20 07:37 BRT — AWS STS permite credenciais temporárias com escopo reduzido para agentes

- Fonte: [AWS — anúncio da API GetScopedCredentials](https://aws.amazon.com/about-aws/whats-new/2026/11/sts-getscopedcredentials/)
- Publicado: 2026-11-19 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: A nova API `GetScopedCredentials` deriva credenciais temporárias com permissões, duração ou ambas reduzidas em relação à sessão chamadora, preservando a identidade original. Seu uso depende de política IAM e cada chamada é registrada no CloudTrail. A AWS informa disponibilidade nas regiões comerciais, GovCloud, European Sovereign Cloud e China.
- Por que importa: Permite atribuir privilégio mínimo a agentes e subagentes sem criar nova identidade para cada tarefa. Equipes devem definir políticas e testar a propagação de permissões antes de usar em produção.
- Tags: #aws #sts #iam #agentes-ia #credenciais #seguranca #api
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-20 07:37 BRT — Google Cloud Storage lança enriquecimento de objetos para contexto de agentes

- Fonte: [Google Cloud — object enrichments no Cloud Storage](https://cloud.google.com/blog/products/storage-data-transfer/cost-effective-ai-context-extraction-from-unstructured-gcs-data)
- Publicado: 2026-11-19 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: Em preview, `object enrichments` aplica modelos de IA a objetos no Cloud Storage e grava metadados contextuais junto aos próprios objetos. O anúncio cobre anotações de imagens, como detecção e rotulação, e classificação de PDFs, com configuração via console ou API. Funções mais amplas com Gemini para texto, áudio e vídeo são futuras e exigem solicitação de acesso; não fazem parte da disponibilidade geral deste preview.
- Por que importa: Oferece uma forma gerenciada de indexar acervos de imagens e documentos usados por agentes, reduzindo infraestrutura própria de pré-processamento. Custo e adequação a imagens geoespaciais precisam ser testados em amostras reais.
- Tags: #google-cloud #cloud-storage #metadados #imagens #documentos #agentes-ia #preview
- Relações: [[NAVIS / GeoFramework]], [[Bracell — POC RGB + LiDAR]]
- Confiança: alta

### 2026-11-20 07:37 BRT — AWS AppConfig versiona prompts e parâmetros de modelos sem redeploy

- Fonte: [AWS — perfis nativos de configuração de IA no AppConfig](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-appconfig-native-ai-model-invocation-prompt-configurations/)
- Publicado: 2026-11-19 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: O AppConfig adicionou perfis para configurações de invocação de modelos e para prompts, permitindo alterar modelo, parâmetros e mensagens em aplicações em execução sem novo deploy. Os perfis podem ser versionados e distribuídos gradualmente, com rollback automático por alarmes de observabilidade. A AWS informa disponibilidade nas regiões do AppConfig sem custo adicional do recurso.
- Por que importa: Dá controle de mudança e reversão a agentes em produção, inclusive quando um ajuste de prompt ou modelo piora resultados ou custos. Não substitui avaliação funcional dos fluxos GeoIA.
- Tags: #aws #appconfig #prompts #agentes-ia #rollout #rollback #release
- Relações: [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-20 07:37 BRT — Google Agent Registry adiciona metadados de controle para ferramentas MCP

- Fonte: [Google Cloud — release notes do Agent Registry](https://docs.cloud.google.com/agent-registry/release-notes#november_19_2026)
- Publicado: 2026-11-19 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada).
- Resumo: O Agent Registry passou a aceitar, em preview, metadados de protocolo de ferramentas MCP, incluindo indicadores de política do Identity-Aware Proxy para habilitação de ferramentas, controles de aprovação humana e atributos de provedor. A nota de versão não afirma que esses controles são aplicados automaticamente a todas as ferramentas registradas.
- Por que importa: Aumenta a capacidade de descrever requisitos de acesso e supervisão humana de ferramentas disponibilizadas a agentes. Antes de adoção, verificar como os metadados são interpretados pelo cliente e pelo ambiente de execução.
- Tags: #google-cloud #agent-registry #mcp #iap #human-in-the-loop #governanca #preview
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-19 07:31 BRT — Duas versões de `agent-framework` no PyPI continham código para roubo de credenciais

- Fonte: [GitHub Advisory Database — código malicioso em agent-framework](https://github.com/advisories/GHSA-764m-3ppc-5m73)
- Publicado: aviso em 2026-11-18 (horário/fuso não informados; inclusão do aviso na janela exata de 24 horas não confirmada). Pacotes afetados foram publicados em 2026-11-17.
- Resumo: O aviso de segurança identifica as versões 1.26.1 e 1.26.2 do pacote PyPI `agent-framework`, do Microsoft Agent Framework, como maliciosas. Elas acrescentaram um arquivo `.pth` que executa código ao iniciar o Python, mesmo sem importar o pacote, para coletar e enviar credenciais e variáveis de ambiente. As duas versões foram removidas do PyPI; 1.26.0 é a última versão não afetada identificada no aviso. O alerta não é um comunicado da Microsoft.
- Por que importa: Quem instalou 1.26.1 ou 1.26.2 deve tratar o ambiente como exposto, verificar instalações e rotacionar segredos acessíveis, inclusive de CI. A remoção do PyPI não desfaz instalações já realizadas.
- Tags: #microsoft #agent-framework #pypi #cadeia-de-suprimentos #seguranca #agentes-ia #credenciais
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-19 07:31 BRT — ArcGIS Pro 3.8 adiciona análise semântica e novas ferramentas GeoAI

- Fonte: [Esri — novidades do ArcGIS Pro 3.8](https://doc.esri.com/en/arcgis-pro/latest/get-started/whats-new-in-arcgis-pro.html)
- Publicado: ciclo de vida oficial da Esri marca 2026-11-19 para 3.8 e 3.8.1; horário de liberação não informado, portanto inclusão na janela exata de 24 horas não confirmada
- Resumo: A documentação da versão 3.8 lista três ferramentas novas na caixa GeoAI: `Detect Changes Using Embeddings` para comparar mudanças semânticas entre dados geoespaciais, `Detect Objects In 3D Space` para extrair objetos 3D de imagens orientadas com modelo treinado e `Find Features By Description` para buscar feições por semelhança com uma descrição. O ModelBuilder também ganha inspeção de problemas antes da execução, agendamento e compartilhamento de modelos como ferramentas web. O ciclo de vida da Esri registra 19 de novembro como data da versão, sem hora de disponibilidade.
- Por que importa: Amplia opções nativas para monitorar mudanças, objetos e feições em projetos GeoIA. Antes de adoção, validar requisitos de modelos, licenças, acurácia e compatibilidade dos fluxos existentes.
- Tags: #esri #arcgis-pro #geoai #embeddings #deteccao-de-mudancas #imagem-orientada #modelbuilder #release
- Relações: [[Vale — GeoIA SAB.IA]], [[Amaggi — Monitoramento de desmatamento]], [[Bracell — POC RGB + LiDAR]]
- Confiança: alta

### 2026-11-19 07:31 BRT — ArcGIS Enterprise 12.2 permite implantar Solutions sem conexão à internet

- Fonte: [Esri — ArcGIS Solutions em Enterprise desconectado](https://www.esri.com/arcgis-blog/products/arcgis-enterprise/announcements/deploy-arcgis-solutions-content-in-a-disconnected-enterprise-environment)
- Publicado: 2026-11-18 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: A Esri detalhou que administradores do ArcGIS Enterprise 12.2 podem obter um pacote `.epk` no My Esri, transferi-lo para um ambiente isolado e hospedar localmente o conteúdo de ArcGIS Solutions. A versão inclui 29 soluções compatíveis com implantação desconectada, com galeria, mapas, aplicativos, fluxos e documentação acessíveis sem ArcGIS Online. São necessários privilégios de administração e pacote correspondente à versão do Enterprise.
- Por que importa: Viabiliza uso de soluções prontas em instalações GIS segregadas, comuns em operações sensíveis. A aplicabilidade a cada projeto depende de suas políticas de rede e do catálogo das 29 soluções, não de implantação anunciada nesses clientes.
- Tags: #esri #arcgis-enterprise #arcgis-solutions #ambiente-desconectado #implantacao #gis
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-19 07:31 BRT — Claude Code 2.1.328 permite bloquear falha de hook MCP

- Fonte: [Anthropic — release Claude Code v2.1.328](https://github.com/anthropics/claude-code/releases/tag/v2.1.328)
- Publicado: 2026-11-19 01:14 UTC, conforme release oficial do GitHub (dentro da janela pesquisada)
- Resumo: A versão adiciona `onFailure: "block"` a hooks `mcp_tool`: quando o hook falha, a ação pode ser bloqueada. Também amplia o modo automático para modelos Claude Opus e Sonnet 4.6 em Bedrock, Google Cloud Agent Platform, Microsoft Foundry e gateway Claude apps. Corrige perda de outras tarefas agendadas ao salvar quando o arquivo de tarefas não podia ser lido, além de evitar apagar uma tarefa com erro de digitação no arquivo.
- Por que importa: Hooks MCP passam a ter opção explícita de falhar de forma fechada, relevante para controles de agentes. Quem usa tarefas agendadas e provedores externos deve testar a atualização e seus modos de permissão.
- Tags: #anthropic #claude-code #mcp #hooks #agentes-ia #seguranca #tarefas-agendadas #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-19 07:31 BRT — Microsoft Foundry libera observação de agentes externos sem migração

- Fonte: [Microsoft — agentes externos no Foundry em disponibilidade geral](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/external-agents-in-microsoft-foundry-are-now-generally-available/4572630)
- Publicado: 2026-11-18 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: A Microsoft disponibilizou de forma geral o registro de agentes externos no Foundry, com visualização de traces, Agent Insights e avaliação contínua de traces de produção. O agente continua em seu ambiente e envia telemetria OpenTelemetry ao Application Insights; o registro exige convenções semânticas GenAI e `gen_ai.agent.id`. Outros recursos citados no artigo ainda estão em preview. A própria Microsoft alerta que gravar prompts e respostas nos traces exige decisão sobre acesso, retenção e ocultação de conteúdo sensível.
- Por que importa: Dá caminho para governar e avaliar agentes já implantados sem reconstruí-los no Foundry. Em projetos com dados corporativos, configurar privacidade dos traces antes de habilitar captura de conteúdo.
- Tags: #microsoft #foundry #agentes-ia #opentelemetry #observabilidade #avaliacao #governanca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-19 07:31 BRT — AWS Glue libera agente de otimização Spark acessível por MCP

- Fonte: [AWS — Apache Spark Optimization Agent para Glue ETL](https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-aws-glue-etl/)
- Publicado: 2026-11-18 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: O AWS Glue ETL passou a oferecer um agente que analisa execuções Spark concluídas e recomenda mudanças de configuração para custo ou desempenho, apoiadas em logs, configuração e telemetria do job. O acesso ocorre no console Glue ou por ferramentas externas via servidor MCP do SageMaker Unified Studio. A AWS informa disponibilidade sem custo adicional para jobs Glue 4.0 ou posterior nas regiões Glue, exceto GovCloud dos EUA e China; permanecem os custos normais do serviço.
- Por que importa: Pode acelerar diagnóstico de ETL geoespacial pesado quando esse processamento usa Glue. Recomendações precisam ser testadas com cargas próprias; o anúncio não prova redução de custo em projetos específicos.
- Tags: #aws #glue #spark #etl #mcp #agentes-ia #otimizacao #release
- Relações: [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-19 07:31 BRT — Copernicus anuncia migração do catálogo CSV e fim do acesso direto ao bucket

- Fonte: [Copernicus Data Space Ecosystem — nova interface do catálogo CSV](https://dataspace.copernicus.eu/news/2026-11-17-new-copernicus-catalogue-csv-interface)
- Publicado: 2026-11-18 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: O Copernicus anunciou que a interface antiga do catálogo CSV será substituída em 20 de janeiro de 2027. Até lá, as interfaces antiga e nova funcionarão em paralelo. O acesso direto ao bucket `s3.waw3-1.cloudferro.com/swift/v1/CatalogueCSV/` será encerrado, e o operador orienta migrar automações desse acesso para a API documentada. O endereço `api.csv.dataspace.copernicus.eu` não será alterado pela troca de interface.
- Por que importa: Pipelines de inventário de imagens Sentinel que leem o bucket diretamente precisam testar a migração. Relação com projetos depende de usarem esse acesso; a API CSV atual não tem mudança de endereço anunciada.
- Tags: #copernicus #catalogo-csv #api #sentinel #automacao #migracao #ciclo-de-vida
- Relações: [[NAVIS / GeoFramework]], [[Amaggi — Monitoramento de desmatamento]]
- Confiança: alta

### 2026-11-19 07:31 BRT — ICMM publica base global de mineração e biodiversidade

- Fonte: [ICMM — lançamento da Global Mining and Metals Biodiversity Dataset](https://www.prnewswire.com/news-releases/new-global-dataset-maps-where-mining-and-metals-intersect-with-biodiversity-302940342.html)
- Publicado: 2026-11-18 05:00 ET (10:00 UTC). Capturado na rotina setorial das 06:47 BRT; 28 minutos anterior ao início da janela exata desta consolidação.
- Resumo: O ICMM publicou um conjunto de dados que cruza cerca de 12 mil instalações de mineração e metalurgia com indicadores de condição de ecossistemas, áreas-chave para biodiversidade e áreas protegidas ou conservadas. Segundo a entidade, 22% das instalações ficam em paisagens de condição ecológica alta ou muito alta; 5% intersectam áreas-chave para biodiversidade e 4% áreas protegidas ou conservadas. São resultados divulgados pelo ICMM, não validados independentemente neste radar.
- Por que importa: A base serve para triagem geoespacial e planejamento de recuperação ou fechamento de minas. Instalações são representadas por pontos, não limites operacionais; a análise não mede impacto de cada ativo nem substitui dados locais.
- Tags: #mineracao #biodiversidade #dados-geoespaciais #ecossistemas #areas-protegidas #fechamento-de-minas
- Relações: [[Vale — Fechamento de minas]], [[IMAC — Plataforma GIS]]
- Confiança: média

### 2026-11-18 07:36 BRT — Servidores MCP de referência corrigem oito vulnerabilidades

- Fonte: [Model Context Protocol — release dos servidores v2.5.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.5.0)
- Publicado: 2026-11-18 09:13 UTC, conforme release oficial do GitHub (dentro da janela pesquisada)
- Resumo: A versão 2.5.0 do repositório oficial de servidores MCP corrige oito vulnerabilidades em três servidores. As versões indicadas são `mcp-server-git 2026.11.18`, `@modelcontextprotocol/server-filesystem 2.4.0` e `@modelcontextprotocol/server-everything 2.3.1`. As correções do servidor Git tratam caminhos em que configurações de repositórios podiam disparar comandos durante operações ou até leituras; a versão também reforça limites do servidor de arquivos.
- Por que importa: Projetos que expõem repositórios ou arquivos a agentes via esses servidores devem inventariar instalações e atualizar os componentes afetados. O risco depende dos servidores e versões efetivamente usados.
- Tags: #mcp #agentes-ia #seguranca #git #filesystem #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-18 07:36 BRT — Esri disponibiliza patch crítico para ArcGIS Enterprise 11.5–12.2

- Fonte: [Esri — aviso Brotli/Node.js atualizado em 17 de novembro](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/brotli-vulnerabilities-broccoli2shell)
- Publicado: aviso inicial de 2026-10-28, atualizado em 2026-11-17 (horário/fuso não informados; inclusão da atualização na janela exata de 24 horas não confirmada)
- Resumo: A Esri atualizou o estado da vulnerabilidade Brotli/Node.js no ArcGIS Enterprise, classificada como crítica (CVSS 9,4), e informa patch cumulativo Security 2026 Update 4 para as versões 11.5, 12.0, 12.1 e 12.2. Há patch para ArcGIS Mission Server nas versões afetadas; para ArcGIS Pro 3.5 ou posterior, o patch ainda está pendente. A Esri também orienta atualizar versões de Node.js gerenciadas pelo cliente quando aplicável.
- Por que importa: É uma ação de segurança diretamente relevante a ambientes ArcGIS corporativos. Verificar versão, componentes instalados e pré-requisitos do patch antes de aplicá-lo; não presumir que toda implantação usa a superfície afetada.
- Tags: #esri #arcgis-enterprise #arcgis-pro #seguranca #vulnerabilidade #patch #nodejs
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-18 07:36 BRT — Codex 0.170.0 corrige autenticação MCP e preservação de sandbox

- Fonte: [OpenAI — release Codex 0.170.0](https://github.com/openai/codex/releases/tag/rust-v0.170.0)
- Publicado: 2026-11-18 03:40 UTC, conforme release oficial do GitHub (dentro da janela pesquisada)
- Resumo: O Codex 0.170.0 adiciona suporte experimental a servidores MCP com o mesmo nome em ambientes diferentes. Corrige condições de corrida nas credenciais OAuth do MCP durante cancelamento, login e logout. Também corrige atualizações de permissões e threads filhas que podiam perder restrições existentes de sandbox, além de melhorar reconexão de conversas na nuvem.
- Por que importa: Equipes que operam agentes com MCP e permissões restritas devem testar a atualização, especialmente fluxos de autenticação e isolamento. O suporte a nomes homônimos ainda é experimental.
- Tags: #openai #codex #mcp #oauth #sandbox #agentes-ia #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-18 07:36 BRT — Claude Code 2.1.327 protege arquivos ignorados e configuração MCP

- Fonte: [Anthropic — release Claude Code v2.1.327](https://github.com/anthropics/claude-code/releases/tag/v2.1.327)
- Publicado: 2026-11-17 23:17 UTC, conforme release oficial do GitHub (dentro da janela pesquisada)
- Resumo: A versão acrescenta `claude mcp add-json <name> -` para ler a configuração JSON pela entrada padrão, evitando expor tokens na linha de comando. Corrige comandos de adicionar/remover servidores MCP no escopo do projeto que apagavam outras chaves de `.mcp.json`. Corrige ainda um caso em que parar Remote Control em modo worktree apagava arquivos ignorados de uma sessão ativa, como `.env`.
- Por que importa: A atualização reduz risco de perda de configuração e arquivos locais em automações de desenvolvimento. Convém validar plugins e worktrees antes de uso amplo.
- Tags: #anthropic #claude-code #mcp #worktree #seguranca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-18 07:36 BRT — ArcGIS Monitor 2026.1 abre MCP de observabilidade em beta

- Fonte: [Esri — suporte a MCP no ArcGIS Monitor 2026.1](https://www.esri.com/arcgis-blog/products/monitor/administration/arcgis-monitor-2026-1-support-for-ai-with-model-context-protocol-mcp)
- Publicado: 2026-11-17 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: A Esri anunciou suporte a MCP em beta público no ArcGIS Monitor 2026.1. Clientes de IA podem consultar métricas de saúde, desempenho e uso de ambientes GIS para apoiar investigação de incidentes, análise de impacto e planejamento de capacidade. A Esri distingue esse conector de observabilidade do MCP disponibilizado para o ArcGIS Enterprise.
- Por que importa: Permite avaliar diagnóstico operacional assistido por agentes em plataformas ArcGIS. Por ser beta, requer teste de acesso, confiabilidade das respostas e limites de uso antes de produção.
- Tags: #esri #arcgis-monitor #mcp #observabilidade #agentes-ia #beta
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-11-18 07:36 BRT — NASA encerrará coleta científica do satélite Terra em 1º de dezembro

- Fonte: [NASA Science — encerramento da missão Terra](https://science.nasa.gov/blogs/science-news/2026/11/17/nasas-terra-mission-to-end/)
- Publicado: 2026-11-17 12:50 (fuso não informado na página; inclusão na janela exata de 24 horas não confirmada)
- Resumo: A NASA anunciou que o satélite Terra deixará de coletar dados científicos em 1º de dezembro de 2026, após 27 anos de operação, por envelhecimento dos sistemas e deriva orbital. A missão inclui MODIS, ASTER, MISR e CERES; alguns componentes já haviam sido desligados. A equipe planeja baixar a órbita com o combustível restante e desligar os sistemas em janeiro de 2027. O acervo histórico continuará disponível gratuitamente.
- Por que importa: Pipelines agrícolas e florestais dependentes de novas observações da plataforma Terra precisam planejar continuidade. O encerramento não retira o acervo nem implica fim de todas as observações MODIS.
- Tags: #nasa #terra #modis #aster #sensoriamento-remoto #ciclo-de-vida #agro #florestal
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-11-18 07:36 BRT — Anomalia no Sentinel-2C causa perda irrecuperável de aquisições

- Fonte: [Copernicus Data Space Ecosystem — indisponibilidade de dados Sentinel-2C](https://dataspace.copernicus.eu/news/2026-11-17-copernicus-sentinel-2c-data-unavailability-17-november-2026)
- Publicado: 2026-11-17 (horário/fuso do aviso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: O Copernicus informou que uma anomalia a bordo do Sentinel-2C causou perda irrecuperável de todos os dados adquiridos desde 17 de novembro às 08:25 UTC. Novas aquisições podem ser afetadas enquanto a falha persistir. O operador investiga o problema e prevê informar as aquisições afetadas no painel de eventos da missão.
- Por que importa: Lacunas podem afetar séries de monitoramento de lavouras, florestas e desmatamento. Pipelines devem detectar ausências e avaliar alternativas; o aviso não quantifica impacto em áreas específicas dos projetos.
- Tags: #copernicus #sentinel-2c #indisponibilidade #qualidade-de-dados #sensoriamento-remoto #agro #florestal
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]], [[São Martinho — Planejamento agrícola]]
- Confiança: alta

### 2026-11-17 07:35 BRT — Esri detalha toolkit agêntico para desenvolver aplicações ArcGIS

- Fonte: [Esri — ArcGIS agentic developer toolkit](https://www.esri.com/arcgis-blog/products/developers/developers/improving-ai-assisted-workflows-with-the-arcgis-agentic-developer-toolkit)
- Publicado: 2026-11-16 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: A Esri apresentou o ArcGIS agentic developer toolkit como combinação de servidor MCP público de documentação e skills para agentes de desenvolvimento. O servidor permite buscar e recuperar guias, referências de APIs e SDKs e exemplos oficiais; as skills orientam padrões de implementação, autenticação e tratamento de erros em aplicações ArcGIS. A Esri entrega as skills também por plugin. O anúncio de 16 de novembro descreve componentes já disponíveis, sem comprovar que todos foram lançados naquele dia.
- Por que importa: Dá a Codex e Claude Code contexto técnico oficial para implementar aplicações geoespaciais. O MCP descrito consulta documentação; não é acesso automático a dados ou operações de uma organização ArcGIS.
- Tags: #esri #arcgis #mcp #skills #agentes-ia #desenvolvimento #documentacao
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-17 07:35 BRT — Esri marca ArcGIS Enterprise 12.2 e documenta acesso MCP externo

- Fonte: [Esri — novidades do ArcGIS Enterprise 12.2](https://doc.esri.com/en/arcgis-enterprise/latest/introduction/what-s-new-in-arcgis-enterprise.html)
- Publicado: ciclo de vida oficial marca lançamento em 2026-11-17; horário de disponibilidade não informado, portanto inclusão na janela exata de 24 horas não confirmada
- Resumo: A documentação da versão 12.2 descreve configuração centralizada de recursos de IA, acesso de clientes externos à organização por MCP e catálogos MCP personalizados para agrupar ferramentas por fluxo de trabalho. Também lista o módulo `arcgis.ai` na API for Python para tarefas com conteúdo não estruturado e novos recursos para imagens orientadas, incluindo referência a imagens em armazenamento de nuvem. A página de ciclo de vida da Esri marca 17 de novembro de 2026 como data de lançamento; não há hora comprovada de disponibilização.
- Por que importa: Relevante para desenho de agentes com governança no ArcGIS Enterprise e para pipelines de imagens. Antes de planejar migração, verificar disponibilidade efetiva, licenças, beta/GA por recurso e compatibilidade dos ambientes.
- Tags: #esri #arcgis-enterprise #mcp #agentes-ia #arcgis-python #imagens-orientadas #release
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-17 07:35 BRT — Claude Code 2.1.326 corrige isolamento de ferramentas MCP paralelas

- Fonte: [Anthropic — release Claude Code v2.1.326](https://github.com/anthropics/claude-code/releases/tag/v2.1.326)
- Publicado: 2026-11-16 22:11 UTC, conforme release oficial do GitHub (dentro da janela pesquisada)
- Resumo: A versão 2.1.326 permite usar Code Mode com equipes de agentes. Corrige casos em que duas chamadas MCP paralelas com resultados longos, concluídas no mesmo milissegundo, podiam ler o resultado salvo uma da outra; a busca de ferramentas também podia carregar ferramenta de outro servidor MCP com o mesmo nome. A versão ajusta avisos de permissões e sandbox, inclusive o resumo incorreto de comandos que apagam ou sobrescrevem arquivos como se fossem leitura.
- Por que importa: Corrige riscos de atribuição errada de resultados e de interpretação de ações destrutivas em automações multiagente. Testar fluxos com MCP e hooks ao atualizar.
- Tags: #anthropic #claude-code #mcp #agentes-ia #code-mode #seguranca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-17 07:35 BRT — AWS amplia identidade e auditoria em WorkSpaces para agentes

- Fonte: [AWS — novas capacidades de Amazon WorkSpaces para agentes](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-AI-agents-connect-govern/)
- Publicado: 2026-11-16 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: A AWS anunciou que WorkSpaces para agentes passa a aceitar provedores de identidade OIDC além de SAML e oferece entrada em nome do usuário, preservando sua identidade, permissões e políticas de diretório no desktop. A nova reprodução de sessão combina capturas de tela em vídeo com transcrição das ações; os registros ficam em bucket S3 do cliente, criptografados com suas chaves. A AWS também descreve configuração guiada por skills MCP a partir de assistentes de código e conexão direta de agentes Bedrock AgentCore.
- Por que importa: Oferece controles de identidade e trilha de auditoria para agentes que operam aplicativos corporativos. Avaliar privacidade das gravações, custo e políticas antes de uso em dados de projetos.
- Tags: #aws #workspaces #agentes-ia #mcp #oidc #identidade #auditoria #seguranca
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-17 07:35 BRT — Kodiak integra LiDAR IRIS à plataforma de caminhões autônomos

- Fonte: [Kodiak AI e MicroVision — integração do LiDAR IRIS](https://kodiakrobotics.gcs-web.com/news-releases/news-release-details/microvision-lidar-powers-commercial-driverless-trucking-scale)
- Publicado: 2026-11-16 08:00 EST (13:00 UTC; dentro da janela pesquisada)
- Resumo: A Kodiak AI e a MicroVision anunciaram que o LiDAR IRIS de longo alcance já integra a sexta geração da plataforma autônoma da Kodiak, que combina LiDAR, câmeras e radar. Segundo as empresas, o sensor detecta objetos a mais de 250 metros e foi validado sob vibração, poeira, clima e iluminação de operações comerciais. A Kodiak informa 37 caminhões com sua tecnologia em frota operada por cliente em 3 de novembro. O serviço comercial de longa distância sem motorista está previsto, mas não concluído, para o fim de 2026.
- Por que importa: Evidência de percepção de longo alcance integrada a frota logística real. Aplicação a transporte florestal ou de grãos é hipótese, não implantação anunciada.
- Tags: #logistica #caminhoes-autonomos #lidar #percepcao #sensores #integracao #implantacao
- Relações: [[Suzano — Rotas e logística]], [[GeoNext — LiDAR e rodovias]]
- Confiança: alta

### 2026-11-17 07:35 BRT — Agente Augie integra trabalho fora do TMS ao MasterMind

- Fonte: [Augment — parceria com Mastery Logistics Systems e casos Werner/Schneider](https://www.goaugment.com/blog/mastery-and-augment-partner)
- Publicado: 2026-11-16 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: Mastery Logistics Systems e Augment anunciaram a conexão do agente Augie ao TMS MasterMind por APIs abertas. O agente reúne dados recebidos fora do TMS, como e-mails, e grava atualizações no sistema. Segundo as empresas, Werner utiliza Augie para construir cargas fora de fluxos automáticos e Schneider para confirmação de entrega e etapas de faturamento.
- Por que importa: Caso operacional de agente conectado a sistema transacional de frete, com clientes identificados. Pode orientar integração logística; não comprova roteirização geoespacial ou ganhos quantitativos independentes.
- Tags: #logistica #tms #agentes-ia #api #automacao #frete #implantacao
- Relações: [[Suzano — Rotas e logística]], [[NAVIS / GeoFramework]]
- Confiança: média

### 2026-11-17 07:35 BRT — USGS programa pausa de ferramentas e processamento Landsat em 23 de novembro

- Fonte: [USGS EROS — manutenção programada de 23 de novembro](https://www.usgs.gov/centers/eros/2026-11-23-planned-maintenance)
- Publicado: aviso listado em 2026-11-16 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: O USGS EROS programou manutenção dos sistemas de acesso e geração de produtos para 23 de novembro, das 07:00 às 14:00 no horário Central dos EUA. EarthExplorer, M2M, GloVis e outras ferramentas serão afetadas. O acesso direto a dados existentes na nuvem permanecerá disponível, mas novos dados não serão adicionados nesse intervalo; processamento Landsat ficará pausado e aquisições Landsat 8/9 aguardarão retomada.
- Por que importa: Pipelines dependentes de M2M ou de novos produtos Landsat devem tolerar indisponibilidade e atraso. Relação com projetos é condicional ao uso desses serviços.
- Tags: #usgs #landsat #m2m #api #manutencao #disponibilidade #sensoriamento-remoto
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]]
- Confiança: alta

### 2026-11-17 07:35 BRT — Copernicus identifica erro de QA em produtos Sentinel-5P de ozônio e nuvens

- Fonte: [Copernicus Data Space Ecosystem — aviso sobre QA após UPAS 3.0.1](https://dataspace.copernicus.eu/news/2026-11-16-sentinel-5p-nrti-o3-and-cloud-products-qa-value-issue-following-upas-301-upgrade)
- Publicado: 2026-11-16 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: Após atualização dos processadores Sentinel-5P, o Copernicus identificou que, em casos raros de alta fração de nuvens, especialmente sobre América do Sul e África, os valores de qualidade (QA) dos produtos quase em tempo real de nuvens e ozônio (O3) podem ficar abaixo do esperado. O QA de O3 também é afetado por utilizar QA de nuvens como entrada. O problema não invalida os produtos; correção está em teste. Até lá, o operador recomenda limiar de QA 0,4 para O3 quase em tempo real.
- Por que importa: Filtros automáticos podem descartar observações válidas nessas regiões. Revisar limiar em fluxos que usam O3; o aviso não indica impacto em produtos de metano.
- Tags: #copernicus #sentinel-5p #ozonio #nuvens #qualidade-de-dados #processamento #sensoriamento-remoto
- Relações: [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-11-16 07:30 BRT — sem_novidade

### 2026-11-13 07:36 BRT — Experience Builder incorpora AI Chat para operar mapas, dados e widgets

- Fonte: [Esri — novidades do ArcGIS Experience Builder em novembro de 2026](https://www.esri.com/arcgis-blog/products/experience-builder/announcements/whats-new-in-arcgis-experience-builder-november-2026)
- Publicado: 2026-11-12 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: A atualização de novembro do ArcGIS Experience Builder no ArcGIS Online acrescenta AI Chat em beta. Em aplicativos configurados, usuários podem consultar, filtrar, agrupar e resumir dados; navegar no mapa; e acionar operações de widgets compatíveis, como tabela, gráfico, rotas e impressão. A resposta pode mostrar mapas, tabelas ou detalhes de feições, e algumas alterações feitas pela conversa oferecem opção de desfazer. O autor habilita o recurso no painel geral do aplicativo, sem reconstruí-lo.
- Por que importa: Permite testar interfaces conversacionais sobre aplicativos GIS existentes. Uso exige usuário autenticado e agentes de IA habilitados na organização; a Esri prevê cobrança de créditos após o beta. Cada ação precisa de revisão de permissões e resultado.
- Tags: #esri #arcgis-online #experience-builder #agentes-ia #mapas #widgets #beta #release
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-13 07:36 BRT — Claude Code 2.1.323 adiciona Code Mode e valida compatibilidade de plugins

- Fonte: [Anthropic — release Claude Code v2.1.323](https://github.com/anthropics/claude-code/releases/tag/v2.1.323)
- Publicado: 2026-11-12 22:12 UTC, conforme API de releases do GitHub (dentro da janela pesquisada)
- Resumo: A versão 2.1.323 introduz Code Mode experimental, opt-in, no qual Claude escreve JavaScript para chamar ferramentas. Plugins agora podem declarar em `engines["claude-code"]` as versões compatíveis; versões fora do intervalo não são instaladas nem carregadas. O comando `claude plugin validate` passa a verificar tipos de hooks TypeScript, com falha em modo `--strict`. A versão também ajusta proteções de sandbox e aprovação de servidores MCP, além de corrigir falhas de reconexão e histórico de ferramentas.
- Por que importa: Quem mantém automações com plugins ou MCP precisa testar compatibilidade e fluxo de autorização antes de atualizar. Code Mode pode mudar a forma de orquestrar ferramentas, mas ainda é experimental.
- Tags: #anthropic #claude-code #code-mode #plugins #mcp #seguranca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-13 07:36 BRT — Codex 0.169.0 reforça confiança de projetos e amplia trabalho no terminal

- Fonte: [OpenAI — release Codex 0.169.0](https://github.com/openai/codex/releases/tag/rust-v0.169.0)
- Publicado: 2026-11-13 08:37 UTC, conforme API de releases do GitHub (dentro da janela pesquisada)
- Resumo: O Codex 0.169.0 adiciona múltiplos side chats no workspace de terminal opt-in, busca de tarefas antigas e configuração de provedores de modelos diretamente no terminal. Na segurança, `codex exec` mantém configurações de projeto e servidores MCP desabilitados em diretórios não confiáveis mesmo com sandbox `workspace-write`; confiar no projeto passa a exigir `--trust` explícito. A versão também corrige casos de sandbox no Windows.
- Por que importa: Evita que um repositório ainda não confiável ative MCPs por efeito colateral da permissão de escrita. Equipes que automatizam execução e revisão devem testar o novo fluxo de confiança antes de atualizar.
- Tags: #openai #codex #mcp #seguranca #terminal #agentes-ia #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-13 07:36 BRT — AWS torna AgentCore Runtime V2 padrão para novos agentes

- Fonte: [AWS — nova geração do Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/about-aws/whats-new/2026/11/new-agentcore-runtime-default/)
- Publicado: 2026-11-12 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: Novos runtimes do Amazon Bedrock AgentCore passam a usar a geração V2 por padrão nas regiões indicadas pela AWS, incluindo São Paulo. Cada sessão continua isolada em microVM Firecracker, mas agora pode restaurar o agente de um snapshot, escalar até 8 vCPU e 32 GB de memória, usar imagem de até 10 GB e reduzir recursos ociosos a zero. Segundo a AWS, uma imagem de 2 GB inicia em menos de 2 segundos no percentil 75, ante 29,7 segundos na geração anterior. Runtimes existentes não migram automaticamente; `platformVersion=V2` faz a opção explícita.
- Por que importa: Afeta latência, custo e planejamento de implantação de agentes corporativos, inclusive na região brasileira. Números de desempenho são medições divulgadas pela AWS; validar com cargas próprias antes de migrar.
- Tags: #aws #bedrock #agentcore #agentes-ia #runtime #escalabilidade #custo #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-13 07:36 BRT — Cognito libera troca OAuth de tokens para agentes e servidores MCP

- Fonte: [AWS — suporte a OAuth 2.0 token exchange no Amazon Cognito](https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-token-exchange/)
- Publicado: 2026-11-12 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: O Amazon Cognito passou a oferecer troca de tokens OAuth 2.0 conforme RFC 8693 pelo endpoint de token ou pela nova API `GetDerivedToken`. Um agente ou serviço que atua em nome do usuário pode receber um token restrito a escopo e destinatário específicos, sem refresh token. Com token de ator, a reivindicação `act` identifica o intermediário; a AWS cita servidores MCP como exemplo. A capacidade está nos planos Essentials e Plus nas regiões que oferecem Cognito.
- Por que importa: Dá mecanismo padrão para delegar acesso a APIs sem repassar o token original do usuário a cada ferramenta. Útil para desenhar permissões de agentes que consultam dados corporativos, sujeito a teste de identidade e auditoria.
- Tags: #aws #cognito #oauth #mcp #agentes-ia #identidade #seguranca #api
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-11-13 07:36 BRT — Google abre Agent Gateway para agentes em GKE em preview

- Fonte: [Google Cloud — notas de versão do GKE de 12 de novembro](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-new-features#November_12_2026)
- Publicado: 2026-11-12 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: O Agent Gateway para GKE entrou em preview no canal Rapid, para clusters a partir da versão `1.37.2-gke.1042000`, inicialmente nas regiões `europe-west1` e `us-central1`. A camada centraliza o controle do tráfego de entrada, saída e entre agentes hospedados em GKE. A documentação descreve políticas baseadas em identidade, integração com Agent Registry e Model Armor, além de observabilidade de interações com ferramentas e servidores MCP.
- Por que importa: Referência de arquitetura para governar agentes autogerenciados e acesso a ferramentas. Ainda não está disponível em região brasileira; adoção nos projetos depende de requisitos de residência de dados e maturidade do preview.
- Tags: #google-cloud #gke #agent-gateway #agentes-ia #mcp #governanca #seguranca #preview
- Relações: [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-13 07:36 BRT — Copernicus muda processamento operacional de produtos Sentinel-5P

- Fonte: [Copernicus Data Space Ecosystem — ativação dos novos processadores Sentinel-5P](https://dataspace.copernicus.eu/news/2026-11-12-copernicus-sentinel-5-precursor-s5p-products-improvement-operational-switch)
- Publicado: 2026-11-12 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: O Copernicus informou que atualizou em 11 de novembro o sistema operacional de processamento do Sentinel-5P. Os novos processadores abrangem produtos de nível 1B e nível 2 para metano (CH4), monóxido de carbono (CO), dióxido de nitrogênio (NO2), dióxido de enxofre (SO2) e outras variáveis atmosféricas. Os dados processados com as novas versões já estão no Copernicus Data Space Ecosystem: produtos de tempo quase real começam na órbita 47046, de 11 de novembro; produtos offline, na órbita 47001, de 8 de novembro. Produtos de tempo quase real adquiridos durante a parada de processamento não foram gerados.
- Por que importa: Pipelines de emissões em óleo e gás devem registrar versão do processador e lacuna de dados antes de comparar séries temporais. Relação com monitoramento de gasodutos é potencial; o anúncio não demonstra detecção de vazamentos pontuais nesses ativos.
- Tags: #copernicus #sentinel-5p #metano #oleo-e-gas #emissoes #processamento #dados #ciclo-de-vida
- Relações: [[TAG / TBG / NTS]]
- Confiança: alta

### 2026-11-12 07:28 BRT — Google Maps libera ferramentas Pro para agentes e busca ao longo de rotas

- Fonte: [Google Maps Platform — notas de versão das Maps Experience agent tools](https://developers.google.com/maps/ai/maps-experience-agent-tools/release-notes#november_11_2026)
- Publicado: 2026-11-11 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: O Google tornou as opções Pro de `search_places` e `compute_routes` disponíveis para todos os projetos Google Cloud, sem lista de permissão, e adicionou um método REST para cada ferramenta. A nova `search_along_route` procura lugares ao longo de um trajeto descrito por pontos de origem e destino, polilinha codificada ou token de uma rota calculada antes. A resposta reúne lugares ranqueados e estimativas de distância e tempo de desvio; chamadas usam o SKU Maps Grounding Pro.
- Por que importa: Abre uma API concreta para agentes consultarem paradas e desvios em fluxos logísticos. Aplicação a rotas florestais ou de grãos ainda depende de testar cobertura, custo e restrições operacionais; não é uma implantação nesses projetos.
- Tags: #google-maps #agentes-ia #api #roteirizacao #logistica #preco #release
- Relações: [[Suzano — Rotas e logística]], [[Bracell — GeoIA Estradas]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-11-12 07:28 BRT — AWS lança emulador local para testar APIs e agentes antes do deploy

- Fonte: [AWS — lançamento do AWS Emulator](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-emulator-now-available/)
- Publicado: 2026-11-11 (horário/fuso não informados; inclusão na janela exata de 24 horas não confirmada)
- Resumo: A AWS lançou o AWS Emulator para executar localmente chamadas existentes da AWS CLI e dos SDKs contra um endpoint HTTPS, sem conta AWS nem implantação em nuvem. Cada instância tem porta, credenciais e estado em memória próprios; operações ainda não implementadas retornam `501 Not Implemented`. A empresa publicou o código-fonte e informa que não há cobrança adicional pelo emulador.
- Por que importa: Permite que agentes de código e testes de integração exercitem automações AWS isoladamente antes de usar recursos reais. A fidelidade varia por API; respostas do emulador não substituem validação final na nuvem.
- Tags: #aws #agentes-ia #automacao #desenvolvimento #testes #api #lancamento
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-11 07:32 BRT — ArcGIS Maps SDK for JavaScript 5.2 amplia agentes e anuncia migração de APIs de interface

- Fonte: [Esri — novidades do ArcGIS Maps SDK for JavaScript 5.2](https://www.esri.com/arcgis-blog/products/js-api-arcgis/announcements/arcgis-maps-sdk-for-javascript-whats-new-in-5-2)
- Publicado: 2026-11-10 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A versão 5.2 do ArcGIS Maps SDK for JavaScript atualiza componentes de IA em beta: agentes podem compartilhar recursos no mesmo espaço de trabalho e ser definidos com habilidades reutilizáveis carregadas de arquivos Markdown. O ArcGIS Enterprise 12.2 passa a aceitar aplicativos agentes que consultam mapas do portal, desde que a organização habilite agentes de IA e forneça credenciais de uma organização ArcGIS Online para os modelos. A Esri também informa que 5.2 é a última versão com widgets e APIs de interface legadas; a versão 6.0, planejada para o primeiro trimestre de 2027, deve removê-las.
- Por que importa: Oferece base concreta para aplicativos geoespaciais com agentes e cria prazo de migração para interfaces que ainda dependem de widgets. Recursos de IA seguem em beta e exigem revisão de identidade e permissões.
- Tags: #esri #arcgis #javascript #agentes-ia #skills #arcgis-enterprise #api #ciclo-de-vida
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-11 07:32 BRT — Field Maps ganha escolhas dinâmicas offline e localização por conexão satelital

- Fonte: [Esri — atualização de novembro do ArcGIS Field Maps](https://www.esri.com/arcgis-blog/products/field-maps/field-mobility/whats-new-in-arcgis-field-maps-november-2026)
- Publicado: 2026-11-10 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O release de novembro do ArcGIS Field Maps adiciona listas de escolhas em formulários geradas por expressões Arcade a partir de campos, camadas ou tabelas. Elas funcionam offline quando os dados referenciados estão incluídos na área de mapa baixada. A atualização também integra localizadores de redes subterrâneas com RTK e permite envio de última posição e histórico de trilha por redes satelitais oferecidas por operadoras, em aparelhos compatíveis; mapas offline continuam recomendados em campo remoto.
- Por que importa: Reduz manutenção de formulários e amplia coleta/localização em áreas de pouca conectividade, relevantes para ativos lineares e operações florestais. Uso depende de dispositivo, operadora e preparo correto dos dados offline.
- Tags: #esri #field-maps #campo #offline #arcade #rtk #satelite #release
- Relações: [[Bracell — GeoIA Estradas]], [[TAG / TBG / NTS]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-11-11 07:32 BRT — Survey123 libera análise de imagem/texto com IA e envio automático ao reconectar

- Fonte: [Esri — novidades do ArcGIS Survey123 em novembro de 2026](https://www.esri.com/arcgis-blog/products/survey123/announcements/whats-new-in-arcgis-survey123-november-2026)
- Publicado: 2026-11-10 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Esri tornou a análise de imagem e texto por IA geralmente disponível no Survey123 Mobile e na versão web. Autores podem configurar extração de atributos de fotos ou respostas textuais, mas o processamento requer conexão, permissões administrativas para IA e serviços premium e consome créditos do ArcGIS Online. A atualização também traz autosend: registros na caixa de saída podem ser transmitidos automaticamente quando a conexão retorna. A Esri alerta para uma falha conhecida de login pelo endereço padrão do ArcGIS Online em parte dos aplicativos Mobile e Studio e indica, provisoriamente, o URL específico da organização.
- Por que importa: Possibilita transformar registros de campo em dados estruturados e acelerar sincronização após trabalho offline. Antes de ampliar uso, equipes devem testar custo por formulário, conexão e o problema de login comunicado.
- Tags: #esri #survey123 #ia #visao-computacional #coleta-de-campo #offline #creditos #release
- Relações: [[IMAC — Plataforma GIS]], [[Itaminas — Monitoramento geotécnico]], [[Bracell — POC RGB + LiDAR]]
- Confiança: alta

### 2026-11-11 07:32 BRT — Google Cloud permite governança semântica central de agentes em vários projetos

- Fonte: [Google Cloud — notas de versão de 10 de novembro do Gemini Enterprise Agent Platform](https://docs.cloud.google.com/release-notes/#November_10_2026)
- Publicado: 2026-11-10 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Google Cloud documentou políticas de governança semântica entre projetos para agentes no Gemini Enterprise Agent Platform. Em arquitetura com projeto central e projetos membros, uma fronteira de gestão com capacidade `AGENT_MANAGEMENT` permite ao Agent Registry descobrir agentes preservando suas identidades de execução. Um Agent Gateway e um mecanismo de políticas no projeto central aplicam regras aos agentes vinculados. A documentação classifica a política semântica como pré-GA/preview, exige configuração de identidade e gateway e alerta que decisões baseadas em LLM podem falhar.
- Por que importa: Oferece arquitetura para controlar agentes corporativos sem centralizar todas as cargas em um único projeto. A adoção requer desenho de identidades, regiões e políticas, além de validação humana dos veredictos.
- Tags: #google-cloud #agent-platform #agentes-ia #governanca #seguranca #identidade #preview
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-11 07:32 BRT — Fleet Space lança Tau 3.8 para modelagem de depósitos minerais

- Fonte: [Fleet Space Technologies — lançamento do Tau 3.8 e teste no projeto Valeriano](https://www.prnewswire.com/news-releases/ai-trained-on-ten-million-synthetic-earths-outperforms-conventional-copper-estimates-at-tsxv-listed-atexs-valeriano-project-302934678.html)
- Publicado: 2026-11-10 11:15 ET (16:15 UTC; dentro da janela pesquisada)
- Resumo: A Fleet Space Technologies lançou o Tau 3.8 nos Estados Unidos e no Canadá para modelar sistemas minerais com dados sísmicos 3D, sondagens, geologia, geofísica e mineralogia. Segundo a empresa, o modelo foi treinado em dez milhões de cenários geológicos sintéticos e estima continuidade do depósito, classifica alvos e sugere medições que reduzam incerteza. No projeto de cobre e ouro Valeriano, no Chile, a Fleet relata que testou a previsão em furos de sondagem retidos do treinamento e obteve erro de teor de cobre 38% menor que uma estimativa por krigagem feita com as mesmas sondagens. A comparação foi divulgada pela própria empresa e não equivale a validação independente em outros depósitos.
- Por que importa: Caso técnico para avaliar fusão de geofísica e sondagens com incerteza explícita no planejamento de exploração mineral. Métrica do Valeriano não deve ser extrapolada a minas ou projetos brasileiros sem teste local.
- Tags: #mineracao #geofisica #ia #modelagem-3d #sondagem #incerteza #lancamento
- Relações: [[Vale — GeoIA SAB.IA]], [[Itaminas — Monitoramento geotécnico]]
- Confiança: média

### 2026-11-11 07:32 BRT — USGS testa convergência de mapas de favorabilidade geotérmica feitos com aprendizado de máquina

- Fonte: [USGS — relatório de Stanley Mordensky, Erick Burns e John Lipor](https://pubs.usgs.gov/publication/sir20265071)
- Publicado: 2026-11-10 10:25 EST, conforme índice de novas publicações do USGS (15:25 UTC; dentro da janela pesquisada)
- Resumo: Pesquisadores do USGS e da Portland State University avaliaram quantas divisões aleatórias entre treino e teste são necessárias para estabilizar mapas de favorabilidade de recursos hidrotermais no Great Basin, nos Estados Unidos. O método gera várias realizações de aprendizado supervisionado por validação cruzada Monte Carlo e agrega previsões pela mediana de cada célula. No estudo, cerca de 600 realizações produziram previsão robusta; conjuntos de 100 a 200 podem servir à exploração preliminar. Os autores ressaltam que esses números variam com os dados e o modelo, enquanto as métricas de convergência podem ser reaplicadas.
- Por que importa: Oferece critério operacional para medir estabilidade de mapas preditivos antes de orientar investimento em exploração. Aplicação a depósitos minerais ou risco geotécnico é hipótese metodológica, não resultado demonstrado pelo artigo.
- Tags: #usgs #paper #geoia #aprendizado-de-maquina #validacao-cruzada #incerteza #recursos-naturais
- Relações: [[Vale — GeoIA SAB.IA]], [[Itaminas — Monitoramento geotécnico]]
- Confiança: alta

### 2026-11-11 07:32 BRT — ShipStation informa agentes de IA em produção para cotação e reserva de frete

- Fonte: [ShipStation Global — automação de cotação a embarque no frete LTL](https://www.shipstationglobal.com/news/shipstation-global-puts-ai-agents-to-work-booking-freight-in-minutes-not-hours/)
- Publicado: 2026-11-10 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A ShipStation Global descreveu uma cadeia de agentes para ler solicitações de frete fracionado por e-mail, consultar tarifas contratadas e preferências do cliente, preparar a cotação, reservar a transportadora, emitir o conhecimento de embarque e agendar coleta. Casos incompletos ou incomuns são encaminhados a um especialista humano com o contexto reunido. A empresa informa que o fluxo está em produção em suas marcas Worldwide Express, GlobalTranz e Unishippers e que, desde o início do ano, processou mais de 340 mil solicitações e cotações e criou mais de 100 mil conhecimentos de embarque. Os volumes e ganhos de tempo são números da própria empresa.
- Por que importa: Exemplo concreto de agentes especializados com acesso a dados contratuais e transferência para humano em exceções, útil como referência de arquitetura para fluxos logísticos. Não demonstra desempenho em roteirização geoespacial.
- Tags: #logistica #frete #agentes-ia #automacao #implantacao #humano-no-circuito
- Relações: [[Suzano — Rotas e logística]], [[NAVIS / GeoFramework]]
- Confiança: média

### 2026-11-11 07:32 BRT — Motive e Routeware integram vídeo e telemetria à execução de rotas de frota

- Fonte: [Motive — integração com Routeware SmartCity e Elements](https://gomotive.com/motive-and-routeware-partner-to-bring-ai-powered-visual-proof-of-service-to-waste-and-public-works-fleets/)
- Publicado: 2026-11-10 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: Motive e Routeware anunciaram integração disponível para clientes comuns nos Estados Unidos e no Canadá. Dados de câmeras, GPS ao vivo, eventos de segurança e telemetria de veículos aparecem junto ao progresso das rotas nas plataformas Routeware SmartCity e Elements, usadas por operações de coleta de resíduos e serviços públicos. Eventos de atendimento podem vincular vídeo à parada para verificação posterior. A futura integração de modelos de visão computacional para identificar excessos de coleta foi anunciada para 2027; não faz parte da capacidade atual descrita.
- Por que importa: Referência operacional para unir evidência visual georreferenciada, segurança e status de rota em um mesmo fluxo. Transferência a operações florestais ou de transporte de grãos é possibilidade técnica, não implantação anunciada.
- Tags: #logistica #frotas #telematica #gps #visao-computacional #integracao #implantacao
- Relações: [[Suzano — Rotas e logística]], [[Bracell — GeoIA Estradas]], [[GeoNext — LiDAR e rodovias]]
- Confiança: alta

### 2026-11-10 07:34 BRT — Esri amplia GeoAI com MCP, agentes cartográficos e modelo multissensor

- Fonte: [Esri — novidades em IA geoespacial de novembro de 2026](https://www.esri.com/arcgis-blog/products/arcgis/geoai/whats-new-in-geospatial-ai-november-2026)
- Publicado: 2026-11-09 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Esri informou que o suporte a MCP para conectar agentes externos ao ArcGIS está em beta no ArcGIS Location Platform e no ArcGIS Enterprise. O ArcGIS Maps SDK for JavaScript também oferece componentes de IA em beta para aplicativos cartográficos conversacionais, inclusive um agente de conhecimento que consulta serviços de grafo. No ArcGIS Pro 3.8, a empresa apresentou o modelo de observação da Terra EO-DINO, treinado com imagens RGB, multiespectrais e SAR, além de ferramentas de busca e detecção de mudanças por embeddings. Serviços de análise de texto, imagem e tradução estão disponíveis em geral no ArcGIS Online, com consumo de créditos.
- Por que importa: Há caminhos concretos para integrar agentes a dados espaciais e testar detecção semântica de mudanças. MCP e componentes conversacionais ainda são beta; adoção em projetos exige avaliar permissões, custos e desempenho local.
- Tags: #esri #arcgis #geoai #mcp #agentes-ia #eo-dino #embeddings #release
- Relações: [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]], [[Amaggi — Monitoramento de desmatamento]]
- Confiança: alta

### 2026-11-10 07:34 BRT — ArcGIS Velocity adiciona feeds de frota, análise contínua e suporte operacional no Enterprise

- Fonte: [Esri — novidades do ArcGIS Velocity em novembro de 2026](https://www.esri.com/arcgis-blog/products/arcgis-velocity/real-time/whats-new-in-arcgis-velocity-november-2026)
- Publicado: 2026-11-09 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O release de novembro acrescenta feeds para AIS marítimo, eventos de segurança e condições de vias da Samsara, inteligência de frota/estradas de outros fornecedores e entradas TCP/UDP no ArcGIS Enterprise. Novas análises incluem estatísticas móveis e extração por expressão regular; o Velocity também preserva valores M para referência linear. Na implantação Enterprise, há suporte a ArcGIS Monitor, federação de múltiplos sites e proxy reverso. A disponibilidade de cada feed ou recurso difere entre ArcGIS Online e Enterprise.
- Por que importa: Integração de telemetria, vias e eventos em tempo real pode apoiar rotas, logística e redes lineares. A edição demanda checar licença, fonte dos feeds e modalidade de implantação antes de desenhar o fluxo.
- Tags: #esri #arcgis-velocity #gis-tempo-real #logistica #frotas #telemetria #release
- Relações: [[Suzano — Rotas e logística]], [[Bracell — GeoIA Estradas]], [[TAG / TBG / NTS]]
- Confiança: alta

### 2026-11-10 07:34 BRT — ModelBuilder do Map Viewer passa a combinar análise raster e vetorial em beta

- Fonte: [Esri — análise raster no ModelBuilder do Map Viewer](https://www.esri.com/arcgis-blog/products/arcgis-online/announcements/raster-analysis-comes-to-modelbuilder-in-map-viewer-beta)
- Publicado: 2026-11-09 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O ArcGIS Online adicionou ao ModelBuilder do Map Viewer, em beta, 14 ferramentas raster, entradas de imagem hospedada e ambientes de análise configuráveis. Os modelos podem encadear operações raster e vetoriais, incluindo hidrologia, estatística zonal e conversão raster-vetor. Uma sessão Raster Optimized atende cargas maiores; durante o beta, usa a tarifa de créditos já aplicada às sessões do ModelBuilder. O uso requer tipo de usuário Professional ou superior e privilégio de análise de imagens.
- Por que importa: Permite prototipar processos reproduzíveis de terreno, vegetação e imagem sem separar modelos raster e vetoriais. A restrição a serviços de imagem hospedados e o consumo de créditos precisam entrar na avaliação.
- Tags: #esri #arcgis-online #modelbuilder #raster #automacao-geoespacial #beta
- Relações: [[Eucatex — Monitoramento de vigor florestal]], [[Itaminas — Monitoramento geotécnico]], [[São Martinho — Planejamento agrícola]]
- Confiança: alta

### 2026-11-10 07:34 BRT — Busca semântica chega em beta ao ArcGIS Online e ao Enterprise 12.2

- Fonte: [Esri — Semantic search (beta) no ArcGIS](https://www.esri.com/arcgis-blog/products/arcgis-online/announcements/semantic-search)
- Publicado: 2026-11-09 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Esri lançou busca semântica em beta no ArcGIS Online, com chegada anunciada ao ArcGIS Enterprise 12.2 ainda em novembro. O recurso usa embeddings de título, resumo e descrição dos itens para recuperar conteúdo por significado, além da correspondência literal de palavras-chave. No Online, um administrador precisa permitir recursos beta e a distribuição ocorre gradualmente; no Enterprise, a configuração requer credenciais de uma organização ArcGIS Online para o serviço de embeddings. A função retorna itens relacionados, não respostas gerais de um chatbot.
- Por que importa: Pode melhorar descoberta de camadas e mapas em catálogos grandes, desde que metadados estejam bem descritos. A dependência do serviço de embeddings e o status beta exigem revisão de governança.
- Tags: #esri #arcgis-online #arcgis-enterprise #busca-semantica #embeddings #metadados #beta
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-10 07:34 BRT — ArcGIS Workforce é aposentado; tarefas migram para Field Maps

- Fonte: [Esri — ArcGIS Workforce is retired](https://www.esri.com/arcgis-blog/products/field-maps/field-mobility/arcgis-workforce-is-retired)
- Publicado: 2026-11-09 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Esri confirmou a aposentadoria do ArcGIS Workforce com a atualização de novembro do ArcGIS Online e o ArcGIS Enterprise 12.2; o produto não recebe mais suporte. A função de coordenação de trabalho passa a Tasks no ArcGIS Field Maps, compatível com ArcGIS Online e Enterprise 11.5 ou posterior. O aplicativo móvel Workforce permanecerá nas lojas até outubro de 2027 para transição, mas sem atualizações, correções ou garantia de funcionamento contínuo.
- Por que importa: Operações de campo que ainda usem Workforce precisam planejar migração de projetos e treinamento para Tasks. A relação com os projetos citados é condicional ao uso desse produto.
- Tags: #esri #arcgis-workforce #field-maps #tarefas #campo #ciclo-de-vida
- Relações: [[IMAC — Plataforma GIS]], [[GeoFiscal-Sinter]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-11-10 07:34 BRT — Anthropic lança Claude Fable 5.2 e Mythos 5.2 para trabalho técnico complexo

- Fonte: [Anthropic — Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- Publicado: 2026-11-09 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Anthropic lançou Fable 5.2 e Mythos 5.2, variantes do mesmo modelo com salvaguardas de segurança diferentes. Fable é disponibilizado amplamente para tarefas técnicas, inclusive Claude Code; Mythos exige verificação para aplicações sensíveis em segurança cibernética ou biomedicina. A empresa informa preço de US$ 8 por milhão de tokens de entrada e US$ 40 por milhão de saída, com modo rápido opcional a US$ 16/US$ 80. Ganhos de desempenho e velocidade apresentados no anúncio são avaliações da própria Anthropic, não validação de resultados nos projetos.
- Por que importa: Muda a opção de modelo e custo para agentes de programação e pesquisa. Vale testar em tarefas próprias antes de adotar métricas de benchmark como ganho operacional.
- Tags: #anthropic #claude-code #agentes-ia #modelos #api #preco #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Klabin — IA]]
- Confiança: alta

### 2026-11-10 07:34 BRT — Copernicus avisa possível interrupção de APIs de processamento entre 10 e 13 de novembro

- Fonte: [Copernicus Data Space Ecosystem — atualização programada do Browser e Sentinel Hub](https://dataspace.copernicus.eu/news/2026-11-9-upgrade-copernicus-browser-and-sentinel-hub-services)
- Publicado: 2026-11-09 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Copernicus Data Space Ecosystem anunciou uma atualização de seus serviços Copernicus Browser e Sentinel Hub, prevista entre 10 e 13 de novembro de 2026. O aviso informa possibilidade de breves interrupções nas APIs Batch Processing, Asynchronous Processing e Batch Statistical, além de pequenos atrasos em visualizações de novos produtos de observação da Terra e na ingestão de tiles BYOC ou criação de coleções e configurações OGC. O comunicado não afirma indisponibilidade contínua durante todo o período.
- Por que importa: Pipelines de imagens e estatísticas que dependem dessas APIs devem prever tentativas de repetição, monitoramento e tolerância a atraso. Impacto nos projetos citados é condicional ao uso efetivo do serviço.
- Tags: #copernicus #sentinel-hub #api #sensoriamento-remoto #disponibilidade #operacao
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-11-10 07:34 BRT — DALTEX anuncia implantação da plataforma agronômica ORTH em suas operações

- Fonte: [Aydi Technologies/DALTEX — anúncio da implantação do ORTH](https://www.globenewswire.com/news-release/2026/11/09/3398825/0/en/daltex-one-of-the-world-s-largest-fresh-potato-exporters-deploys-ai-at-scale-with-orth.html)
- Publicado: 2026-11-09 12:04 ET (17:04 UTC; dentro da janela pesquisada)
- Resumo: A DALTEX, grupo agrícola egípcio, anunciou implantação da plataforma ORTH, da Aydi Technologies, em suas operações. Segundo as empresas, a solução reúne registros de campo, histórico de culturas, irrigação, previsões meteorológicas e imagens de satélite para fornecer respostas e alertas contextualizados a agrônomos e equipes de campo. O anúncio descreve uso operacional, mas não fornece avaliação independente dos alegados ganhos de produtividade ou redução de perdas.
- Por que importa: Exemplo verificável de integração de dados agronômicos e sensoriamento remoto em assistência à decisão no campo. Transferência a cana ou grãos exige validação própria; resultados anunciados não são prova de desempenho nesses cultivos.
- Tags: #agronegocio #agentes-ia #sensoriamento-remoto #irrigacao #agronomia #implantacao
- Relações: [[BP — Nutrição de plantas]], [[São Martinho — Planejamento agrícola]], [[CTC — Centro de Tecnologia Canavieira]]
- Confiança: média

### 2026-11-09 07:25 BRT — sem_novidade

### 2026-11-07 12:33 BRT — Claude Code adiciona proteção provisória contra exposição de e-mail em chamadas web

- Fonte: [Anthropic — discussão técnica e resposta da equipe no repositório Claude Code](https://github.com/anthropics/claude-code/issues/107757)
- Publicado: 2026-11-06 (horário/fuso da resposta não informados; janela exata de 24 horas não confirmada)
- Resumo: Usuários relataram que o Claude Code incluiu o e-mail da conta em cabeçalhos `User-Agent` de requisições geradas pelo agente. Integrantes da equipe Anthropic confirmaram que o endereço foi colocado no contexto do modelo e informaram que a versão 2.1.317 ou posterior traz uma proteção integrada, ativada por padrão, para barrar ou pedir confirmação em determinadas chamadas web e comandos `curl` que contenham o e-mail. A equipe também declarou que pretende retirar o endereço do contexto do modelo em um próximo release; essa remoção ainda não foi confirmada como entregue. A proteção atual não cobre todos os caminhos, como scripts escritos e executados pelo agente.
- Por que importa: Agentes com acesso à rede e dados corporativos precisam de controles de saída independentes do modelo. Equipes que usam Claude Code devem conferir versão/canal e evitar tratar a mitigação provisória como correção completa.
- Tags: #anthropic #claude-code #agentes-ia #seguranca #privacidade #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-07 12:33 BRT — Gemini ganha conectores para consulta governada de dados corporativos

- Fonte: [Google Cloud — Data Cloud connectors no Gemini](https://cloud.google.com/blog/products/data-analytics/query-enterprise-data-in-gemini-with-data-cloud-connectors/)
- Publicado: 2026-11-06 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Google Cloud apresentou, em prévia, conectores do Data Cloud que permitem consultar dados empresariais diretamente no Gemini por linguagem natural. A integração usa Knowledge Catalog para localizar fontes e interpretar termos, gera consultas sob a identidade do usuário e respeita permissões por linha e coluna. A cobertura descrita inclui BigQuery, Spanner, AlloyDB, Cloud SQL e Looker, com estados de disponibilidade distintos; administradores configuram conexões de leitura. Agentes analíticos configurados pela equipe de dados permanecem opção separada para fluxos mais controlados.
- Por que importa: Arquitetura concreta para perguntas sobre bases heterogêneas sem conceder privilégios globais ao agente. Relevância para sistemas corporativos e acervos geoespaciais é inferência de aplicação, não implantação nos projetos.
- Tags: #google-cloud #gemini #agentes-ia #bigquery #governanca #dados #preview
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-07 12:33 BRT — BigQuery DataFrames expõe funções de IA em objetos pandas

- Fonte: [Google Cloud — BigQuery AI Functions in Pandas](https://cloud.google.com/blog/products/data-analytics/bigquery-ai-functions-in-pandas)
- Publicado: 2026-11-06 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Google Cloud documentou um novo acessor `.bigquery` do BigQuery DataFrames para chamar funções de IA a partir de DataFrames pandas. No exemplo, `ai.predict()` traduz a operação para GoogleSQL e executa o modelo TabFM na infraestrutura do BigQuery, devolvendo resultados em pandas. A proposta abrange previsão, classificação e embeddings sem transferir a computação principal para o notebook local; uso requer projeto Google Cloud autorizado e configuração da biblioteca.
- Por que importa: Pode reduzir código de integração entre notebooks e análise escalável de tabelas operacionais. Aplicação a séries agrícolas, florestais ou logísticas é possibilidade técnica, não resultado já validado.
- Tags: #google-cloud #bigquery #pandas #ia #api #analise-de-dados #release
- Relações: [[São Martinho — Planejamento agrícola]], [[Eucatex — Monitoramento de vigor florestal]], [[Suzano — Rotas e logística]]
- Confiança: alta

### 2026-11-03 07:31 BRT — NOAA encerra distribuição de dados do satélite S-NPP

- Fonte: [NOAA/NESDIS — aviso operacional de encerramento do S-NPP](https://www.nesdis.noaa.gov/news/update-4-cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-november-02-2026-1540-utc-and-decommissioning-issued-november-2-2026-1800-utc)
- Publicado: 2026-11-02 18:00 UTC; interrupção efetiva em 2026-11-02 15:40 UTC (ambos dentro da janela pesquisada)
- Resumo: A NOAA confirmou o fim permanente da distribuição de produtos científicos do satélite Suomi NPP às 15:40 UTC de 2 de novembro. A transmissão direta HRD também foi desligada. A mudança afeta, entre outros instrumentos, o VIIRS; a agência indica NOAA-21 como fonte principal e NOAA-20 como secundária para produtos científicos semelhantes.
- Por que importa: Fluxos de monitoramento florestal, queimadas ou ambiente que dependam especificamente de S-NPP/VIIRS precisam verificar fonte substituta e continuidade da série. Não implica fim de todos os produtos VIIRS.
- Tags: #noaa #snpp #viirs #sensoriamento-remoto #florestal #ciclo-de-vida #dados
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]], [[Klabin — IA]]
- Confiança: alta

### 2026-11-03 07:31 BRT — Halliburton lança plataforma para decisões de desenvolvimento de campos de óleo e gás

- Fonte: [Halliburton — Agile Asset Management](https://ir.halliburton.com/node/36696/pdf)
- Publicado: 2026-11-03 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Halliburton anunciou o Agile Asset Management (AAM), solução em nuvem da Landmark que integra dados e fluxos de subsuperfície, poços, instalações e economia para comparar alternativas de desenvolvimento de campos. Segundo a empresa, agentes de IA apoiam recuperação de dados, checagens de qualidade e orientação ao usuário. Aker BP participou do codesenvolvimento e descreve uso para avaliar alternativas com trilha auditável de premissas e decisões.
- Por que importa: Integração multidisciplinar e rastreabilidade são referência técnica para projetos de conhecimento e planejamento no setor de óleo e gás. Ganhos de tempo anunciados ainda não constituem validação independente.
- Tags: #oleo-e-gas #halliburton #landmark #agentes-ia #planejamento #dados #lancamento
- Relações: [[Petrobras — Segundo cérebro]], [[TAG / TBG / NTS]]
- Confiança: alta

### 2026-11-03 07:31 BRT — ADNOC, OpenAI e G42 firmam parceria para decisões integradas em energia

- Fonte: [ADNOC — parceria com OpenAI e G42](https://www.adnoc.ae/media-center/news/2026/11/ADNOC-Signs-Landmark-Partnership-Agreement-with-OpenAI)
- Publicado: 2026-11-02 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A ADNOC anunciou parceria plurianual com OpenAI e G42 para desenvolver e implantar capacidade de decisão baseada em agentes, usando modelos da OpenAI e infraestrutura de IA nos Emirados Árabes Unidos. O primeiro foco é planejamento integrado de campos, conectando dados de poços, reservatórios, instalações e custos; o segundo é análise de decisões ao longo da cadeia de produção, refino, logística e comercialização. A empresa afirma que especialistas manterão supervisão das decisões consequenciais.
- Por que importa: Caso setorial de arquitetura que conecta dados técnicos e comerciais em vez de otimizar cada etapa isoladamente. Trata-se de parceria e plano de implantação; resultados operacionais das duas aplicações ainda não foram demonstrados publicamente.
- Tags: #oleo-e-gas #adnoc #openai #g42 #agentes-ia #planejamento #parceria
- Relações: [[Petrobras — Segundo cérebro]], [[TAG / TBG / NTS]]
- Confiança: alta

### 2026-11-03 07:31 BRT — Artigo testa indicadores espaciais de acesso em estradas florestais

- Fonte: [Turkish Journal of Forestry — sistema espacial para acessibilidade de estradas florestais](https://dergipark.org.tr/en/pub/tjf/article/1946209)
- Publicado: 2026-11-02 conforme página do periódico (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: Taha Yasin Hatay apresentou um sistema web de apoio à decisão que automatiza análise de acesso em redes de estradas florestais com GeoPandas, Shapely e Leaflet. Em estudo com 245,9 km de estradas e 11.463,4 ha, a área considerada acessível variou de 18,33% a 66,00% conforme cenário de buffer de 50 a 250 m, apesar de a densidade nominal da rede ser 26,23 m/ha. O artigo mostra que densidade de estradas, sozinha, não descreve a cobertura operacional.
- Por que importa: Métrica espacial e análise por cenários são transferíveis como hipótese de avaliação para malhas florestais; percentuais do estudo turco não devem ser aplicados diretamente a operações brasileiras.
- Tags: #florestal #estradas-florestais #gis #logistica #paper #acessibilidade #planejamento
- Relações: [[Bracell — GeoIA Estradas]], [[Suzano — Rotas e logística]]
- Confiança: alta

### 2026-11-03 07:31 BRT — Google amplia detecção de anomalias em agentes com inscrição automática

- Fonte: [Google Cloud — Agent Anomaly Detection](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-anomalies-overview)
- Publicado: recurso adicionado em 2026-11-02; documentação atualizada em 2026-11-03 UTC (horário de lançamento não informado; janela exata de 24 horas não confirmada)
- Resumo: O Google Cloud adicionou à prévia de Agent Anomaly Detection a inscrição automática de agentes elegíveis encontrados em um projeto. O serviço analisa logs e rastros OpenTelemetry de forma assíncrona para detectar uso indevido de ferramentas, abuso de privilégios, falhas em cascata e consumo anormal de recursos. A ativação depende de requisitos como ADK Python 2.1.0+, telemetria configurada e acesso aprovado ao produto; agentes descobertos não geram análise ou custo até serem habilitados.
- Por que importa: Governança de agentes pode ganhar cobertura automática, mas exige instrumentação e política explícita de coleta de prompts e respostas. É referência para arquiteturas corporativas, não recurso disponível universalmente.
- Tags: #google-cloud #agentes-ia #observabilidade #seguranca #opentelemetry #preview
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-11-03 07:31 BRT — Mandiant documenta abuso de credenciais e endpoints de modelos de IA

- Fonte: [Google Threat Intelligence/Mandiant — LLMJacking](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models/)
- Publicado: 2026-11-02 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Mandiant relatou incidentes reais de 2026 em que invasores usaram chaves de API válidas ou endpoints de modelos expostos para consumir recursos de IA de empresas sem autorização. A investigação cobre múltiplos provedores e organizações de vários continentes, inclusive transporte; em casos observados, as cobranças fraudulentas ultrapassaram US$ 100 mil em um único dia. O relatório descreve também intermediários que revendem o acesso desviado.
- Por que importa: Projetos com agentes e modelos em nuvem precisam controlar credenciais, exposição de endpoints, limites de uso e alertas de custo. Valores relatados são dos incidentes investigados, não previsão de risco para estes projetos.
- Tags: #agentes-ia #seguranca #api #credenciais #custos #mandiant #incidente
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-11-02 07:28 BRT — sem_novidade

### 2026-10-30 07:33 BRT — Codex CLI 0.166.0 amplia retomada de tarefas e diagnóstico de rede

- Fonte: [OpenAI — Codex CLI 0.166.0](https://github.com/openai/codex/releases/tag/rust-v0.166.0)
- Publicado: 2026-10-29 19:47 (horário exibido pelo GitHub; fuso não informado)
- Resumo: A OpenAI lançou o Codex CLI 0.166.0 com `codex queue --resume`, que retoma uma conversa não carregada após enfileirar uma mensagem, e `codex doctor --network-only`, voltado a diagnósticos de configuração, conexão e WebSocket. O release também adiciona GPT-6.1 Terra aos catálogos de modelos locais, Vertex AI e Amazon Bedrock, além de melhorar a explicação de bloqueios de segurança e a preservação de permissões ao retomar ou bifurcar conversas.
- Por que importa: Retomada mais confiável e diagnóstico isolado ajudam a operar agentes de desenvolvimento em fluxos longos e ambientes corporativos. A disponibilidade de modelos em cada provedor ainda depende da conta e da região.
- Tags: #openai #codex #agentes-ia #cli #automacao #diagnostico #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-30 07:33 BRT — Google Knowledge Catalog passa a reunir modelos semânticos para agentes

- Fonte: [Google Cloud — suporte ampliado a modelos semânticos no Knowledge Catalog](https://cloud.google.com/blog/products/data-analytics/expanded-semantic-model-support-in-knowledge-catalog/)
- Publicado: 2026-10-29 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Google Cloud anunciou disponibilidade geral do suporte ampliado a modelos semânticos no Knowledge Catalog. A plataforma indexa definições de métricas e relações de LookML, BigQuery Graph, dbt MetricFlow, Snowflake Semantic Views, Databricks Metric Views e SAP CSN em um grafo de contexto, associando-as a metadados como linhagem, qualidade e glossário. Definições divergentes são mantidas com proveniência para revisão, sem exigir migração dos dados ou reescrita da lógica de negócio.
- Por que importa: Agentes analíticos podem consultar conceitos e métricas governados em vez de inferir junções e fórmulas a cada pergunta. É referência de arquitetura para ligar dados corporativos e projetos, não evidência de implantação nesses projetos.
- Tags: #google-cloud #knowledge-catalog #agentes-ia #modelo-semantico #grafo-de-contexto #governanca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-30 07:33 BRT — Esri Calcite 5.2 melhora componentes de interfaces ArcGIS

- Fonte: [Esri — novidades do Calcite Design System 5.2](https://www.esri.com/arcgis-blog/products/developers/announcements/calcite-design-system-whats-new-in-5-2)
- Publicado: 2026-10-29 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Esri detalhou o Calcite Design System 5.2, biblioteca de componentes usada em aplicações da plataforma ArcGIS. A versão acrescenta edição inline em campos de entrada, cabeçalho fixo em tabelas, novos comportamentos de barra de ações e grupos, suporte ao esquema de cores do navegador e melhorias de acessibilidade e internacionalização. O componente Inline Editable foi descontinuado e está previsto para remoção em uma futura versão com mudanças incompatíveis.
- Por que importa: Equipes que mantêm interfaces GIS customizadas podem aproveitar os componentes novos e planejar a substituição do componente descontinuado antes da próxima quebra de compatibilidade.
- Tags: #esri #arcgis #calcite #interface-gis #acessibilidade #ciclo-de-vida #release
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-30 07:33 BRT — Purdue demonstra protótipo de modelo de crescimento florestal para o Peru

- Fonte: [Purdue University — protótipo MATRIX Peru](https://ag.purdue.edu/news/2026/10/prototype-forest-growth-model-demonstrated-for-peru-application.html)
- Publicado: 2026-10-29 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: Pesquisadores da Purdue University, com a FAO e o serviço florestal peruano SERFOR, relataram a demonstração de um protótipo do Global Forest MATRIX adaptado ao Peru durante oficina realizada em agosto. O trabalho busca usar inventários florestais locais para projetar mudanças sob cenários de ambiente e manejo; um harmonizador de dados foi apresentado para converter registros coletados por protocolos distintos a um formato comum.
- Por que importa: A adaptação ilustra um caminho prático para conectar inventários heterogêneos a modelos de dinâmica florestal. Ainda é protótipo em desenvolvimento, sem validação publicada para florestas brasileiras.
- Tags: #florestal #geoia #ia #inventario-florestal #modelagem #peru #prototipo
- Relações: [[Eucatex — Monitoramento de vigor florestal]], [[Klabin — IA]]
- Confiança: alta

### 2026-10-29 07:35 BRT — Plugin MCP do ServiceNow chega ao marketplace OpenAI

- Fonte: [OpenAI — expansão da parceria com ServiceNow](https://openai.com/index/openai-servicenow-partnership-expansion/)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: plugin MCP já disponível conecta contexto e ações de instâncias ServiceNow ao ChatGPT, respeitando regras e permissões do cliente. É referência concreta para agentes corporativos que consultam incidentes e executam ações governadas; integração Codex no AI Workflow Factory é apenas planejada para 2027, não recurso atual.
- Tags: #openai #servicenow #mcp #agentes-ia #codex #integracao #governanca
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-29 07:35 BRT — Gemini Enterprise passa a oferecer região Brasil com residência local de dados

- Fonte: [Google Cloud — release notes de 28/10](https://docs.cloud.google.com/release-notes#October_28_2026)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: Google anuncia região brasileira para Gemini Enterprise, com dados em repouso e processamento de ML na região; disponibilidade geral condicionada a allowlist. Pode destravar avaliação de agentes sobre dados corporativos brasileiros sensíveis, mas requer acesso liberado e verificação contratual antes de qualquer arquitetura.
- Tags: #google-cloud #gemini-enterprise #brasil #residencia-de-dados #agentes-ia #governanca #release
- Relações: [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-10-29 07:35 BRT — AlloyDB libera índice vetorial de quatro níveis para até 10 bilhões de linhas

- Fonte: [Google Cloud — release notes do AlloyDB AI](https://docs.cloud.google.com/release-notes#October_28_2026)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: índice ScaNN 4LT em PostgreSQL 17+ entra em disponibilidade geral, com manutenção automática e busca filtrada com melhor recuperação; `Vector assist` também passa a GA. Amplia opção de busca semântica em grandes acervos geoespaciais/documentais, sem implicar necessidade de escala bilionária nos projetos atuais.
- Tags: #google-cloud #alloydb #busca-vetorial #embeddings #rag #postgresql #release
- Relações: [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-29 07:35 BRT — Google publica skills oficiais para agentes criarem integrações via API

- Fonte: [Google Cloud — Application Integration agent skills](https://docs.cloud.google.com/application-integration/docs/agent-skills-overview)
- Publicado: 2026-10-28 (data do release e da atualização da documentação; horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: três skills abertas orientam agentes a configurar, criar/publicar e diagnosticar integrações do Google Cloud Application Integration via REST API. Fornecem referência operacional para automatizar fluxos entre sistemas corporativos com IAM e versionamento; uso nos projetos depende da adoção dessa plataforma.
- Tags: #google-cloud #skills #agentes-ia #integracao #api #automacao #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-29 07:35 BRT — CodeMender 0.17 reforça limites de sandbox e políticas de agentes de código

- Fonte: [Google Cloud — release notes de 28/10, CodeMender 0.17.0](https://docs.cloud.google.com/release-notes#October_28_2026)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: nova versão separa configuração de sandbox da política de comandos, protege `.git/hooks`, `.git/config` e `.codemender` contra alterações durante correções e fecha travessia por symlinks fora de `allowedRoots`. Medidas relevantes ao avaliar agentes que editam repositórios com acesso a dados ou infraestrutura corporativa.
- Tags: #google-cloud #codemender #agentes-ia #seguranca #sandbox #desenvolvimento #release
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-28 12:35 BRT — Esri publica medidas para falha crítica no Brotli; impacto em ArcGIS sob investigação

- Fonte: [Esri — Brotli Vulnerabilities (Broccoli2Shell)](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/brotli-vulnerabilities-broccoli2shell)
- Publicado: 2026-10-27 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: Esri investiga o impacto de CVE-2026-111497 em seus produtos e recomenda atualizar o .NET Framework usado por ArcGIS Pro, Web Adaptor em IIS e extensões SOE/SOI; ArcGIS Online já recebeu medidas mitigadoras. Quem opera ArcGIS Enterprise deve verificar versões e acompanhar a avaliação, sem presumir que todo produto está vulnerável.
- Tags: #esri #arcgis #arcgis-enterprise #brotli #cve #seguranca #patch
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-28 12:35 BRT — Patch corrige geocodificação quebrada entre ArcGIS Pro 3.6 e Server 11.5

- Fonte: [Esri — ArcGIS Server 11.5 Geocoding Capability Patch](https://support.esri.com/en-us/patches-updates/2026/arcgis-server-11-5-geocoding-capability-patch)
- Publicado: 2026-10-27 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: serviços de geocodificação publicados do ArcGIS Pro 3.6 ou posterior no ArcGIS Server 11.5 podem devolver zero resultados, inclusive via `FindAddressCandidates` e `GeocodeAddresses`. Esri recomenda o patch para instalações afetadas; planejar reinício do serviço e rollback antes de aplicar.
- Tags: #esri #arcgis-enterprise #arcgis-pro #geocodificacao #api #patch #logistica
- Relações: [[Suzano — Rotas e logística]], [[GeoNext — LiDAR e rodovias]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-10-28 12:35 BRT — EDGX divulga demonstração de computação de IA em órbita

- Fonte: [EDGX — Sterna em órbita](https://www.edgx.space/blog/edgx-launches-ai-computing-platform-in-orbit-on-spacex-transporter-16-using-nvidia-accelerated-computing)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: empresa reporta que carga baseada em NVIDIA Jetson, lançada em março, já retornou dados operacionais em órbita; outra ainda está em comissionamento. Processar imagens a bordo pode reduzir volume transmitido e latência de alertas geoespaciais, mas a fonte não demonstra ainda serviço comercial ou desempenho dessas aplicações.
- Tags: #geoia #edge-ai #observacao-da-terra #satelites #nvidia #demonstracao
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Vale — GeoIA SAB.IA]]
- Confiança: média

### 2026-10-23 07:29 BRT — OlmoEarth v1.3 libera embeddings planetários anuais de 10 m

- Fonte: [Ai2 — OlmoEarth v1.3](https://allenai.org/blog/olmoearth-v1-3)
- Publicado: 2026-10-22 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: o Ai2 liberou modelo, dados e embeddings globais pré-computados (64/128 dimensões) e um explorador para encontrar áreas semelhantes e criar mapas com poucos exemplos. Reduz o esforço para testar classificação de culturas, vigor e mudança de cobertura em projetos GeoIA; desempenho local ainda precisa ser validado.
- Tags: #geoia #olmoearth #sensoriamento-remoto #embeddings #sentinel #landsat #agro #florestal #release
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-23 07:29 BRT — PLANTEUR expõe lacuna de generalização na classificação de culturas tropicais

- Fonte: [Ai2 — PLANTEUR: benchmark de culturas tropicais](https://allenai.org/blog/planteur)
- Publicado: 2026-10-22 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: novo conjunto aberto reúne séries Sentinel-1/2 e Landsat-8 de 4.506 km² de parcelas, sete classes de culturas (incluindo cana) e testes fora da região de treino. Nos testes dos autores, todos os métodos perderam cerca de metade da acurácia em uma ilha não vista: alerta concreto para validar modelos agrícolas fora da área de treinamento.
- Tags: #geoia #paper #benchmark #agro #cana-de-acucar #classificacao-de-culturas #generalizacao #sentinel
- Relações: [[CTC — Centro de Tecnologia Canavieira]], [[Atvos — Visão computacional]], [[São Martinho — Planejamento agrícola]]
- Confiança: alta

### 2026-10-23 07:29 BRT — Claude Code 2.1.309 corrige contornos de sandbox e proteção de configuração MCP

- Fonte: [Anthropic — Claude Code v2.1.309](https://github.com/anthropics/claude-code/releases/tag/v2.1.309)
- Publicado: 2026-10-22 22:18 (horário exibido pelo GitHub; fuso não informado)
- Por que importa: o release corrige execução de arquivos de inicialização do shell fora do sandbox, falhas de regras de escrita via symlink, alteração indevida do arquivo `--mcp-config` e contornos de permissões Bash/worktree. É atualização prioritária para agentes com acesso a código, arquivos e servidores MCP; revisar políticas após atualizar.
- Tags: #anthropic #claude-code #mcp #agentes-ia #sandbox #seguranca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-23 07:29 BRT — OpenAI disponibiliza Decisions API para decisões delimitadas de agentes

- Fonte: [OpenAI — Decisions API](https://openai.com/index/decisions-api/)
- Publicado: 2026-10-22 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: API agora em disponibilidade geral responde probabilidade, escolha ou escore a partir de texto, imagem ou JSON, com até 400 perguntas por requisição. Pode reduzir latência/custo de triagem e roteamento em agentes e eventos geoespaciais; o ganho de até 10 vezes é alegação da OpenAI, não garantia para estes projetos.
- Tags: #openai #decisions-api #agentes-ia #api #classificacao #roteamento #release
- Relações: [[NAVIS / GeoFramework]], [[Atvos — Visão computacional]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-23 07:29 BRT — ICEYE e OroraTech integram dados térmicos e SAR para incêndios

- Fonte: [OroraTech — parceria com ICEYE](https://ororatech.com/resources/news-blog/iceye-partners-with-ororatech-to-deliver-full-lifecycle-wildfire-intelligence-2)
- Publicado: 2026-10-22 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: a parceria anuncia integração de detecção/avanço do fogo por satélites térmicos com observações SAR para avaliar impactos mesmo sob fumaça e nuvens. É combinação relevante para monitoramento florestal e resposta a incêndios; a fonte não traz validação independente de latência ou implantação em cliente.
- Tags: #sensoriamento-remoto #sar #termal #incendios #florestal #parceria #observacao-da-terra
- Relações: [[Eucatex — Monitoramento de vigor florestal]], [[Amaggi — Monitoramento de desmatamento]]
- Confiança: alta

### 2026-10-22 07:27 BRT — Claude Code 2.1.307 evita duplicar chamadas de escrita via MCP HTTP

- Fonte: [Anthropic — Claude Code v2.1.307](https://github.com/anthropics/claude-code/releases/tag/v2.1.307)
- Publicado: 2026-10-21 22:17 (horário exibido pelo GitHub; fuso não informado)
- Por que importa: se a conexão caía durante uma chamada MCP HTTP, ferramentas podiam ser acionadas duas vezes; agora só operações de leitura ou idempotentes são repetidas. Release também adiciona evento OpenTelemetry para decisões de segurança e corrige atualização de ferramentas de servidores MCP do SDK durante tarefas em segundo plano — pontos críticos para agentes que escrevem em sistemas corporativos.
- Tags: #anthropic #claude-code #mcp #agentes-ia #idempotencia #observabilidade #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-22 07:27 BRT — Modelos OpenAI e fluxos Codex entram no Google Cloud em prévia privada

- Fonte: [Google Cloud — OpenAI models in Model Garden](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers) e [OpenAI — parceria com Google Cloud](https://openai.com/index/openai-models-google-cloud/)
- Publicado: 2026-10-21 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: GPT-6 Astra, GPT-6.1 Sol e GPT-6 Luna começam a chegar ao Model Garden para clientes empresariais selecionados; Google informa que esses clientes já podem conectar Codex CLI/Desktop para inferência na plataforma. Isso cria opção de testar agentes e desenvolvimento com governança, auditoria e faturamento Google Cloud, mas ainda não é disponibilidade geral.
- Tags: #openai #codex #google-cloud #model-garden #agentes-ia #parceria #preview
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-22 07:27 BRT — Esri avalia impacto de duas falhas críticas de PHP no ecossistema ArcGIS

- Fonte: [Esri — Recent PHP Vulnerabilities](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/recent-php-vulnerabilities) e [PHP Project — alerta e versões corrigidas](https://www.php.net/archive/2026.php)
- Publicado: 2026-10-21 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: PHP corrigiu CVE-2026-109618 e CVE-2026-109619, ambas com potencial de execução remota sem autenticação, nas versões 8.5.12, 8.4.27, 8.3.36 e 8.2.35. Esri informa que ArcGIS Online não usa PHP e ainda avalia demais produtos; não há impacto confirmado em ArcGIS Enterprise. Verificar componentes PHP próprios ou adjacentes e acompanhar conclusão da avaliação Esri.
- Tags: #esri #arcgis #php #seguranca #cve #infraestrutura #avaliacao-de-impacto
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-21 07:27 BRT — Claude Code 2.1.305 corrige integração MCP, gateways e retomada de agentes

- Fonte: [Anthropic — Claude Code v2.1.305](https://github.com/anthropics/claude-code/releases/tag/v2.1.305)
- Publicado: 2026-10-20 20:46 (horário exibido pelo GitHub; fuso não informado)
- Por que importa: corrige a substituição indevida de servidores MCP fornecidos pela sessão em nuvem/SDK e falhas de requisições via Vertex, Bedrock ou gateways sem ToolSearch. A retomada de workflows deixa de reexecutar agentes já concluídos. A nova opção de namespaces aninhados no Linux permite Chromium/Podman, mas pode contornar proteções de arquivos do sandbox; requer avaliação antes de habilitar.
- Tags: #anthropic #claude-code #mcp #agentes-ia #workflow #seguranca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-21 07:27 BRT — Alerta de segurança no SDK TypeScript do MCP exige validação explícita de audiência

- Fonte: [GitHub Advisory — GHSA-rvq5-wwqv-78pq / CVE-2026-111771](https://github.com/advisories/GHSA-rvq5-wwqv-78pq)
- Publicado: aviso original em 2026-10-05; publicado na base de advisories e atualizado em 2026-10-20 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: servidores MCP HTTP que usam `requireBearerAuth()`/`verifyBearerToken()` podem aceitar token emitido para outro serviço se o emissor atende múltiplos recursos e o verificador não checa `aud`. Versões corrigidas existem, mas só atualizar não ativa a proteção: é preciso configurar `expectedResource` e devolver `AuthInfo.resource`, ou validar `aud` no verificador.
- Tags: #mcp #typescript #sdk #oauth #seguranca #cve #agentes-ia
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-21 07:27 BRT — Gemini em Google Distributed Cloud ganha busca RAG isolada da internet

- Fonte: [Google Cloud — Managed RAG search inside the sovereign perimeter](https://cloud.google.com/blog/topics/hybrid-cloud/managed-rag-search-inside-the-sovereign-perimeter-gemini-on-gdc-enterprise-search)
- Publicado: 2026-10-21 (horário/fuso não informados; posição exata na janela de 24 horas não confirmada)
- Por que importa: em *preview*, busca empresarial multimodal com citações roda em GDC air-gapped, com ingestão, embeddings, PostgreSQL e controles de identidade dentro do perímetro local. Arquitetura relevante para agentes sobre dados técnicos sigilosos de mineração e óleo e gás; ainda não é disponibilidade geral.
- Tags: #google-cloud #gemini #rag #air-gap #dados-sensiveis #agentes-ia #busca-empresarial
- Relações: [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-10-21 07:27 BRT — llm-d 1.0 publica infraestrutura aberta para inferência de agentes em escala

- Fonte: [Google Cloud — Announcing llm-d 1.0](https://cloud.google.com/blog/topics/ai-infrastructure/llm-d-1-0-an-open-source-stack-for-distributed-inference)
- Publicado: 2026-10-20 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: release Kubernetes-native reúne roteamento com afinidade de cache, QoS multitenant, cache KV em camadas, alta disponibilidade e atualização sem interromper sessões. É base técnica para avaliar custo e latência de agentes auto-hospedados com contexto longo e tráfego irregular, sem implicar ganho garantido nos projetos.
- Tags: #google-cloud #llm-d #inferencia #kubernetes #agentes-ia #infraestrutura #open-source
- Relações: [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-21 07:27 BRT — Tanager-2 demonstra detecção hiperespectral de metano na primeira imagem

- Fonte: [Planet — First light from Tanager-2 and SuperDove Flock 4J](https://www.planet.com/pulse/sharing-first-light-images-from-tanager-2-and-superdove-flock-4j/)
- Publicado: 2026-10-20 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: a Planet divulgou a primeira imagem do Tanager-2, capturada em 07/10, na qual a Carbon Mapper detectou pluma de metano na costa espanhola. Demonstra uma aplicação da nova constelação para emissões e prospecção mineral, mas os satélites ainda estão em comissionamento; não equivale a serviço operacional disponível.
- Tags: #planet #tanager #hiperespectral #metano #oleo-e-gas #mineracao #observacao-da-terra
- Relações: [[TAG / TBG / NTS]], [[Vale — GeoIA SAB.IA]], [[Itaminas — Monitoramento geotécnico]]
- Confiança: alta

### 2026-10-20 07:28 BRT — Servidores oficiais MCP chegam à versão 2.0

- Fonte: [Model Context Protocol — servers v2.0.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.0.0)
- Publicado: 2026-10-19 06:46 (horário exibido pelo GitHub; fuso não informado; posição exata na janela de 24 horas não confirmada)
- Por que importa: servidores oficiais de filesystem, memory, fetch, git e time passam a servir a revisão MCP 2026-07-28 mantendo clientes legados. Pacotes TypeScript exigem Node 24; Python exige `mcp>=2.3,<3`. A atualização altera respostas de erro e corrige condições de corrida na atualização de roots do filesystem, exigindo testes de compatibilidade e permissões.
- Tags: #mcp #servidores #release #interoperabilidade #seguranca #nodejs #python #agentes-ia
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-20 07:28 BRT — Gemini Enterprise documenta MCP Apps interativos com servidor privado

- Fonte: [Google Cloud — Developer’s guide to implementing MCP apps in Gemini](https://cloud.google.com/blog/topics/developers-practitioners/devs-guide-to-mcp-apps-in-gemini)
- Publicado: 2026-10-19 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: ferramentas MCP podem entregar interface interativa dentro do chat do Gemini Enterprise, hospedada em Cloud Run privado. O guia detalha dois níveis de autenticação, controles de acesso e aprovação humana; arquitetura útil para agentes que combinam mapas, inspeção espacial e ações corporativas sem recriar chat e identidade.
- Tags: #google-cloud #gemini-enterprise #mcp-apps #agentes-ia #interface-interativa #cloud-run #governanca
- Relações: [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-20 07:28 BRT — Exyn integra equipe selecionada para projeto de mapeamento autônomo subterrâneo

- Fonte: [Exyn Technologies — MAP-POD/Mine of the Future](https://www.globenewswire.com/fr/news-release/2026/10/19/3383494/0/en/exyn-technologies-joins-national-laboratory-led-autonomous-mining-project-selected-under-doe-s-29-5-million-mine-of-the-future-initiative.html) e [DOE — projetos selecionados](https://www.energy.gov/cmei/mining/lab-call-mine-future-research-development-and-demonstration)
- Publicado: 2026-10-19 09:00 ET (comunicado da Exyn); seleção do DOE anunciada em 2026-09-30
- Por que importa: projeto MAP-POD combina robótica, sensores hiperespectrais e IA para mapear minas e localizar minerais em ambiente sem GPS. A Exyn prevê contribuir navegação autônoma para veículos terrestres; o financiamento ainda está em negociação, portanto não é implantação concluída.
- Tags: #mineracao #geoia #robotica #mapeamento-subterraneo #hiperespectral #autonomia #sem-gps
- Relações: [[Itaminas — Monitoramento geotécnico]], [[Vale — GeoIA SAB.IA]], [[Vale — Fechamento de minas]]
- Confiança: alta

### 2026-10-20 07:28 BRT — OpenAI publica benchmark reproduzível para codificação e migração de legados

- Fonte: [OpenAI — Advancing coding in low-resource programming languages](https://openai.com/index/low-resource-programming-languages/) e [MultiLangBench — código e testes](https://github.com/openai/MultiLangBench)
- Publicado: 2026-10-19 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: avaliação em 20 linguagens mede geração de software e migração com testes de comportamento; resultados e suíte são liberados para inspeção. Mostra ganhos em COBOL, Fortran e Visual Basic, mas a aplicação em sistemas críticos ainda requer validação humana e testes próprios — referência para modernização de código técnico legado.
- Tags: #openai #modelos-de-codigo #benchmark #fortran #cobol #modernizacao #migracao-de-codigo #avaliacao
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-19 07:31 BRT — sem_novidade

### 2026-10-17 09:09 BRT — Claude Code 2.1.302 corrige interoperabilidade MCP e altera execução de subagentes

- Fonte: [Anthropic — Claude Code v2.1.302](https://github.com/anthropics/claude-code/releases/tag/v2.1.302)
- Publicado: 2026-10-16 20:53 (horário exibido pelo GitHub; fuso não informado)
- Por que importa: corrige servidores MCP que negociam o protocolo 2026-07-28 sem certos campos de resposta e muda o comportamento padrão de subagentes no desktop, VS Code e Agent SDK. Integrações e fluxos multiagente devem ser testados após atualização; também corrige uma rotina em nuvem que podia repetir trabalho depois de falhar.
- Tags: #anthropic #claude-code #mcp #agentes-ia #subagentes #release #automacao
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-17 09:09 BRT — AWS encerra criação de relatórios AgentCore Insights na prévia

- Fonte: [AWS — AgentCore Insights](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/insights.html)
- Publicado: mudança efetiva em 2026-10-16 (horário/fuso e data de publicação do aviso não informados; janela exata de 24 horas não confirmada)
- Por que importa: novos relatórios em lote ou recorrentes deixam de ser criados em 16/10; os recorrentes existentes param de gerar relatórios em 31/10. Equipes que usam essa prévia para avaliar falhas de agentes precisam preservar resultados e planejar outra observabilidade antes da descontinuação.
- Tags: #aws #bedrock #agentcore #agentes-ia #observabilidade #ciclo-de-vida
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-17 09:09 BRT — Google muda modelo estável do Agent Search

- Fonte: [Google Cloud — Agent Search release notes](https://docs.cloud.google.com/generative-ai-app-builder/docs/release-notes)
- Publicado: 2026-10-16 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Por que importa: o alias `stable` de geração de respostas passa de Gemini 2.5 Flash para `gemini-3.5-flash/answer_gen/v1`. Aplicações de busca e resposta que dependem desse alias podem mudar qualidade, latência e comportamento sem alterar código; convém revalidar avaliações e respostas críticas.
- Tags: #google-cloud #agent-search #gemini #modelo #api #avaliacao #agentes-ia
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-15 07:29 BRT — Esri publica correção crítica para ArcGIS Server

- Fonte: [Esri — ArcGIS Server Security 2026 Update 3 Patch](https://support.esri.com/en-us/patches-updates/2026/arcgis-server-security-2026-update-3-patch) e [boletim de segurança](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/october-2026-arcgis-security-bulletin)
- Publicado: patch em 2026-10-13; boletim em 2026-10-14 (horário/fuso não informado; janela exata de 24 horas não confirmada)
- Por que importa: patch cumulativo cobre ArcGIS Server 12.1, 12.0, 11.5, 11.3 e 11.1 em Windows e Linux, incluindo falha de injeção SQL com CVSS 9,8. Ambientes ArcGIS Enterprise devem verificar versão, planejar implantação e considerar que a instalação reinicia o serviço.
- Tags: #esri #arcgis-server #arcgis-enterprise #seguranca #patch #cve #sql-injection
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-15 07:29 BRT — Planet adiciona banda red-edge e acelera entrega de imagens ARPS

- Fonte: [Planet Documentation — ARPS v1.2.0 Release Notes](https://docs.planet.com/)
- Publicado: 2026-10-14 (horário/fuso não informado; janela exata de 24 horas não confirmada)
- Por que importa: ARPS 1.2 oferece produto opcional de cinco bandas com red-edge; o produto de quatro bandas chega cerca de 17 horas antes e recebeu correções radiométricas para vegetação densa e ciclos rápidos de crescimento, além de máscara de nuvens melhorada. Isso afeta séries de NDVI e detecção de vigor em florestas e lavouras; a quinta banda exige nova assinatura e o acervo anterior não será reprocessado.
- Tags: #planet #arps #red-edge #ndvi #sensoriamento-remoto #florestal #agricultura #qualidade-de-dados
- Relações: [[Eucatex — Monitoramento de vigor florestal]], [[BP — Nutrição de plantas]], [[São Martinho — Planejamento agrícola]]
- Confiança: alta

### 2026-10-14 07:27 BRT — Google disponibiliza Gemini 4 Argon por API com preço introdutório

- Fonte: [Google Cloud — Gemini 4 Argon available on Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud)
- Publicado: 2026-10-13 (horário/fuso não informado; janela exata de 24 horas não confirmada)
- Por que importa: modelo `gemini-4-argon` está disponível em GA na plataforma Gemini, com contexto combinado de 1.048.576 tokens. Preço introdutório até 30/11: US$ 2 por milhão de tokens de entrada e US$ 10 por milhão de saída; depois, US$ 4 e US$ 20. Mudança concreta para comparar custo e capacidade em agentes de análise e desenvolvimento.
- Tags: #google-cloud #gemini #modelo #api #preco #agentes-ia #desenvolvimento
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-14 07:27 BRT — Google amplia ADK para cinco linguagens com MCP e A2A

- Fonte: [Google Cloud — One Agent Development Kit, five languages](https://cloud.google.com/blog/topics/developers-practitioners/one-agent-development-kit-five-languages)
- Publicado: 2026-10-13 (horário/fuso não informado; janela exata de 24 horas não confirmada)
- Por que importa: ADK cobre Python, Go, TypeScript, Java e Kotlin; cada versão inclui cliente MCP e suporte a comunicação A2A. O CLI gera projetos com endpoints A2A e configuração para Cloud Run, Gemini Enterprise Agent Runtime ou GKE, facilitando integração de agentes em stacks corporativas existentes.
- Tags: #google-cloud #adk #mcp #a2a #agentes-ia #sdk #interoperabilidade
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-14 07:27 BRT — Planet inicia piloto de monitoramento e solicitação automática de imagens para incêndios

- Fonte: [Planet — Slovenia's Automated Space Resilience Infrastructure](https://www.planet.com/pulse/inside-slovenia-s-automated-space-resilience-infrastructure-reshaping-disaster-management-across/)
- Publicado: 2026-10-13 (horário/fuso não informado; janela exata de 24 horas não confirmada)
- Por que importa: Planet e Lucis desenvolverão, em 12 meses, plataforma financiada pela ESA para proteção civil da Eslovênia. O desenho liga detecção contínua por série temporal, alerta por limiar e solicitação automática de imagens VHR à entrega em mapa operacional — arquitetura aplicável ao monitoramento florestal; trata-se de projeto iniciado, não implantação concluída.
- Tags: #planet #esa #observacao-da-terra #automacao-geoespacial #incendios #florestal #tasking
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]], [[Bracell — GeoIA Estradas]]
- Confiança: alta

### 2026-10-13 07:30 BRT — Planet disponibiliza mapa global de população em grade de 40 metros

- Fonte: [Planet — Introducing Populace](https://www.planet.com/pulse/introducing-populace-mapping-humanity-in-unprecedented-detail/)
- Publicado: 2026-10-12 (horário/fuso não informado; janela exata de 24 horas não confirmada)
- Por que importa: o Populace combina imagens Planet, modelos da Microsoft e dados demográficos do IHME para estimar população global em grade de 40 m, com atualização trimestral. Pode enriquecer análises de traçados rodoviários, infraestrutura e exposição de comunidades; uso gratuito é restrito a pesquisa e organizações sem fins lucrativos, enquanto uso comercial requer outras condições.
- Tags: #planet #observacao-da-terra #dados-geoespaciais #populacao #infraestrutura #logistica #licenciamento
- Relações: [[GeoNext — LiDAR e rodovias]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-10-13 07:30 BRT — Esri detalha Countdown para ranquear feições em mapas interativos

- Fonte: [Esri — Countdown Instant App](https://www.esri.com/arcgis-blog/products/instant-apps/mapping/rank-compare-and-highlight-features-with-countdown-instant-app)
- Publicado: 2026-10-12 (horário/fuso não informado; janela exata de 24 horas não confirmada)
- Por que importa: o ArcGIS Instant Apps permite ordenar feições por atributo numérico, filtrar rankings e comparar itens no mapa com pop-ups fixados. Recurso pode criar painéis rápidos de priorização espacial de ativos e áreas sem desenvolver uma aplicação própria.
- Tags: #esri #arcgis #instant-apps #ranking #visualizacao-geoespacial #ativos
- Relações: [[IMAC — Plataforma GIS]], [[Itaminas — Monitoramento geotécnico]]
- Confiança: alta

### 2026-10-13 07:30 BRT — Anthropic publica impacto técnico de novas defesas contra extração de raciocínio

- Fonte: [Anthropic — Strengthening our defenses against distillation attacks](https://www.anthropic.com/research/distillation-defenses)
- Publicado: 2026-10-12 (horário/fuso não informado; janela exata de 24 horas não confirmada)
- Por que importa: a Anthropic relata queda de 90% a 99% na extração indevida de tokens de raciocínio após reforçar classificadores e controles de contexto. Integrações que manipulam histórico de raciocínio podem exigir ajuste; bloqueios preventivos podem gerar cobrança e falsos positivos, pontos a testar em agentes corporativos.
- Tags: #anthropic #claude #agentes-ia #seguranca #api #integracao #raciocinio
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-09 07:31 BRT — Google lança Gemini agent para trabalho empresarial persistente e multiagente

- Fonte: [Google Cloud — Gemini at Work 2026](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026/)
- Publicado: 2026-10-08 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: o Gemini agent une execução persistente em nuvem, memória, skills, ferramentas e orquestração dinâmica de subagentes, inclusive por MCP. A plataforma traz identidade, políticas, permissões, sandbox, *gateways* de rede, *Smart Routing* e limites de gasto — referência concreta para agentes corporativos governados que cruzam dados e sistemas de registro.
- Tags: #google-cloud #gemini #agentes-ia #mcp #multiagente #governanca #skills #execucao-persistente
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-09 07:31 BRT — OpenAI acelera steering de tarefas em execução no Codex Desktop

- Fonte: [Notas de versão do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- Publicado: 2026-10-08 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: mensagens de acompanhamento agora redirecionam mais cedo uma tarefa em execução no Codex. A configuração de comportamento de *follow-up* escolhe entre intervir na execução atual ou aguardar a próxima, reduzindo retrabalho em tarefas longas e preservando controle humano sobre agentes.
- Tags: #openai #codex #steering #agentes-ia #desktop #controle-de-execucao
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-09 07:31 BRT — MassDOT operacionaliza drones e LiDAR como sistema de registro estadual

- Fonte: [Esri — MassDOT drone imagery as infrastructure](https://www.esri.com/about/newsroom/blog/massdot-drone-imagery-as-infrastructure)
- Publicado: 2026-10-08 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: implantação padronizou o pipeline de drones, transformando imagens em sistema de registro compartilhado; a equipe transmitiu 400 milhões de pontos LiDAR para iPad em campo via 5G. É evidência operacional de distribuição *edge* de nuvem de pontos em inspeções de infraestrutura e manutenção.
- Tags: #esri #drones #lidar #infraestrutura #dados-geoespaciais #campo #5g
- Relações: [[GeoNext — LiDAR e rodovias]], [[Bracell — POC RGB + LiDAR]], [[Itaminas — Monitoramento geotécnico]]
- Confiança: alta

### 2026-10-08 07:32 BRT — Anthropic lança Claude Haiku 5.5 e reduz custo de agentes

- Fonte: [Anthropic — Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)
- Publicado: 2026-10-07 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: Haiku 5.5 é voltado a tarefas de alto volume — sumarização, compactação, consultas a banco, classificação e subagentes — com custo médio declarado 75% menor que Haiku 4.5. A Anthropic também reduz pela metade o preço de leitura de cache do Sonnet 5.5, tornando trabalho agentivo cerca de 20% mais barato, e adiciona crédito mensal de API para Max e Team.
- Tags: #anthropic #claude #haiku-5-5 #subagentes #custos #cache #agentes-ia #api
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-07 07:31 BRT — Google lança MCP Toolbox Java SDK 1.0 para acesso corporativo a dados por agentes

- Fonte: [Google Cloud — MCP Toolbox Java SDK 1.0](https://cloud.google.com/blog/topics/developers-practitioners/announcing-mcp-toolbox-java-sdk-v10-agentic-data-access-for-the-enterprise)
- Publicado: 2026-10-06 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: SDK Java 1.0 adiciona orquestração MCP tipada para agentes corporativos, com identidade via Application Default Credentials e tokens OIDC sem chaves fixas. A separação entre Toolbox e agente Spring Boot permite escalar acesso a dados e conversas com controles adequados a sistemas transacionais.
- Tags: #google-cloud #mcp #java #sdk #agentes-ia #oidc #seguranca #dados-corporativos
- Relações: [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-10-06 07:32 BRT — Google lança portfólio Modernize com avaliação e migração assistidas por agentes

- Fonte: [Google Cloud — Modernize](https://cloud.google.com/blog/products/infrastructure-modernization/google-cloud-modernize-accelerate-transformation-with-ai)
- Publicado: 2026-10-05 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: o novo portfólio reúne avaliação, modernização de plataforma e aplicações; o Modernization Hub analisa código e dependências, enquanto o Agentic Quick Estimator está em GA para estimar TCO a partir de inventários VMware. Inclui a migração EKS→GKE protegida por guardrails, oferecendo trilha para atualizar plataformas que hospedam dados e agentes corporativos.
- Tags: #google-cloud #modernizacao #agentes-ia #migracao #gke #vmware #governanca #ga
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-10-05 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, observação da Terra e papers recentes.
- Por que importa: na janela examinada, não foi identificado lançamento, alteração de API/preço, vulnerabilidade, ciclo de vida ou implantação verificável com impacto técnico direto na carteira. Resultados recentes eram relatos comunitários, material de suporte ou atualizações anteriores à janela e foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-10-02 07:30 BRT — GPT-6.1 Sol chega ao ChatGPT Work e Codex

- Fonte: [Notas de versão do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- Publicado: 2026-10-01 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: GPT-6.1 Sol melhora o desempenho de *agentic coding*, uso de computador e trabalho profissional sobre GPT-6 Sol. O rollout começa em Pro e se expande a Plus, Business, Enterprise e Edu; organizações podem governar o acesso via papéis e permissões do workspace.
- Tags: #openai #codex #chatgpt-work #gpt-6-1-sol #agentes-ia #governanca #rollout
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-02 07:30 BRT — OpenAI introduz dots, agentes persistentes com computador em nuvem

- Fonte: [Notas de versão do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- Publicado: 2026-10-01 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: os *dots* recebem um objetivo, apps conectados e limites de autonomia; continuam o trabalho entre conversas em computador próprio de nuvem, com resultados retornando para revisão. Estão em rollout para Pro e Business Premium, com beta Enterprise desligada por padrão — modelo de execução persistente relevante para rotinas operacionais.
- Tags: #openai #agentes-ia #automacao #computador-em-nuvem #apps-conectados #governanca #beta
- Relações: [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-10-02 07:30 BRT — ArcGIS Earth 3.0 adiciona cenas locais, Gaussian splats e projetos

- Fonte: [Esri — ArcGIS Earth October 2026](https://www.esri.com/arcgis-blog/products/arcgis-earth/3d-gis/whats-new-in-arcgis-earth-october-2026)
- Publicado: 2026-10-01 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: ArcGIS Earth desktop passa a suportar cenas locais, camadas de edifícios 3D, *Gaussian splats* georreferenciados e projetos; mobile ganha cenas locais e camadas de edifícios. Isso preserva sistemas de coordenadas locais e leva captura de realidade, terreno e ativos para inspeção e operação de campo.
- Tags: #esri #arcgis-earth #3d-gis #gaussian-splats #captura-de-realidade #lidar #campo
- Relações: [[GeoNext — LiDAR e rodovias]], [[Bracell — POC RGB + LiDAR]], [[Itaminas — Monitoramento geotécnico]]
- Confiança: alta

### 2026-10-02 07:30 BRT — OpenAI depreca GPT-5.3-Codex; migração para GPT-6 Sol até abril de 2027

- Fonte: [OpenAI — Depreciações de API](https://developers.openai.com/api/docs/deprecations)
- Publicado: 2026-10-01
- Por que importa: `gpt-5.3-codex`, `gpt-5.1` e `gpt-5.4-nano` foram depreciados e deixam a API em 2027-04-01. A substituição indicada é GPT-6 Sol para Codex/5.1 e GPT-6 Luna para Nano; fluxos produtivos devem testar compatibilidade, custo e avaliações antes do desligamento.
- Tags: #openai #codex #api #deprecacao #migracao #gpt-6-sol #gpt-6-luna
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-01 07:30 BRT — Google libera Data Agent Kit em disponibilidade geral para Codex, Claude Code e MCP

- Fonte: [Google Cloud — Data Agent Kit GA](https://cloud.google.com/blog/topics/developers-practitioners/data-agent-kit-is-now-ga-bring-google-data-cloud-to-any-coding-agent)
- Publicado: 2026-09-30 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: conjunto gratuito de ferramentas MCP e *agent skills* passa a conectar Codex, Claude Code e outros agentes diretamente a produtos de dados do Google Cloud. A versão GA adiciona BigQuery Graph, Bigtable, Spark gerenciado e acesso federado ao Lakehouse, reduzindo a necessidade de criar pipelines de ingestão apenas para dar contexto aos agentes.
- Tags: #google-cloud #mcp #skills #codex #claude-code #bigquery #lakehouse #ga
- Relações: [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-10-01 07:30 BRT — Google lança servidor MCP remoto para gcloud e BigQuery em preview

- Fonte: [Google Cloud — Cloud CLI remote MCP server](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-cli-remote-mcp-server-in-preview)
- Publicado: 2026-09-30 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: agentes passam a acessar centenas de comandos `gcloud` e `bq` por um único servidor MCP gerenciado. O controle é por API própria e papel IAM `roles/mcp.toolUser`, criando caminho auditável para operações de infraestrutura e dados sem expor credenciais estáticas ao agente.
- Tags: #google-cloud #mcp #gcloud #bigquery #iam #agentes-ia #seguranca #preview
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-10-01 07:30 BRT — Esri publica release de setembro do ArcGIS Solutions, com cinco soluções novas

- Fonte: [Esri — ArcGIS Solutions September 2026 Release](https://www.esri.com/arcgis-blog/products/arcgis-solutions/announcements/whats-new-in-arcgis-solutions-september-2026-release)
- Publicado: 2026-09-29 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: release adiciona configurações operacionais para permissões de uso conjunto elétrico, inspeção de painéis solares, análise costeira, planejamento de mercado e reporte virtual de danos com imagem e GeoAI. Também move cinco soluções para fase de ciclo de vida *Mature*, sinal relevante para governança de portfólio ArcGIS.
- Tags: #esri #arcgis-solutions #geoai #utilities #inspecao #ciclo-de-vida #release
- Relações: [[IMAC — Plataforma GIS]], [[TAG / TBG / NTS]], [[Suzano — Rotas e logística]]
- Confiança: alta

### 2026-09-30 07:31 BRT — AWS e OpenAI lançam Bedrock Managed Agents em preview

- Fonte: [AWS — Amazon Bedrock Managed Agents](https://aws.amazon.com/about-aws/whats-new/2026/09/bedrock-managed-agents-preview/)
- Publicado: 2026-09-29 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: o serviço, construído sobre versão customizada da Agents API da OpenAI, executa agentes com modelos OpenAI dentro da AWS, com sessões duráveis, skills reutilizáveis e conexão a ferramentas via MCP. Cada agente recebe papel IAM próprio, aprovações humanas para ações consequentes e trilha no CloudTrail — controles relevantes para automações empresariais auditáveis.
- Tags: #aws #bedrock #openai #agentes-ia #mcp #iam #cloudtrail #governanca #preview
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-09-29 08:02 BRT — Anthropic lança Claude Sonnet 5.5 com menor custo e maior velocidade para agentes

- Fonte: [Anthropic — Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)
- Publicado: 2026-09-28 (horário/fuso não informado; não é possível confirmar a posição exata na janela móvel)
- Por que importa: novo modelo para tarefas bem delimitadas, correções e artefatos, com preço de US$ 2/US$ 10 por milhão de tokens de entrada/saída e geração 30%+ mais rápida que Sonnet 5. Introduz salvaguardas cibernéticas e *fallbacks*, além de estar disponível também em AWS, Google Cloud e Azure; opção prática para agentes de engenharia e automação de dados sob governança.
- Tags: #anthropic #claude #claude-code #agentes-ia #modelos #seguranca #custos #cloud
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-09-28 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, observação da Terra e papers recentes.
- Por que importa: na janela examinada, não foi identificado lançamento, alteração de API/preço, vulnerabilidade, ciclo de vida ou implantação verificável com impacto técnico direto na carteira. Atualizações oficiais localizadas eram anteriores à janela e não foram reclassificadas como novidade atual.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-09-25 07:30 BRT — AlloyDB anuncia PostgreSQL para agentes com leitura isolada de dados de produção

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/databases/announcing-postgresql-for-agents-in-alloydb)
- Publicado: 2026-09-24 (horário/fuso não informado na fonte)
- Por que importa: em preview, AlloyDB passa a provisionar instâncias de banco isoladas para picos de agentes, com leitura atualizada e somente leitura dos dados de produção. A arquitetura usa IAM, VPC Service Controls, criptografia e auditoria, permitindo consultas espaciais, vetoriais e textuais sem competir com o sistema transacional.
- Tags: #google-cloud #alloydb #postgresql #agentes-ia #dados-em-tempo-real #dados-geoespaciais #seguranca #preview
- Relações: [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-09-25 07:30 BRT — Google libera plugin de migração EKS→GKE com skills, MCP e guardrails

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/containers-kubernetes/gke-agentic-migration)
- Publicado: 2026-09-24 (horário/fuso não informado na fonte)
- Por que importa: a ferramenta open source combina skills de agentes e servidor MCP local para converter IaC e manifestos Kubernetes em *landing zones* GKE por Pull Requests. Os guardrails determinísticos e a revisão via Git preservam rastreabilidade e rollback, em vez de alterar clusters ativos diretamente.
- Tags: #google-cloud #gke #mcp #skills #agentes-ia #cicd #governanca #open-source
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-09-24 07:31 BRT — ChatGPT Voice passa a executar plugins e tarefas em Work

- Fonte: [Notas de versão do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- Publicado: 2026-09-23 (horário/fuso não informado na fonte)
- Por que importa: Voice agora usa plugins e apps conectados em web e mobile; no Work pode criar artefatos, usar apps e operar navegador, com tarefa inacabada continuando em texto. Amplia a interface para operações em campo, mas mantém permissões e limites das conexões já configuradas.
- Tags: #openai #chatgpt-work #voice #plugins #agentes-ia #automacao #apps-conectados
- Relações: [[Petrobras — Segundo cérebro]], [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-09-23 07:32 BRT — GPT-6 Sol e Luna chegam ao ChatGPT Work e Codex

- Fonte: [Notas de versão do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-plus)
- Publicado: 2026-09-22 (horário/fuso não informado na fonte)
- Por que importa: novos modelos passam a estar disponíveis em Work e Codex, separados dos modelos do Chat, e o desktop preserva a seleção manual. Isso amplia opções de roteamento entre capacidade e volume para tarefas de código, dados e agentes; a combinação disponível depende de plano e políticas do workspace.
- Tags: #openai #codex #gpt-6-sol #gpt-6-luna #agentes-ia #modelos #roteamento
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-09-23 07:32 BRT — Anthropic lança Claude Opus 5.5, com modo rápido no Claude Code

- Fonte: [Anthropic — Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)
- Publicado: 2026-09-22 (horário/fuso não informado na fonte)
- Por que importa: Opus 5.5 entra como novo modelo de ponta da família, com alegação de 40% menos custo que Opus 5 e modo rápido de até 2,5× no Claude Code. A ênfase em delegação de subagentes, verificação e controles como *preserved thinking* torna a atualização relevante para workflows de desenvolvimento com governança.
- Tags: #anthropic #claude-code #claude-opus-5-5 #agentes-ia #subagentes #seguranca #custos
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-09-22 07:31 BRT — V7 conecta memória institucional e workflows MCP ao Codex

- Fonte: [OpenAI — estudo de caso V7](https://openai.com/index/v7/)
- Publicado: 2026-09-21 (horário/fuso não informado na fonte)
- Por que importa: V7 transforma arquivos em entidades de uma ontologia, preserva evidências citáveis e permite criar workflows do V7 Go via MCP no Codex. O caso mostra uma arquitetura concreta para “segundo cérebro” que combina extração estruturada, grafo de contexto e rastreabilidade de fonte.
- Tags: #openai #codex #mcp #grafo-de-conhecimento #memoria-institucional #rastreabilidade #agentes-ia
- Relações: [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-09-22 07:31 BRT — AWS atualiza AgentCore Runtime para sessões de agentes mais eficientes

- Fonte: [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-builder-center-mobile-apps-amazon-connect-talent-ga-amazon-corretto-27-and-more-september-14-2026/)
- Publicado: 2026-09-21 (horário/fuso não informado na fonte)
- Por que importa: a nova versão do runtime gerenciado libera memória conforme a sessão reduz uso e prepara/snapshota o ambiente para manter partidas a frio previsíveis. É melhoria de ciclo de vida e custo para agentes persistentes, especialmente em fluxos com ferramentas, arquivos e execuções intermitentes.
- Tags: #aws #bedrock #agentcore #agentes-ia #runtime #custos #observabilidade
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-09-22 07:31 BRT — Google libera novas capacidades de CI/CD seguro em GA

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/identity-security/strengthen-your-cicd-pipeline-with-new-secure-source-manager-capabilities)
- Publicado: 2026-09-21 (horário/fuso não informado na fonte)
- Por que importa: as capacidades de Secure Source Manager fortalecem autenticação e autorização unificadas para código e CI/CD. É base de segurança para agentes que alteram repositórios ou acionam automações de entrega, reduzindo o risco de transformar o pipeline em vetor de comprometimento.
- Tags: #google-cloud #cicd #seguranca #supply-chain #devsecops #agentes-ia
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-09-21 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, observação da Terra e papers recentes.
- Por que importa: na janela examinada, não foi identificado lançamento, alteração de API/preço, vulnerabilidade, ciclo de vida ou implantação verificável com impacto técnico direto na carteira. Resultados recentes eram relatos comunitários, pedidos de recurso ou problemas não confirmados por fonte primária.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-09-18 22:09 BRT — Google descreve pipeline agêntico para corrigir vulnerabilidades no ciclo de desenvolvimento

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure)
- Publicado: 2026-09-18 (horário/fuso não informado na fonte)
- Por que importa: relato operacional mostra agentes inseridos no ciclo de desenvolvimento para varredura e correção de vulnerabilidades em cada mudança de código, com centenas de falhas bloqueadas por mês. Reforça padrão de alto sinal: agentes em escopo específico, integrados à revisão e *patching*, não com autonomia irrestrita sobre produção.
- Tags: #google-cloud #agentes-ia #seguranca #devsecops #vulnerabilidades #automacao
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-09-18 22:09 BRT — BigQuery anuncia cache cross-cloud para Lakehouse em preview

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/borderless-lakehouse-cross-cloud-caching-and-connections)
- Publicado: 2026-09-18 (horário/fuso não informado na fonte)
- Por que importa: o recurso permite consultar dados governados onde residem em S3, ADLS, GCS e catálogos Iceberg, com cache que pode reduzir transferência entre nuvens. É relevante para agentes que cruzam telemetria, dados operacionais e acervos geoespaciais sem duplicação ampla; por estar em preview, não deve sustentar fluxo crítico ainda.
- Tags: #google-cloud #bigquery #lakehouse #dados-geoespaciais #agentes-ia #iceberg #preview
- Relações: [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-09-18 22:09 BRT — Codex adiciona aba de analytics de consumo por tarefa e subagente

- Fonte: [OpenAI Developer Community](https://community.openai.com/c/codex/37)
- Publicado: 2026-09-18 (horário/fuso não informado na fonte)
- Por que importa: a nova visualização discrimina quanto tarefas, subagentes e conversas consomem da cota. É controle operacional importante para orquestrações de longa duração, permitindo localizar fluxos caros antes de ampliar uso de agentes.
- Tags: #openai #codex #agentes-ia #subagentes #observabilidade #custos
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: média

### 2026-09-15 07:30 BRT — BigQuery adiciona funções de analytics aumentada prontas para agentes

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/bigquery-augmented-analytics-tvfs)
- Publicado: 2026-09-14 (horário/fuso não informado na fonte)
- Por que importa: seis funções TVF combinam IA, ML e estatística dentro do BigQuery para diagnóstico de mudanças, tendência, relação entre variáveis e efeito causal, retornando SQL estruturado que pode virar *skills* de agentes. Evita exportar dados para investigação exploratória e cria base mais auditável para perguntas operacionais.
- Tags: #google-cloud #bigquery #analytics #agentes-ia #sql #causalidade #governanca
- Relações: [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-09-15 07:30 BRT — Dataflow disponibiliza pause/resume em GA e GPUs RTX PRO 6000

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/new-dataflow-features-to-enable-large-scale-ai-workloads)
- Publicado: 2026-09-14 (horário/fuso não informado na fonte)
- Por que importa: pausa e retomada de jobs batch chegam a GA, e G4/RTX PRO 6000 amplia capacidade para preparação de dados e inferência pesada. Pode reduzir custo e tempo de operações descontínuas de imagem, LiDAR e séries temporais, desde que o dimensionamento de GPU seja justificado pelo pipeline.
- Tags: #google-cloud #dataflow #gpu #mlops #dados-geoespaciais #lidar #automacao
- Relações: [[Bracell — POC RGB + LiDAR]], [[GeoNext — LiDAR e rodovias]], [[Eucatex — Monitoramento de vigor florestal]]
- Confiança: alta

### 2026-09-15 07:30 BRT — Agent Search libera controle de preço por consulta em GA

- Fonte: [Google Cloud — release notes](https://docs.cloud.google.com/generative-ai-app-builder/docs/release-notes)
- Publicado: 2026-09-14 (horário/fuso não informado na fonte)
- Por que importa: `searchAddonSpec` entra em GA na API v1, permitindo ligar ou desligar complementos por busca e controlar custo programaticamente. É mecanismo útil para equilibrar profundidade de recuperação e orçamento em agentes que consultam acervos técnicos e documentos de projeto.
- Tags: #google-cloud #agent-search #agentes-ia #api #precos #rag #governanca
- Relações: [[Petrobras — Segundo cérebro]], [[IMAC — Plataforma GIS]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-09-14 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, observação da Terra e papers recentes.
- Por que importa: na janela examinada, não foi identificado lançamento, alteração de API/preço, vulnerabilidade, ciclo de vida ou implantação verificável com impacto técnico direto na carteira. Itens oficiais relevantes encontrados eram publicados antes da janela e não foram reclassificados como novidade atual.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-09-11 07:32 BRT — OpenAI lança Agents API em beta público, baseada no harness do Codex

- Fonte: [OpenAI — Agents API](https://openai.com/index/introducing-the-agents-api/)
- Publicado: 2026-09-10 (horário/fuso não informado na fonte)
- Por que importa: API entrega o harness do Codex para agentes de longa duração, subagentes, ferramentas, MCP e escolha de sandbox gerenciado, infraestrutura própria ou parceiros. Reduz esforço para implantar automações governadas, mas ainda está em beta público e requer avaliação de permissões, custo e isolamento antes de produção.
- Tags: #openai #agents-api #codex #agentes-ia #mcp #sandbox #automacao #beta
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-09-11 07:32 BRT — Data agent chega a ChatGPT Work e Codex para análise de dados conectados

- Fonte: [OpenAI — Data agent](https://openai.com/index/put-data-to-work/)
- Publicado: 2026-09-10 (horário/fuso não informado na fonte)
- Por que importa: o agente conecta dados empresariais, investiga mudanças e produz relatórios e painéis interativos via conversa; consultas respeitam permissões da conta conectada. Abre caminho direto para análises exploratórias de operação, mas exige configurar fontes, autorização e definições de métricas antes de uso confiável.
- Tags: #openai #codex #chatgpt-work #data-agent #analytics #dashboard #governanca
- Relações: [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-09-11 07:32 BRT — Google publica plugin portátil para agentes de código, com skills e MCP

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/introducing-the-google-cloud-developer-plugin-for-ai-coding-agents)
- Publicado: 2026-09-10 (horário/fuso não informado na fonte)
- Por que importa: o plugin `google-cloud-developer` empacota skills, documentação oficial e MCP de conhecimento em padrão aberto; há instruções de instalação para Claude Code e Codex CLI. É referência prática para distribuir capacidades de nuvem com autenticação e guardrails consistentes entre agentes.
- Tags: #google-cloud #codex #claude-code #mcp #skills #plugins #agentes-ia #governanca
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-09-10 07:30 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, observação da Terra e papers recentes.
- Por que importa: na janela examinada, não foi identificado lançamento, alteração de API/preço, vulnerabilidade, ciclo de vida ou implantação verificável com impacto técnico direto na carteira. Publicações encontradas eram material comunitário, reconhecimento de mercado ou atualização sem capacidade nova verificável.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-09-09 07:31 BRT — Codex com GPT-5.6 Sol é aplicado a ciclo experimental em computação quântica

- Fonte: [OpenAI — estudo de caso](https://openai.com/index/codex-quantum-computing-experiments/)
- Publicado: 2026-09-08 (horário/fuso não informado na fonte)
- Por que importa: estudo aplicado descreve agentes Codex recebendo objetivos estreitos para escrever, modificar e testar código de controle, análise e simulação de medições laboratoriais. É evidência operacional de um padrão útil para ciclos de dados instrumentais: escopo restrito, execução verificável e humano concentrado no desenho do experimento.
- Tags: #openai #codex #gpt-5-6-sol #agentes-ia #automacao #dados-instrumentais #estudo-de-caso
- Relações: [[Itaminas — Monitoramento geotécnico]], [[Vale — GeoIA SAB.IA]], [[CTC — Centro de Tecnologia Canavieira]]
- Confiança: alta

### 2026-09-09 07:31 BRT — Google detalha control plane de agentes com Antigravity SDK

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/power-agent-hubs-or-custom-harnesses-with-the-antigravity-sdk)
- Publicado: 2026-09-08 (horário/fuso não informado na fonte)
- Por que importa: SDK expõe runtime para agentes com políticas declarativas, persistência de estado e telemetria de ações/ferramentas em tempo real. O desenho de *control plane* é aplicável a automações geoespaciais que precisam de trilha de execução, isolamento e supervisão — além do simples chat.
- Tags: #google-cloud #agentes-ia #sdk #observabilidade #governanca #automacao #sandbox
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-09-09 07:31 BRT — Google registra evolução de ataques para fluxos autônomos com agentes

- Fonte: [Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai)
- Publicado: 2026-09-08 (horário/fuso não informado na fonte)
- Por que importa: relatório primário descreve campanhas que usaram fluxos multiagente para escaneamento, tratamento de erros e coleta de credenciais, comprimindo o tempo de resposta dos defensores. Reforça que agentes ligados a dados, repositórios e portais devem operar com identidade mínima, isolamento e revisão de ferramentas.
- Tags: #google-cloud #seguranca #agentes-ia #supply-chain #credenciais #governanca
- Relações: [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-09-09 07:31 BRT — Data Agent Kit demonstra investigação entre BigQuery, PostgreSQL e arquivos via MCP

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/agentic-analytics-with-the-data-agent-kit)
- Publicado: 2026-09-08 (horário/fuso não informado na fonte)
- Por que importa: demonstração usa o Data Agent Kit para investigar uma pergunta de negócio cruzando *warehouse*, banco operacional e arquivos, incluindo acesso ao Cloud Storage por servidor MCP. É padrão prático para conectar dados de projetos sem transformar o agente em acesso irrestrito ao ambiente.
- Tags: #google-cloud #data-agent-kit #mcp #agentes-ia #bigquery #analytics #governanca
- Relações: [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-09-08 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, observação da Terra e papers recentes.
- Por que importa: na janela examinada, não foi identificado lançamento, alteração de API/preço, vulnerabilidade, ciclo de vida ou implantação verificável com impacto técnico direto na carteira. Material recente encontrado foi comunitário, *roundup* sem anúncio primário novo ou publicação fora da janela.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-09-07 07:32 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, observação da Terra e papers recentes.
- Por que importa: na janela examinada, não foi identificado lançamento, alteração de API/preço, vulnerabilidade, ciclo de vida ou implantação verificável com impacto técnico direto na carteira. Resultados recentes eram material comunitário, publicação anterior à janela ou atualização genérica e foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-09-04 07:31 BRT — OpenAI inicia rollout limitado do GPT-6 Astra para trabalho agêntico complexo

- Fonte: [OpenAI — GPT-6 Astra](https://openai.com/index/gpt-6-astra/)
- Publicado: 2026-09-03 (horário/fuso não informado na fonte)
- Por que importa: o modelo entra em rollout controlado para tarefas longas de pesquisa, código, documentos e uso de computador, com API e contexto de até 1,05 milhão de tokens. É uma opção de maior capacidade para fluxos auditáveis que cruzam dados, regras e automação; disponibilidade ainda é limitada, portanto não deve ser assumida como padrão de produção.
- Tags: #openai #gpt-6-astra #agentes-ia #automacao #api #ferramentas-dev #seguranca
- Relações: [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-09-04 07:31 BRT — ChatGPT Work e Codex passam a usar Site tools via WebMCP

- Fonte: [Notas de versão do ChatGPT](https://help.openai.com/en/articles/6825453)
- Publicado: 2026-09-03 (horário/fuso não informado na fonte)
- Por que importa: sites compatíveis podem expor ferramentas diretamente ao navegador integrado do ChatGPT Work e do Codex via WebMCP. Isso reduz a necessidade de integrações ad hoc para operações web, mas depende de site, plano e modelo compatíveis; é relevante para avaliar portais GIS e dados que possam oferecer ações controladas.
- Tags: #openai #codex #webmcp #mcp #agentes-ia #automacao-web #integracao
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-09-03 07:30 BRT — Google abre o Mantis, harness de agentes para encontrar, reproduzir e corrigir falhas

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs)
- Publicado: 2026-09-02 (horário/fuso não informado na fonte)
- Por que importa: o framework open source orquestra agentes de crítica e revisão, análise de repositório e reprodução isolada de vulnerabilidades antes do *patch*. Oferece um padrão operacional de segurança para usar agentes de código com contexto, critérios de aceitação e evidência reprodutível — não apenas varredura baseada em LLM.
- Tags: #google-cloud #seguranca #agentes-ia #ferramentas-dev #open-source #sandbox
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-09-02 07:32 BRT — BigQuery Graph atinge disponibilidade geral e ganha skill para agentes

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/bigquery-graph-connecting-data-and-ai-at-scale/)
- Publicado: 2026-09-01 (horário/fuso não informado na fonte)
- Por que importa: BigQuery Graph entra em GA com GQL nativo e sem ETL para um banco de grafos separado. A integração com Data Agent Kit leva uma skill de grafos a Codex e Claude Code, e o *context graph* registra decisões de agentes como trilhas consultáveis e auditáveis.
- Tags: #google-cloud #bigquery #grafo-de-conhecimento #agentes-ia #codex #claude-code #governanca
- Relações: [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-09-01 07:30 BRT — Google Cloud lança Data Agent Kit para pipelines e MLOps assistidos por agentes

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/build-data-pipelines-in-less-time-with-data-agent-kit)
- Publicado: 2026-08-31 (horário/fuso não informado na fonte)
- Por que importa: o kit aberto integra IDEs e agentes de código, incluindo Codex e Claude Code, para consultar dados, criar pipelines, treinar modelos e operar ciclos de MLOps. O exemplo combina dados geográficos, BigQuery, Spark e inferência diária, oferecendo um caminho concreto para automatizar pipelines geoespaciais com governança de dados.
- Tags: #google-cloud #codex #claude-code #agentes-ia #mlops #dados-geoespaciais #automacao
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-08-31 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, observação da Terra e papers recentes.
- Por que importa: na janela examinada, não foi identificado lançamento, alteração de API/preço, vulnerabilidade, ciclo de vida ou implantação verificável com impacto técnico direto na carteira. Discussões comunitárias, eventos e atualizações rotineiras de dados foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-28 07:30 BRT — ArcGIS Routing chega ao R-ArcGIS Bridge

- Fonte: [Esri ArcGIS Blog](https://www.esri.com/arcgis-blog/products/r-bridge/developers/welcome-arcgisrouting-to-the-r-arcgis-bridge-%F0%9F%91%8B)
- Publicado: 2026-08-27 (horário/fuso não informado na fonte)
- Por que importa: o novo pacote `{arcgisrouting}` expõe no R rotas, áreas de serviço/isócronas, roteirização de frotas, *map matching* de GPS e alocação de localização — incluindo requisições assíncronas e de grande porte. Reduz atrito para colocar análise logística reprodutível sobre serviços ArcGIS.
- Tags: #arcgis #r #roteirizacao #logistica #automacao-geoespacial #api
- Relações: [[Suzano — Rotas e logística]], [[Bracell — GeoIA Estradas]], [[GeoNext — LiDAR e rodovias]]
- Confiança: alta

### 2026-08-28 07:30 BRT — Cloud Run Instances entra em prévia para agentes persistentes

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/serverless/introducing-cloud-run-instances)
- Publicado: 2026-08-27 (horário/fuso não informado na fonte)
- Por que importa: a nova modalidade mantém uma instância Cloud Run ativa para cargas com estado e longa duração, que não se ajustam ao padrão *scale-to-zero*. É uma alternativa de implantação para agentes contínuos, com menos partidas a frio e sem operar infraestrutura própria.
- Tags: #google-cloud #cloud-run #agentes-ia #infraestrutura #serverless #preview
- Relações: [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-08-27 09:33 BRT — Google Cloud adiciona cobrança flexível e limites de gasto para agentes

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/flexible-billing-and-cost-controls-for-agents-on-google-cloud)
- Publicado: 2026-08-26 (horário/fuso não informado na fonte)
- Por que importa: Gemini Enterprise ganhou opção pay-as-you-go, quotas compartilhadas entre agentes e ferramentas de desenvolvimento, limites mensais por projeto e detecção de anomalias. Isso torna custo, pausa automática e governança do uso de agentes parâmetros operacionais — não só estimativas de arquitetura.
- Tags: #google-cloud #agentes-ia #finops #governanca #preco #ferramentas-dev
- Relações: [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-08-27 09:33 BRT — Knowledge Catalog passa a organizar contexto verificável para agentes via OKF

- Fonte: [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/scale-okf-bundles-across-an-organization-with-knowledge-catalog)
- Publicado: 2026-08-26 (horário/fuso não informado na fonte)
- Por que importa: o padrão Open Knowledge Format (OKF) pode ser publicado no Knowledge Catalog com proveniência, verificação, atualização, linhagem e IAM. É uma referência prática para transformar bases Markdown e dados corporativos em contexto pesquisável e governado por agentes.
- Tags: #google-cloud #agentes-ia #conhecimento #governanca #linhagem #markdown
- Relações: [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]], [[NAVIS / GeoFramework]]
- Confiança: média

### 2026-08-26 07:32 BRT — WebMCP Challenge: sites expõem ferramentas diretamente a agentes

- Fonte: [anúncio da OpenAI Developer Community](https://community.openai.com/t/the-webmcp-challenge-is-here/1392582)
- Publicado: 2026-08-25 20:46 (fuso não informado na fonte)
- Por que importa: o WebMCP é um padrão aberto experimental para que aplicações web exponham ferramentas que agentes podem usar diretamente na página. É um sinal de arquitetura para portais e plataformas GIS tornarem ações geoespaciais invocáveis por agentes; ainda não é uma implantação validada nos projetos.
- Tags: #openai #webmcp #mcp #agentes-ia #ferramentas-dev #plataformas-web
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-08-25 07:30 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, GeoIA e papers recentes.
- Por que importa: nenhum anúncio verificável nas últimas 24 h alterou decisão, arquitetura ou oportunidade da carteira. Relatos comunitários de falhas de Codex/MCP não são anúncio nem impacto confirmado em projeto; foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-24 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, GeoIA e papers recentes.
- Por que importa: nenhum anúncio verificável nas últimas 24 h alterou decisão, arquitetura ou oportunidade da carteira. Atualizações sobre MCP, ArcGIS e ferramentas de agentes encontradas eram anteriores à janela; foram descartadas.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-21 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, GeoIA e papers recentes.
- Por que importa: nenhuma publicação verificável nas últimas 24 h alterou decisão, arquitetura ou oportunidade da carteira. Eventos, discussões comunitárias e materiais históricos foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-20 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens, GeoIA e papers recentes.
- Por que importa: nenhuma publicação verificável nas últimas 24 h alterou decisão, arquitetura ou oportunidade da carteira. Eventos e treinamentos publicados no período não configuram atualização técnica; foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-19 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens e GeoIA; papers recentes de sensoriamento remoto.
- Por que importa: nenhuma publicação verificável nas últimas 24 h cria oportunidade, mudança técnica ou ação útil para a carteira. Resultados sobre agentes e GeoIA eram anteriores à janela; foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-18 07:30 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens e GeoIA; papers recentes de sensoriamento remoto.
- Por que importa: nenhum anúncio verificável nas últimas 24 h altera decisão, arquitetura ou oportunidade da carteira. Materiais retornados sobre agentes e GeoIA eram anteriores à janela; foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-17 07:31 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: fontes oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, nuvens e GeoIA; papers recentes de sensoriamento remoto.
- Por que importa: não houve anúncio verificável nas últimas 24 h que agregue diretamente à carteira. Materiais de segurança da Anthropic e papers GeoIA retornados são anteriores à janela; foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-16 14:33 BRT — Nenhuma novidade de alto sinal

- Estado: `sem_novidade`
- Escopo consultado: anúncios e documentação oficiais de Esri/ArcGIS, OpenAI/Codex, Anthropic/Claude Code, MCP, GeoAI e provedores de nuvem; papers recentes.
- Por que importa: nenhum lançamento, mudança de API/produto, paper operacional ou aviso de ciclo de vida confirmou publicação nas últimas 24 h. Itens de conferência, posts comunitários e materiais anteriores foram descartados.
- Tags: #sem_novidade #ia #geoia #arcgis #codex #claude-code #mcp
- Relações: nenhuma
- Confiança: alta

### 2026-08-16 — Nenhum anúncio oficial de alto sinal nas últimas 24 h

- Estado: `sem_novidade`
- Escopo consultado: OpenAI/Codex, Anthropic/Claude Code, Esri/ArcGIS, MCP e GeoIA.
- Nota: preservar este resultado evita transformar ausência de atualização em ruído.

### ArcGIS Enterprise 10.8.1: aposentado em 1º de agosto de 2026

- Fonte: [ciclo de vida oficial](https://support.esri.com/en-us/products/arcgis-enterprise/life-cycle)
- Por que importa: instalações 10.8.1 deixam de ter suporte. Mapear servidores que sustentam GIS de operações, logística, minas e ativos de O&G; priorizar plano de atualização.
- Tags: #arcgis #arcgis-enterprise #lifecycle #automacao-geoespacial #operacoes
- Relações: [[gestao-de-ativos]] · [[logistica]] · [[mineracao]] · [[oleo-e-gas]]

### Conteúdo técnico da Esri UC 2026 disponível desde 13 de agosto

- Fonte: [acesso virtual oficial](https://www.esri.com/en-us/about/events/uc/plan/virtual-attendance)
- Por que importa: as gravações disponibilizadas após a conferência são fonte primária para identificar recursos, padrões e demos aplicáveis antes de notícias secundárias.
- Tags: #esri #arcgis #geoia #automacao-geoespacial #fonte-primaria
- Relações: [[arcgis-roadmap]] · [[projetos-geoia]]

### ArcGIS Imagery MOOC: geospatial AI, imagens e sensoriamento remoto

- Fonte: [anúncio da Esri](https://www.esri.com/about/newsroom/arcnews/training-and-certification-offerings-5)
- Por que importa: trilha oficial, com início em 26 de agosto, combina imagens, sensoriamento remoto e dados geoespaciais — competências diretas para florestal, sulco/grãos e mineração.
- Tags: #esri #geoia #sensoriamento-remoto #florestal #agro #mineracao
- Relações: [[monitoramento-florestal]] · [[agricultura-de-precisao]] · [[observacao-da-terra]]

### Codex: agentes cada vez mais usados para automação e análise estruturada

- Fonte: [pesquisa oficial da OpenAI](https://openai.com/index/how-agents-are-transforming-work/)
- Por que importa: evidencia uso de Codex além de código, incluindo automação, transformação de dados e análise — padrão útil para orquestrar coleta, classificação e ligação com projetos.
- Tags: #openai #codex #agentes-ia #automacao #dados
- Relações: [[pipeline-de-noticias]] · [[base-de-projetos]] · [[mcp]]

### Claude Sonnet 5 disponível no Claude Code

- Fonte: [anúncio da Anthropic](https://www.anthropic.com/news/claude-sonnet-5)
- Por que importa: atualização de modelo para fluxos de agentes, ferramentas e código; acompanhar custo, limites e ganhos reais antes de mudar automações existentes.
- Tags: #anthropic #claude-code #agentes-ia #ferramentas-dev
- Relações: [[automacao-de-desenvolvimento]] · [[agentes]]

## Taxonomia inicial

- Tecnologias: #ia #geoia #arcgis #esri #codex #claude-code #mcp #agentes-ia #automacao-geoespacial #ferramentas-dev
- Setores: #agro #florestal #sulco-e-graos #mineracao #logistica #oleo-e-gas
- Tipo: #release #paper #caso-de-uso #lifecycle #seguranca #regulacao #sem_novidade

## Projetos relacionáveis

- [[TTG — GeoIA]] · [[Bom Jesus — GeoIA]] · [[GeoNext — LiDAR e rodovias]] · [[Itaminas — Monitoramento geotécnico]]
- [[IMAC — Plataforma GIS]] · [[Petrobras — Segundo cérebro]] · [[Amaggi — Monitoramento de desmatamento]] · [[BP — Nutrição de plantas]]
- [[Atvos — Visão computacional]] · [[Exposibram]] · [[São Martinho — Planejamento agrícola]] · [[Bracell — GeoIA Estradas]]
- [[Bracell — POC RGB + LiDAR]] · [[Suzano — Rotas e logística]] · [[Eucatex — Monitoramento de vigor florestal]] · [[Vale — GeoIA SAB.IA]]
- [[Vale — Fechamento de minas]] · [[Klabin — IA]] · [[Imersão Comercial]] · [[NAVIS / GeoFramework]]
- [[TAG / TBG / NTS]] · [[GeoFiscal-Sinter]] · [[CTC — Centro de Tecnologia Canavieira]]

> Relações devem usar apenas nomes desta lista, quando houver aderência material.

## Esquema para próximas entradas

```md
### Título curto

- Fonte: [nome](https://exemplo.com)
- Publicado: AAAA-MM-DD HH:MM TZ
- Por que importa: 1–3 linhas, impacto técnico/profissional verificável.
- Tags: #tema #setor #tipo
- Relações: [[projeto-ou-tema-1]] · [[projeto-ou-tema-2]]
- Confiança: alta | média
```
