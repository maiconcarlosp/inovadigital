# inovadigital.com.br — site institucional da Inova Digital

Site estático de uma página só (HTML + CSS + um pouco de JS, sem build e sem dependências),
hospedado gratuitamente no **GitHub Pages**.

Tema: desenvolvimento de sistemas web integrados a hardware físico, com foco em
**integração de sistemas**. Público: indústria, comércio/varejo e software houses.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | Conteúdo da página, script de ano e JSON-LD de SEO |
| `styles.css` | Layout responsivo e identidade visual em azul-marinho e turquesa |
| `Imagens/` | Fontes da marca em SVG e PNG, com nomes descritivos (`inova-digital-*`) |
| `assets/` | Versões WebP dos logos usadas na página e no favicon, mais `og-inova-digital.png`, o cartão de compartilhamento |
| `.github/workflows/indexnow.yml` | A cada publicação, avisa o IndexNow (Bing e afins) que a home mudou |
| `<32 hex>.txt` na raiz | Chave do IndexNow — o nome do arquivo **é** a chave; não renomeie nem apague |
| `llms.txt` | Resumo complementar do negócio; não substitui o HTML nem garante citações por IA |
| `robots.txt` | Mantém o acesso permitido aos crawlers, inclusive agentes de busca e treinamento |
| `sitemap.xml` | Sitemap — atualize o `<lastmod>` a cada mudança relevante (ainda é manual) |
| `CNAME` | Diz ao GitHub Pages qual domínio customizado usar — **não apague** |
| `favicon.svg` | Ícone anterior; o site agora usa o símbolo da marca em `assets/` |
| `404.html` | Exibe uma página de erro com link para a home, sem redirecionamento automático |
| `REVISAO-SEO.md` | Diagnóstico, melhorias aplicadas e prioridades depois da publicação |
| `.nojekyll` | Impede o GitHub de processar o site com Jekyll |

## Contato — WhatsApp é o canal único

Por decisão do cliente, o site **não oferece telefone nem e-mail**. Todo contato passa
pelo WhatsApp.

| Canal | Onde aparece |
|---|---|
| WhatsApp (`wa.me/5554991167177`) | Botão principal da seção de contato, link no rodapé, `contactPoint` do JSON-LD, `llms.txt` |

Regras a manter em qualquer alteração futura:

- **O número nunca é escrito como texto visível** — ele existe só dentro dos `href`
  do `wa.me` e no JSON-LD. Não voltar a exibir `(54) 99116-7177` na tela.
- **Sem links `tel:`** — o cliente não quer receber ligações.
- **Sem links `mailto:` e sem e-mail visível** em nenhuma parte da página.

O `telephone` do JSON-LD mantém o número comercial já existente, e o `contactPoint`
explica que o atendimento ocorre por mensagem no WhatsApp. Esses dados ajudam na
interpretação da empresa, mas não criam nem atualizam automaticamente um Perfil da
Empresa no Google.

## Rodar localmente

Basta abrir o `index.html` no navegador. Ou, para servir em `http://localhost:8000`:

```bash
python serve.py
```

O servidor de prévia envia os tipos corretos dos logos WebP e desativa o cache local
para que um recarregamento mostre as últimas alterações. Isso não altera o cache da hospedagem pública.

## Publicar alterações

```bash
git add -A
git commit -m "Atualiza o site"
git push
```

Confira o resultado do workflow do GitHub Pages; o tempo de publicação pode variar.
Antes do commit, revise `git diff` e selecione os arquivos desejados para evitar incluir
alterações de outros trabalhos. Esta revisão não fez commit, push ou publicação.

## Ser encontrado: o que é automático e o que não é

**Automático.** O workflow `indexnow.yml` dispara a cada push que toque a home e
avisa o IndexNow de que a página mudou. Isso encurta o tempo até o Bing rastrear
de novo — e, com ele, o Copilot e parte das buscas com IA. O Google não usa
IndexNow; ele relê o `sitemap.xml` sozinho. Avisar não garante indexação,
posição nem citação.

**Não automatizável, e é onde está o maior ganho.** Nenhuma automação substitui
estes três, todos manuais e gratuitos:

1. **Perfil da Empresa no Google.** É o que faz a Inova Digital aparecer nas
   buscas por "integração de sistemas Caxias do Sul" e no mapa. Exige
   verificação da empresa pelo Google e não tem API que crie o perfil.
