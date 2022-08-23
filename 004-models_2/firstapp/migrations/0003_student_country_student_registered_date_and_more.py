# Generated by Django 4.1 on 2022-08-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0002_alter_student_options_student_about_student_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="country",
            field=models.CharField(
                choices=[
                    ("TR", "Turkey"),
                    ("US", "America"),
                    ("DE", "Germany"),
                    ("FR", "France"),
                ],
                default="TR",
                max_length=2,
                verbose_name="Ülke",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="registered_date",
            field=models.DateTimeField(auto_now_add=True, default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="updated_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="about",
            field=models.TextField(blank=True, null=True, verbose_name="Hakkında"),
        ),
        migrations.AlterField(
            model_name="student",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/", verbose_name="Resim"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="first_name",
            field=models.CharField(max_length=50, verbose_name="Adı"),
        ),
        migrations.AlterField(
            model_name="student",
            name="last_name",
            field=models.CharField(max_length=50, verbose_name="Soyadı"),
        ),
        migrations.AlterField(
            model_name="student",
            name="number",
            field=models.IntegerField(verbose_name="Numara"),
        ),
    ]