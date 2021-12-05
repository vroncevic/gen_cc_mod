# -*- coding: utf-8 -*-

project = u'gen_cc_mod'
copyright = u'2020, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'2.0'
release = u'https://github.com/vroncevic/gen_cc_mod/releases'
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'gen_cc_moddoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'gen_cc_mod.tex', u'gen\\_cc\\_mod Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'gen_cc_mod', u'gen_cc_mod Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'gen_cc_mod', u'gen_cc_mod Documentation', author,
    'gen_cc_mod', 'One line description of project.', 'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
