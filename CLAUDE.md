# Rotina do Instagram da WFtec (@wftec_)

Este repositório é **público**. Ele guarda só os arquivos dos posts, que ficam públicos no Instagram de qualquer forma. Nunca coloque aqui nada que não iria para o feed: senhas, tokens, dados de clientes, planilhas internas.

**Pedido do Wanderson Fortunato (dono da WFtec, Natal/RN), em 29/10/2026:**
- **Publicação direta**, sem aprovação prévia, com **dois posts por dia**.
- **Um VÍDEO NOVO todo dia.** Nada de repostar vídeo antigo.
- **Só três assuntos:** **Double Check Folha**, **ferramenta de Sindicatos** e **WFtec Ponto**.
- Os fatos de cada produto estão em **`produtos.md`**. Use só o que estiver lá.

## Como publicar

- **Metricool:** marca `blogId 7176830`, fuso `America/Fortaleza`, rede `instagram`.
- **Horários:**
  - **Seg a Sex (dias úteis):** **11:47** (post do almoço) e **18:37** (Reels).
  - Sábado, domingo e feriado: sem post.
  - Por que esses horários:
    - Sprout Social 2026 (software/tecnologia e serviços financeiros): 11h–14h nos dias úteis.
    - Hootsuite 2026: fim da tarde, entre 15h e 19h.
    - Metricool 2026: 18h–21h, com Reels mais fortes à noite.
    - Dados da própria conta no Metricool: picos às 10–12h e às 18h.
  - Revise isso todo mês: rode `getBestTimeToPostByNetwork` e ajuste em até 1 h se os dados da conta mudarem.
- **Envio:** `createScheduledPost` com `autoPublish: true` e `draft: false`.
  - Reels: `instagramData.type = "REEL"` e `videoThumbnailUrl` = capa.jpg.
  - Carrossel: várias imagens em `media`, na ordem.
- **Stories (todo post vai também para os Stories):** para cada post do feed, agende um segundo post `instagramData.type = "STORY"`, **2 minutos depois**, sem `text`.
  - Reels: use o mesmo vídeo. Pode reaproveitar a URL `static.metricool.com` que o Metricool devolveu no post do feed.
  - **Carrossel: TODOS os slides vão para os Stories, um por um (pedido do Wanderson, 06/11).** Só a capa nos Stories deixa a sequência pela metade e fica feio.
    - Gere com `python3 kit/story.py AAAA-MM/AAAA-MM-DD-tema`. Ele cria `-story-1.jpg … -story-N.jpg` (1080×1920, slide centralizado, contagem "2 / 6").
    - Agende um Story por slide, **um minuto depois do outro e na ordem**, começando 2 minutos depois do post do feed (11:49, 11:50, 11:51…).
  - Imagem única: um Story com `-story-1.jpg` (o mesmo `kit/story.py` serve).
  - Registre o Story também em `publicados.md`.
- **Mídia:** use URLs `https://raw.githubusercontent.com/wandersonfortunato1-eng/wftec-midia/main/<caminho>`. O Metricool baixa e copia o arquivo.
  - Faça **commit e push antes** de agendar.
  - Antes de agendar, confira com `curl -sI` que a URL responde 200.
- **Registro:** depois de agendar, acrescente uma linha em `publicados.md` com o id do Metricool, e faça commit e push.
- **Duplicidade:** antes de criar, rode `getScheduledPosts` para o dia-alvo e só crie o horário que estiver vazio.

## Dias sem post

Não há post em sábado, domingo nem nos feriados e emendas abaixo. A tarefa diária, quando o dia seguinte for um desses, termina sem produzir nada.

| Ano | Datas |
| --- | --- |
| 2026 | 02/11 (Finados), 20/11 (Consciência Negra), 24/12 a 01/01 (Natal e Ano-Novo) |
| 2027 | 01/01, 08/02 e 09/02 (Carnaval), 26/03 (Sexta-feira Santa), 21/04 (Tiradentes), 01/05, 27/05 (Corpus Christi), 07/09, 12/10, 02/11, 15/11, 20/11, 24/12 a 31/12 |

Antes de cada ano novo, confira as datas na web e acrescente o ano seguinte aqui.

## O que publicar

### Post da noite: Reels NOVO, todo dia

Os três produtos se revezam assim:

| Seg | Ter | Qua | Qui | Sex |
| --- | --- | --- | --- | --- |
| Sindicatos | Double Check | Ponto | Sindicatos | Double Check ou Ponto (alternando a cada semana) |

