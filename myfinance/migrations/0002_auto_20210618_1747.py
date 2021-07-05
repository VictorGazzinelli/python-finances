# Generated by Django 3.0.7 on 2021-06-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao', models.CharField(choices=[('DT', 'Dívida de terceiros'), ('DO', 'Doação'), ('SA', 'Salário'), ('SP', 'Serviço prestado'), ('OU', 'Outros'), ('VE', 'Vendas')], default='OU', max_length=2)),
                ('data_expectativa', models.DateField(null=True)),
                ('data_recebimento', models.DateField()),
                ('descricao', models.CharField(max_length=255)),
                ('formaRecebimento', models.CharField(choices=[('B', 'Boleto'), ('C', 'Crédito'), ('D', 'Débito'), ('P', 'Depósito'), ('O', 'Outros')], default='O', max_length=1)),
                ('situacao', models.CharField(choices=[('PR', 'Recebido'), ('AR', 'A receber')], default='AR', max_length=2)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AlterField(
            model_name='despesa',
            name='classificacao',
            field=models.CharField(choices=[('AG', 'Água'), ('AL', 'Alimentação'), ('AG', 'Aluguel'), ('EN', 'Energia'), ('LA', 'Lazer'), ('OU', 'Outros'), ('TE', 'Telecomunicações'), ('TR', 'Transporte')], default='OU', max_length=2),
        ),
    ]