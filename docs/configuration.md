# Configuração — moodle-atto_justify

Após instalar o plugin no servidor, é necessário habilitar o botão na barra de ferramentas do editor Atto.

---

## Passo a Passo de Configuração

1. Faça login no Moodle como **Administrador**.
2. Acesse:  
   **Administração do site → Plug-ins → Editores de texto → Configurações da barra de ferramentas Atto**.
3. Na lista de módulos instalados, confirme que o módulo **Justify align** (`atto_justify`) está presente.
4. Role a página até a caixa de texto **Configuração da barra de ferramentas**.
5. Localize o grupo de alinhamento:
   ```text
   align = align
   ```
6. Adicione a chave `, justify` ao grupo:
   ```text
   align = align, justify
   ```
7. Salve as alterações.

---

## Verificação

Abra qualquer área de edição de texto do Moodle (como a descrição de um curso ou fórum) usando o editor Atto e verifique se o ícone de alinhamento justificado está visível na barra de ferramentas.
