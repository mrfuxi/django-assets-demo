from django_assets import Bundle, register
js = Bundle(
    'app/first.css', 'app/second.css', filters='cssmin', output='gen/app.css',
)
register('css_all', js)
