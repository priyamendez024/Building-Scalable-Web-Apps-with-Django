
# Chapter 21: Managing Production Databases & Migrations

# Example zero-downtime migration in Django
# Add a new column and backfill data
ALTER TABLE users ADD COLUMN last_login_ip VARCHAR(45) NULL;

# Backfill data
python manage.py backfill_last_login_ip
    