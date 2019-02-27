# Generated by Django 2.1.7 on 2019-02-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190228_0100'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tester',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='issutd',
            new_name='isSUTD',
        ),
        migrations.RemoveField(
            model_name='pillar',
            name='pillar',
        ),
        migrations.RemoveField(
            model_name='project',
            name='featuredimage',
        ),
        migrations.RemoveField(
            model_name='user',
            name='admingroup',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contactemail',
        ),
        migrations.RemoveField(
            model_name='user',
            name='displaypicture',
        ),
        migrations.RemoveField(
            model_name='user',
            name='personallinks',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='pillar',
            name='name',
            field=models.CharField(default='None', max_length=4),
        ),
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.CharField(default='https://via.placeholder.com/150', max_length=200),
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='admin_groups',
            field=models.ManyToManyField(to='projects.Category'),
        ),
        migrations.AddField(
            model_name='user',
            name='contact_email',
            field=models.CharField(default='none@example.com', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='display_picture',
            field=models.CharField(default='https://via.placeholder.com/150', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='personal_links',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectuid',
            field=models.CharField(default='NONE9999', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(default='Not Approved', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='displayname',
            field=models.CharField(default='Tom', max_length=20),
        ),
        migrations.DeleteModel(
            name='AdminGroup',
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]