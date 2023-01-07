# PlayChildren

## Erste Schritte

1. Python installieren
2. venv aktivieren
    - macOS: source venv/Scripts/activate
    - windows: venv/Scripts/activate
Wenn die venv korrekt aktiviert ist, kommt im Comandozeile nach dem $ (venv)



## Server Starten
python manage.py runserver

## Migration
Ich führe immer beide aus, wenn ich etwas an dem Model gemacht habe. 

python manage.py makemigrations
python manage.py migrate


## Settings
Die Static Files habe ich neu konfiguriert. 
```python

# Static files (CSS, JavaScript, Images)
## Das sind die Static File konfiguration (https://docs.djangoproject.com/en/4.1/howto/static-files/)
    
STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = ('static',)


## Wenn du später mal noch Bilder hochladen willst, muss das vorhanden sein.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Templates
## Die Templates müssen unter TEMPLATES im DIRS angegeben werden. Dadurch unktioniert das automatische suchen des templates Ordner. 
TEMPLATES = [
    {
        # ...
        'DIRS': [BASE_DIR / 'templates'], # Habe ich noch aktualisiert
        # ...
    },
]

```

## Benutzerdaten
Diese Benutzerdaten sind notwendig, wenn du dich unter https://127.0.0.1/admin/ anmelden möchtest. 

user: admin
password: teko*3