# Supabase Setup for CompText AIR

## Recommendation

Use a **new Supabase project** named:

```text
comptext-air
```

Region:

```text
eu-central-1
```

Do not use `haasenwerkstatt`.  
Do not use unrelated production projects.

## Local-first setup

```bash
supabase init
supabase start
cp 04_supabase/migrations/20260616_comptext_air_schema.sql supabase/migrations/
cp 04_supabase/seed/comptext_air_seed.sql supabase/seed/
supabase db reset
```

## Remote setup

Only after project creation:

```bash
supabase link --project-ref <PROJECT_REF>
supabase db push
```

## Smoke SQL

```sql
select * from public.search_air_terms('monitorability');
select * from public.air_terms_by_tag('evidence');
select * from public.air_codex_tasks_by_priority('high');
```

## pgvector

pgvector is optional in v0.1.  
Keep vector columns commented until embeddings are actually implemented.
