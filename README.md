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
| `assets/` | Versões WebP dos logos, com compressão sem perda visual, usadas na página e favicon |
| `llms.txt` | Resumo complementar do negócio; não substitui o HTML nem garante citações por IA |
| `robots.txt` | Mantém o acesso permitido aos crawlers, inclusive agentes de busca e treinamento |
| `sitemap.xml` | Sitemap — atualize o `<lastmod>` a cada mudança relevante |
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
