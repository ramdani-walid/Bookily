# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CatergorieStructure(models.Model):
    idcatergorie_structure = models.AutoField(db_column='idCATERGORIE_STRUCTURE', primary_key=True)  # Field name made lowercase.
    type_struct = models.CharField(db_column='TYPE_STRUCT', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.idcatergorie_structure

    class Meta:
        managed = False
        db_table = 'CATERGORIE_STRUCTURE'


class Client(models.Model):
    idclient = models.AutoField(db_column='idCLIENT', primary_key=True)  # Field name made lowercase.
    nom_client = models.CharField(db_column='NOM_CLIENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prenom_client = models.CharField(db_column='PRENOM_CLIENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_de_naissance_client = models.CharField(db_column='DATE_DE_NAISSANCE_CLIENT', max_length=45)  # Field name made lowercase.
    adresse_client = models.CharField(db_column='ADRESSE_CLIENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=45)  # Field name made lowercase.
    numero_telephone = models.IntegerField(db_column='NUMERO_TELEPHONE')  # Field name made lowercase.
    mot_de_passe_client = models.CharField(db_column='MOT_DE_PASSE_CLIENT', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENT'


class Demander(models.Model):
    service_idservice = models.OneToOneField('Service', models.DO_NOTHING, db_column='SERVICE_idSERVICE', primary_key=True)  # Field name made lowercase.
    client_idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='CLIENT_idCLIENT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEMANDER'
        unique_together = (('service_idservice', 'client_idclient'),)


class Rdv(models.Model):
    idrdv = models.AutoField(db_column='idRDV', primary_key=True)  # Field name made lowercase.
    date_rdv = models.DateTimeField(db_column='DATE_RDV')  # Field name made lowercase.
    heure_rdv = models.DateTimeField(db_column='HEURE_RDV')  # Field name made lowercase.
    client_idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='CLIENT_idCLIENT')  # Field name made lowercase.
    structure_idstructure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='STRUCTURE_idSTRUCTURE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RDV'


class Service(models.Model):
    idservice = models.AutoField(db_column='idSERVICE', primary_key=True)  # Field name made lowercase.
    nom_service = models.CharField(db_column='NOM_SERVICE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    duree_service = models.CharField(db_column='DUREE_SERVICE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    structure_idstructure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='STRUCTURE_idSTRUCTURE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERVICE'


class Servir(models.Model):
    service_idservice = models.OneToOneField(Service, models.DO_NOTHING, db_column='SERVICE_idSERVICE', primary_key=True)  # Field name made lowercase.
    staff_idstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='STAFF_idSTAFF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERVIR'
        unique_together = (('service_idservice', 'staff_idstaff'),)


class Staff(models.Model):
    idstaff = models.AutoField(db_column='idSTAFF', primary_key=True)  # Field name made lowercase.
    nom_staff = models.CharField(db_column='NOM_STAFF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prenom_staff = models.CharField(db_column='PRENOM_STAFF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    structure_idstructure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='STRUCTURE_idSTRUCTURE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STAFF'


class Structure(models.Model):
    idstructure = models.AutoField(db_column='idSTRUCTURE', primary_key=True)  # Field name made lowercase.
    nom_struct = models.CharField(db_column='NOM_STRUCT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adresse_struct = models.CharField(db_column='ADRESSE_STRUCT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_idUSER')  # Field name made lowercase.
    catergorie_structure_idcatergorie_structure = models.ForeignKey(CatergorieStructure, models.DO_NOTHING, db_column='CATERGORIE_STRUCTURE_idCATERGORIE_STRUCTURE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STRUCTURE'


class Users(models.Model):
    iduser = models.AutoField(db_column='idUSER', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='PRENOM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_de_naissance = models.DateField(db_column='DATE_DE_NAISSANCE')  # Field name made lowercase.
    adresse = models.CharField(db_column='ADRESSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numero_telephone = models.IntegerField(db_column='NUMERO_TELEPHONE')  # Field name made lowercase.
    mot_de_passe = models.CharField(db_column='MOT_DE_PASSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    code_postal = models.IntegerField(db_column='CODE_POSTAL')  # Field name made lowercase.

    def __str__(self):
        return "the user is {0}".format(self.nom)

    class Meta:
        managed = False
        db_table = 'USERS'
