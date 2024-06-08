from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context
import os
import sys
import pkgutil
from sqlalchemy.ext.declarative import declarative_base

from src.db import Base
from src.config import DATABASE_URL

config = context.config

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def import_submodules(package):
    """ Import all submodules of a module, recursively """
    package_name = package.__name__
    package_path = package.__path__
    for _, name, is_pkg in pkgutil.iter_modules(package_path):
        full_name = f"{package_name}.{name}"
        __import__(full_name)
        if is_pkg:
            import_submodules(sys.modules[full_name])

import src.models
import_submodules(src.models)

fileConfig(config.config_file_name)

target_metadata = Base.metadata
config.set_main_option('sqlalchemy.url', DATABASE_URL)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())
