# Os 3 produtos dos posts (fatos confirmados)

Use só o que está aqui. Se precisar de um fato que não está nesta lista, não afirme.

## 1. Double Check Folha (ex-Comparativo de Folha)

- **Pergunta-gancho:** "Fechou a folha? O que mudou em relação ao mês passado?"
- **O que entra:**
  - Você envia o espelho do mês anterior e o do mês atual, em **PDF do SCI, Excel ou CSV**.
  - **Os arquivos são lidos no computador do usuário**, sem ficarem guardados.
- **O que ele compara:**
  - Funcionário por funcionário e **verba por verba**.
  - Quem foi **admitido**, quem **saiu**, quem está de **férias** e cada valor que mudou.
- **Filtros:**
  - Por **verba**, **centro de custo** ou **funcionário**, e busca pelo nome.
  - **Tolerância em reais** e opção de **ver só o que tem diferença**.
- **Exportação:** Excel, CSV ou relatório em PDF.
- **Auditoria de folha:** aponta o que precisa de atenção, como **salário abaixo do mínimo**, **líquido negativo** e **salário-família indevido**.
- **Custo da folha:** proventos, **INSS patronal** e **FGTS**, com a variação do mês.
- **NUNCA** citar o Fortunato (a IA) nos posts do Double Check.

## 2. Ferramenta de Sindicatos da WFtec

### Busca de Convenções

- **Filtros:**
  - Estado, categoria, CNPJ do sindicato e vigência (vigentes, todas, não vigentes).
  - Tipo de documento: convenção, acordo, termo aditivo ou circular do sindicato.
- **Cores dos cards:** convenção = branco, acordo = verde, aditivo = amarelo, circular = azul.
- **Documento oficial:** dá para baixar o documento oficial do Ministério do Trabalho (Mediador).

### Monitoramento e varredura

- Varredura **diária** no Mediador e em **mais de 6 mil sites de sindicatos**, nos 27 estados.
- Documento recém-chegado vem com o selo **"Nova"**.

### Novas convenções e Notificações

- **O sino no topo da busca** mostra tudo o que entrou nos **últimos 60 dias**, por tipo e por estado.
- **Aba "Novas convenções":** só as últimas publicadas.
- **Aba "Notificações":** o histórico de cada dia (por exemplo, "28/10: 164 instrumentos novos · SP 56 · RS 23…").
- O aviso fecha **todo dia às 8h** (horário de Brasília).
- **É só dentro da ferramenta:** NÃO prometer e-mail nem WhatsApp.

### Apresentação da convenção

- Você anexa a convenção em **PDF ou Word** e a WFtec monta a apresentação.
- Os slides trazem reajuste, pisos, jornada, benefícios e pontos de atenção, **cada item com a cláusula de origem**.
- A apresentação pode ser salva em PDF.

### Enquadramento Sindical

- Você digita o **CNPJ**, a WFtec analisa o **CNAE** e aponta os sindicatos (laboral e patronal) com convenção vigente, **explicando cada decisão**.

### Dados que podem ser usados

Os números do acervo são públicos e reais. Consulte no D1 a tabela `alertas_convencoes` e a tabela `instrumentos` (com `descoberto_em` e `tipo`).

## 3. WFtec Ponto

### Marcação

- Ponto pelo **celular** (no navegador do iPhone e do Android).
- **A marcação nunca é bloqueada:**
  - Fora do local, GPS fraco ou sem localização: a batida é gravada com aviso para o gestor.
  - A única recusa é toque repetido em menos de 1 minuto.
- **O que a batida grava:**
  - A **hora do servidor**, as coordenadas, a rua, o bairro e o município.
  - Distância do local, precisão do GPS, IP, aparelho e **código de auditoria** que não pode ser alterado.
  - Nenhuma batida é apagada ou alterada: a correção vira um registro novo.
- Se o deslocamento for impossível, o sistema avisa: **possível GPS falso**.
- **A localização é registrada SÓ no momento da batida.** NUNCA dizer que o funcionário é rastreado ou monitorado o tempo todo.

### Aprovação

- Batida dentro do horário e da tolerância: aprovada sozinha.
- Fora do quadro de horário ou do local: vai para o RH aprovar.

### Painel do gestor

- Batidas com aprovação ou rejeição em lote.
- Planilha do mês no estilo SCI, com ocorrências: Férias, Atestado, Falta justificada, Horas justificadas e Falta.
- Pedidos de ajuste.
- Espelho mensal e fechamento, com exportação para Excel.
- Funcionários (com CPF validado) e locais com feriados estaduais em 1 clique.

### Motor CLT (o espelho já sai calculado)

| Regra | Base legal |
| --- | --- |
| Tolerância de 10 min/dia (5+5) | CLT art. 58 §1º |
| Hora noturna reduzida das 22h às 5h (fator 8/7) | CLT art. 73 |
| Extra de 50%, e de 100% em folga ou feriado | CLT art. 59; Súmula 146 TST |
| Mais de 6h sem intervalo vira ocorrência | CLT art. 71 |
| Mais de 2h extras no dia vira ocorrência | CLT art. 59 |
| Interjornada menor que 11h vira ocorrência | CLT art. 66 |

Feriados nacionais entram automaticamente.

### Banco de horas

- Saldo anterior, saldo do mês e total.
- **Alerta** quando há saldo positivo parado há 6 meses ou mais.
- Fechar a competência consolida o banco. Reabrir **estorna**.

### O que NUNCA falar no Ponto

- "REP", "REP-P", "homologado" ou "certificado" (até sair o registro no INPI).
- "Reconhecimento facial" (ainda não existe).
- "App nas lojas" (por enquanto funciona no navegador do celular).