A ferramenta de Sindicatos foi o tema mais visto até agora (veja "Análise da conta"). Por isso ela entra 2 vezes por semana.

Cada Reels mostra **um ângulo só**: uma dor, uma função, um número. Vídeo-resumo de tudo não entra. Nunca repita ângulo dos últimos 21 Reels de `publicados.md`.

**Ideias de ângulo:**
- **Double Check Folha:**
  - quem saiu e continuou na folha;
  - a verba que sumiu;
  - filtro por centro de custo;
  - tolerância em reais;
  - salário abaixo do mínimo;
  - líquido negativo;
  - salário-família indevido;
  - custo da folha (INSS patronal e FGTS);
  - arquivos lidos no seu computador;
  - exportar para Excel, CSV ou PDF.
- **Sindicatos:**
  - enquadramento pelo CNPJ e CNAE;
  - cores por tipo de documento;
  - circular do sindicato;
  - aditivo que muda o piso;
  - varredura em mais de 6 mil sites;
  - selo "Nova";
  - aviso dos 60 dias;
  - notificações do dia, com o número real do D1;
  - apresentação da convenção com a cláusula de origem;
  - filtro de vigência;
  - convenção do estado X.
- **Ponto:**
  - batida nunca bloqueada;
  - aviso de possível GPS falso;
  - código de auditoria;
  - hora do servidor;
  - aprovação automática dentro da tolerância;
  - pedido de ajuste;
  - planilha estilo SCI;
  - ocorrências (férias, atestado);
  - motor CLT (tolerância, hora noturna, extras);
  - interjornada de 11h;
  - banco de horas com alerta de 6 meses;
  - fechamento que consolida e estorna;
  - feriados estaduais em 1 clique.

### Post do almoço (11:47): conteúdo de VALOR, que dá vontade de salvar e mandar para o colega

**Por que mudou (06/11):** em uma semana a conta foi de 481 para 483 seguidores. Os posts falam só do produto, e quem vê é quase só quem já segue. Ninguém compartilha nem salva propaganda. Quem dá seguidor é o conteúdo útil, que circula.

- Tema dentro dos assuntos dos 3 produtos (folha, convenção/sindicato, ponto/jornada), mas **ensinando**, não vendendo. O produto aparece só no último slide, como "na WFtec isso é automático".
- Séries fixas (o nome da série vai no kicker e na capa, para criar hábito):
  - **Seg · Prazo da semana:** o que vence nesta semana no DP (eSocial, FGTS Digital, DCTFWeb, salário, 13º…). Datas conferidas na web.
  - **Ter · Erro de folha:** um erro comum de fechamento e como pegar antes (verba que some, desligado na folha, piso desatualizado…).
  - **Qua · Convenções da semana:** número real do D1 por estado, com destaque para RN e o Nordeste. Termine com "comente o seu estado" (gera comentário).
  - **Qui · CLT em 1 minuto:** uma regra de jornada ou ponto explicada com exemplo (tolerância, hora noturna, interjornada, banco de horas). Artigo da CLT citado.
  - **Sex · Checklist para salvar:** lista prática (fechamento de folha, admissão, convenção nova chegou…). Último slide: "Salve para usar no fechamento".
- Carrossel de 6 a 8 slides. Imagem única só se o assunto couber em uma tela.

### Se algo falhar

Se não der para fazer o vídeo (a voz falhou, deu erro na renderização):
- publique um carrossel no horário da noite;
- avise o Wanderson.

Nunca deixe o dia sem post e nunca reposte um vídeo antigo.

## Como fazer o Reels novo (voz do Antonio na nuvem)

1. **Roteiro:** escreva de 5 a 7 falas, uma por linha, em `voz/AAAA-MM-DD-tema/falas.txt`.
   - Fala 1 = gancho em pergunta, até 12 palavras. Última fala = "<produto>. <frase de efeito>. Fale com a gente."
   - Total de 35 a 55 s. **O máximo é 60 s.**
   - Números e siglas por extenso para a voz ler certo ("dez minutos", "I P").
   - **Pronúncia de siglas (pedido do Wanderson):** CNAE se fala como palavra ("cnáe"), não soletrado. Em `falas.txt` escreva **"Cnáe"**.
     - Quando a fala usar grafia de pronúncia, crie também `legendas.txt` (mesmas linhas, grafia correta: "CNAE"). A legenda na tela sai desse arquivo.
     - CNPJ, CPF, FGTS e INSS continuam soletrados, como se fala no DP.
