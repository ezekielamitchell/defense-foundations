// Read-only consumer of the generated Aegis authority. This app never writes
// task completion or evidence. Local storage is used only for scratch notes;
// legacy reset-scoped checkbox keys are deliberately left untouched.
const PROJECTION_URL = "../docs/aegis-phase0-projection.json";
const PROJECTION_SCHEMA = "aegis.phase0-projection.v1";

// Curriculum labels only; generated dates and evidence remain separately authoritative.
const phases = [
  [
    "P0",
    "Programming Foundations From Zero",
    "Main route · start from zero · evidence-gated",
    "scheduled; work unverified"
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
let weeks = [];

function parseDate(value, endOfDay = false) {
  const [year, month, day] = value.split("-").map(Number);
  return new Date(
    year,
    month - 1,
    day,
    endOfDay ? 23 : 0,
    endOfDay ? 59 : 0,
    endOfDay ? 59 : 0,
    endOfDay ? 999 : 0
  );
}

function shortDate(value) {
  return parseDate(value).toLocaleDateString(undefined, { month: "short", day: "numeric" });
}

function timeFromIso(value) {
  return value.slice(11, 16);
}

function getCurrentWeek(today = new Date()) {
  const time = today.getTime();
  const active = weeks.find((week) => {
    return time >= parseDate(week.start).getTime() && time <= parseDate(week.end, true).getTime();
  });
  if (active) return active;
  if (time < parseDate(weeks[0].start).getTime()) return weeks[0];
  return weeks[weeks.length - 1];
}

function day0Actions(projection) {
  const actionByLane = {
    research: "Read the selected previous-local-day Hugging Face paper for 60 minutes; log it as research, never Foundation proof.",
    python: "Inspect file_stats, define one shared fixture, and write the smallest Python test; capture observed output or one blocker.",
    rust: "Mirror the same fixture and output contract in hello-stats; capture observed parity output or one blocker.",
    endr: "Use the separate endr block for one permitted G0 outcome or an exact blocker; never count it as Foundation evidence.",
    admin: "Record observed proof or no-proof, one blocker, and the exact next command."
  };
  return projection.day0.events.map((event) => {
    return `${timeFromIso(event.start)}–${timeFromIso(event.end)} · ${event.action || actionByLane[event.lane] || event.title}`;
  });
}

function buildWeeks(projection) {
  const parallel = projection.course_routing?.mode === "parallel-defense-curriculum-v1";
  return projection.capacity.weekly.map((week, index) => ({
    ...week,
    dates: `${week.start} → ${week.end}`,
    evidence: "Resume the oldest unmet Python/Rust criterion. Record the actual command/result or one blocker; this read-only row is never Foundation evidence.",
    actions: index === 0 ? day0Actions(projection) : parallel ? [
      "Open the current Calendar action card and course map; Calendar owns time.",
      "Learn Python, Rust, agents, battlefield AI and warfare in parallel, at the oldest unmet step in each track.",
      "Use 2–3-hour studios and one-hour curriculum readings, with one primary course per track.",
      "Prove each language independently before parity; agent and research work remain non-gate.",
      "Save actual output or a blocker and the exact source resume point."
    ] : [
      "Open the dated Aegis note and exact Calendar action card before starting; the manifest owns timing.",
      "Run the separate Python and Rust blocks on one shared fixture contract; preserve the weekly pair_cycle_id even when degree commitments split the languages across days.",
      "Use an optional agent block only where the manifest permits it; max three read-only tools and three steps, cut first.",
      "Keep source pulls issue-bound and immediately applied; save the exact course resume point.",
      "Close with observed output or no-proof, one blocker, and one copyable next command."
    ]
  }));
}

async function loadProjection() {
  const response = await fetch(PROJECTION_URL, { cache: "no-store" });
  if (!response.ok) throw new Error(`projection request failed (${response.status})`);
  const projection = await response.json();
  if (projection.schema_version !== PROJECTION_SCHEMA) throw new Error("unsupported projection schema");
  const required = ["authority", "period", "checkpoints", "capacity", "day0", "evidence"];
  if (required.some((key) => !projection[key])) throw new Error("projection is incomplete");
  if (projection.evidence.schedule_is_evidence !== false || projection.evidence.task_state_is_evidence !== false) {
    throw new Error("projection weakens the evidence boundary");
  }
  return projection;
}

function renderDashboard() {
  const parallel = phase0Projection.course_routing?.mode === "parallel-defense-curriculum-v1";
  document.getElementById("current-focus").textContent = parallel ? "Python · Rust · AI agents · battlefield AI · warfare" : "Follow the current course map and exact Calendar plan";
  document.getElementById("work-allocation").textContent = phase0Projection.capacity.normal_week_targets ? `${Object.entries(phase0Projection.capacity.normal_week_targets).filter(([key]) => key !== "unreserved").reduce((total, [, minutes]) => total + minutes, 0) / 60}h outside class · normal week` : "Follow exact weekly reservations";
  const current = getCurrentWeek();
  const beforeStart = Date.now() < new Date(phase0Projection.authority.boundary).getTime();
  document.getElementById("phase-status").textContent = beforeStart ? "P0 prelaunch · work unverified" : "P0 scheduled · evidence required";
  document.getElementById("current-week").textContent = current.label;
  document.getElementById("current-week-dates").textContent = current.dates;
  document.getElementById("week-title").textContent = `${current.label}: ${current.dates}`;
  document.getElementById("week-primary").textContent = current.focus;
  document.getElementById("week-evidence").textContent = current.evidence;
  document.getElementById("baseline-date").textContent = shortDate(phase0Projection.checkpoints.baseline);
  document.getElementById("readiness-date").textContent = `readiness ${shortDate(phase0Projection.checkpoints.readiness)}`;
  document.getElementById("final-date").textContent = shortDate(phase0Projection.checkpoints.final_capability);
  document.getElementById("final-window").textContent = `review ${phase0Projection.checkpoints.final_review_window} · horizon ${timeFromIso(phase0Projection.checkpoints.horizon_cutoff)} PDT`;
  document.getElementById("phase-progress").textContent = "pending";
  document.querySelector(".phase-meter").setAttribute("aria-label", "Work unverified; this projection does not track completion");
  document.getElementById("phase-message").textContent = `Read-only projection, not gate progress. ${current.label}: ${current.focus}. Authority: ${phase0Projection.authority.config_path}.`;
}

function renderWeeks() {
  const list = document.getElementById("week-list");
  const current = getCurrentWeek();
  list.replaceChildren();

  weeks.forEach((week) => {
    const card = document.createElement("article");
    card.className = `week-card${week.id === current.id ? " current" : ""}`;
    const header = document.createElement("div");
    header.className = "week-header";
    const heading = document.createElement("div");
    const title = document.createElement("h3");
    title.textContent = week.label;
    const dates = document.createElement("div");
    dates.className = "week-date";
    dates.textContent = week.dates;
    heading.append(title, dates);
    header.appendChild(heading);
    if (week.id === current.id) {
      const badge = document.createElement("span");
      badge.className = "week-badge";
      badge.textContent = "Current";
      header.appendChild(badge);
    }

    const primary = document.createElement("p");
    primary.textContent = week.focus;
    const evidence = document.createElement("div");
    evidence.className = "callout";
    const evidenceTitle = document.createElement("span");
    evidenceTitle.textContent = "Evidence boundary";
    const evidenceText = document.createElement("p");
    evidenceText.textContent = week.evidence;
    evidence.append(evidenceTitle, evidenceText);

    const actions = document.createElement("div");
    week.actions.forEach((action) => {
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
  document.getElementById("phase-message").textContent = `${error.message}. Use Aegis Nexus directly; no cached date or task state is treated as current.`;
  document.getElementById("week-primary").textContent = "Generated authority could not be loaded.";
  document.getElementById("week-evidence").textContent = "Fail closed: this screen makes no schedule or completion claim.";
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
    weeks = buildWeeks(phase0Projection);
    renderDashboard();
    renderWeeks();
  } catch (error) {
    renderProjectionFailure(error);
  }
}

initialize();
