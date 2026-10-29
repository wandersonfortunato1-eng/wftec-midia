# Rotina do Instagram da WFtec (@wftec_)

Este repositório é **público**. Ele guarda só os arquivos dos posts, que ficam públicos no Instagram de qualquer forma. Nunca coloque aqui nada que não iria para o feed: senhas, tokens, dados de clientes, planilhas internas.

O Wanderson Fortunato (dono da WFtec, Natal/RN) autorizou **publicação direta**, sem aprovação prévia, **dois posts por dia**, com **conteúdo misto**.

## Como publicar

- **Metricool:** marca `blogId 7176830`, fuso `America/Fortaleza`, rede `instagram`.
- **Horários (dois por dia):**
  - **Seg a Sex:** **11:47** e **18:37**.
  - **Sáb e Dom:** **11:47** e **19:07**.
  - Por que esses horários:
    - Sprout Social 2026 (setores de software/tecnologia e serviços financeiros) aponta 11h–14h nos dias úteis.
    - Hootsuite 2026 aponta o fim da tarde, entre 15h e 19h.
    - O estudo Metricool 2026 aponta 18h–21h, com Reels e carrossel mais fortes à noite.
    - Os dados da própria conta no Metricool mostram picos às 10–12h e às 18h.
  - Revise isso todo mês: rode `getBestTimeToPostByNetwork` e ajuste em até 1 h se os dados da conta mudarem.
- **Envio:** `createScheduledPost` com `autoPublish: true` e `draft: false`.
- **Mídia:** use URLs `https://raw.githubusercontent.com/wandersonfortunato1-eng/wftec-midia/main/<caminho>`. O Metricool baixa e copia o arquivo.
  - Faça **commit e push antes** de agendar.
  - Antes de agendar, confira com `curl -sI` que a URL responde 200.
- **Registro:** depois de agendar, acrescente uma linha em `publicados.md` com o id do Metricool, e faça commit e push.
- **Duplicidade:** antes de criar, rode `getScheduledPosts` para o dia-alvo e só crie o horário que estiver vazio.

## Calendário semanal

| Dia | Post 1: 11:47 (almoço) | Post 2: 18:37 (fim de semana: 19:07) |
| --- | --- | --- |
| Seg | Carrossel educativo de DP (prazos, eSocial, férias, 13º, rescisão, convenção) | Imagem: dica de uma ferramenta WFtec |
| Ter | Imagem: mito × verdade do DP | **Reels** de produto |
| Qua | Imagem: dado da semana (convenções novas, número real do D1) | Carrossel de produto (dor do DP → solução) |
| Qui | Carrossel educativo de DP | **Reels** de produto |
| Sex | Carrossel de produto | Imagem: lembrete dos prazos da semana seguinte (confira as datas na web) |
| Sáb | Imagem leve (bastidor, frase do DP) | **Reels** |
| Dom | Imagem: frase ou pergunta para comentar | Carrossel educativo |

**Regras gerais:**
- Os dois posts do dia nunca têm o mesmo produto nem o mesmo tema.
- Reels sempre no horário da noite, que é o melhor para Reels.

**Fila de Reels:**
- **Reels prontos:** `backlog/backlog.json` traz o arquivo, a capa (`-capa.jpg`) e a legenda. Use **na ordem**, sem repetir o que já está em `publicados.md`.
- **Quando a fila acabar:** faça um Reels novo **sem narração** (texto animado + trilha). O processo está em "Reels sem voz" abaixo.
- **Se não der para fazer o Reels:** troque por um carrossel. Nunca deixe o dia sem post.

## Produtos e regras de conteúdo (obrigatórias)

### Nomes de produto

| Use | Não use |
| --- | --- |
| **Double Check Folha** | "Comparativo de Folha" |
| **ferramenta de Sindicatos da WFtec** (Busca de Convenções, Monitoramento, Enquadramento Sindical) | "3 ferramentas" |

### Dados pessoais e de empresas

- **Esconda** nomes de clientes, empregados e empresas, CNPJ e CPF. Use uma tarja `.mask` ou dados claramente ilustrativos, com o selo "exemplos ilustrativos".
- **Pode mostrar:** convenções coletivas, sindicatos e números agregados do acervo, que são públicos.

### Por produto

- **Double Check Folha:** não cite o Fortunato (a IA).
- **Ponto:**
  - Não diga "REP", "REP-P" nem "homologado".
  - A localização é registrada **só na batida**. Nunca diga que o funcionário é rastreado ou monitorado o tempo todo.
  - A marcação nunca é bloqueada.
- **Notificações de convenção:** o aviso aparece **dentro da ferramenta**, no sino do topo da busca e na aba Notificações. Não prometa e-mail nem WhatsApp. A varredura fecha o aviso **todo dia às 8h**.

### Números e fatos

- Não invente número. Para dados de convenção, consulte o D1 (`cc3e5370-9d3f-458c-9bb9-5c526ba44457`):
  - tabela `alertas_convencoes`: `dia`, `total`, `por_uf`, `por_origem`;
  - tabela `instrumentos`: `tipo`, `uf`, `descoberto_em`, `vigencia_fim`, `origem`.
- Datas e prazos legais (eSocial, FGTS, 13º etc.): confira na web antes de afirmar. Se houver dúvida, fale de forma geral, sem número.

### Legenda

- Português do Brasil.
- Gancho na 1ª linha, de 3 a 6 linhas úteis e um CTA "👉 Fale com a gente: wftec.com.br".
- De 5 a 8 hashtags. Sempre `#wftec`, mais `#departamentopessoal`, `#folhadepagamento`, `#rh`, `#contabilidade` e as do tema.
- Tom: direto, de quem vive DP. Sem exagero e sem promessas legais.

## Visual

- Use o **`kit/base.css`**, tema claro dos vídeos:
  - fundo `#F6F2EF`, laranja `#F15A25`, títulos em Archivo itálico 900, texto em IBM Plex;
  - classe `.dark` para slides escuros (`#141312`).
- **Carrossel e imagem:** 1080×1350. Escreva um HTML em `AAAA-MM/AAAA-MM-DD-tema.html`, com um `<section class="slide">` por slide e link `../kit/base.css`. Gere as imagens com `python3 kit/render.py AAAA-MM/AAAA-MM-DD-tema.html AAAA-MM/AAAA-MM-DD-tema`, que cria os PNGs `-1.png`, `-2.png`…
  - Modelo: `kit/exemplo.html`.
  - Antes de publicar, olhe os PNGs (Read) para conferir que nada está cortado ou sobreposto.
  - Converta os PNGs para JPG (qualidade 90) e envie em `media`, na ordem.
  - Primeiro slide: gancho forte. Último slide: CTA com logo e wftec.com.br.
- Evite neon, robôs e circuitos.

## Reels sem voz (quando a fila acabar)

- Formato: HTML com `window.render(t)` determinístico, 1080×1920, 30 fps, de 20 a 35 s.
- Gere os quadros com Playwright e faça `ffmpeg libx264 crf 20 yuv420p`.
- Trilha: `kit/trilha.wav` em −12 dB, com fade-out de 2 s. Legendas grandes na tela, porque não há narração.
- Capa: um quadro forte, em JPG, enviado em `videoThumbnailUrl`.
- No Instagram: `instagramData.type = "REEL"`.
