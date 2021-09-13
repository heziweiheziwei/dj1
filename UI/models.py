# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Archive(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    enable = models.IntegerField(blank=True, null=True)
    share = models.IntegerField(blank=True, null=True)
    mode = models.IntegerField(blank=True, null=True)
    hash = models.IntegerField(blank=True, null=True)
    encryption = models.IntegerField(blank=True, null=True)
    compression = models.IntegerField(blank=True, null=True)
    replication = models.IntegerField(blank=True, null=True)
    dedupe = models.IntegerField(blank=True, null=True)
    policy = models.IntegerField(blank=True, null=True)
    protocol = models.IntegerField(blank=True, null=True)
    storageid = models.IntegerField(db_column='storageId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'archive'


class License(models.Model):
    license_key = models.CharField(primary_key=True, max_length=35)

    class Meta:
        managed = False
        db_table = 'license'


class Policy(models.Model):
    id = models.AutoField(db_column='storageId', primary_key=True)  # Field name made lowercase.
    archiveid = models.BigIntegerField(db_column='archiveId')  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    rettime = models.CharField(db_column='retTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    retsec = models.BigIntegerField(db_column='retSec', blank=True, null=True)  # Field name made lowercase.
    gracetime = models.CharField(db_column='graceTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gracesec = models.BigIntegerField(db_column='graceSec', blank=True, null=True)  # Field name made lowercase.
    autodelete = models.IntegerField(db_column='autoDelete', blank=True, null=True)  # Field name made lowercase.
    dateenabled = models.DateTimeField(db_column='dateEnabled', blank=True, null=True)  # Field name made lowercase.
    enableauth = models.CharField(db_column='enableAuth', max_length=80, blank=True, null=True)  # Field name made lowercase.
    datedisabled = models.DateTimeField(db_column='dateDisabled', blank=True, null=True)  # Field name made lowercase.
    disableauth = models.CharField(db_column='disableAuth', max_length=80, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'policy'
        unique_together = (('archiveid', 'type'),)


class Properties(models.Model):
    k = models.TextField(primary_key=True)
    v = models.TextField()

    class Meta:
        managed = False
        db_table = 'properties'


class Rule(models.Model):
    id = models.AutoField(db_column='storageId', primary_key=True)  # Field name made lowercase.
    archiveid = models.BigIntegerField(db_column='archiveId')  # Field name made lowercase.
    name = models.TextField()
    path = models.TextField()
    type = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    attr = models.IntegerField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    access = models.BigIntegerField(blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule'


class Schedule(models.Model):
    archiveid = models.BigIntegerField(db_column='archiveId')  # Field name made lowercase.
    name = models.TextField()
    value = models.TextField()
    enabled = models.IntegerField(blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class Storage(models.Model):
    storageid = models.AutoField(db_column='storageId', primary_key=True)  # Field name made lowercase.
    storage1 = models.IntegerField(blank=True, null=True)
    storage2 = models.IntegerField(blank=True, null=True)
    storage3 = models.IntegerField(blank=True, null=True)
    storage4 = models.IntegerField(blank=True, null=True)
    storage5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage'
