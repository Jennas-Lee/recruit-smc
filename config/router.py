class DatabaseRouter:
    router_app_labels = {
        'authentication',
        'check',
        'index',
        'info',
        'score',
        'recruit',
        'contenttypes'
    }

    def db_for_read(self, model, **hints):
        return 'read'

    def db_for_write(self, model, **hints):
        return 'write'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
