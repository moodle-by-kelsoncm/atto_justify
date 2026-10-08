Usage & Development Guide
===========================

User Guide
----------

1. When creating or editing content (such as a page, label, or forum post) in Moodle, select your text.
2. Click the justify alignment icon on the Atto toolbar.
3. The selected text is formatted with CSS style ``text-align: justify``.

Developer Guide (Building with Shifter)
---------------------------------------

The JavaScript source for Atto plugins uses the YUI framework.

1. Button functionality is located at:

.. code-block:: text

   yui/src/button/js/button.js

2. After making modifications to JavaScript source, compile with ``shifter``:

.. code-block:: bash

   cd yui/src/button
   sudo shifter

3. Purge Moodle caches at **Site Administration → Development → Purge caches**.
