# apollo-assistent

Este projeto é modular e escalável, permitindo fácil manutenção e adição de novas funcionalidades. Algumas sugestões de melhorias:

Segurança: Implementar autenticação e autorização utilizando OAuth2.
Escalabilidade: Para muitos usuários, considere usar filas para processar rotinas e agendamentos.
Testes: Implementar testes unitários e de integração para garantir a qualidade do código.
Documentação: Utilizar Swagger (já embutido no FastAPI) para gerar documentação automática.

Tabelas
users

id (UUID, Primary Key)
name (VARCHAR)
email (VARCHAR, Unique)
password (HASHED VARCHAR)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
tasks

id (UUID, Primary Key)
user_id (UUID, Foreign Key)
title (VARCHAR)
description (TEXT)
date (TIMESTAMP)
is_completed (BOOLEAN)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
schedules

id (UUID, Primary Key)
user_id (UUID, Foreign Key)
google_account_id (VARCHAR)
event_id (VARCHAR)
title (VARCHAR)
start_time (TIMESTAMP)
end_time (TIMESTAMP)
description (TEXT)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
routines

id (UUID, Primary Key)
user_id (UUID, Foreign Key)
title (VARCHAR)
description (TEXT)
start_time (TIMESTAMP)
end_time (TIMESTAMP)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
exercises

id (UUID, Primary Key)
user_id (UUID, Foreign Key)
name (VARCHAR)
sets (INTEGER)
reps (INTEGER)
weight (FLOAT)
progress (TEXT)
date (TIMESTAMP)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
finances

id (UUID, Primary Key)
user_id (UUID, Foreign Key)
income (FLOAT)
fixed_expenses (FLOAT)
variable_expenses (FLOAT)
savings (FLOAT)
month (TIMESTAMP)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
Backend - Python com FastAPI