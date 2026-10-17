from pathlib import Path
import hashlib
import json
import re


def fenced_blocks(text):
    blocks = []
    active = None
    current = []
    for line in text.splitlines(keepends=True):
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            token = match.group(1)
            if active is None:
                active = (token[0], len(token))
                current = [line]
                continue
            if token[0] == active[0] and len(token) >= active[1]:
                current.append(line)
                blocks.append(''.join(current))
                active = None
                continue
        if active is not None:
            current.append(line)
    return blocks


def subsequence(expected, actual):
    iterator = iter(actual)
    return all(any(block == candidate for candidate in iterator) for block in expected)


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'localization/source-manifest.json').read_text())
    problems = []
    represented = {item['source'] for key in ['documents', 'supplementary_translations', 'unchanged_asset_copies', 'code_prose_supplements'] for item in manifest.get(key, [])}
    for item in manifest['upstream_files']:
        if item['path'] not in represented:
            problems.append({'path': item['path'], 'problem': 'source has no translation or explanatory mapping'})
    for item in manifest['upstream_files']:
        path = (root / item['path']).resolve()
        if root not in path.parents or not path.is_file():
            problems.append({'path': item['path'], 'problem': 'missing or unsafe source path'})
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item['sha256']:
            problems.append({'path': item['path'], 'problem': 'source hash changed'})
    for item in manifest['documents']:
        path = (root / item['translation']).resolve()
        if root not in path.parents or not path.is_file():
            problems.append({'path': item['translation'], 'problem': 'missing or unsafe translation path'})
            continue
        text = path.read_text()
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['translation_sha256']:
            problems.append({'path': item['translation'], 'problem': 'translation hash changed'})
        original = (root / item['source']).read_text()
        metadata = re.match(r'\A---\n.*?\n---(?:\n|\Z)', original, re.S)
        if metadata and not text.startswith(metadata.group()):
            problems.append({'path': item['translation'], 'problem': 'original frontmatter changed'})
        if not subsequence(fenced_blocks(original), fenced_blocks(text)):
            problems.append({'path': item['translation'], 'problem': 'original fenced block missing or changed'})
        if re.search(r'ZXQ(?:KEEP|UNIT)\d+QXZ', text):
            problems.append({'path': item['translation'], 'problem': 'unresolved translation token'})
    for item in manifest.get('supplementary_translations', []) + manifest.get('unchanged_asset_copies', []):
        source = root / item['source']
        output = root / item['output']
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != item['source_sha256']:
            problems.append({'path': item['source'], 'problem': 'supplement source missing or changed'})
        if not output.is_file() or hashlib.sha256(output.read_bytes()).hexdigest() != item['output_sha256']:
            problems.append({'path': item['output'], 'problem': 'supplement output missing or changed'})
    for item in manifest.get('code_prose_supplements', []):
        output = root / item['output']
        if not output.is_file():
            problems.append({'path': item['output'], 'problem': 'code prose supplement missing'})
            continue
        text = output.read_text()
        matches = re.finditer(r'原文：\n\n(?P<fence>`{3,}|~{3,})text\n(?P<quote>.*?)\n(?P=fence)\n\n日本語：', text, re.S)
        quotes = [match.group('quote') for match in matches]
        digest = hashlib.sha256(json.dumps(quotes, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
        if len(quotes) != item['quote_count']:
            problems.append({'path': item['output'], 'problem': 'original prose quotation count changed'})
        if digest != item['original_quotes_sha256']:
            problems.append({'path': item['output'], 'problem': 'original prose quotation changed'})
        if hashlib.sha256(output.read_bytes()).hexdigest() != item['output_sha256']:
            problems.append({'path': item['output'], 'problem': 'code prose supplement hash changed'})
    result = {'upstream_commit': manifest['upstream_commit'],
              'source_files_checked': len(manifest['upstream_files']),
              'documents_checked': len(manifest['documents']),
              'supplementary_translations_checked': len(manifest.get('supplementary_translations', [])),
              'unchanged_asset_copies_checked': len(manifest.get('unchanged_asset_copies', [])),
              'code_prose_supplements_checked': len(manifest.get('code_prose_supplements', [])),
              'problems': problems}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if problems else 0)


if __name__ == '__main__':
    main()
