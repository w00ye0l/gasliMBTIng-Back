# Generated by Django 3.2.13 on 2022-12-07 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbti',
            name='mbti',
            field=models.CharField(choices=[('ENTJ', 'ENTJ'), ('ESFJ', 'ESFJ'), ('ENTP', 'ENTP'), ('ISPT', 'ISTP'), ('ISFP', 'ISFP'), ('INFJ', 'INFJ'), ('INTJ', 'INTJ'), ('INFP', 'INFP'), ('ESFP', 'ESFP'), ('ESTP', 'ESTP'), ('ESTJ', 'ESTJ'), ('ISFJ', 'ISFJ'), ('ISTJ', 'ISTJ'), ('ENFP', 'ENFP'), ('INTP', 'INTP'), ('ENFJ', 'ENFJ')], max_length=50),
        ),
    ]
