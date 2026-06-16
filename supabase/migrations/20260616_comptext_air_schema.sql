-- CompText AIR Supabase schema
-- Apply only to local Supabase, a new project, or a development branch.

create extension if not exists "pgcrypto";
-- Optional future semantic search:
-- create extension if not exists "vector";

create table if not exists public.air_sources (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  title text not null,
  authors text[] default '{}',
  year int,
  source_type text not null default 'paper',
  url text,
  local_path text,
  citation_note text,
  created_at timestamptz not null default now()
);

create table if not exists public.air_terms (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  term text not null,
  short_definition text not null,
  long_definition text,
  risk_category text,
  comptext_relevance text,
  engineering_implication text,
  codex_task_hint text,
  implementation_status text not null default 'proposed',
  tags text[] not null default '{}',
  -- embedding vector(1536),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.air_term_sources (
  term_id uuid not null references public.air_terms(id) on delete cascade,
  source_id uuid not null references public.air_sources(id) on delete cascade,
  evidence_note text,
  primary key (term_id, source_id)
);

create table if not exists public.air_relations (
  id uuid primary key default gen_random_uuid(),
  from_term_id uuid not null references public.air_terms(id) on delete cascade,
  to_term_id uuid not null references public.air_terms(id) on delete cascade,
  relation_type text not null,
  note text,
  created_at timestamptz not null default now(),
  constraint air_relations_no_self_loop check (from_term_id <> to_term_id)
);

create table if not exists public.air_codex_tasks (
  id uuid primary key default gen_random_uuid(),
  term_id uuid references public.air_terms(id) on delete set null,
  task_title text not null,
  task_prompt text not null,
  priority text not null default 'medium',
  status text not null default 'proposed',
  target_files text[] not null default '{}',
  created_at timestamptz not null default now()
);

create table if not exists public.air_runs (
  id uuid primary key default gen_random_uuid(),
  run_id text unique not null,
  goal text not null,
  input_text text,
  air_json jsonb not null default '{}'::jsonb,
  model_provider text,
  model_name text,
  validation_status text not null default 'draft',
  hash_chain_root text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.air_evidence_events (
  id uuid primary key default gen_random_uuid(),
  run_id uuid not null references public.air_runs(id) on delete cascade,
  event_id text not null,
  parent_event_id text,
  actor text not null default 'ctxt',
  action_type text not null,
  tool_name text,
  input_digest text,
  output_digest text,
  artifact_paths text[] not null default '{}',
  contract_ids text[] not null default '{}',
  invariant_results jsonb not null default '{}'::jsonb,
  previous_hash text,
  event_hash text not null,
  created_at timestamptz not null default now(),
  unique (run_id, event_id)
);

create index if not exists air_terms_tags_gin_idx on public.air_terms using gin(tags);
create index if not exists air_terms_risk_category_idx on public.air_terms(risk_category);
create index if not exists air_terms_status_idx on public.air_terms(implementation_status);
create index if not exists air_events_run_idx on public.air_evidence_events(run_id);

create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists trg_air_terms_updated_at on public.air_terms;
create trigger trg_air_terms_updated_at before update on public.air_terms
for each row execute function public.set_updated_at();

drop trigger if exists trg_air_runs_updated_at on public.air_runs;
create trigger trg_air_runs_updated_at before update on public.air_runs
for each row execute function public.set_updated_at();

create or replace function public.search_air_terms(query_text text)
returns table (
  id uuid,
  slug text,
  term text,
  short_definition text,
  risk_category text,
  tags text[]
)
language sql stable
as $$
  select id, slug, term, short_definition, risk_category, tags
  from public.air_terms
  where slug ilike '%' || query_text || '%'
     or term ilike '%' || query_text || '%'
     or short_definition ilike '%' || query_text || '%'
     or comptext_relevance ilike '%' || query_text || '%'
  order by term asc;
$$;

create or replace function public.air_terms_by_tag(tag_text text)
returns setof public.air_terms
language sql stable
as $$
  select * from public.air_terms where tag_text = any(tags) order by term asc;
$$;

create or replace function public.air_codex_tasks_by_priority(priority_filter text)
returns setof public.air_codex_tasks
language sql stable
as $$
  select * from public.air_codex_tasks where priority = priority_filter order by created_at asc;
$$;

-- RLS intentionally not enabled for the local/admin prototype.
-- Enable RLS before exposing this through a public app.