2. **Voz:** faça commit e push. A Action **"Voz do Antonio"** (`.github/workflows/voz.yml`) gera `fala1.mp3…` com `pt-BR-AntonioNeural +14% +2Hz` em cerca de 1 minuto.
   - Acompanhe com `gh api repos/wandersonfortunato1-eng/wftec-midia/actions/runs --jq '.workflow_runs[0]|.status,.conclusion'`.
   - Depois rode `git pull --rebase`.
3. **Composição:** crie `AAAA-MM/AAAA-MM-DD-tema/video.html`, partindo de um modelo de `kit/video/ref/`. O melhor exemplo completo é `2026-10/2026-10-31-ponto-clt/video.html`.
   - Uma cena por fala.
   - Gancho escuro de impacto, depois telas claras que imitam o sistema, depois o outro com logo e CTA.
   - Dados fictícios levam `.mask` e o selo "exemplos ilustrativos".
   - **Atenção:** os `falas.txt` dos modelos `ref/` são antigos. Não copie "Comparativo de Folha" nem "Fortunato".
4. **Configuração:** crie `video.json` com:
   - `{"voz": "voz/AAAA-MM-DD-tema", "min": {"1": 5.2}, "dest": [palavras-chave em laranja], "cues": {...}, "capa": segundos}`.
5. **Cues:** rode `python3 kit/video/build.py PASTA --analisar`. O comando mostra as pausas de cada fala, e com elas você ajusta os `cues` para cada animação cair na palavra certa.
6. **Conferência:** rode `python3 kit/video/build.py PASTA --preview 2,6,10,...`.
   - Olhe os quadros com Read: nada cortado, sobreposto ou vazio demais.
   - Corrija e repita até ficar bom.
7. **CAPA (atenção redobrada, pedido do Wanderson):** a capa NUNCA é um quadro do meio do vídeo, porque esse quadro aparece com legenda e tela pela metade e fica feio na grade do perfil.
   - Gere uma capa desenhada: `python3 kit/capa.py PASTA/capa.jpg "KICKER" "Pergunta com <em>destaque</em>?" "Subtítulo curto"`.
   - O kicker é o nome do produto em caixa alta. O título é a pergunta-gancho, com até cerca de 7 palavras.
   - Tudo fica dentro da faixa central que a grade 3:4 mostra.
   - Rode **depois** do build final, porque o build sobrescreve `capa.jpg`. Olhe a capa com Read antes de publicar.
8. **Renderização:** rode `python3 kit/video/build.py PASTA`. Ele gera `video.mp4` e `capa.jpg` em cerca de 3 minutos.
   - Faça commit só de `video.html`, `video.json`, `video.mp4` e `capa.jpg`. O `.gitignore` já ignora o resto.

## Regras de conteúdo (obrigatórias)

### Nomes de produto

| Use | Não use |
| --- | --- |
| **Double Check Folha** | "Comparativo de Folha" |
| **ferramenta de Sindicatos da WFtec** | "3 ferramentas" |
| **WFtec Ponto** | — |

### Dados pessoais e de empresas

- **Esconda** nomes de clientes, empregados e empresas, CNPJ e CPF. Use uma tarja `.mask` ou dados claramente ilustrativos, com o selo "exemplos ilustrativos".
- **Pode mostrar:** convenções coletivas, sindicatos e números agregados do acervo, que são públicos.

### Por produto

- **Double Check Folha:** não cite o Fortunato (a IA).
- **Ponto:**
  - Não diga "REP", "REP-P", "homologado" nem "certificado".
  - A localização é registrada **só na batida**. Nunca diga que o funcionário é rastreado ou monitorado o tempo todo.
  - A marcação nunca é bloqueada.
- **Notificações de convenção:** só dentro da ferramenta (sino e aba Notificações), fechadas às 8h. Não prometa e-mail nem WhatsApp.

### Números e fatos

- Não invente número. Para dados de convenção, consulte o D1 (`cc3e5370-9d3f-458c-9bb9-5c526ba44457`):
  - tabela `alertas_convencoes`: `dia`, `total`, `por_uf`, `por_origem`;
  - tabela `instrumentos`: `tipo`, `uf`, `descoberto_em`, `vigencia_fim`, `origem`.
- Lei e prazos: confira na web antes de afirmar.

### Legenda

