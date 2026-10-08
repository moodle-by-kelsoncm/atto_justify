Configuration
=============

Once the plugin is installed on the server, you must enable the button in the Atto toolbar configuration.

Configuration Steps
-------------------

1. Log in to Moodle as an **Administrator**.
2. Navigate to: **Site Administration → Plugins → Text editors → Atto toolbar settings**.
3. Under the list of installed plugins, confirm that **Justify align** (``atto_justify``) is present.
4. Scroll down to the **Toolbar config** text area.
5. Locate the alignment button group:

.. code-block:: text

   align = align

6. Append ``, justify`` to the group:

.. code-block:: text

   align = align, justify

7. Save changes.

Verification
------------

Open any text editing area in Moodle (such as a course description or forum post) using the Atto editor and verify that the justify alignment button appears in the toolbar.
