# Minimal admin CLI for listing users and broadcasting (reads DATABASE_URL env)
import os, asyncpg, asyncio

DATABASE_URL = os.getenv("DATABASE_URL")

async def list_users():
    if not DATABASE_URL:
        print("DATABASE_URL not set")
        return
    pool = await asyncpg.create_pool(DATABASE_URL)
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, tg_id, username, premium, created_at FROM users ORDER BY id DESC LIMIT 100")
        for r in rows:
            print(r)
    await pool.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "list":
        asyncio.run(list_users())
    else:
        print("Usage: python admin/cli.py list")
