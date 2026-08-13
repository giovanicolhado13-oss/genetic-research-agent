import os
import json

def test_run_cycle_monkeypatch(monkeypatch, tmp_path):
    fake_articles = [{
        'pmid': '123',
        'title': 'Fake study on fibromyalgia',
        'abstract': 'This is an abstract about fibromyalgia and genetics.'
    }]

    def fake_fetch(query, retmax=5):
        return fake_articles

    import importlib
    fetcher = importlib.import_module('agent.agents.fetcher')
    monkeypatch.setattr(fetcher, 'fetch', fake_fetch)

    from agent.src.orchestrator import run_cycle
    out = run_cycle('fibromyalgia', retmax=1, max_sentences=1)
    assert os.path.exists(out['json'])
    with open(out['json'], 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert data['query'] == 'fibromyalgia'
    assert len(data['results']) == 1
