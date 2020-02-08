# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class CatergorieStructure(models.Model):
    idcatergorie_structure = models.AutoField(db_column='idCATERGORIE_STRUCTURE', primary_key=True)  # Field name made lowercase.
    type_struct = models.CharField(db_column='TYPE_STRUCT', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.type_struct

    class Meta:
        managed = True
        db_table = 'CATERGORIE_STRUCTURE'


class Client(models.Model):
    idclient = models.AutoField(db_column='idCLIENT', primary_key=True)  # Field name made lowercase.
    nom_client = models.CharField(db_column='NOM_CLIENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prenom_client = models.CharField(db_column='PRENOM_CLIENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_de_naissance_client = models.CharField(db_column='DATE_DE_NAISSANCE_CLIENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adresse_client = models.CharField(db_column='ADRESSE_CLIENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numero_telephone = models.IntegerField(db_column='NUMERO_TELEPHONE', blank=True, null=True)  # Field name made lowercase.
    mot_de_passe_client = models.CharField(db_column='MOT_DE_PASSE_CLIENT', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nom_client
    class Meta:
        managed = True
        db_table = 'CLIENT'


class Demander(models.Model):
    service_idservice = models.OneToOneField('Service', models.DO_NOTHING, db_column='SERVICE_idSERVICE', primary_key=True)  # Field name made lowercase.
    client_idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='CLIENT_idCLIENT')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DEMANDER'
        unique_together = (('service_idservice', 'client_idclient'),)


class Proprietaire(models.Model):
    idproprietaire = models.IntegerField(db_column='idPROPRIETAIRE', primary_key=True)  # Field name made lowercase.
    numero_telephone = models.IntegerField(db_column='NUMERO_TELEPHONE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PROPRIETAIRE'


class Rdv(models.Model):
    idrdv = models.AutoField(db_column='idRDV', primary_key=True)  # Field name made lowercase.
    date_rdv = models.DateTimeField(db_column='DATE_RDV')  # Field name made lowercase.
    heure_rdv = models.DateTimeField(db_column='HEURE_RDV')  # Field name made lowercase.
    client_idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='CLIENT_idCLIENT')  # Field name made lowercase.
    structure_idstructure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='STRUCTURE_idSTRUCTURE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'RDV'


class Service(models.Model):
    idservice = models.AutoField(db_column='idSERVICE', primary_key=True)  # Field name made lowercase.
    nom_service = models.CharField(db_column='NOM_SERVICE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    debut_service = models.TimeField(db_column='DEBUT_SERVICE',blank=True, null=True)  # Field name made lowercase.
    fin_service = models.TimeField(db_column='FIN_SERVICE',blank=True, null=False)  # Field name made lowercase.
    structure_idstructure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='STRUCTURE_idSTRUCTURE')  # Field name made lowercase.
    userpropr_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_service

    class Meta:
        managed = True
        db_table = 'SERVICE'


class Servir(models.Model):
    service_idservice = models.OneToOneField(Service, models.DO_NOTHING, db_column='SERVICE_idSERVICE', primary_key=True)  # Field name made lowercase.
    staff_idstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='STAFF_idSTAFF')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SERVIR'
        unique_together = (('service_idservice', 'staff_idstaff'),)


class Staff(models.Model):
    idstaff = models.AutoField(db_column='idSTAFF', primary_key=True)  # Field name made lowercase.
    nom_staff = models.CharField(db_column='NOM_STAFF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prenom_staff = models.CharField(db_column='PRENOM_STAFF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    structure_idstructure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='STRUCTURE_idSTRUCTURE')  # Field name made lowercase.
    userpropr_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_staff
    class Meta:
        managed = True
        db_table = 'STAFF'


class Structure(models.Model):
    idstructure = models.AutoField(db_column='idSTRUCTURE', primary_key=True)  # Field name made lowercase.
    nom_struct = models.CharField(db_column='NOM_STRUCT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adresse_struct = models.CharField(db_column='ADRESSE_STRUCT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    catergorie_structure_idcatergorie_structure = models.ForeignKey(CatergorieStructure, models.DO_NOTHING, db_column='CATERGORIE_STRUCTURE_idCATERGORIE_STRUCTURE')  # Field name made lowercase.
    code_postal = models.SmallIntegerField(db_column='CODE_POSTAL', blank=True, null=True)  # Field name made lowercase.
    userpropr = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_struct

    class Meta:
        managed = True
        db_table = 'STRUCTURE'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
