from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
@receiver(post_migrate)
def crear_grupos(sender, **kwargs):
    if sender.name != 'usuarios':
        return

    admin_group, _ = Group.objects.get_or_create(name='Administradores')
    empleados_group, _ = Group.objects.get_or_create(name='Empleados')
    clientes_group, _ = Group.objects.get_or_create(name='Clientes')

    permisos_propiedad = Permission.objects.filter(
        content_type__app_label='propiedades',
        content_type__model='propiedad'
    )

    permisos_cliente = Permission.objects.filter(
        content_type__app_label='clientes',
        content_type__model='cliente'
    )

    admin_group.permissions.set(
        list(permisos_propiedad) + list(permisos_cliente)
    )

    empleados_group.permissions.set(
        list(permisos_propiedad) + list(permisos_cliente)
    )

    permisos_cliente_solo_lectura = Permission.objects.filter(
        content_type__app_label='propiedades',
        content_type__model='propiedad',
        codename='view_propiedad'
    )

    clientes_group.permissions.set(permisos_cliente_solo_lectura)