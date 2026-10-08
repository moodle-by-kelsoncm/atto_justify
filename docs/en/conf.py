import moodle_docs_theme

project = "moodle-atto_justify"
copyright = "2026, KelsonCM contributions to Moodle community"
author = "KelsonCM"
release = "1.0.0"

extensions = [
    "sphinx.ext.githubpages",
    "moodle_docs_theme",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

html_theme_options = {
    "primary_color": "#6c336d",
    "secondary_color": "#f98012",
    "project_name": "moodle-atto_justify",
    "tagline": "Justify text alignment button for Atto editor in Moodle",
    "github_url": "https://github.com/moodle-by-kelsoncm/atto_justify",
    "github_repo": "moodle-by-kelsoncm/atto_justify",
    "github_version": "main",
    "doc_path": "docs/en/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "enable_language_selector": True,
    "navigation_links": "Home|index, Installation|installation, Configuration|configuration, Usage|usage",
}

html_static_path = []
