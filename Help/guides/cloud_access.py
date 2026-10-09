"""Shared, sourced Cloud access instructions; no credentials or account calls."""

import streamlit as st


IMPORT_URL = "https://docs.comfy.org/cloud/import-models"
CODEX_MCP_URL = "https://learn.chatgpt.com/docs/extend/mcp?surface=cli"
ACCESS_SOURCES = [
    {"title": "Comfy Cloud · import models and provider secrets", "url": IMPORT_URL,
     "note": "Download links, provider credentials, import validation, destination selection and My Models."},
    {"title": "Civitai · API key settings", "url": "https://github.com/civitai/civitai/blob/main/src/components/Account/ApiKeysCard.tsx",
     "note": "Current API Keys section and key creation control; surrounding account-menu labels can change."},
    {"title": "Civitai · file access rules", "url": "https://github.com/civitai/civitai/blob/main/src/server/services/file.service.ts",
     "note": "Download authentication can be required by global policy or by the model version."},
    {"title": "Civitai · download responses", "url": "https://github.com/civitai/civitai/blob/main/src/pages/api/download/models/%5BmodelVersionId%5D.ts",
     "note": "Read the error message as well as its status: authentication, disabled downloads, early access and archival differ."},
    {"title": "Hugging Face · access tokens", "url": "https://huggingface.co/docs/hub/security-tokens",
     "note": "Read and fine-grained repository access; downloading does not need write permission."},
    {"title": "Hugging Face · public and authenticated downloads", "url": "https://huggingface.co/docs/huggingface_hub/quick-start",
     "note": "Public ungated files can be accessed without a token; private access requires authentication."},
    {"title": "Hugging Face · gated models", "url": "https://huggingface.co/docs/hub/models-gated",
     "note": "The provider account must hold access to the gated repository before a token can download its files."},
    {"title": "Codex · MCP authentication", "url": CODEX_MCP_URL,
     "note": "Named MCP servers have their own OAuth login. This is separate from a provider token saved in Comfy Cloud."},
    {"title": "Comfy · credit usage", "url": "https://support.comfy.org/articles/1982697177-partner-nodes-pricing",
     "note": "Comfy GPU runtime and Partner Nodes use Comfy credits; a Civitai model-source token does not transfer Buzz."},
]

IMPORT_STEPS = (
    ("Check whether a new import is needed",
     "Look for the required model in Cloud's shared catalog and My Models first. If an existing compatible file is available, skip the provider-access, secret and import steps and continue to Confirm the handoff. Record that you reused the existing file."),
    ("Confirm access to the exact file",
     "For a missing file, open its exact version on Civitai and check download availability. If authenticated downloading is required and no suitable key is saved, create a named key in your account's API Keys section, under Security & Apps in the shared screenshot. Choose read/download access where offered; a key only carries access the account already has."),
    ("Save the provider credential in Cloud",
     "When needed, use Comfy Cloud Settings → Secrets / API Keys & Secrets → Add Secret, choose Civitai, and enter the key there. Reuse an existing valid entry; its label can be anything. Keep the key out of chat, workflow JSON and field notes."),
    ("Import a missing model file",
     "Copy the exact file's download-button link. In Cloud, use Models → Import, paste that link, let it validate and choose Continue. Select the model type and destination requested by the workflow. For authenticated downloads, Cloud uses the saved provider secret; keep credentials out of the link."),
    ("Confirm the handoff",
     "For a new import, wait for completion and find the file in My Models. For either an imported file or an existing catalog file, select it in the compatible loader and check companion files and supported nodes. After reviewing the displayed usage, run a small test and inspect its saved output. Record model availability and render results separately."),
)

CHECKPOINTS = (
    ("Provider access, if importing", "The chosen provider file is downloadable with the access required; otherwise record 'not needed: existing Cloud file'."),
    ("Secret stored, if required", "The correct provider entry appears in Cloud Secrets; record its label only, or 'not needed' for an existing Cloud file or an import that needs no authentication."),
    ("Model available", "Record the exact filename and type in the shared catalog or My Models, and whether it was reused or newly imported."),
    ("Workflow ready", "The correct loader selects it; required companion models and nodes are available."),
    ("Automation connected, if used", "A read-only Comfy tool succeeds from the chosen client after login."),
    ("Small render reviewed", "An actual completed job has a playable/viewable output and recorded settings."),
)

