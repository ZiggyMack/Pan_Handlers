"""Timestamped annotations for the October 4 CFA tutorial intake.

Observations paraphrase supplied transcripts. Current primary references and
local CFA records supply qualifications; these are not our execution results.
"""

from Help.content.tutorial_register import SOURCES

_CORE = ("Core text encoders, conditioning and model sockets", "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py")
_STRINGS = ("Core string concatenation", "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_string.py")
_SD3 = ("SD3 Medium package contents", "https://huggingface.co/stabilityai/stable-diffusion-3-medium")
_FLUX = ("Official FLUX.1 examples and component roles", "https://comfyanonymous.github.io/ComfyUI_examples/flux/")
_FLUX_GUIDE = ("Current FLUX.1 text-to-image recipes", "https://docs.comfy.org/tutorials/flux/flux-1-text-to-image")
_KLEIN = ("Separate FLUX.2 Klein recipes", "https://docs.comfy.org/tutorials/flux/flux-2-klein")
_CLOUD = ("Managed Cloud custom nodes", "https://support.comfy.org/articles/6791455062-custom-nodes-on-cloud")
_IMPORT = ("Cloud model import route", "https://docs.comfy.org/cloud/import-models")
_REPRO = ("Limits of seed reproducibility", "https://docs.pytorch.org/docs/stable/notes/randomness.html")
_WORKFLOW = ("Opening workflow JSON or image metadata", "https://docs.comfy.org/get_started/first_generation")
_LORA = ("LoRA example and routing", "https://docs.comfy.org/tutorials/basic/lora")
_H3 = ("Official MiniMax H3 guide; separate from the creator video", "https://docs.comfy.org/tutorials/video/minimax/minimax-h3")


def _lesson(seconds, title, takeaway, observed, apply, keep, *sources):
    return dict(seconds=seconds, title=title, takeaway=takeaway, observed=observed,
                apply=apply, keep=keep, sources=sources)


EP5 = (
    _lesson(44, "Read what each package contains",
            "A different encoder package is not automatically a different image-model architecture.",
            "The creator selects SD3 Medium packages with CLIP only or additional T5 in different precisions.",
            "The SD3 Medium card identifies the same image-model and VAE weights with different text-encoder contents. Record those contents instead of calling all three unrelated models. CFA's October 4 catalog found SD3.5 entries, not confirmation of these original SD3 Medium packages; keep any substitution explicit.",
            "Exact model, bundled or separate encoders, VAE, precision, loader and Cloud availability status.", _SD3, _IMPORT),
    _lesson(181, "Keep the latent and sampler recipe model-specific",
            "Shared comparison controls do not make an SDXL graph interchangeable with SD3.",
            "The tutorial changes to EmptySD3LatentImage and uses 28 or 30 steps, CFG 4.5, dpmpp_2m and sgm_uniform.",
            "Treat these as the historical SD3 example. Preserve each model branch's required latent, encoding, sampling and decoding setup. The numbers are not defaults for the distilled Klein editor, whose validated recipe uses different nodes and guidance.",
            "Per-branch model family, dimensions, seed, steps, sampler, scheduler and guidance.", _SD3, _KLEIN),
    _lesson(281, "Share the raw words, encode them separately",
            "One STRING can feed two text inputs; each model keeps its own encoder.",
            "At 05:00 the encoder text widgets become inputs. A Primitive supplies positive text to multiple encoders; another supplies negative text. At 06:44 the seed is promoted and fixed.",
            "Fan out the same raw prompt STRING to each branch's own text encoder. Its matching CLIP or other encoder object supplies that model's encoding. CONDITIONING is already encoded and cannot be shared across incompatible architectures just because both sockets have the same label. Practice the two paths in Workflow anatomy → Node map → Prompt composition.",
            "Raw text, the encoder in each branch, typed connections and actual compiled seed.", _CORE, _STRINGS, _REPRO),
    _lesson(496, "Label outputs and preserve the baseline",
            "A comparison needs attributable saved outputs, not just two previews.",
            "The tutorial assigns a saved-image prefix to each model, then examines paired results across seeds.",
            "Use distinct A/B prefixes, fixed shared inputs and complete sample/decode/save branches. An identical integer seed does not establish identical noise across different architectures. CFA applies this method to paired Klein baseline versus Candid Film 0.5; paired v4 was validated but not rendered. Earlier separate stills do not establish a winning adapter.",
            "A and B outputs, exact model/settings, baseline, one changed variable and a concrete observation.", _REPRO, _CORE),
    _lesson(607, "Judge the shot rather than inherit a ranking",
            "Creator preferences and hardware timings are observations from that demonstration.",
            "The creator compares SD3 with a Juggernaut SDXL fine-tune and comments on detail, prompt adherence and anatomical errors.",
            "Use the same written brief and inspect anatomy, likeness, requested objects and composition in your own outputs. Different architectures need their supported settings; one shared prompt is not a controlled claim that one model always wins. Record limitations and rejected results. Do not treat the creator's suggested cause of errors or local GPU timings as account measurements.",
            "Success criterion, both result files, observed defect, elapsed time if measured and next decision.", _REPRO),
)

