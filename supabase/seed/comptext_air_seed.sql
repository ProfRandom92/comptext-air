insert into public.air_sources (slug, title, authors, year, source_type, local_path, citation_note)
values
('jose-2025-illegible-cot', 'Reasoning Models Sometimes Output Illegible Chains of Thought', array['Arun Jose'], 2025, 'paper', 'papers/01-jose-2025-illegible-cot.pdf', 'Legibility risk for CoT monitoring.'),
('korbak-2025-cot-monitorability', 'Chain of Thought Monitorability', array['Tomek Korbak','Mikita Balesni'], 2025, 'paper', 'papers/02-korbak-2025-cot-monitorability.pdf', 'CoT monitorability is useful but fragile.'),
('chen-2025-cot-controllability', 'Reasoning Models Struggle to Control their Chains of Thought', array['Chen Yueh-Han'], 2025, 'paper', 'papers/05-chen-2025-cot-controllability.pdf', 'CoT controllability vs output controllability.'),
('schoen-2025-anti-scheming', 'Stress Testing Deliberative Alignment for Anti-Scheming Training', array['Bronson Schoen'], 2025, 'paper', 'papers/07-schoen-2025-anti-scheming.pdf', 'Scheming and covert action risks.')
on conflict (slug) do nothing;

insert into public.air_terms
(slug, term, short_definition, risk_category, comptext_relevance, engineering_implication, codex_task_hint, tags)
values
('agent-intermediate-representation', 'Agent Intermediate Representation', 'Structured representation between natural language and agent execution.', 'air', 'Core identity for CompText AIR.', 'Define schema, fixtures, validators.', 'Create schemas/air.schema.json and docs/air.', array['air','ir','compiler']),
('cot-monitorability', 'CoT Monitorability', 'Ability to inspect reasoning traces for unsafe behavior.', 'monitorability', 'CompText complements CoT monitoring with deterministic evidence.', 'Add evidence summaries and validators.', 'Implement evidence validation docs/tests.', array['cot','monitoring','safety']),
('illegible-thinking', 'Illegible Thinking', 'Reasoning that becomes hard to interpret.', 'opacity', 'Motivates AIR as stable intermediate representation.', 'Validate behavior via external artifacts.', 'Add final-answer evidence-reference rule.', array['opacity','audit','air']),
('evidence-event', 'Evidence Event', 'Single auditable runtime action record.', 'evidence', 'Core primitive for CompText AIR audit.', 'Store digests and hash continuity.', 'Create evidence schema and fixtures.', array['evidence','hash','runtime']),
('hash-chain', 'Hash Chain', 'Tamper-evident sequence of evidence events.', 'integrity', 'Protects evidence continuity.', 'Validate event ordering and hashes.', 'Create hash-chain validator task.', array['hash','integrity','audit'])
on conflict (slug) do nothing;
