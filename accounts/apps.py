from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'perfiles'

    # Se llama cuando se carga la aplicacion y se utiliza para realizar cualquier inicializacion o configuracion adicional que deba realizarse antes de que se pueda usar la app.
    def ready(self):
        import accounts.signals