EP6 = (
    _lesson(93, "Join conditioning after encoding",
            "ConditioningConcat accepts CONDITIONING, not readable text.",
            "Two separate CLIP Text Encode nodes feed ConditioningConcat, which feeds the SDXL sampler's positive input.",
            "Keep the matching encoder connected to both text nodes. ConditioningConcat joins encoded token data; it is different from joining STRINGs before one encoder, and it is not a 50/50 style mixer. Its metadata behavior also matters. Use a compatible, documented recipe rather than moving this SDXL construction unchanged into a different model family.",
            "Both encoded branches, their model/encoder and the final CONDITIONING connection.", _CORE),
    _lesson(304, "A style preset begins as text",
            "The selector's positive and negative outputs must pass through text encoders.",
            "The creator initially leaves styles off, then connects a CSV style's text into a promoted encoder text input; the negative style later gets its own encoded branch.",
            "STRING → encoder text is the valid connection. STRING cannot replace a CLIP object or go straight to KSampler positive. Start with empty optional style text, then add one style. In a supported SDXL recipe positive and negative conditioning are active; CFA's distilled Klein CFG-1 baseline has no effective conventional negative branch, so its negative field remains inactive notes.",
            "Effective positive/negative text, style-off baseline and which branches actually affect this recipe.", _CORE, _KLEIN),
    _lesson(451, "Expose useful controls without changing their behavior",
            "A compact interface should still lead to the actual executable settings.",
            "The creator groups nodes and renames, reorders or hides widgets to simplify an SDXL workflow.",
            "Keep an inspectable expanded graph and check resolved settings. CFA's Klein controls are distributed across RandomNoise, KSamplerSelect, Flux2Scheduler and CFGGuider feeding SamplerCustomAdvanced. Do not replace them with the screenshot's SDXL 30-step, CFG-7, Karras recipe. Collapsing or hiding a control does not deactivate it.",
            "Editor JSON, resolved execution settings and whether controls were validated or actually rendered.", _CORE, _KLEIN),
    _lesson(739, "Test styles against the subject you must preserve",
            "More styles can obscure the subject instead of improving it.",
            "Chinese ink brush and graffiti are combined around 12:19–12:44. At 13:17 long exposure overwhelms the robot until the creator revises the prompt.",
            "Save a no-style baseline. Add one style with fixed input, seed and sampling, then inspect identity, clothing, framing and requested change before trying a second. A CSV and a local Manager install do not provision managed Cloud. Use supported explicit style text if the remote selector has no library.",
            "The complete text and one style change, paired output, preservation failure or success.", _CLOUD, _REPRO),
)

