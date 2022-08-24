from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [ 
        ('blog', '0004_alter_comment_options_alter_post_options_and_more'),
    ]
    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS pg_trgm'),
    ]
