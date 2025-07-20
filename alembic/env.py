from logging.config import fileConfig

# --- BİZİM EKLEDİĞİMİZ KISIM BAŞLANGIÇ ---
from sqlalchemy import engine_from_config, pool

from alembic import context

# Projemizin ayarlarını ve temel modelini import ediyoruz
# Bu satırlar, Alembic'in projemizin veritabanı yapılandırmasına
# ve SQLAlchemy modellerine erişmesini sağlar.
from app.core.config import settings
from app.db.base import Base

# --- BİZİM EKLEDİĞİMİZ KISIM SON ---

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# --- BİZİM DEĞİŞTİRDİĞİMİZ KISIM BAŞLANGIÇ ---
# Alembic'e, takip etmesi gereken modellerin Base'den türeyen
# modeller olduğunu söylüyoruz. app.db.base.py dosyasında modellerimizi
# import ettiğimiz için Alembic hepsini buradan bulacaktır.
target_metadata = Base.metadata

# Alembic'e, veritabanı URL'sini doğrudan bizim ayar dosyamızdan
# almasını söylüyoruz. Bu, konfigürasyonu merkezi tutar.
# alembic.ini dosyasındaki sqlalchemy.url satırını kullanmasına gerek kalmaz.
config.set_main_option("sqlalchemy.url", str(settings.DATABASE_URL))
# --- BİZİM DEĞİŞTİRDİĞİMİZ KISIM SON ---


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # Bu bölüm, Alembic'in veritabanına bağlanmasını sağlar.
    # Bizim yaptığımız değişikliklerle, 'configuration' sözlüğü
    # zaten doğru sqlalchemy.url değerini içeriyor olacak.
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
