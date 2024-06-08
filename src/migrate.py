import subprocess

def run_migration():
    try:
        result = subprocess.run(
            ["alembic", "upgrade", "head"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Alembic upgrade failed: {e.stderr.decode()}")