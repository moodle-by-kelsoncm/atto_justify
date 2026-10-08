Installation
============

System Requirements
-------------------

* **Moodle**: 3.x or 4.x with Atto text editor enabled.
* **Permissions**: Administrative access to Moodle or file system access to the server.

Installation Methods
--------------------

Option A — Git Installation (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Navigate to the Atto editor plugins directory in your Moodle root:

.. code-block:: bash

   cd /path/to/moodle/lib/editor/atto/plugins

2. Clone this repository into a folder named ``justify``:

.. code-block:: bash

   git clone https://github.com/moodle-by-kelsoncm/atto_justify.git justify

Option B — ZIP Package Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download the ``.zip`` archive from GitHub releases or repository.
2. Extract the contents into ``/lib/editor/atto/plugins/justify``.
3. Or upload the archive via Moodle web interface at: **Site Administration → Plugins → Install plugins**.

Completing Installation
-----------------------

Visit the Moodle notifications page at **Site Administration → Notifications** to complete the database upgrade.
