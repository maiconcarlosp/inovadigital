# inovadigital.com.br — landing page de venda do domínio

Site estático de uma página só (HTML + CSS + um pouco de JS, sem build, sem dependências),
hospedado gratuitamente no **GitHub Pages**.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | A landing page inteira (estilo e script embutidos) |
| `CNAME` | Diz ao GitHub Pages qual domínio customizado usar — **não apague** |
| `favicon.svg` | Ícone da aba do navegador |
| `404.html` | Redireciona qualquer URL inexistente para a home |
| `robots.txt` / `sitemap.xml` | SEO básico |
| `.nojekyll` | Impede o GitHub de processar o site com Jekyll |

## Dados que ainda são fictícios (trocar antes de divulgar)

- [ ] **Preço**: `R$ 12.000` — aparece no card de preço e no JSON-LD (`"price": "12000"`)
- [ ] **E-mail**: `contato@exemplo.com.br` — aparece 3x (botão mailto e rodapé de contato)
- [ ] **WhatsApp**: `5511999999999` e `(11) 99999-9999` — no link `wa.me` e no texto
- [ ] **Números da seção de estatísticas** (opcional, são argumentos de marketing)

Busque por `exemplo.com.br` e `999999` no `index.html` para achar todos de uma vez.

## Rodar localmente

Basta abrir o `index.html` no navegador. Ou, para servir em `http://localhost:8000`:

```bash
python -m http.server 8000
```

## Publicar alterações

```bash
git add -A
git commit -m "Atualiza dados de contato"
git push
```

O GitHub Pages republica sozinho em ~1 minuto.
