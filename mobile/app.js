// Read-only consumer of the public educational projection. The private Aegis
// schedule, protected commitments, and company work are never served here.
// Local storage is used only for scratch notes.
const PROJECTION_URL = "../docs/aegis-phase0-projection.json";
const PROJECTION_SCHEMA = "aegis.phase0-public-projection.v1";

// Curriculum labels only; generated dates and evidence remain separately authoritative.
const phases = [
  [
    "P0",
    "Programming Foundations From Zero",
    "Main route · start from zero · evidence-gated",
    "active; work unverified"
  ],
  [
    "P1",
    "Contracts, Measurement and Replay",
    "Main route · after P0 · evidence-gated",
    "not started"
  ],
  [
    "P2",
    "Quantitative Reasoning and Trustworthy Evaluation",
    "Main route · after P1 · evidence-gated",
    "not started"
  ],
  [
    "P4",
    "Reliable Rust Services and Distributed Systems",
    "Main route · after P1, P2 · evidence-gated",
    "not started"
  ],
  [
    "P6",
    "Deterministic Simulation and Adapter Integration",
    "Main route · after P4 · evidence-gated",
    "not started"
  ],
  [
    "P8",
    "Human Authority and Bounded Agent Interfaces",
    "Main route · after P6 · evidence-gated",
    "not started"
  ],
  [
    "P10",
    "Multi-Agent Coordination Under Degraded Communications",
    "Main route · after P4, P6, P8 · evidence-gated",
    "not started"
  ],
  [
    "P11",
    "Assurance, Security and Test Evaluation",
    "Main route · after P10 · evidence-gated",
    "not started"
  ],
  [
    "P12",
    "Integrated Capstone and Technical Communication",
    "Main route · after P10, P11 · evidence-gated",
    "not started"
  ],
  [
    "P3",
    "Computer Vision and Deep Learning",
    "Optional depth · after P2 · evidence-gated",
    "not started"
  ],
  [
    "P5",
    "Embedded and Physical Interfaces",
    "Optional depth · after P4 · evidence-gated",
    "not started"
  ],
  [
    "P7",
    "State Estimation and Navigation",
    "Optional depth · after P6 · evidence-gated",
    "not started"
  ],
  [
    "P9",
    "Reinforcement Learning and Decision Experiments",
    "Optional depth · after P2, P6 · evidence-gated",
    "not started"
  ]
];

const storageKeys = {
  // Keep the historical notes key so a projection refresh cannot erase real text.
  notes: "df-mobile-final-20260901-0900-notes"
};

let phase0Projection;
let topics = [];

function buildTopics(projection) {
  const project = projection.project0;
  return [
    {
      id: "project0",
      label: "Project 0 · Python and Rust",
      focus: project.contract,
      evidence: project.proof,
      actions: [
        `Inspect ${project.python} and ${project.rust}.`,
        "Resume the oldest unmet behavior in each language.",
        "Compare identical fixtures only after each implementation has independent proof."
      ]
    },
    {
      id: "parallel",
      label: "Parallel learning tracks",
      focus: projection.curriculum.parallel_topics.join(" · "),
      evidence: "Study and course attendance are not Foundation proof.",
      actions: [
        projection.curriculum.source_policy,
        projection.curriculum.intro_policy,
        "Keep research and agent exercises separate from Project 0 gate evidence."
      ]
    },
    {
      id: "route",
      label: "Competency route",
      focus: projection.curriculum.core_route.join(" → "),
      evidence: "Each phase requires observed proof and an explicit gate decision.",
      actions: [`Optional depth: ${projection.curriculum.optional_depth.join(", ")}.`]
    }
  ];
}

async function loadProjection() {
  const response = await fetch(PROJECTION_URL, { cache: "no-store" });
  if (!response.ok) throw new Error(`projection request failed (${response.status})`);
  const projection = await response.json();
  if (projection.schema_version !== PROJECTION_SCHEMA) throw new Error("unsupported projection schema");
  const required = ["phase", "curriculum", "project0", "evidence", "source"];
  if (required.some((key) => !projection[key])) throw new Error("projection is incomplete");
  if (projection.evidence.schedule_is_evidence !== false || projection.evidence.task_state_is_evidence !== false) {
    throw new Error("projection weakens the evidence boundary");
  }
  return projection;
}

function renderDashboard() {
  const current = topics[0];
  document.getElementById("current-focus").textContent = phase0Projection.curriculum.parallel_topics.join(" · ");
  document.getElementById("work-allocation").textContent = "Private Aegis plan and Calendar";
  document.getElementById("phase-status").textContent = "P0 active · work unverified";
  document.getElementById("current-week").textContent = "P0 Foundation";
  document.getElementById("current-week-dates").textContent = "Educational scope only";
  document.getElementById("week-title").textContent = current.label;
  document.getElementById("week-primary").textContent = current.focus;
  document.getElementById("week-evidence").textContent = current.evidence;
  document.getElementById("baseline-date").textContent = "Observed proof";
  document.getElementById("readiness-date").textContent = "Check the private plan";
  document.getElementById("final-date").textContent = "Explicit gate decision";
  document.getElementById("final-window").textContent = "No automatic promotion";
  document.getElementById("phase-progress").textContent = "pending";
  document.querySelector(".phase-meter").setAttribute("aria-label", "Work unverified; this projection does not track completion");
  document.getElementById("phase-message").textContent = "Read-only public curriculum summary. Use the private Aegis plan for current dates and reservations.";
}

