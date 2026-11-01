# Start here: the front door of Pan Handlers

Written 2026-10-31 by Claude, the Master Repo steward, at Ziggy's word (the guidance map audit of October 30, choice 6). This file routes four kinds of reader to their first page. It adds no new rules; everything it points at already exists. When a page it names moves, this file is the one to fix first.

## Who are you?

**A learner who wants to follow the production method** (video from existing footage, reference discipline, prompts that travel).
Open Pathfinder, the learner app: from the repository root run `python -m streamlit run Help/app.py`, and begin at its own Start here page. The written guide is [Help/README.md](Help/README.md); the page-to-file map is [Help/FILE_MAP.md](Help/FILE_MAP.md). Pathfinder teaches the method and links provenance; it holds no production media and never reads the production repository at runtime.

**A maintainer or developer of this repository.**
Begin with the [README](README.md) section "For Developers", then [PAN_HANDLERS_SPEC.md](PAN_HANDLERS_SPEC.md) (what the repository is for) and [MANIFEST.md](MANIFEST.md) (what is in it). For the dashboard, [dashboard/START_HERE.md](dashboard/START_HERE.md) is the cold-boot guide. The deploy source of record for the hosted apps is the Hall at the root `pages/` folder and its launcher script (confirmed 2026-10-31).

**A collaborator agent arriving from CFA** (the production repository, which is private; this one is public).
The working channel between the two repositories is [REPO-SYNC/README.md](REPO-SYNC/README.md): outbound briefings in `REPO-SYNC/MASTER_REPO_SYNC_OUT.md`, inbound replies as one verbatim file each in `REPO-SYNC/SYNC_IN/pending/`. The best reply route is a mailbox message to `claude` in CFA's collaborators mailbox, since it is a file; the other two routes are a verbatim paste into `SYNC_IN/pending/` through Ziggy, or the dot. Nothing in this repository commits on your behalf; a commit here is a publication.

**A Claude session booted cold as the steward.**
Read [REPO-SYNC/README.md](REPO-SYNC/README.md), then check `REPO-SYNC/SYNC_IN/pending/` for anything waiting, then the two guidance documents of the moment: the [guidance map audit of October 30](REPO-SYNC/GUIDANCE_MAP_AUDIT_20261030.md) (what is stale, duplicated or contradictory, with Ziggy's choices recorded as they are made) and the [rules of the road, draft v001](REPO-SYNC/RULES_OF_THE_ROAD_DRAFT_20261027.md) (how the collaborators are worked with; a draft until adopted). Dashboard work starts at [dashboard/START_HERE.md](dashboard/START_HERE.md). The repository is public: commit only when Ziggy says so.

## Names, as decided on 2026-10-31

The shared vocabulary lives in [data/glossary.md](data/glossary.md). Where older files disagree with the forms below, the forms below are right and the files are corrected in the follow-up pass:

- CFA is Contextual Framework Analysis.
- ABI is the American Bureau of Intelligence.
- NDO is the Nyquist Data Observatory.
- DCIA is the Decentralized Intelligence Agency (the acronym keeps its legacy spelling).

## What this file is not

Not a map of every document (that is [MANIFEST.md](MANIFEST.md)), not the learner's course (that is Pathfinder), and not a statement of status for the production work, which lives in CFA and is restated here only where [Help](Help/README.md) says it is.
