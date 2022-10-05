# Generated by Django 4.1 on 2022-09-15 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ObjectClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Identifying name for this class.",
                        max_length=255,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="Time of last update."
                    ),
                ),
                (
                    "max_object_size",
                    models.BigIntegerField(
                        default=-1,
                        help_text="Max size in characters for the stored JSONs. Set to -1 to let any size.",
                    ),
                ),
                (
                    "max_per_user",
                    models.IntegerField(
                        default=-1,
                        help_text="Max number of objects allowed to be created per user. Set to -1 to let any amount.",
                    ),
                ),
                (
                    "allow_user_permissions",
                    models.BooleanField(
                        default=True,
                        help_text="Allow users to change permissions on objects from this class.",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_object_classes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updated_object_classes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "object class",
                "verbose_name_plural": "object classes",
            },
        ),
        migrations.CreateModel(
            name="Object",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="Time of last update."
                    ),
                ),
                (
                    "version",
                    models.IntegerField(
                        default=0,
                        help_text="Incrementing number after each update to the object.",
                    ),
                ),
                (
                    "document",
                    models.JSONField(help_text="Serialized object as a JSON document."),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_objects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "object_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="objects",
                        to="baas_objects.objectclass",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updated_objects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "object",
                "verbose_name_plural": "objects",
            },
        ),
        migrations.CreateModel(
            name="ObjectUserObjectPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="baas_objects.object",
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.permission",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("user", "permission", "content_object")},
            },
        ),
        migrations.CreateModel(
            name="ObjectGroupObjectPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="baas_objects.object",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auth.group"
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("group", "permission", "content_object")},
            },
        ),
        migrations.CreateModel(
            name="ObjectClassUserObjectPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="baas_objects.objectclass",
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.permission",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("user", "permission", "content_object")},
            },
        ),
        migrations.CreateModel(
            name="ObjectClassGroupObjectPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="baas_objects.objectclass",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auth.group"
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("group", "permission", "content_object")},
            },
        ),
        migrations.AddIndex(
            model_name="objectclass",
            index=models.Index(fields=["name"], name="baas_object_name_cd222a_idx"),
        ),
        migrations.AddIndex(
            model_name="object",
            index=models.Index(
                fields=["object_class"], name="baas_object_object__1d2c4b_idx"
            ),
        ),
    ]