EP7 = (
    _lesson(66, "Compose strings before encoding",
            "Instruction STRING + optional style STRING → STRING → encoder → CONDITIONING.",
            "The creator replaces the previous conditioning-concatenation approach with text concatenation and later routes the combined text into SDXL encoders.",
            "Join readable text with an explicit delimiter and preview the exact result. Easy Positive/Negative or Primitive text nodes supply strings; their colors and names do not turn them into encoders. String concatenation is not ConditioningConcat, so keep socket types visible. The Prompt composition practice shows both paths.",
            "Core instruction, optional style text, delimiter and effective combined prompt.", _CORE, _STRINGS),
    _lesson(173, "Inspect the assembled prompt before generation",
            "A text preview answers what will be sent; it cannot show an unrun image.",
            "The tutorial saves joined text to a file, demonstrating delimiter, whitespace and find/replace behavior before creating images.",
            "Read the complete effective prompt after all selectors and transformations. Label input image previews separately from prior generated outputs. CFA's Prompt and Reference Check completed an input-only Cloud job; it is an independent copy, so transfer chosen text, style indices and crops to the renderer explicitly. It contains no model or sampler, and its text-widget appearance was not browser-inspected.",
            "Effective prompt, selected inputs/crops and the settings transferred to the rendering graph.", _STRINGS),
    _lesson(286, "Adapt the library to managed Cloud",
            "A local CSV path cannot configure Cloud's style selector.",
            "The tutorial edits the WAS configuration to point at a local styles CSV, then selects multiple style strings.",
            "In CFA's reviewed Cloud session, the WAS selector offered only None. The working replacement embedded styles in ImpactStringSelector with multiline off and index 0 blank. Keep no style as the default and inspect the resolved selection. This is a library of prompt text, not a trained concept LoRA. Check current remote node availability before adopting it.",
            "Node/package, embedded library revision, style indices and exact strings; no account secrets.", _CLOUD),
    _lesson(597, "Start with styles off and compare one addition",
            "The optional style should support a readable core instruction.",
            "Positive and negative instruction/style strings are joined before encoding. The creator begins with no styles, then adds long exposure, flowers and a cartoon treatment.",
            "Capture the no-style output, add one style and compare at fixed seed. Prompt order can affect results, but the assertion that the first style is always strongest is not a universal rule. In SDXL preserve the appropriate negative route; in CFA's Klein CFG-1 baseline do not promise effects from the inactive negative-notes field. Keep the expanded graph available after grouping.",
            "No-style baseline, full effective prompt, one changed style and a concrete preservation check.", _CORE, _KLEIN, _REPRO),
)