2. **Verificar o domínio no Search Console e no Bing Webmaster Tools.** Uma vez
   só. Depois disso o sitemap passa a ser relido sozinho, e você enxerga por
   quais termos as pessoas chegam.
3. **Links de fora apontando para o site.** O link no perfil do LinkedIn, em
   cadastros de fornecedor e em associações comerciais da região valem mais do
   que qualquer ajuste técnico nesta página.

**O que aumenta o clique quando o link é compartilhado.** `og-inova-digital.png`
é o cartão que WhatsApp, LinkedIn e Telegram exibem ao colar o endereço. Como o
WhatsApp é o único canal de contato, esse cartão é a primeira impressão de boa
parte das conversas. Se o texto ou os serviços mudarem, vale regerar a imagem.

## DNS do domínio

Registros atuais no Registro.br, todos corretos:

| Tipo | Nome | Valor |
|---|---|---|
| A | inovadigital.com.br | 185.199.108.153 |
| A | inovadigital.com.br | 185.199.109.153 |
| A | inovadigital.com.br | 185.199.110.153 |
| A | inovadigital.com.br | 185.199.111.153 |
| CNAME | www.inovadigital.com.br | maiconcarlosp.github.io. |

**Sim, os quatro registros A são necessários.** São os quatro endereços que o
GitHub publica para o Pages, e não são servidores diferentes com conteúdos
diferentes: são quatro pontos de entrada da mesma rede. Com os quatro no ar, se
um ficar indisponível o navegador tenta o seguinte sozinho. Com apenas um,
funcionaria na maior parte do tempo, mas uma falha naquele endereço específico
derrubaria o site sem necessidade. É a configuração que o GitHub documenta e a
única que ele dá suporte.

Opcional: o GitHub também publica endereços IPv6 (`2606:50c0:8000::153` até
`:8003::153`, registros do tipo AAAA). Não são obrigatórios — a ausência deles
não quebra nada para ninguém hoje.

## Passo a passo: corrigir o HTTPS do www

Sintoma: `https://inovadigital.com.br` funciona, `https://www.inovadigital.com.br`
falha na conexão. O DNS está certo; o que falta é o certificado, emitido apenas
para o domínio raiz.

Isso acontece quando o domínio customizado foi salvo no GitHub Pages **antes** de
o registro CNAME do `www` existir. O certificado foi emitido naquele momento e não
é reemitido sozinho.

1. Abra `https://github.com/maiconcarlosp/inovadigital/settings/pages`.
2. Em **Custom domain**, apague o conteúdo do campo e clique em **Save**.
   O site sai do ar por alguns minutos — é esperado.
3. Digite `inovadigital.com.br` no mesmo campo e clique em **Save** de novo.
4. O GitHub mostra "DNS check in progress". Aguarde virar o check verde.
5. Quando a caixa **Enforce HTTPS** deixar de estar acinzentada, marque-a.
   Ela fica bloqueada enquanto o certificado não terminou de ser emitido —
   pode levar de alguns minutos a uma hora.
6. Confira: `https://www.inovadigital.com.br` deve abrir e redirecionar para o
   endereço sem `www`.

Pela linha de comando, a verificação é esta — deve listar os dois nomes:

```bash
echo | openssl s_client -connect inovadigital.com.br:443   -servername inovadigital.com.br 2>/dev/null   | openssl x509 -noout -text | grep -A2 "Subject Alternative Name"
```

Não apague o arquivo `CNAME` do repositório durante o processo: o GitHub o
reescreve sozinho ao salvar o domínio, e é ele que mantém a configuração.

## Passo a passo: ser encontrado

Na ordem de retorno. Os três primeiros são gratuitos e feitos uma única vez.

### 1. Perfil da Empresa no Google

É o maior ganho isolado. É o que coloca a Inova Digital no mapa e nas buscas do
tipo "integração de sistemas Caxias do Sul", acima dos resultados normais.

1. Acesse `https://business.google.com` e entre com a conta Google da empresa.
2. Crie o perfil com o nome exato **Inova Digital** — igual ao do site.
3. Categoria principal: **Serviço de desenvolvimento de software**. Adicione
   como secundárias "Consultor de TI" e "Serviço de automação industrial".
4. Endereço: se atende no seu endereço, pode ocultá-lo e marcar como **área de
   atendimento**, informando Caxias do Sul e região. Perfil sem endereço visível
   é permitido para quem atende no cliente.