HANDOFF_MARKDOWN = """## When a collaborator must click Import

In CFA's September 12 Comfy MCP toolset, model discovery and workflow execution
were available, but model import was a browser step. This is a limitation of
that observed toolset, not a requirement that every client always works this way.

The assistant or collaborator should research and prepare the missing dependency
first, then send one timely **Import needed** request for a concrete experiment:

- Experiment and why this model is needed:
- Exact model/version and file:
- Direct import link, without credentials:
- Model type and Cloud destination folder:
- Expected filename and reported Cloud download size:
- Completion signal: it appears in My Models, or report the import error.

Continue independent work while waiting. After the learner reports completion,
verify the imported entry, compatible loader and companion models before running.
Reuse that file for later workflows. A public import can succeed without proving
the saved key's access to a protected file. Browser-only learners can follow the
same import checks without setting up an assistant connection.
"""

FAILURES = (
    ("The import link will not validate",
     "Check that you copied the specific file's download link. A model browsing-page URL, unsupported file format or unavailable version can fail before credentials are involved. Check the current Cloud import requirements."),
    ("Civitai returns 401 or 403",
     "Read the response text. Check the saved provider token and the account's file access, but also check disabled downloads, early access or another access restriction. Replacing a token cannot grant rights the account lacks."),
    ("The version is archived or no longer downloadable",
     "Find an available authorized version and record the substitution. Including archived entries in search does not restore file access; the Civitai download handler can return 410 for archival."),
    ("The import succeeded but the workflow still fails",
     "Check the file role, architecture, precision, loader, companion files and Cloud's available nodes. An SDXL image checkpoint is not a complete video or lip-sync stack."),
    ("Cloud opens in the browser, but Codex reports OAuth failure",
     "Use the separate Codex connection instructions. A saved Civitai token and a working Cloud browser session do not prove the client's MCP connection is authenticated."),
    ("A run reports a plan or credit issue",
     "Check the execution service named in the error and its current plan/credit requirements. Civitai Buzz and Comfy credits are separate balances; model access and compute access are different checks."),
)


def guide_markdown():
    lines = ["# Cloud model access and import checklist", "",
             "Guide reviewed September 12, 2026. This blank checklist does not confirm account access, import or rendering.",
             "Store provider tokens directly in Cloud Secrets. Record labels and outcomes here, never credential values.", "",
             "## Civitai → Comfy Cloud", ""]
    for index, (title, detail) in enumerate(IMPORT_STEPS, 1):
        lines.extend([f"### {index}. {title}", "", detail, ""])
    lines.extend([HANDOFF_MARKDOWN, "", "## Evidence checklist", ""])
    lines.extend(f"- [ ] {title}: {evidence}" for title, evidence in CHECKPOINTS)
    lines.extend(["", "## Record this attempt", "",
                  "- Provider and secret label (no key), or not needed:", "- Model page, version and filename (no token-bearing URL):",
                  "- File role and loader:", "- Existing file reused, or import result and date:", "- Connector check, or not used:",
                  "- Render job/output reference and result:", "- Time/cost observed:", "- Error and next step:", "",
                  "## Optional Codex connection", "",
                  "For a configured OAuth MCP server, find its name with `codex mcp list`, then use `codex mcp login <server-name>`. The case used the name `comfy-cloud`. Complete browser authorization and retry a read-only tool. This is separate from the Civitai provider secret.", "",
                  "## Sources", ""])
    lines.extend(f'- [{source["title"]}]({source["url"]})' for source in ACCESS_SOURCES)
    return "\n".join(lines) + "\n"


