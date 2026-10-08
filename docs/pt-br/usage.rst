Guia de Uso e Desenvolvimento
=============================

Guia de Uso
-----------

1. Ao criar ou editar um rótulo, página ou atividade no Moodle, selecione o texto desejado.
2. Clique no ícone de alinhamento justificado na barra de ferramentas do Atto.
3. O texto selecionado receberá a regra de estilo CSS ``text-align: justify``.

Guia para Desenvolvedores (Build com Shifter)
---------------------------------------------

O código JavaScript do plugin Atto utiliza o framework YUI.

1. As funções do botão ficam localizadas em:

.. code-block:: text

   yui/src/button/js/button.js

2. Após realizar alterações no JavaScript, compile utilizando a ferramenta ``shifter``:

.. code-block:: bash

   cd yui/src/button
   sudo shifter

3. Limpe o cache do Moodle em **Administração do site → Desenvolvimento → Limpar caches**.