5. Telefone: o mesmo número do WhatsApp. Site: `https://inovadigital.com.br`.
6. O Google pede **verificação** — por vídeo, cartão postal ou telefone,
   conforme o caso. É a etapa que leva dias; sem ela o perfil não aparece.
7. Depois de verificado, preencha serviços e horário, e publique fotos reais.

Mantenha nome, telefone e site **idênticos** aos do site. Divergência entre eles
enfraquece o reconhecimento da empresa pelo Google.

### 2. Google Search Console

Mostra por quais termos as pessoas chegam e avisa se algo quebrar.

1. Acesse `https://search.google.com/search-console` e escolha **Prefixo do
   URL**, com `https://inovadigital.com.br/`.
2. Escolha verificar por **tag HTML**. O Google mostra uma linha assim:
   `<meta name="google-site-verification" content="...">`.
3. Me mande essa linha que eu a coloco no `index.html` e publico; depois é só
   clicar em "Verificar". (Alternativa sem código: verificar por DNS, criando um
   registro TXT no Registro.br com o valor que o Google fornecer.)
4. Verificado, vá em **Sitemaps** e envie `sitemap.xml`.
5. Em **Inspeção de URL**, cole a home e clique em "Solicitar indexação".

Os dados levam alguns dias para aparecer. Não é sinal de problema.

### 3. Bing Webmaster Tools

Vale por si e porque alimenta o Copilot e parte das buscas com IA.

1. Acesse `https://www.bing.com/webmasters`.
2. Use **Importar do Google Search Console** — leva a verificação junto e
   dispensa refazer tudo. Se preferir não conectar, a verificação por tag HTML
   funciona igual à do Google e eu coloco a tag para você.
3. Envie o `sitemap.xml`.

A chave do IndexNow já está publicada no site e o workflow já avisa a cada
publicação; nada a fazer aqui além do cadastro.

### 4. Link do site no LinkedIn

Links de fora são o que mais pesa depois do conteúdo, e este é o mais fácil.

1. No seu perfil, **Editar apresentação** → campo **Site** → `https://inovadigital.com.br`.
2. Vale mais do que parece: crie também uma **Página da empresa** no LinkedIn
   para a Inova Digital, com o site no campo próprio. É um segundo link, de um
   domínio com muita autoridade, e aparece nas buscas pelo nome da empresa.
3. Ao publicar sobre um projeto, cole o endereço do site no texto — agora o
   cartão de compartilhamento aparece com logo e descrição.

Outros links que costumam valer o esforço: cadastro de fornecedor nos clientes
que já atende, associações comerciais e industriais da região, e o perfil no
GitHub.

## Checklist de SEO depois de publicar

- [ ] Cadastrar o site no [Google Search Console](https://search.google.com/search-console) e enviar o `sitemap.xml`
- [ ] Cadastrar no [Bing Webmaster Tools](https://www.bing.com/webmasters) e enviar o sitemap
- [ ] Avaliar a elegibilidade para o **Perfil da Empresa no Google** e manter os dados reais de atendimento atualizados
- [ ] Validar os dados estruturados no [Rich Results Test](https://search.google.com/test/rich-results)
- [ ] Validar também no [Schema Markup Validator](https://validator.schema.org/); nem todo schema gera resultado especial no Google
- [ ] Confirmar que a home publicada apresenta a empresa e não a antiga oferta de venda do domínio
- [ ] Testar em celular e desktop, incluindo navegação por teclado e tema escuro
- [ ] Confirmar resposta HTTP 404 em uma URL inexistente e HTTPS nas variantes do domínio

## Manutenção de conteúdo para SEO e IA

Ao editar perguntas e respostas, atualize também `FAQPage.mainEntity` no JSON-LD.
Ao mudar serviços ou contatos, revise o conteúdo visível, o JSON-LD e `llms.txt` juntos.
Não adicione avaliações, clientes, resultados ou certificações sem evidência real.
Os 20 anos apresentados correspondem à experiência profissional do responsável.

O Google informa que não é necessário um arquivo especial para aparecer em suas
[experiências de busca com IA](https://developers.google.com/search/docs/appearance/ai-features).
Priorize conteúdo útil, rastreável e consistente; a permissão de rastreamento não garante
indexação, posição ou citação. As permissões anteriores de treinamento foram preservadas
em `robots.txt`; acesso para treinamento e visibilidade em buscas são coisas diferentes.