- Português do Brasil.
- Gancho na 1ª linha, de 3 a 6 linhas úteis.
- **CTA de crescimento (06/11):** em todo post, peça uma ação que espalhe ou que traga seguidor.
  - Conteúdo de valor: "💾 Salve para usar no fechamento" + "📲 Mande para quem fecha folha com você" + "➕ Siga @wftec_ para receber o próximo".
  - Produto: "➕ Siga @wftec_" + "👉 Fale com a gente: wftec.com.br".
- **Primeiro comentário** (`firstCommentText`): uma pergunta simples que dá vontade de responder ("Qual o seu estado?", "Você confere isso hoje como?").
- **Palavras de busca:** a 1ª frase da legenda leva o termo que o pessoal pesquisa no Instagram ("fechamento de folha", "convenção coletiva", "controle de ponto"), porque a busca lê a legenda.
- De 5 a 8 hashtags. Sempre `#wftec`, mais `#departamentopessoal`, `#folhadepagamento`, `#rh`, `#contabilidade` e as do tema. Uma vez por semana, inclua as locais `#contabilidadenatal` e `#natalrn`.

### Alcance para quem não segue (Trial Reels)

- **Terça e quinta,** o Reels sai como **Reels de teste** (`instagramData.type = "TRIAL_REEL"`). O Instagram mostra primeiro só para quem NÃO segue a conta, que é exatamente o público para ganhar seguidor.
- Ele não aparece na grade até ser compartilhado com os seguidores. Isso pode ser feito pelo app, se o resultado for bom.
- Nos outros dias, Reels normal.
- Toda segunda, na leitura das métricas, compare o alcance dos Trial Reels com o dos normais e anote aqui.

## Análise da conta (29/10/2026)

**Números da conta:** 481 seguidores e 7 Reels publicados à mão antes desta rotina. Visualizações de cada Reels:

| Reels | Visualizações |
| --- | --- |
| "Pensou que Sindicatos era só busca de convenção?" | **299** |
| Double Check "O que mudou na folha deste mês?" | 231 |
| FAQ da Busca de Convenções | 201 |
| "Site por site?" | 186 |
| Ponto "Cada batida, um ponto no mapa" | 140 |
| "Atenção, DP! 17:11:55" | 72 |
| "Ainda procurando convenção site por site?" | não lido |

**O que os números dizem:**
- O que mais rende:
  - **pergunta no primeiro quadro**;
  - **tema Sindicatos**;
  - **tela clara do sistema**.
- O que menos rende: alerta genérico em fundo escuro ("Atenção, DP!").

**Os 7 vídeos de `backlog/` JÁ FORAM POSTADOS e não devem ser repostados.**

**Leitura de 02/11/2026 (Reels de 27/10 a 02/11, via Metricool):**
- "Saiu convenção nova da sua categoria…" (Sindicatos, 30/10): 24 visualizações, alcance 11, tempo médio 5,1 s, 0 compartilhamentos e 0 salvamentos.
- "Seu ponto calcula a CLT sozinho…" (Ponto, 29/10): 19 visualizações, alcance 13, tempo médio 3,2 s, 0 compartilhamentos e 0 salvamentos.
- Conclusão: amostra pequena e tempo médio baixo (3 a 5 s). O que pesa é o primeiro segundo: a pergunta-gancho tem de aparecer já no quadro 1 e ser curta. Sindicatos segue na frente. Ganchos com uma dor concreta (uma verba, uma batida) em vez de lista de funções.

**Atualização:** o Metricool só tem dados a partir de 29/10. Toda segunda-feira, leia as métricas de Reels da semana anterior com `getAnalyticsDataByMetrics`:
- Campos: `IGRE02` (data), `IGRE03` (texto), `IGRE23` (visualizações), `IGRE11` (alcance), `IGRE24` (tempo médio), `IGRE27` (retenção), `IGRE21` (compartilhamentos), `IGRE12` (salvamentos).
- Anote as conclusões aqui e ajuste ganchos e temas.

## Visual dos carrosséis e imagens

- Use o **`kit/base.css`**, 1080×1350:
  - fundo `#F6F2EF`, laranja `#F15A25`, títulos em Archivo itálico 900, texto em IBM Plex;
  - classe `.dark` para slides escuros.
- Escreva um HTML em `AAAA-MM/AAAA-MM-DD-tema.html`, com um `<section class="slide">` por slide.
- Gere com `python3 kit/render.py <html> <prefixo>`.
  - Modelos: `kit/exemplo.html` e `2026-10/2026-10-30-double-check-folha.html`.
- Olhe os PNGs com Read e converta para JPG (qualidade 90).
- Primeiro slide: gancho em pergunta. Último slide: CTA com wftec.com.br.
