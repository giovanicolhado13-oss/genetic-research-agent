import json
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_cycle(query, retmax=5, max_sentences=3):
    articles = []
    try:
        from agent.agents import fetcher
        articles = fetcher.fetch(query, retmax=retmax)
    except Exception:
        articles = []
    ts = int(time.time())
    fname = os.path.join(OUTPUT_DIR, f'cycle_{ts}.json')
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump({'query': query, 'results': articles}, f, ensure_ascii=False, indent=2)
    # No PDF generation in minimal version
    return {'json': fname, 'pdf': None}
