# Revisão do site institucional — 12/09/2026

## Diagnóstico principal

A home pública `https://inovadigital.com.br/` respondeu HTTP 200, mas ainda apresentou
o título “inovadigital.com.br está à venda” e dados estruturados de produto com preço
de R$ 8.000. A versão institucional estava apenas no projeto local. A prioridade é
publicar a versão revisada e solicitar novo rastreamento; nenhuma melhoria local altera
o conteúdo que Google, Bing e assistentes recebem antes dessa publicação.

As alterações locais anteriores foram preservadas. Não foi feito commit, push ou deploy.

## O que já estava bom

- HTML estático com o conteúdo completo disponível sem JavaScript, sem fontes externas ou bibliotecas obrigatórias.
- Idioma `pt-BR`, URL canônica HTTPS, sitemap e rastreamento permitido.
- Serviços, setores, processo, exemplo de projeto e perguntas frequentes no conteúdo visível.
- Contato pelo WhatsApp, cidade, CNPJ e informações de experiência profissional.

## Melhorias aplicadas nesta revisão

- Título e descrição mais objetivos; H1 e título de serviços explicitam integração e desenvolvimento.
- Experiência de 20 anos atribuída à trajetória profissional, evitando confusão com a idade da empresa.
- Identidade estruturada como `Organization`, sem presumir um estabelecimento de atendimento presencial.
- Página, site, organização e quatro serviços conectados por identificadores no JSON-LD.
- Seis perguntas e respostas estruturadas sincronizadas com o texto visível, inclusive experiência profissional.
- Resposta sobre compatibilidade de equipamentos condicionada à avaliação técnica e à prova de conceito.
- Navegação de seções acessível no celular, foco de teclado destacado e respeito à preferência de movimento reduzido.
- Página de erro com retorno explícito à home, sem redirecionamento automático; favicon com caminho absoluto.
- Links para seções no `llms.txt` e documentação corrigida sobre o alcance de SEO, IA e dados estruturados.

## Próximas ações, em ordem de prioridade

1. **Publicar e conferir o domínio.** Validar a home institucional, robots, sitemap e uma URL inexistente com HTTP 404. Conferir HTTPS e redirecionamentos entre variantes do domínio.
2. **Configurar medição e indexação.** Verificar a propriedade no Google Search Console e Bing Webmaster Tools, enviar o sitemap e solicitar inspeção da home. A revisão não teve acesso a essas contas; não avaliou posições, cobertura ou tráfego.
3. **Fortalecer evidências reais.** Acrescentar imagens autorizadas do terminal e da plataforma do projeto apresentado. Se disponíveis, informar problema, participação da Inova Digital e resultados verificáveis; não inventar números, clientes ou depoimentos.
4. **Criar imagem de compartilhamento.** Falta uma imagem social em formato raster, com URL absoluta em `og:image`, dimensões e texto alternativo. É uma melhoria de apresentação em links compartilhados, não uma garantia de ranking.
5. **Aprofundar serviços conforme houver material.** Páginas próprias sobre integração de ERP, equipamentos industriais e TEF podem atender buscas específicas quando tiverem conteúdo original suficiente. Evitar páginas quase idênticas por cidade ou palavra-chave.
6. ~~**Conferir a oferta comercial.**~~ **Resolvido.** O responsável confirmou que faz integração de NF-e e NFC-e. O serviço passou a se chamar "Pagamentos e emissão fiscal", com NF-e e NFC-e no texto visível, no `hasOfferCatalog`, no `knowsAbout` e no `llms.txt`.

## Buscadores com IA

O HTML visível é a fonte principal. `llms.txt` é um resumo complementar e precisa
continuar alinhado à página. Não há garantia de que assistentes o leiam. Não foram
inseruídas instruções ocultas, palavras-chave repetitivas ou promessas de recomendação.
Permitir um crawler não significa indexação ou citação, e permissões de treinamento
não são equivalentes a acesso de buscadores. A política de acesso existente foi mantida.

O Google declara que não exige arquivos ou marcações especiais para suas experiências
de busca com IA e recomenda conteúdo textual acessível e dados estruturados coerentes.
[Documentação do Google](https://developers.google.com/search/docs/appearance/ai-features).
As orientações do Bing também tratam descoberta, indexação e apresentação do conteúdo
em suas experiências de busca e IA.
[Diretrizes do Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a).

## Validação e limites

A revisão inclui verificações locais de JSON-LD, correspondência da FAQ, IDs e links
internos, sitemap, regras de rastreamento e preservação do contato apenas por WhatsApp.
Também foi consultado o HTML público por HTTP. Não houve acesso a um navegador conectado
na sessão: a aparência em desktop/celular, a interação por teclado e métricas de
Core Web Vitals precisam de validação visual e de desempenho após disponibilizar um navegador.
Não foram executados Lighthouse, Rich Results Test ou Schema Markup Validator.

O arquivo `404.html` não configura sozinho o status HTTP: o servidor precisa responder
404 nas URLs inexistentes. O GitHub Pages deve ser conferido após publicar.
[Referência sobre status HTTP e rastreamento](https://developers.google.com/crawling/docs/troubleshooting/http-status-codes).
