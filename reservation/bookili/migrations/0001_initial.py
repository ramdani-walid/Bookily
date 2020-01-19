# Generated by Django 3.0.2 on 2020-01-19 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('idclient', models.AutoField(db_column='idCLIENT', primary_key=True, serialize=False)),
                ('nom_client', models.CharField(blank=True, db_column='NOM_CLIENT', max_length=45, null=True)),
                ('prenom_client', models.CharField(blank=True, db_column='PRENOM_CLIENT', max_length=45, null=True)),
                ('date_de_naissance_client', models.CharField(blank=True, db_column='DATE_DE_NAISSANCE_CLIENT', max_length=45, null=True)),
                ('adresse_client', models.CharField(blank=True, db_column='ADRESSE_CLIENT', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=45, null=True)),
                ('numero_telephone', models.IntegerField(blank=True, db_column='NUMERO_TELEPHONE', null=True)),
                ('mot_de_passe_client', models.CharField(blank=True, db_column='MOT_DE_PASSE_CLIENT', max_length=45, null=True)),
            ],
            options={
                'db_table': 'CLIENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('idproprietaire', models.IntegerField(db_column='idPROPRIETAIRE', primary_key=True, serialize=False)),
                ('numero_telephone', models.IntegerField(blank=True, db_column='NUMERO_TELEPHONE', null=True)),
            ],
            options={
                'db_table': 'PROPRIETAIRE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rdv',
            fields=[
                ('idrdv', models.AutoField(db_column='idRDV', primary_key=True, serialize=False)),
                ('date_rdv', models.DateTimeField(db_column='DATE_RDV')),
                ('heure_rdv', models.DateTimeField(db_column='HEURE_RDV')),
            ],
            options={
                'db_table': 'RDV',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('idservice', models.AutoField(db_column='idSERVICE', primary_key=True, serialize=False)),
                ('nom_service', models.CharField(blank=True, db_column='NOM_SERVICE', max_length=45, null=True)),
                ('duree_service', models.CharField(blank=True, db_column='DUREE_SERVICE', max_length=45, null=True)),
            ],
            options={
                'db_table': 'SERVICE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('idstaff', models.AutoField(db_column='idSTAFF', primary_key=True, serialize=False)),
                ('nom_staff', models.CharField(blank=True, db_column='NOM_STAFF', max_length=45, null=True)),
                ('prenom_staff', models.CharField(blank=True, db_column='PRENOM_STAFF', max_length=45, null=True)),
            ],
            options={
                'db_table': 'STAFF',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CatergorieStructure',
            fields=[
                ('idcatergorie_structure', models.AutoField(db_column='idCATERGORIE_STRUCTURE', primary_key=True, serialize=False)),
                ('type_struct', models.CharField(blank=True, db_column='TYPE_STRUCT', max_length=45, null=True)),
            ],
            options={
                'db_table': 'CATERGORIE_STRUCTURE',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Demander',
            fields=[
                ('service_idservice', models.OneToOneField(db_column='SERVICE_idSERVICE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='bookili.Service')),
            ],
            options={
                'db_table': 'DEMANDER',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servir',
            fields=[
                ('service_idservice', models.OneToOneField(db_column='SERVICE_idSERVICE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='bookili.Service')),
            ],
            options={
                'db_table': 'SERVIR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('idstructure', models.AutoField(db_column='idSTRUCTURE', primary_key=True, serialize=False)),
                ('nom_struct', models.CharField(blank=True, db_column='NOM_STRUCT', max_length=45, null=True)),
                ('adresse_struct', models.CharField(blank=True, db_column='ADRESSE_STRUCT', max_length=45, null=True)),
                ('code_postal', models.TextField(blank=True, db_column='CODE_POSTAL', null=True)),
                ('catergorie_structure_idcatergorie_structure', models.ForeignKey(db_column='CATERGORIE_STRUCTURE_idCATERGORIE_STRUCTURE', on_delete=django.db.models.deletion.DO_NOTHING, to='bookili.CatergorieStructure')),
                ('userpropr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'STRUCTURE',
                'managed': True,
            },
        ),
    ]
