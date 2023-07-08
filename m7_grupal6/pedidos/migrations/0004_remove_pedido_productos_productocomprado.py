# Generated by Django 4.2.2 on 2023-07-08 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_alter_pedido_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.CreateModel(
            name='ProductoComprado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('comprado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Producto', to='pedidos.producto')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Pedido', to='pedidos.pedido')),
            ],
        ),
    ]
