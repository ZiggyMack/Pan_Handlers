"""A portable, read-only CFA worked example; no provider or journal calls."""

from io import BytesIO
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

import streamlit as st


CASE_DIR = Path(__file__).resolve().parent / "examples" / "cfa_pump_v001"
CASE_FILES = (
    "README.md", "manifest.json", "pump_concept_v001.png",
    "pump_concept_prompt.txt", "pump_concept_v001.record.json",
    "pump_concept_v001.editor.json", "pump_concept_v001.api.json",
)


def case_record():
    return json.loads((CASE_DIR / "pump_concept_v001.record.json").read_text(encoding="utf-8"))


def case_bundle():
    """Include only the fixed evidence sample, never the checkout or model files."""
    output = BytesIO()
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for filename in CASE_FILES:
            archive.writestr("cfa_pump_v001/" + filename, (CASE_DIR / filename).read_bytes())
    return output.getvalue()


def render(key_prefix):
    record = case_record()
    st.subheader("Worked example · the first Observatory pump")
    st.caption("CFA field evidence · September 12, 2026 · Comfy Cloud · one completed still image")
    st.write("The question was whether one concept image could communicate a practical village pump with visible maintenance history. The job completed, but the design still needed revision. Those are two separate results.")
    brief, result = st.columns(2)
    with brief:
        st.markdown("**Source: a written brief**")
        st.write("A compact lake-green housing, brass fittings, pale stone footing, a readable service panel, one replaced coupling, a repair patch, and a socket for a separately modeled lever.")
        st.caption("This was text-to-image. There was no source photograph or video to preserve.")
        with st.expander("Read the exact prompt"):
            st.text((CASE_DIR / "pump_concept_prompt.txt").read_text(encoding="utf-8"))
    with result:
        st.image(str(CASE_DIR / "pump_concept_v001.png"), caption="Actual first output · 1024 × 1024 · seed 42", width=480)

    review, reproduce, evidence = st.tabs(["Brief → result", "Open the recipe", "What this proves"])
    with review:
        st.table({
            "Wanted": ["Green metal, brass and stone", "Readable whole object and service panel", "A visibly repaired, compact pump"],
            "Observed": ["Palette and materials read clearly", "Useful silhouette and three-quarter view", "Too pristine and slender; repair patch, coupling and lever socket unclear"],
            "Decision": ["Keep the direction", "Keep the presentation", "Revise before treating it as a finished prop"],
        })
        st.write("The next production choice was to author repair details in the simple Godot prop and focus on the playable experience. There is no second generated image demonstrating an improvement, and this PNG has not been proved as an imported game mesh.")
        st.info("For a dialogue rewrite, apply the same review habit to source footage: specify what must stay, what may change, and what would make you reject the result. The proposed rehearsal is in Rewrite a scene.")
    with reproduce:
        st.markdown("**1. Open the editor graph**")
        st.write("Download the editor JSON below, then open or drag it into the ComfyUI editor. It is an editor-save graph with a nodes array. Inspect its model selectors before running it.")
        st.download_button("Download editor workflow · open in Comfy", (CASE_DIR / "pump_concept_v001.editor.json").read_bytes(),
                           file_name="pump_concept_v001.editor.json", mime="application/json", key=key_prefix + "_editor")
        st.markdown("**2. Match this recipe's model family**")
        st.code("z_image_turbo_bf16.safetensors  → diffusion model\nqwen_3_4b.safetensors           → text encoder\nae.safetensors                 → VAE", language="text")
        st.write("This historical baseline uses Z-Image, with separate loaders. Our starter preference for new image-model searches remains SDXL + Checkpoint + SafeTensor. Replacing one filename with an SDXL checkpoint would not turn this into a compatible SDXL workflow.")
        st.markdown("**3. Restore the recorded settings before a comparison**")
        st.write("1024 × 1024; batch 1; seed 42; 8 steps; CFG 1; res_multistep sampler; simple scheduler; denoise 1; shift 3. The saved editor graph retains a randomize seed control: explicitly restore seed 42 and choose fixed control for a controlled rerun.")
        st.caption("Check current model/node availability and the execution service's charges before running. The guide itself submits no job.")
        with st.expander("API submission graph · for automation"):
            st.write("This second file uses node-ID keys with class_type and inputs. It is the API submission graph extracted from the same completed PNG. Use it with a compatible submission API; it is not the file to drag into the editor. The editor and API files were preserved separately without hand conversion.")
            st.download_button("Download API submission graph", (CASE_DIR / "pump_concept_v001.api.json").read_bytes(),
                               file_name="pump_concept_v001.api.json", mime="application/json", key=key_prefix + "_api")
    with evidence:
        st.table({
            "Claim": ["Generation completed", "Output quality", "Exact deployed versions", "Runtime and credits", "Civitai import", "Dialogue-rewrite video"],
            "Evidence / limit": [
                "Recorded completed job plus original PNG and matching embedded workflow metadata.",
                "Promising starting direction; documented revision needs. Completion did not mean acceptance.",
                "Model filenames and template metadata are recorded. Deployed core/node versions and immutable model revisions are unknown.",
                "Actual GPU runtime and attributable credits are unknown. The usage window ended before this job; zero API-node estimate excluded GPU time.",
                "Provider secret reported saved; first authenticated import still untested at this checkpoint.",
                "No source video, replacement speech, lip-sync run or completed rewritten clip exists in this case.",
            ],
        })
        st.markdown("**A real failure and recovery**")
        st.write("Comfy OAuth failed with invalid_grant: refresh token reuse detected. The first browser callback timed out; a fresh login for the existing connection succeeded, followed by a responding read-only server-info call. The cause of the recurring rejection remains unknown. Replacing the Civitai provider secret was not the recovery step.")
        st.caption("The successful connection check reported MCP server 0.57.0 and 41 tools. That is the connector version, not a verified ComfyUI core version.")
        st.code(record["job"]["id"], language="text")
        st.caption("Completion was observed at " + record["job"]["completion_observed_at_utc"] + ". This observation time is not a GPU runtime measurement.")
    st.download_button("Download this evidence sample · ZIP", case_bundle(),
                       file_name="cfa_pump_v001_evidence.zip", mime="application/zip", key=key_prefix + "_bundle")
    st.caption("Includes the actual PNG, prompt, editor/API graphs, run record, instructions and hashes. No model weights or credentials. Browsing this example leaves your journal and chosen path unchanged.")
