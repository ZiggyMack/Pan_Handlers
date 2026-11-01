"""Every relative Markdown link in the guidance documents must resolve.

Run with: python -m unittest discover -s tests -p test_markdown_links.py -v
Added 2026-10-31 after the guidance map audit of 2026-10-30 (proposal P8).

Scope: README.md, START_HERE.md, Help/*.md, REPO-SYNC/*.md and dashboard/*.md.
A link target is checked when it is relative to the repository: anchors are
stripped, links with a scheme (http, https, mailto, a drive letter) are
skipped, and a target that climbs out of the repository with ../ is skipped
because the sibling checkout it names is not part of this repository.
Links inside fenced code blocks and inline code spans are not links.
"""

import os
from pathlib import Path
import re
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
GUIDANCE_PATTERNS = ("README.md", "START_HERE.md", "Help/*.md", "REPO-SYNC/*.md", "dashboard/*.md")

FENCED_BLOCK = re.compile(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]+`")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]*>|[^\s)]+)")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")


def guidance_files():
    files = []
    for pattern in GUIDANCE_PATTERNS:
        files.extend(sorted(ROOT.glob(pattern)))
    return files


def _blank_code(text):
    """Replace code with whitespace so line numbers stay stable."""
    text = FENCED_BLOCK.sub(lambda match: "\n" * match.group(0).count("\n"), text)
    return INLINE_CODE.sub(lambda match: " " * len(match.group(0)), text)


def relative_link_targets(markdown_file):
    """Yield (line_number, raw_target) for each link target that is relative to this repository."""
    text = _blank_code(markdown_file.read_text(encoding="utf-8"))
    for line_number, line in enumerate(text.splitlines(), 1):
        for match in MARKDOWN_LINK.finditer(line):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1].strip()
            target = target.split("#", 1)[0]
            if not target or target.startswith("/") or SCHEME.match(target):
                continue
            yield line_number, target


def resolve_target(markdown_file, target):
    """Return (resolved_path, inside_repository, case_matches)."""
    typed = os.path.abspath(os.path.join(markdown_file.parent, unquote(target)))
    typed_root = os.path.abspath(ROOT)
    inside = typed == typed_root or typed.startswith(typed_root + os.sep)
    resolved = Path(typed)
    case_matches = True
    if inside and resolved.exists():
        # Windows resolves case-insensitively; a public repository may be cloned on a
        # case-sensitive file system, so the typed spelling must match the disk spelling.
        on_disk = os.path.relpath(os.path.realpath(typed), os.path.realpath(typed_root))
        as_typed = os.path.relpath(typed, typed_root)
        case_matches = on_disk == as_typed
    return resolved, inside, case_matches


class MarkdownLinkTests(unittest.TestCase):
    def test_guidance_documents_are_present(self):
        names = {path.relative_to(ROOT).as_posix() for path in guidance_files()}
        for required in ("README.md", "START_HERE.md", "Help/README.md", "Help/FILE_MAP.md", "REPO-SYNC/README.md"):
            self.assertIn(required, names)

    def test_relative_markdown_links_resolve(self):
        broken = []
        for markdown_file in guidance_files():
            for line_number, target in relative_link_targets(markdown_file):
                resolved, inside, case_matches = resolve_target(markdown_file, target)
                if not inside:
                    continue
                label = f"{markdown_file.relative_to(ROOT).as_posix()}:{line_number} -> {target}"
                if not resolved.exists():
                    broken.append(label + " (missing)")
                elif not case_matches:
                    broken.append(label + " (spelling differs from the file on disk)")
        self.assertEqual(broken, [], "Broken relative Markdown links:\n" + "\n".join(broken))


if __name__ == "__main__":
    unittest.main()
