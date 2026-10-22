# Model Card — HITL Multimodal AAC-ES v0.0

## Model details
- **Name / version:** HITL Multimodal AAC-ES v0.0 — research specification
- **Owner / contact:** Miguel Ángel Patiño Antonioli — UNMSM Doctoral Program in Deep Tech, AI & Emerging Technologies
- **Documentation date:** 18 October 2026
- **Development status:** Research-stage prototype specification; not yet trained, clinically validated, or deployed.
- **Architecture:** Planned multimodal AAC artifact integrating photographs/pictograms, text, synthesized speech, contextual information, interaction history, adaptive suggestion/ranking, and human-in-the-loop review. The child retains final control to select, reject, modify, ignore, or stop.
- **License:** UNKNOWN — to investigate before any public release.

## Intended use
- **Primary intended uses:** Research prototype to support independent functional communication in Spanish for a bounded subgroup of minimally speaking or nonspeaking autistic children requiring very substantial support, within one structured therapeutic communication context.
- **Intended users:** Research participants supported by caregivers and qualified professionals; researchers evaluating the artifact under an approved protocol.
- **Out-of-scope / misuse:** NOT for autism diagnosis, clinical or medical recommendations, inference of thoughts or internal states, autonomous communication on behalf of the child, unsupervised deployment, or replacement of AAC/clinical professionals.

## Factors
- **Relevant groups / conditions:** Communication profile; functional communication repertoire; sensory/contextual needs; Spanish-language and Peruvian sociocultural context; activity/context; caregiver/specialist configuration; individual interaction history.
- **Evaluation factors:** Planned disaggregation by participant and experimental condition (intelligent prototype vs predefined static AAC comparator). Where feasible, results will also be examined by communicative function and prompting level.

## Metrics
- **Primary outcome 1:** Independent functional communication acts per session.
- **Primary outcome 2:** Communicative diversity — range of communicative functions or concepts expressed.
- **Primary outcome 3:** Assistance / prompting level required to communicate.
- **Secondary / process measures:** Message-selection time; rejected or modified AI suggestions; treatment fidelity; inter-observer agreement; focused caregiver/specialist feedback.
- **Variation approach:** Repeated within-participant comparisons across sessions. Report participant-level trajectories and condition-wise summaries. For stochastic ML benchmarking, use mean ± std over at least 5 seeds, confidence intervals, and paired comparisons when appropriate.

## Evaluation data
- **Dataset / design:** NOT YET COLLECTED. Planned pilot evaluation: minimum four participants from one clearly defined subgroup; one structured therapeutic communication context; alternating-treatments single-case design comparing the intelligent prototype with a predefined static AAC condition.
- **Evaluation protocol:** Conditions counterbalanced or randomized where feasible; repeated measurement across sessions; prespecified session procedures, prompting hierarchy, fidelity checklist, safety/stopping rules, coding rules, and analysis logic.
- **Preprocessing:** Planned pseudonymization and session-level coding; identifiers stored separately; a prespecified subset independently double-coded. Exact preprocessing pipeline is UNKNOWN — to investigate and freeze before data collection.

## Training data
- **Datasets:** No thesis participant data have been collected or used for model training as of this deliverable. The final foundation model/provider and any fine-tuning or adaptation data are UNKNOWN — to investigate and document before implementation.
- **Personalization data:** If used, personalization will rely only on authorized, minimized interaction history and configured preferences; it must not silently convert test/evaluation interactions into training data.
- **Known limitations:** No final training corpus, model checkpoint, data license, or multilingual/cultural coverage assessment is yet available.

## Quantitative analyses
- **Overall results:** NO THESIS RESULTS YET — no participant-level or model-performance claims are made in Deliverable 7.
- **Disaggregated results:** Planned disaggregated reporting: per-participant and per-condition trajectories, with prompting/assistance explicitly separated. Aggregate summaries will not replace individual trajectories.
- **Statistical interpretation:** Quantitative results will be treated as bounded pilot evidence rather than population-level clinical effectiveness. Repeated within-participant comparisons will be emphasized.

## Ethical considerations
- **Risks:** Privacy and security risks involving minors; unsafe or contextually inappropriate suggestions; bias; homogenization of communication; over-personalization; dependency; misinterpretation; reduction of user agency; inadvertent disclosure of sensitive routines or communication content.
- **Mitigations:** Caregiver informed consent; communication-appropriate assent/withdrawal signals; data minimization; restricted access; pseudonymization; preference for on-device processing where feasible; human review; traceability of suggestions/modifications; ability to reject/ignore/stop; low-confidence blocking; bias/error review; no diagnosis or medical advice.
- **Human agency principle:** AI outputs are suggestions, never decisions. The system must not speak autonomously on behalf of the child.

## Caveats and recommendations
- **Caveats:** Research-stage specification only. No clinical effectiveness, safety, generalizability, subgroup performance, external validation, or production reliability has been established.
- **Recommendations:** Freeze the artifact version, comparator, eligibility criteria, model/provider, data schema, preprocessing, prompting hierarchy, coding rules, stopping rules, statistical plan, retention/deletion policy, and software environment before human-data collection. Version every DSR change and justify deviations.