EP8 = (
    _lesson(134, "A workflow recipe and its model package are separate",
            "Trace MODEL, encoder and VAE roles rather than infer them from a filename extension.",
            "The creator opens early FLUX.1 Dev/Schnell FP8 checkpoint packages through a simple loader; later the full graph loads components separately.",
            "A bundled checkpoint may expose MODEL, CLIP and VAE; a standalone diffusion file does not necessarily contain encoders or a VAE. Inspect the official recipe and exact package. In Cloud first find the supported files and loaders, then use supported imports where needed. A .safetensors extension alone does not identify the role or guarantee compatibility.",
            "Exact model package/variant, precision, loader, encoder files and VAE.", _FLUX, _IMPORT),
    _lesson(215, "Open the graph or load the pixels deliberately",
            "Workflow metadata restores a recipe; Load Image supplies image pixels.",
            "The creator downloads example images containing workflows and opens those images to restore Dev or Schnell graphs.",
            "A metadata-bearing original PNG can reopen its graph. Uploading an image to Load Image instead supplies IMAGE data for a recipe. These operations are different, and metadata may be removed by screenshots or sharing. Preserve an explicit editor JSON plus original source images, then actually reopen the graph and check missing models/nodes.",
            "Editor JSON, original metadata-bearing image if present, source image and reopen result.", _WORKFLOW, _FLUX),
    _lesson(330, "Keep guidance attached to the exact variant",
            "Classic CFG, FLUX.1 guidance and Klein's recipe are different controls.",
            "The tutorial uses CFG 1 and four steps for Schnell, then more steps and FluxGuidance for Dev, later changing Dev's sampler/scheduler to address blur in that test.",
            "Those are historical FLUX.1 recipes. At CFG 1 the conventional negative branch has no guidance effect in this baseline; that does not prove every FLUX-based workflow lacks negative-prompt techniques. FLUX.2 Klein base and distilled variants use their own recipes. Neither SDXL settings nor this FLUX.1 FluxGuidance node should be silently substituted into the validated Klein editor.",
            "Family, exact variant, active guidance node, steps, sampler/schedule and branch behavior.", _FLUX_GUIDE, _KLEIN, _CORE),
    _lesson(494, "Reuse style strings while retaining the model's encoder",
            "Prompt-text controls can be shared without sharing model-specific conditioning.",
            "The creator joins a prompt and optional style text before encoding, then compares no style with selected styles at fixed seed.",
            "Reuse the raw-string composition method from Episode 7. Keep styles empty by default, preview the final text and encode it with the selected model's own encoder. A style preset's effect can change between model families; preserve a separate baseline for each recipe.",
            "Effective text, encoder/model version and paired no-style/style outputs.", _STRINGS, _CORE),
    _lesson(952, "Read separate model, encoder and VAE loaders",
            "The graph's extra loaders describe dependencies rather than extra artistic controls.",
            "The full FLUX.1 example separately loads the diffusion model, CLIP/T5 encoders and ae VAE, then uses a guider and advanced sampler.",
            "Trace diffusion MODEL to the guider, text encoders to text conditioning, LATENT through sampling, and VAE to decode. Current recipes may use different folder labels than the older clip/unet tutorial. Those paths describe a self-managed server; Cloud uses its remote model catalog and categories. Our FLUX.2 Klein reference editor is a different graph with different companions.",
            "Dependency manifest with each file's role, exact variant and corresponding loader.", _FLUX, _FLUX_GUIDE, _KLEIN),
    _lesson(1210, "Precision and LoRA compatibility need the exact recipe",
            "FP8, NF4, family and base-versus-distilled are separate compatibility questions.",
            "The tutorial installs an early BNB NF4 loader, compares precision variants, and at 25:16 adds a FLUX.1 Dev realism LoRA after saving an adapter-off result.",
            "Do not repeat the historical local NF4 installation on managed Cloud. Confirm the precise format's loader and runtime support and the adapter creator's target family, size and variant. A FLUX.1 Dev adapter is not a Klein adapter. CFA's Candid Film examples target Klein 9B base while its test uses distilled: execution establishes loading, not creator-endorsed compatibility or improvement. Keep that pairing experimental.",
            "Model/adapter source pages, precision, loader, target variant, strength and accepted or rejected A/B findings.", _CLOUD, _FLUX, _KLEIN, _LORA),
)

