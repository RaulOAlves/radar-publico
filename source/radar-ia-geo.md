# Radar IA, GeoIA e Setores

> Base relacional de notícias para projetos. Atualizado: 2026-10-29 07:35 (BRT).

## Critério de sinal

- Prioridade: anúncio oficial, release, mudança de API/produto, paper primário, vulnerabilidade, ciclo de vida ou caso de uso operacional.
- Janela padrão: últimas 24 h. Sem item de alto sinal, registrar `sem_novidade` e não preencher com notícia genérica.
- Relevância: primeiro `ArcGIS`, automação geoespacial, agentes, Claude Code e Codex; depois impacto nos setores-alvo.

## Registros

### 2026-10-29 07:35 BRT — Plugin MCP do ServiceNow chega ao marketplace OpenAI

- Fonte: [OpenAI — expansão da parceria com ServiceNow](https://openai.com/index/openai-servicenow-partnership-expansion/)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A OpenAI e a ServiceNow anunciaram expansão da parceria para conectar fluxos da ServiceNow ao ChatGPT e ampliar o uso de modelos e agentes da OpenAI nos produtos da empresa. A integração permite conectar uma instância própria da ServiceNow ao ChatGPT para localizar incidentes semelhantes, avaliar riscos de mudanças e atualizar registros durante a conversa.

  As capacidades dependem da configuração do cliente, enquanto o Action Fabric aplica regras de negócio e permissões existentes. O plugin MCP já está no marketplace da OpenAI; recursos adicionais são esperados até o fim de 2026. A integração do Codex ao AI Workflow Factory permanece planejada para 2027.
- Por que importa: plugin MCP já disponível conecta contexto e ações de instâncias ServiceNow ao ChatGPT, respeitando regras e permissões do cliente. É referência concreta para agentes corporativos que consultam incidentes e executam ações governadas; integração Codex no AI Workflow Factory é apenas planejada para 2027, não recurso atual.
- Tags: #openai #servicenow #mcp #agentes-ia #codex #integracao #governanca
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-29 07:35 BRT — Gemini Enterprise passa a oferecer região Brasil com residência local de dados

- Fonte: [Google Cloud — release notes de 28/10](https://docs.cloud.google.com/release-notes#October_28_2026)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: As notas do Google Cloud registram que o aplicativo Gemini Enterprise pode operar na região brasileira (`br`), com residência de dados em repouso e processamento de machine learning dentro do país. A oferta consta como disponibilidade geral, mas exige allowlist: clientes precisam solicitar acesso à equipe de conta do Google.

  O anúncio não significa que qualquer projeto possa habilitar a região imediatamente. Para avaliar uso com informações corporativas sensíveis, ainda é necessário confirmar elegibilidade, escopo dos dados e condições aplicáveis à conta e ao ambiente.
- Por que importa: Google anuncia região brasileira para Gemini Enterprise, com dados em repouso e processamento de ML na região; disponibilidade geral condicionada a allowlist. Pode destravar avaliação de agentes sobre dados corporativos brasileiros sensíveis, mas requer acesso liberado e verificação contratual antes de qualquer arquitetura.
- Tags: #google-cloud #gemini-enterprise #brasil #residencia-de-dados #agentes-ia #governanca #release
- Relações: [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-10-29 07:35 BRT — AlloyDB libera índice vetorial de quatro níveis para até 10 bilhões de linhas

- Fonte: [Google Cloud — release notes do AlloyDB AI](https://docs.cloud.google.com/release-notes#October_28_2026)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Google Cloud anunciou disponibilidade geral dos índices vetoriais ScaNN de árvore de quatro níveis na extensão `alloydb_scann`, para AlloyDB com PostgreSQL 17 ou posterior. A documentação informa suporte a tabelas com até 10 bilhões de linhas vetoriais e manutenção automática dos índices.

  Em buscas filtradas, a opção `scann.satisfy_limit=relaxed_order` permite continuar a varredura por partições até obter resultados suficientes para o `LIMIT`, o que pode melhorar o recall. A atualização também torna o Vector assist disponível para ajudar a configurar embeddings, consultas e índices; desempenho continua dependente da carga e da configuração concreta.
- Por que importa: índice ScaNN 4LT em PostgreSQL 17+ entra em disponibilidade geral, com manutenção automática e busca filtrada com melhor recuperação; `Vector assist` também passa a GA. Amplia opção de busca semântica em grandes acervos geoespaciais/documentais, sem implicar necessidade de escala bilionária nos projetos atuais.
- Tags: #google-cloud #alloydb #busca-vetorial #embeddings #rag #postgresql #release
- Relações: [[Petrobras — Segundo cérebro]], [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-29 07:35 BRT — Google publica skills oficiais para agentes criarem integrações via API

- Fonte: [Google Cloud — Application Integration agent skills](https://docs.cloud.google.com/application-integration/docs/agent-skills-overview)
- Publicado: 2026-10-28 (data do release e da atualização da documentação; horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A documentação do Google Cloud descreve três skills publicadas no repositório aberto `google/skills`: `application-integration-basics`, `application-integration-authoring` e `application-integration-troubleshooting`. Elas orientam agentes a configurar o Application Integration, criar, versionar, publicar e executar integrações pela REST API, além de investigar falhas ou execuções suspensas.

  Os materiais cobrem APIs, regiões, IAM, contas de serviço, promoção entre ambientes e análise de logs, métricas, conectores e cotas. As skills são recursos reutilizáveis para agentes; não substituem permissões, validações ou a operação governada da plataforma.
- Por que importa: três skills abertas orientam agentes a configurar, criar/publicar e diagnosticar integrações do Google Cloud Application Integration via REST API. Fornecem referência operacional para automatizar fluxos entre sistemas corporativos com IAM e versionamento; uso nos projetos depende da adoção dessa plataforma.
- Tags: #google-cloud #skills #agentes-ia #integracao #api #automacao #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-29 07:35 BRT — CodeMender 0.17 reforça limites de sandbox e políticas de agentes de código

- Fonte: [Google Cloud — release notes de 28/10, CodeMender 0.17.0](https://docs.cloud.google.com/release-notes#October_28_2026)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: As notas de versão do Google Cloud descrevem mudanças no CodeMender 0.17.0 voltadas à configuração, diagnóstico e segurança. A versão separa o controle do sandbox das políticas de comandos, substituindo a opção abrangente `--unrestricted` por opções distintas. Durante `cm fix` e `cm verify`, `.git/hooks`, `.git/config` e `.codemender` passam a ser montados como somente leitura em sandboxes graváveis.

  A atualização também aplica os limites de `allowedRoots` a operações de descoberta e correção para impedir travessia por links simbólicos pendentes. Os controles disponíveis não eliminam a necessidade de configurar e revisar o ambiente de execução.
- Por que importa: nova versão separa configuração de sandbox da política de comandos, protege `.git/hooks`, `.git/config` e `.codemender` contra alterações durante correções e fecha travessia por symlinks fora de `allowedRoots`. Medidas relevantes ao avaliar agentes que editam repositórios com acesso a dados ou infraestrutura corporativa.
- Tags: #google-cloud #codemender #agentes-ia #seguranca #sandbox #desenvolvimento #release
- Relações: [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-28 12:35 BRT — Esri publica medidas para falha crítica no Brotli; impacto em ArcGIS sob investigação

- Fonte: [Esri — Brotli Vulnerabilities (Broccoli2Shell)](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/brotli-vulnerabilities-broccoli2shell)
- Publicado: 2026-10-27 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Esri informa que a vulnerabilidade crítica CVE-2026-111497 no decodificador Brotli foi divulgada por pesquisadores da OpenAI em 22 de outubro e entrou na lista KEV da CISA em 27 de outubro. A publicação, datada e atualizada em 29/10, classifica ArcGIS Enterprise 11.5, 12.0 e 12.1 e ArcGIS Pro 3.5 ou posteriores como afetados, com correções ainda pendentes.

  No ArcGIS Online, medidas mitigadoras foram implantadas e atualizações estão em andamento. Para ArcGIS Pro, Web Adaptor em IIS e extensões SOE/SOI, a orientação inclui atualizar o runtime .NET da Microsoft; no ArcGIS Server, a recomendação é desativar feeds de dados personalizados do SDK até o patch, salvo orientação de suporte.
- Por que importa: Esri investiga o impacto de CVE-2026-111497 em seus produtos e recomenda atualizar o .NET Framework usado por ArcGIS Pro, Web Adaptor em IIS e extensões SOE/SOI; ArcGIS Online já recebeu medidas mitigadoras. Quem opera ArcGIS Enterprise deve verificar versões e acompanhar a avaliação, sem presumir que todo produto está vulnerável.
- Tags: #esri #arcgis #arcgis-enterprise #brotli #cve #seguranca #patch
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-28 12:35 BRT — Patch corrige geocodificação quebrada entre ArcGIS Pro 3.6 e Server 11.5

- Fonte: [Esri — ArcGIS Server 11.5 Geocoding Capability Patch](https://support.esri.com/en-us/patches-updates/2026/arcgis-server-11-5-geocoding-capability-patch)
- Publicado: 2026-10-27 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Esri disponibiliza um patch para um defeito em serviços de geocodificação publicados no ArcGIS Server 11.5 a partir do ArcGIS Pro 3.6. Sem a correção, os serviços não retornam candidatos no painel Locate nem pela API FindAddressCandidates; na geocodificação de tabelas, endereços podem ficar sem correspondência, inclusive via GeocodeAddresses.

  O problema BUG-000181366 ocorre porque a capacidade de geocodificação não é habilitada por padrão ao publicar do Pro 3.6 para o Enterprise. A instalação reinicia o serviço ArcGIS Server e pode levar alguns minutos; a Esri orienta preparar rollback e oferece pacotes separados para Windows e Linux.
- Por que importa: serviços de geocodificação publicados do ArcGIS Pro 3.6 ou posterior no ArcGIS Server 11.5 podem devolver zero resultados, inclusive via `FindAddressCandidates` e `GeocodeAddresses`. Esri recomenda o patch para instalações afetadas; planejar reinício do serviço e rollback antes de aplicar.
- Tags: #esri #arcgis-enterprise #arcgis-pro #geocodificacao #api #patch #logistica
- Relações: [[Suzano — Rotas e logística]], [[GeoNext — LiDAR e rodovias]], [[IMAC — Plataforma GIS]]
- Confiança: alta

### 2026-10-28 12:35 BRT — EDGX divulga demonstração de computação de IA em órbita

- Fonte: [EDGX — Sterna em órbita](https://www.edgx.space/blog/edgx-launches-ai-computing-platform-in-orbit-on-spacex-transporter-16-using-nvidia-accelerated-computing)
- Publicado: 2026-10-28 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A EDGX, empresa belga de tecnologia espacial, relata que lançou duas cargas de demonstração na missão compartilhada SpaceX Transporter-16, em março de 2026. Segundo a empresa, uma carga baseada na plataforma Sterna com NVIDIA Jetson já retornou os primeiros dados operacionais em órbita em até duas semanas; a segunda aguardava comissionamento do satélite.

  A proposta é executar computação a bordo para reduzir dependência de infraestrutura terrestre e processar dados mais perto da coleta. A empresa relata primeiros clientes assinados e missões previstas para 2027, mas não apresenta métricas independentes de desempenho nem resultados comerciais verificáveis.
- Por que importa: empresa reporta que carga baseada em NVIDIA Jetson, lançada em março, já retornou dados operacionais em órbita; outra ainda está em comissionamento. Processar imagens a bordo pode reduzir volume transmitido e latência de alertas geoespaciais, mas a fonte não demonstra ainda serviço comercial ou desempenho dessas aplicações.
- Tags: #geoia #edge-ai #observacao-da-terra #satelites #nvidia #demonstracao
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Vale — GeoIA SAB.IA]]
- Confiança: média

### 2026-10-23 07:29 BRT — OlmoEarth v1.3 libera embeddings planetários anuais de 10 m

- Fonte: [Ai2 — OlmoEarth v1.3](https://allenai.org/blog/olmoearth-v1-3)
- Publicado: 2026-10-22 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Ai2 anunciou o OlmoEarth v1.3 junto com embeddings anuais pré-computados para todo o planeta, em resolução de 10 metros e dimensões de 64 ou 128, além de um explorador web para consultar e personalizar mapas. O modelo combina séries temporais de radar Sentinel-1 e imagens multiespectrais Sentinel-2 e Landsat para gerar vetores por pixel.

  A proposta permite que classificação de culturas, cobertura do solo e detecção de mudanças usem classificadores menores, sem repetir o processamento de imagens em cada projeto. Nos benchmarks divulgados pelo Ai2, os embeddings de 128 dimensões lideraram 20 de 27 avaliações; esses resultados não substituem validação em dados locais.
- Por que importa: o Ai2 liberou modelo, dados e embeddings globais pré-computados (64/128 dimensões) e um explorador para encontrar áreas semelhantes e criar mapas com poucos exemplos. Reduz o esforço para testar classificação de culturas, vigor e mudança de cobertura em projetos GeoIA; desempenho local ainda precisa ser validado.
- Tags: #geoia #olmoearth #sensoriamento-remoto #embeddings #sentinel #landsat #agro #florestal #release
- Relações: [[Amaggi — Monitoramento de desmatamento]], [[Eucatex — Monitoramento de vigor florestal]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-23 07:29 BRT — PLANTEUR expõe lacuna de generalização na classificação de culturas tropicais

- Fonte: [Ai2 — PLANTEUR: benchmark de culturas tropicais](https://allenai.org/blog/planteur)
- Publicado: 2026-10-22 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Ai2 apresentou PLANTEUR, um benchmark aberto para classificação de culturas em seis territórios tropicais franceses. O conjunto reúne 2.750 séries temporais alinhadas de Sentinel-2, Sentinel-1 e Landsat-8, com rótulos derivados de parcelas agrícolas que cobrem 4.506 km² e sete classes, entre elas cana-de-açúcar, banana e abacaxi.

  Os autores incluem avaliações deixando uma ilha fora do treinamento e cenários com poucos exemplos. Nos experimentos divulgados, todos os métodos avaliados tiveram desempenho substancialmente inferior ao benchmark PASTIS e perderam cerca de metade da acurácia em ilha não vista; o resultado evidencia limites de transferência geográfica, sem medir diretamente desempenho em outros países.
- Por que importa: novo conjunto aberto reúne séries Sentinel-1/2 e Landsat-8 de 4.506 km² de parcelas, sete classes de culturas (incluindo cana) e testes fora da região de treino. Nos testes dos autores, todos os métodos perderam cerca de metade da acurácia em uma ilha não vista: alerta concreto para validar modelos agrícolas fora da área de treinamento.
- Tags: #geoia #paper #benchmark #agro #cana-de-acucar #classificacao-de-culturas #generalizacao #sentinel
- Relações: [[CTC — Centro de Tecnologia Canavieira]], [[Atvos — Visão computacional]], [[São Martinho — Planejamento agrícola]]
- Confiança: alta

### 2026-10-23 07:29 BRT — Claude Code 2.1.309 corrige contornos de sandbox e proteção de configuração MCP

- Fonte: [Anthropic — Claude Code v2.1.309](https://github.com/anthropics/claude-code/releases/tag/v2.1.309)
- Publicado: 2026-10-22 22:18 (horário exibido pelo GitHub; fuso não informado)
- Resumo: A versão 2.1.309 do Claude Code lista correções para problemas de isolamento e permissões. Entre elas, comandos Bash em sandbox no macOS e Linux executavam arquivos de inicialização do shell fora do sandbox; regras de escrita no macOS podiam falhar quando o caminho passava por symlink; e comandos aceitos automaticamente podiam alterar o arquivo MCP indicado por `--mcp-config`.

  O release também corrige verificações de permissão Bash para alguns comandos compostos, regras de bloqueio de edição contornáveis por redirecionamento e comandos que a proteção de worktree deveria recusar. São correções descritas pelo fornecedor; a publicação não quantifica exposição de instalações anteriores nem afirma exploração.
- Por que importa: o release corrige execução de arquivos de inicialização do shell fora do sandbox, falhas de regras de escrita via symlink, alteração indevida do arquivo `--mcp-config` e contornos de permissões Bash/worktree. É atualização prioritária para agentes com acesso a código, arquivos e servidores MCP; revisar políticas após atualizar.
- Tags: #anthropic #claude-code #mcp #agentes-ia #sandbox #seguranca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-23 07:29 BRT — OpenAI disponibiliza Decisions API para decisões delimitadas de agentes

- Fonte: [OpenAI — Decisions API](https://openai.com/index/decisions-api/)
- Publicado: 2026-10-22 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A OpenAI anunciou disponibilidade geral da Decisions API, construída sobre GPT-6 Luna e voltada a respostas delimitadas, como classificação, roteamento ou seleção de próxima ação. A API aceita contexto em texto, imagens ou JSON e retorna probabilidade, uma opção predefinida ou uma pontuação.

  Segundo a empresa, pode operar até dez vezes mais rápido que GPT-6 Luna via Responses API; essa comparação é alegação da OpenAI, não garantia para qualquer tarefa. O anúncio também registra integração com GPT-Live, cache de prompt, residência de inferência nos EUA e União Europeia e até 400 perguntas por requisição.
- Por que importa: API agora em disponibilidade geral responde probabilidade, escolha ou escore a partir de texto, imagem ou JSON, com até 400 perguntas por requisição. Pode reduzir latência/custo de triagem e roteamento em agentes e eventos geoespaciais; o ganho de até 10 vezes é alegação da OpenAI, não garantia para estes projetos.
- Tags: #openai #decisions-api #agentes-ia #api #classificacao #roteamento #release
- Relações: [[NAVIS / GeoFramework]], [[Atvos — Visão computacional]], [[Petrobras — Segundo cérebro]]
- Confiança: alta

### 2026-10-23 07:29 BRT — ICEYE e OroraTech integram dados térmicos e SAR para incêndios

- Fonte: [OroraTech — parceria com ICEYE](https://ororatech.com/resources/news-blog/iceye-partners-with-ororatech-to-deliver-full-lifecycle-wildfire-intelligence-2)
- Publicado: 2026-10-22 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: ICEYE e OroraTech anunciaram parceria para reunir dados térmicos de satélite da OroraTech com observações de radar de abertura sintética da ICEYE em uma solução de inteligência sobre incêndios. Os dados térmicos destinam-se à detecção de focos e ao acompanhamento da frente ativa; o SAR pode observar através de fumaça, nuvens e escuridão e ajudar a avaliar impactos em edifícios.

  A proposta cobre da detecção inicial ao monitoramento da progressão e à avaliação de danos perto de comunidades e infraestrutura. O anúncio descreve capacidade integrada e usos pretendidos por governos, seguradoras e concessionárias, mas não apresenta validação independente de latência, precisão ou implantação em clientes.
- Por que importa: a parceria anuncia integração de detecção/avanço do fogo por satélites térmicos com observações SAR para avaliar impactos mesmo sob fumaça e nuvens. É combinação relevante para monitoramento florestal e resposta a incêndios; a fonte não traz validação independente de latência ou implantação em cliente.
- Tags: #sensoriamento-remoto #sar #termal #incendios #florestal #parceria #observacao-da-terra
- Relações: [[Eucatex — Monitoramento de vigor florestal]], [[Amaggi — Monitoramento de desmatamento]]
- Confiança: alta

### 2026-10-22 07:27 BRT — Claude Code 2.1.307 evita duplicar chamadas de escrita via MCP HTTP

- Fonte: [Anthropic — Claude Code v2.1.307](https://github.com/anthropics/claude-code/releases/tag/v2.1.307)
- Publicado: 2026-10-21 22:17 (horário exibido pelo GitHub; fuso não informado)
- Resumo: O release publicado em 21 de outubro corrige chamadas de ferramentas MCP via HTTP que podiam ser enviadas duas vezes quando a conexão era interrompida durante a operação. A partir desta versão, o Claude Code só repete chamadas de leitura ou operações idempotentes, reduzindo o risco de duplicar alterações em sistemas externos.

  A atualização acrescenta evento OpenTelemetry para registrar interrupções, pedidos de aprovação e devoluções de chamadas por regras de permissão, hooks ou sandbox. Outro ajuste corrige turnos iniciados sem ferramentas MCP recentes fornecidas pelo SDK quando havia tarefa em segundo plano; o release não detalha métricas de redução de duplicações.
- Por que importa: se a conexão caía durante uma chamada MCP HTTP, ferramentas podiam ser acionadas duas vezes; agora só operações de leitura ou idempotentes são repetidas. Release também adiciona evento OpenTelemetry para decisões de segurança e corrige atualização de ferramentas de servidores MCP do SDK durante tarefas em segundo plano — pontos críticos para agentes que escrevem em sistemas corporativos.
- Tags: #anthropic #claude-code #mcp #agentes-ia #idempotencia #observabilidade #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-22 07:27 BRT — Modelos OpenAI e fluxos Codex entram no Google Cloud em prévia privada

- Fonte: [Google Cloud — OpenAI models in Model Garden](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers) e [OpenAI — parceria com Google Cloud](https://openai.com/index/openai-models-google-cloud/)
- Publicado: 2026-10-21 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: Os anúncios de 21 de outubro apresentam a chegada de modelos OpenAI ao Model Garden do Google Cloud, incluindo GPT-6 Astra, GPT-6.1 Sol e GPT-6 Luna. A OpenAI também informa que fluxos agênticos do Codex serão integrados à plataforma. O Google descreve controles de identidade, auditoria e perímetro de dados, além de cobrança pelo Marketplace e uso de compromissos de gasto existentes.

  A OpenAI diz que a disponibilidade geral estava planejada para as semanas seguintes; portanto, o anúncio não indicava acesso imediato e generalizado. As fontes não afirmam que todos os clientes já tivessem acesso nem que os fluxos do Codex já estivessem disponíveis.
- Por que importa: GPT-6 Astra, GPT-6.1 Sol e GPT-6 Luna começam a chegar ao Model Garden para clientes empresariais selecionados; Google informa que esses clientes já podem conectar Codex CLI/Desktop para inferência na plataforma. Isso cria opção de testar agentes e desenvolvimento com governança, auditoria e faturamento Google Cloud, mas ainda não é disponibilidade geral.
- Tags: #openai #codex #google-cloud #model-garden #agentes-ia #parceria #preview
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-22 07:27 BRT — Esri avalia impacto de duas falhas críticas de PHP no ecossistema ArcGIS

- Fonte: [Esri — Recent PHP Vulnerabilities](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/recent-php-vulnerabilities) e [PHP Project — alerta e versões corrigidas](https://www.php.net/archive/2026.php)
- Publicado: 2026-10-21 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O PHP Project publicou em 21 de outubro correções para duas vulnerabilidades críticas, CVE-2026-109618 e CVE-2026-109619, que podem permitir execução remota de código sem autenticação. O projeto recomenda atualizar instalações que atendem requisições web para PHP 8.5.12, 8.4.27, 8.3.36 ou 8.2.35.

  A nota da Esri, atualizada em 22 de outubro, esclarece que ArcGIS Online e os produtos fundamentais ArcGIS Enterprise — Server, Portal e Data Store —, além do ArcGIS Pro, não são afetados. Produtos com exemplos em PHP exigiriam infraestrutura PHP própria do cliente; nesse caso, essa infraestrutura deve ser atualizada.
- Por que importa: PHP corrigiu CVE-2026-109618 e CVE-2026-109619, ambas com potencial de execução remota sem autenticação, nas versões 8.5.12, 8.4.27, 8.3.36 e 8.2.35. Esri informa que ArcGIS Online não usa PHP e ainda avalia demais produtos; não há impacto confirmado em ArcGIS Enterprise. Verificar componentes PHP próprios ou adjacentes e acompanhar conclusão da avaliação Esri.
- Tags: #esri #arcgis #php #seguranca #cve #infraestrutura #avaliacao-de-impacto
- Relações: [[IMAC — Plataforma GIS]], [[NAVIS / GeoFramework]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-21 07:27 BRT — Claude Code 2.1.305 corrige integração MCP, gateways e retomada de agentes

- Fonte: [Anthropic — Claude Code v2.1.305](https://github.com/anthropics/claude-code/releases/tag/v2.1.305)
- Publicado: 2026-10-20 20:46 (horário exibido pelo GitHub; fuso não informado)
- Resumo: A versão 2.1.305 corrige falhas que faziam requisições falharem em Vertex, Bedrock e outros provedores ou gateways que rejeitam buscas de ferramentas. Também impede que servidores MCP definidos por sessão em nuvem ou SDK sejam substituídos por configurações locais de mesmo nome, e corrige retomada de workflows que podia executar novamente agentes já concluídos.

  No Linux, a opção `sandbox.allowNestedUserNamespaces` permite namespaces aninhados para casos como Chromium e Podman sem privilégios. A própria release alerta que esse recurso pode contornar proteções de arquivos do sandbox, portanto sua habilitação requer avaliação do impacto de segurança.
- Por que importa: corrige a substituição indevida de servidores MCP fornecidos pela sessão em nuvem/SDK e falhas de requisições via Vertex, Bedrock ou gateways sem ToolSearch. A retomada de workflows deixa de reexecutar agentes já concluídos. A nova opção de namespaces aninhados no Linux permite Chromium/Podman, mas pode contornar proteções de arquivos do sandbox; requer avaliação antes de habilitar.
- Tags: #anthropic #claude-code #mcp #agentes-ia #workflow #seguranca #release
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-21 07:27 BRT — Alerta de segurança no SDK TypeScript do MCP exige validação explícita de audiência

- Fonte: [GitHub Advisory — GHSA-rvq5-wwqv-78pq / CVE-2026-111771](https://github.com/advisories/GHSA-rvq5-wwqv-78pq)
- Publicado: aviso original em 2026-10-05; publicado na base de advisories e atualizado em 2026-10-20 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O aviso descreve versões do SDK TypeScript do MCP cuja autenticação bearer no servidor não verificava se o token havia sido emitido para aquele serviço. Se o mesmo servidor de autorização emite tokens para vários serviços e a aplicação não confere o campo `aud`, um token válido destinado a outro serviço pode ser aceito.

  O advisory lista versões afetadas de `@modelcontextprotocol/sdk`, `@modelcontextprotocol/server`, `@modelcontextprotocol/express` e `server-legacy`, além das versões corrigidas. Atualizar sozinho não ativa a checagem: é preciso configurar `expectedResource` e retornar a audiência como `AuthInfo.resource`, ou validar `aud` diretamente no verificador.
- Por que importa: servidores MCP HTTP que usam `requireBearerAuth()`/`verifyBearerToken()` podem aceitar token emitido para outro serviço se o emissor atende múltiplos recursos e o verificador não checa `aud`. Versões corrigidas existem, mas só atualizar não ativa a proteção: é preciso configurar `expectedResource` e devolver `AuthInfo.resource`, ou validar `aud` no verificador.
- Tags: #mcp #typescript #sdk #oauth #seguranca #cve #agentes-ia
- Relações: [[NAVIS / GeoFramework]], [[Petrobras — Segundo cérebro]], [[GeoFiscal-Sinter]]
- Confiança: alta

### 2026-10-21 07:27 BRT — Gemini em Google Distributed Cloud ganha busca RAG isolada da internet

- Fonte: [Google Cloud — Managed RAG search inside the sovereign perimeter](https://cloud.google.com/blog/topics/hybrid-cloud/managed-rag-search-inside-the-sovereign-perimeter-gemini-on-gdc-enterprise-search)
- Publicado: 2026-10-21 (horário/fuso não informados; posição exata na janela de 24 horas não confirmada)
- Resumo: O Google anunciou em prévia uma experiência gerenciada de busca empresarial com Gemini no Google Distributed Cloud air-gapped. A empresa afirma que a solução executa busca RAG dentro do perímetro físico da organização, sem conexão com a internet pública ou infraestrutura global do Google Cloud. Usuários podem consultar arquivos, pedir sínteses, comparações ou traduções e receber respostas com citações.

  A publicação descreve suporte a documentos, planilhas, imagens, áudio e vídeo, com identidade e dados mantidos na implantação local. É uma oferta em prévia, não disponibilidade geral; arquitetura e segurança são declarações do fornecedor, sem resultados independentes de desempenho.
- Por que importa: em *preview*, busca empresarial multimodal com citações roda em GDC air-gapped, com ingestão, embeddings, PostgreSQL e controles de identidade dentro do perímetro local. Arquitetura relevante para agentes sobre dados técnicos sigilosos de mineração e óleo e gás; ainda não é disponibilidade geral.
- Tags: #google-cloud #gemini #rag #air-gap #dados-sensiveis #agentes-ia #busca-empresarial
- Relações: [[Petrobras — Segundo cérebro]], [[Vale — GeoIA SAB.IA]], [[NAVIS / GeoFramework]]
- Confiança: alta

### 2026-10-21 07:27 BRT — llm-d 1.0 publica infraestrutura aberta para inferência de agentes em escala

- Fonte: [Google Cloud — Announcing llm-d 1.0](https://cloud.google.com/blog/topics/ai-infrastructure/llm-d-1-0-an-open-source-stack-for-distributed-inference)
- Publicado: 2026-10-20 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: O Google anunciou a versão 1.0 do llm-d, infraestrutura aberta e nativa de Kubernetes para inferência distribuída de modelos de linguagem. O projeto, cofundado pelo Google com Red Hat, IBM e outros parceiros, combina servidores de modelos e componentes de orquestração para atender cargas com múltiplas etapas, prefixos longos compartilhados e picos de tráfego.

  A publicação destaca roteamento que considera cache e carga, cache KV em camadas, controle de fluxo multitenant e alta disponibilidade. O Google relata demonstração com mil agentes em GKE e frota mista de TPUs e GPUs, mas esse exemplo não é garantia de desempenho para qualquer implantação.
- Por que importa: release Kubernetes-native reúne roteamento com afinidade de cache, QoS multitenant, cache KV em camadas, alta disponibilidade e atualização sem interromper sessões. É base técnica para avaliar custo e latência de agentes auto-hospedados com contexto longo e tráfego irregular, sem implicar ganho garantido nos projetos.
- Tags: #google-cloud #llm-d #inferencia #kubernetes #agentes-ia #infraestrutura #open-source
- Relações: [[NAVIS / GeoFramework]], [[Vale — GeoIA SAB.IA]]
- Confiança: alta

### 2026-10-21 07:27 BRT — Tanager-2 demonstra detecção hiperespectral de metano na primeira imagem

- Fonte: [Planet — First light from Tanager-2 and SuperDove Flock 4J](https://www.planet.com/pulse/sharing-first-light-images-from-tanager-2-and-superdove-flock-4j/)
- Publicado: 2026-10-20 (horário/fuso não informados; janela exata de 24 horas não confirmada)
- Resumo: A Planet publicou primeiras imagens dos satélites Tanager-2 e SuperDove Flock 4J, lançados no início de outubro de 2026. Segundo a empresa, o Tanager-2 capturou sua primeira imagem sobre a Espanha em 7 de outubro, seis dias após o lançamento; usando esses dados, a Carbon Mapper detectou uma pluma de metano na costa espanhola.

  Um SuperDove do novo grupo fotografou parte da Grande Barreira de Corais australiana no dia anterior. A Planet afirma que as imagens indicam satélites saudáveis e em comissionamento; elas não comprovam que a constelação já opere como serviço plenamente disponível.
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
