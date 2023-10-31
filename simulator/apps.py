from django.apps import AppConfig
from django.db.models.signals import post_migrate


class SimulatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simulator'

    def ready(self) -> None:

        from .models.year import year_post_migrate_receiver
        from .models.energy import energy_post_migrate_receiver
        from .models.mileage import mileage_post_migrate_receiver
        from .models.loan_rate import loan_rate_post_migrate_receiver
        from .models.vehicle_type import vehicle_type_post_migrate_receiver
        from .models.loan_rate_ajustement import loan_rate_ajustement_post_migrate_receiver

        post_migrate.connect(year_post_migrate_receiver, sender=self)
        post_migrate.connect(energy_post_migrate_receiver, sender=self)
        post_migrate.connect(mileage_post_migrate_receiver, sender=self)
        post_migrate.connect(loan_rate_post_migrate_receiver, sender=self)
        post_migrate.connect(vehicle_type_post_migrate_receiver, sender=self)
        post_migrate.connect(loan_rate_ajustement_post_migrate_receiver, sender=self)