COMPARISON = (
    _lesson(13, "Turn visual opinions into a shot checklist",
            "Judge appearance and motion/contact separately.",
            "The creator discusses fight-scene motion, sliding feet, merging bodies and a shield that reappears after being dropped.",
            "In Video workshop → 03 / Preview & compare, use the same shot brief and preservation criteria for each candidate. Inspect matched timecodes and the whole clip at normal speed. Attractive still frames do not establish contact, object continuity or original performance preservation. The noisy transcript's model names and rankings are not verified product comparisons.",
            "Candidate/version, source/brief, settings, output link and defect with a timecode."),
    _lesson(205, "Shared inputs help, but do not create a controlled benchmark",
            "Record task, duration, dimensions and settings alongside a shared prompt.",
            "The creator describes using the same initial image and prompt across generators, then demonstrates multi-shot generation with another character reference.",
            "Keep the baseline source and reference roles fixed. Record any supported-input, duration, settings or prompt change made for a candidate. Newly generated motion from one image is a different task from transforming an existing video's performance. Choose the workflow for the actual task before comparing results.",
            "Task, input roles, full prompt, requested/actual duration, dimensions, FPS and candidate recipe."),
    _lesson(506, "Review dialogue and supplied audio independently",
            "Correct words, tone, mouth timing and believable movement each need a check.",
            "The creator checks whispered dialogue, missed lines and lip sync, then at 14:19 introduces a supplied song and image for a performance example.",
            "Retain the intended line or audio file and listen against the exported clip. Check exact wording, speaker assignment, tone, mouth timing, body movement and timing at the start and end. A creator's expressive singing example does not verify our rap workflow. Carry sound and performance defects into the existing take-review notes, with rejected takes preserved.",
            "Source audio/line, exact take, timecoded sound/visual findings and acceptance decision."),
    _lesson(1019, "Test one preservation demand before adding a cast",
            "A complex demonstration is an inspiration, not a reliable starting recipe.",
            "The creator compares emotional beats and later combines six or eleven character/prop references, describing identity loss, duplicates and spatial inconsistencies.",
            "Begin with one subject and one short beat. Establish identity, motion/contact and framing before testing additional references or cuts. Record which reference supplies appearance versus performance. Reject a beautiful shot if it fails the selected preservation criteria; keep why it failed and the next single change.",
            "One-beat brief, ordered references, preservation criteria, rejected output and next decision."),
    _lesson(1453, "Use current account estimates and actual outcomes",
            "Historical prices and creator preferences do not select our winner.",
            "The closing section offers approximate prices, resolution claims and preferred models for different tasks.",
            "Do not copy those amounts into a current cost estimate; the provider, recipe and dates are unresolved. Use the current workspace estimate for a proposed bounded run, then record actual cost if available. In Video workshop → Preview & compare, accept only a reviewed take, retain rejected alternatives, and finish HD/4K after performance passes. Reading this comparison creates no measured project result.",
            "Dated provider estimate, actual job usage if known, outcome, rejection reason or accepted take."),
)

H3 = (
    _lesson(434, "Assign a role to every media reference",
            "Appearance images, performance video and audio are different inputs.",
            "The creator describes reference-to-video using ordered image, video and audio inputs, then demonstrates environment/costume and object changes.",
            "Write an ordered reference list naming the role of every file. Match it to the exact current template and prompt syntax rather than assuming a text-to-video template accepts all media. CFA's discovery establishes template presence only; neither this transcript nor an official guide verifies dependencies or a successful account run. Use Video workshop's existing reference notes and the H3 candidate guidance for the next check.",
            "Template/version, appearance/performance/audio roles, required dependencies and separate availability, validation, execution and acceptance status.", _H3, _CLOUD),
)


FOLLOWUPS = {
    "ep5": ("Episode 5 · SD3 and model comparisons", "00:00–17:06", EP5),
    "ep6": ("Episode 6 · Styles and encoded conditioning", "00:00–15:44", EP6),
    "ep7": ("Episode 7 · Prompt strings and optional styles", "00:00–12:05", EP7),
    "ep8": ("Episode 8 · FLUX.1 loading and comparisons", "00:00–29:51", EP8),
    "h3": ("MiniMax H3 · Media roles and source record", "00:00–09:25", H3),
    "comparison": ("Video-model comparison · Review our own takes", "00:00–25:59", COMPARISON),
}


def episode_entries():
    """Create renderer entries without reading the archived source files."""
    return {
        key: dict(label=label, title=label + " · annotated notes", download=label,
                  filename=f"comfyui-{key}-annotated-notes.md", url=SOURCES[key]["url"],
                  lessons=lessons, coverage=coverage, reviewed=SOURCES[key]["reviewed"],
                  source_key=key,
                  provenance="Annotations of the user-supplied transcript. Creator demonstrations, opinions and historical settings are separate from current guidance and CFA's measured results.")
        for key, (label, coverage, lessons) in FOLLOWUPS.items()
    }
