AUTHOR = 'Adriel Martins'
SITENAME = 'Adriel Martins - ML Engineer Portfolio'
SITEURL = ''

PATH = 'content'
THEME = 'simple'

# Set About page as index
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DIRECT_TEMPLATES = []
INDEX_SAVE_AS = 'blog.html'  # Move default index
# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = False

# Specify About as homepage
STATIC_PATHS = ['pages']
PAGE_PATHS = ['pages']
# Use this configuration instead
DISPLAY_PAGES_ON_MENU = False
PAGES_SORT_ATTRIBUTE = 'title'
# # Add page order metadata
# PAGE_ORDER_BY = 'order'
HOMEPAGE_SAVE_AS = 'index.html'
HOMEPAGE_URL = 'index.html'
ABOUT_PAGE_SAVE_AS = 'index.html'

# Menu structure
MENUITEMS = [
    ('About', '/'),  # Changed to root
    ('Previous Jobs', '/jobs.html'),
    ('Publications', '/publications.html'),
    ('Certifications', '/certifications.html'),
    ('Projects', '/projects.html'),
    ('Keywords', '/keywords.html'),
]
