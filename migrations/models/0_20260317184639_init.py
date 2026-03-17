from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(30) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL,
    "hashed_password" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "tasks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "status" VARCHAR(255) NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "refreshtoken" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "user" VARCHAR(255) NOT NULL,
    "token" VARCHAR(1000) NOT NULL,
    "expires_at" TIMESTAMPTZ NOT NULL,
    "is_revoked" BOOL NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmdlu2zgUhl/F0FUGmClSJ13QOztxpp4mdpGoCzooCFo6tglLpEpSSYzW716S2tfGg9"
    "oDC76zzyIdflzOL+m75TMXPPHMxmJlvel9tyj2Qf0o2P/sWTgIMqs2SDzzTKBUEcaCZ0Jy"
    "7EhlnGNPgDK5IBxOAkkYVVYaep42MkcFErrITCEl30JAki1ALoErx79flZlQFx5BJH+DFZ"
    "oT8NxCncTV9zZ2JNeBsY2pvDKB+m4z5DAv9GkWHKzlktE0mlCprQugwLEEfXnJQ12+ri4e"
    "ZjKiqNIsJCoxl+PCHIeezA13hjKbhdBkaqO7kY2QtQUgh1ENV5UqzOgXuoS/+s/PX52/Pn"
    "t5/lqFmDJTy6tNdOsMTJRo8Exsa2P8WOIowjDOoEoi1eUqXC+WmNeDTRNKbFXRZbYJyTa4"
    "iSGjm62ofeD18SPygC7kUjN98aIF5sfB7cXbwe2JivpD35KpLRBtjEns6kc+TTwjnK+swt"
    "mGx4YFXErrBO0WuPbos62v7AvxzcszPbkZfDa4/XXsuZ5O/k7Cc3NwcT0dltALiWUotlnd"
    "Wcb+gFsBUFdjO9w1HgrgaKvzOZfx60P6AJb27zindeebr2qPaY2rSveKcSAL+g7WBvJYVY"
    "SpU3c6xz3+Q3yZA4O7SVZPYs2aMMcPqVTILyo1djVikNF+H9xdDC5HliE8w87qAXMXFVBr"
    "D+uzkiWNrbr8vl+2YIoXBo4eha45T71GcSWz0ay49ICOiqtbikvPqfm9RVvK5/yexvT/Ii"
    "50pLPTJzSks9PGfqRdxXYEPibeNnzThE7IrD00/CUWS3BRgIV4YLzmmGhmXZPaQerPT5+y"
    "qlVUI3XjK1J3OGgeCMsq8EvlkcSHeujFzBJvN059lvw4RPpqgO6Ueuv4KGt71BjfjO7swc"
    "37wvPG5cAeaU+/8KyRWE9eluYpvUjv09h+29N/e1+mk5HBy4RccHPHLM7+YumacCgZouwB"
    "YTd36ibWhFpVCjYrl9yzfPJ+prgyhnHa1btb8HDDA2XpJdCBzX6TQNzsUtbdwlxN8tJmK6"
    "B18q7gb5V5PIqUaeRR7XVJ7W2r9DraEnciRNI98+T3l0lCBwkryfBE1dEqO6p6+jEg6oD6"
    "D7qjmNlB3XEgOiNhUhEa+WkmAnG4V/ujphEMGfMA04ZmUEgszfJMZe5qYlPLfmd2OJ1eFy"
    "Z1OC6/jf5wMxypnWZmUwWR6EVU0i+Okv4o6Vsk/S5V6wA4cZZWjV6NPa1KFWcxR43aFY16"
    "D1zUfp1sVlG5lA7qqJ0oVb2ptiAch3eQ7m5ejTEqgdY00X/uppOGBpqllLsncWTvR88j4h"
    "A/RbbA1TAKLbLylb38Qb3U+/QFhnWfKvfZzDY/ASJNvAo="
)