def _provider_access():
    st.markdown("**Civitai → Comfy Cloud**")
    st.caption("Public browsing and file downloads have different access rules. A public listing can still require authenticated downloading; an already available Cloud model needs no new import.")
    for index, (title, detail) in enumerate(IMPORT_STEPS, 1):
        st.markdown(f"**{index}. {title}**")
        st.write(detail)
    st.markdown(f"[Official Cloud import walkthrough]({IMPORT_URL})")
    st.caption("Current import documentation covers supported .safetensors files from Civitai and Hugging Face. Cloud's import options determine the available destinations; a local D: drive path does not place a file in Cloud.")
    with st.expander("What does the Hugging Face option unlock?"):
        st.write("It supplies another source of model weights and model cards, including the exact encoders, VAEs, adapters or video-model files a workflow requests. Import support still depends on the file and Cloud workflow.")
        st.markdown("For a private or gated repository, obtain access with your Hugging Face account first, then save an appropriate read or fine-grained token as a **Hugging Face** secret in Cloud. Public ungated files may work without a token. A token does not bypass a model's access approval.")
        st.markdown("[Token permissions](https://huggingface.co/docs/hub/security-tokens) · [Gated-model access](https://huggingface.co/docs/hub/models-gated)")
    with st.expander("Plan the browser handoff with your collaborator"):
        st.markdown(HANDOFF_MARKDOWN)


def _codex_connection():
    st.info("Use this section when Codex is controlling Comfy Cloud. Browser-only users can skip it.")
    st.write("For a configured OAuth MCP connection, find its registered name and start its login:")
    st.code("codex mcp list\ncodex mcp login comfy-cloud", language="powershell")
    st.caption("comfy-cloud is the name in the shared case. Substitute the name registered in your client; a missing server needs the client's setup instructions first.")
    st.write("Complete browser authorization with the intended Comfy account, then retry a read-only tool, such as server information or model discovery. If your connection is managed through an app connector, use that connector's reconnect control.")
    st.caption("If OAuth still fails, record the error without tokens and check the current client/provider instructions. Do not record connection success until the read-only call works.")
    st.markdown(f"[Official Codex MCP instructions]({CODEX_MCP_URL})")


def _verify():
    st.table({"Checkpoint": [row[0] for row in CHECKPOINTS], "Evidence": [row[1] for row in CHECKPOINTS]})
    st.caption("Record results under Follow the steps → Choose where ComfyUI runs → Evidence & notes, or in the model receipt. These instructions do not mark any visitor's checkpoints complete.")
    for symptom, action in FAILURES:
        with st.expander(symptom):
            st.write(action)
    with st.expander("Lesson from the shared setup"):
        st.write("CFA's September 12 records add evidence beyond the original screenshots: a fresh login repaired the separate Comfy OAuth connection, and a read-only server-info call returned authenticated production access (MCP 0.57.0, 41 tools). One Z-Image pump still completed and its PNG/graphs were saved. The first authenticated Civitai import and any dialogue-rewrite render remain untested.")
        st.write("Public Civitai metadata was readable during CFA's model research. The Cloud owned-model search returned zero imports; its shared catalog already offered a RealVisXL SDXL checkpoint. Finding a model, importing it, completing a run and accepting its quality are separate checks.")
        st.caption("Inspect the portable CFA sample in ComfyUI guide → Worked example. These dated observations never complete a visitor's checkpoints; they are not a live check of the visitor's account.")
    with st.expander("Sources for access and troubleshooting"):
        for source in ACCESS_SOURCES:
            st.markdown(f'[{source["title"]}]({source["url"]}) — {source["note"]}')


def render(key_prefix):
    """Render at both setup entry points with a unique download-button key."""
    st.subheader("Confirm model access and workflow readiness")
    st.write("Check what is already available, import any missing model file, and confirm the workflow can use it.")
    st.table({
        "Connection": ["Civitai / Hugging Face → Cloud imports", "Codex → Comfy Cloud tools", "Execution service → compute"],
        "What enables it": ["Provider token in Cloud Settings → Secrets, when required", "The client's separate Comfy OAuth connection, when automation is used", "That service's plan and credits; Civitai Buzz and Comfy credits are separate"],
    })
    provider, codex, verify = st.tabs(["Provider access & import", "Codex connection (optional)", "Verify & troubleshoot"])
    with provider:
        _provider_access()
    with codex:
        _codex_connection()
    with verify:
        _verify()
    st.download_button("Download the Cloud access checklist", guide_markdown(),
                       file_name="comfy-cloud-access-checklist.md", mime="text/markdown",
                       key=key_prefix + "_download")