function renderTopics() {
  const list = document.getElementById("week-list");
  list.replaceChildren();

  topics.forEach((topic) => {
    const card = document.createElement("article");
    card.className = `week-card${topic.id === "project0" ? " current" : ""}`;
    const header = document.createElement("div");
    header.className = "week-header";
    const heading = document.createElement("div");
    const title = document.createElement("h3");
    title.textContent = topic.label;
    heading.append(title);
    header.appendChild(heading);
    if (topic.id === "project0") {
      const badge = document.createElement("span");
      badge.className = "week-badge";
      badge.textContent = "Active";
      header.appendChild(badge);
    }

    const primary = document.createElement("p");
    primary.textContent = topic.focus;
    const evidence = document.createElement("div");
    evidence.className = "callout";
    const evidenceTitle = document.createElement("span");
    evidenceTitle.textContent = "Evidence boundary";
    const evidenceText = document.createElement("p");
    evidenceText.textContent = topic.evidence;
    evidence.append(evidenceTitle, evidenceText);

    const actions = document.createElement("div");
    topic.actions.forEach((action) => {
      const row = document.createElement("div");
      row.className = "read-row";
      const marker = document.createElement("span");
      marker.setAttribute("aria-hidden", "true");
      marker.textContent = "→";
      const text = document.createElement("p");
      text.textContent = action;
      row.append(marker, text);
      actions.appendChild(row);
    });

    card.append(header, primary, evidence, actions);
    list.appendChild(card);
  });
}

function renderPhases() {
  const list = document.getElementById("phase-list");
  list.replaceChildren();
  phases.forEach(([id, title, description, status]) => {
    const card = document.createElement("article");
    card.className = `phase-card${id === "P0" ? " active" : ""}`;
    const heading = document.createElement("div");
    const name = document.createElement("h3");
    name.textContent = `${id} - ${title}`;
    const state = document.createElement("div");
    state.className = "phase-status";
    state.textContent = status;
    const detail = document.createElement("p");
    detail.textContent = description;
    heading.append(name, state);
    card.append(heading, detail);
    list.appendChild(card);
  });
}

function renderProjectionFailure(error) {
  document.getElementById("phase-status").textContent = "Projection unavailable";
  document.getElementById("phase-progress").textContent = "stale";
  document.getElementById("phase-message").textContent = `${error.message}. Use the private Aegis plan directly; this page makes no completion claim.`;
  document.getElementById("week-primary").textContent = "Public curriculum projection could not be loaded.";
  document.getElementById("week-evidence").textContent = "This screen is never the evidence authority.";
}

function setupTabs() {
  const tabs = document.querySelectorAll(".tab");
  const views = document.querySelectorAll(".view");
  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      tabs.forEach((item) => item.classList.remove("active"));
      views.forEach((view) => {
        view.classList.remove("active");
        view.hidden = true;
      });
      const target = document.getElementById(tab.dataset.target);
      tab.classList.add("active");
      target.hidden = false;
      target.classList.add("active");
    });
  });
}

function setupNotes() {
  const textarea = document.getElementById("mobile-notes");
  const saveState = document.getElementById("save-state");
  const copyButton = document.getElementById("copy-notes");
  const clearButton = document.getElementById("clear-notes");
  let saveTimer;

  textarea.value = localStorage.getItem(storageKeys.notes) || "";
  textarea.addEventListener("input", () => {
    localStorage.setItem(storageKeys.notes, textarea.value);
    saveState.textContent = "Saving local scratch note...";
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => {
      saveState.textContent = "Scratch note saved locally; not evidence.";
    }, 350);
  });
  copyButton.addEventListener("click", async () => {
    if (!textarea.value.trim()) {
      saveState.textContent = "Nothing to copy yet.";
      return;
    }
    try {
      await navigator.clipboard.writeText(textarea.value);
      saveState.textContent = "Scratch note copied; verify it before promotion.";
    } catch {
      textarea.select();
      saveState.textContent = "Select and copy the highlighted scratch note.";
    }
  });
  clearButton.addEventListener("click", () => {
    textarea.value = "";
    localStorage.removeItem(storageKeys.notes);
    saveState.textContent = "Scratch note cleared.";
  });
}

function setupInstallPrompt() {
  const installButton = document.getElementById("install-button");
  let deferredPrompt;
  window.addEventListener("beforeinstallprompt", (event) => {
    event.preventDefault();
    deferredPrompt = event;
    installButton.hidden = false;
  });
  installButton.addEventListener("click", async () => {
    if (!deferredPrompt) return;
    deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    deferredPrompt = null;
    installButton.hidden = true;
  });
}

function setupServiceWorker() {
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => navigator.serviceWorker.register("./sw.js"));
  }
}

async function initialize() {
  setupTabs();
  setupNotes();
  setupInstallPrompt();
  setupServiceWorker();
  renderPhases();
  try {
    phase0Projection = await loadProjection();
    topics = buildTopics(phase0Projection);
    renderDashboard();
    renderTopics();
  } catch (error) {
    renderProjectionFailure(error);
  }
}

initialize();
