# Instalação — moodle-atto_justify

## Requisitos de Ambiente

- **Moodle**: 3.x ou 4.x com suporte ao editor de texto Atto.
- **Permissões**: Acesso de administrador ao Moodle ou acesso ao sistema de arquivos do servidor.

---

## Métodos de Instalação

### Opção A — Instalação via Git (Recomendado)

1. Acesse o diretório de plugins do editor Atto no seu Moodle:
   ```bash
   cd /caminho/do/moodle/lib/editor/atto/plugins
   ```

2. Clone o repositório nomeando a pasta como `justify`:
   ```bash
   git clone https://github.com/moodle-by-kelsoncm/moodle-atto_justify.git justify
   ```

### Opção B — Instalação via Arquivo ZIP

1. Baixe o pacote `.zip` do repositório.
2. Extraia o conteúdo na pasta `/lib/editor/atto/plugins/justify`.
3. Ou utilize a interface gráfica do Moodle em:  
   **Administração do site → Plug-ins → Instalar plug-ins**.

---

## Conclusão da Instalação

Acesse a página de notificações do Moodle em **Administração do site → Notificações** para registrar a atualização no banco de dados.
