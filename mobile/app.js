const weeks = [
  {
    id: "week1",
    label: "Week 1",
    dates: "Aug 9",
    start: "2026-08-09",
    end: "2026-08-09",
    primary: "Activate A20 at 16:00, preserve every zero denominator, and use only the separate 16:00-18:00 endr block.",
    evidence: "No inherited credit and no curriculum backfill; Monday's exact diagnostic is fixed.",
    tasks: [
      "Keep every A20 foundation and course denominator at zero.",
      "Complete or honestly resume the endr-owned block.",
      "Protect the 19:30 movie and stage Monday's diagnostic."
    ]
  },
  {
    id: "week2",
    label: "Week 2",
    dates: "Aug 10-16",
    start: "2026-08-10",
    end: "2026-08-16",
    primary: "Build the first tested file_stats slice, diagnose hello-stats honestly, and apply Linux/Git practice to the paired project.",
    evidence: "Runnable Python increment, verified Rust state, tests, and exact command transcripts.",
    tasks: [
      "Build argparse/pathlib behavior and the first pytest case.",
      "Run the Rust diagnostic and fresh Rustlings work through the active range.",
      "Keep OpenCV, HF Agents, papers, and endr in separate non-gate routes."
    ]
  },
  {
    id: "week3",
    label: "Week 3",
    dates: "Aug 17-23",
    start: "2026-08-17",
    end: "2026-08-23",
    primary: "Build the hello-stats Rust increment, deepen error cases, and reconcile shared fixtures.",
    evidence: "Compiling, tested Rust slice plus paired output observations.",
    tasks: [
      "Use Result-based errors and focused cargo tests.",
      "Advance Rustlings only through freshly passing exercises.",
      "Record the Aug 23 reachability review without promoting P1."
    ]
  },
  {
    id: "week4",
    label: "Week 4",
    dates: "Aug 24-30",
    start: "2026-08-24",
    end: "2026-08-30",
    primary: "Harden malformed inputs, add CI and cold-run documentation, and assemble the six-week gate decision.",
    evidence: "Test/lint/format output, paired comparison, README proof, and the Aug 30 written gate decision.",
    tasks: [
      "Add failure fixtures and deterministic checks.",
      "Make README examples match observed output.",
      "Record PASS, PARTIAL PASS, or REMEDIATION REQUIRED on Aug 30."
    ]
  },
  {
    id: "week5",
    label: "Week 5",
    dates: "Aug 31-Sep 6",
    start: "2026-08-31",
    end: "2026-09-06",
    primary: "Apply the gate outcome, close documented gaps, and measure clean-environment recreation.",
    evidence: "Gate-dependent application evidence only if authorized; no automatic advanced-lane activation.",
    tasks: [
      "Remediate only named gate gaps.",
      "Verify cold reproducible runs and benchmarks.",
      "Keep P1-P12 unscheduled without an explicit promotion."
    ]
  },
  {
    id: "week6",
    label: "Week 6",
    dates: "Sep 7-13",
    start: "2026-09-07",
    end: "2026-09-13",
    primary: "Finish maximum-gate remediation, preserve the Rustlings 0-50 cap, and write the pass/close/extend decision.",
    evidence: "Eight-week maximum gate decision on Sep 13 with per-line evidence or remediation.",
    tasks: [
      "Audit Rustlings only through exercise 50.",
      "Re-run clean tests and cold-run instructions.",
      "Record a pass, close, or written extension by Sep 13."
    ]
  }
];

const phases = [
  ["P0", "Foundations", "Python, Rust, Linux, Git", "in progress"],
  ["O0", "Bounded agent sampler", "HF tools, typed I/O, deterministic traces, evaluation", "non-gate; active credit 0"],
  ["P1", "Math and engineering discipline", "Math, Linux, and Git fluency", "not started"],
  ["P2", "Core ML", "Classical ML and honest evaluation", "not started"],
  ["P3", "Computer vision", "OpenCV, PyTorch, and CNNs", "not started"],
  ["P4", "Rust systems", "Production Rust systems", "not started"],
  ["P5", "Robotics and embedded", "Robotics and embedded systems", "not started"],
  ["P6", "Edge AI", "Model optimization and deployment", "not started"],
  ["P7", "Transformers", "Transformers and foundation models", "not started"],
  ["P8", "ROS 2 sensor fusion", "ROS 2, SLAM, and sensor fusion", "not started"],
  ["P9", "Multi-agent swarm", "RL, MARL, and swarms", "not started"],
  ["P10", "Gaze HMT", "Gaze estimation and human-machine teaming", "not started"],
  ["P11", "Doctrine ethics", "Doctrine, policy, and ethics", "not started"],
  ["P12", "Research capstone", "Research specialization", "not started"]
];

const storageKeys = {
  notes: "df-mobile-a20-notes"
};

function parseDate(value) {
  return new Date(`${value}T12:00:00`);
}

function getCurrentWeek(today = new Date()) {
  const time = today.getTime();
  const active = weeks.find((week) => time >= parseDate(week.start) && time <= parseDate(week.end));
  if (active) {
    return active;
  }
  if (time < parseDate(weeks[0].start)) {
    return weeks[0];
  }
  return weeks[weeks.length - 1];
}

function taskKey(weekId, index) {
  return `df-mobile-a20-task-${weekId}-${index}`;
}

function isTaskComplete(weekId, index) {
  return localStorage.getItem(taskKey(weekId, index)) === "true";
}

function setTaskComplete(weekId, index, complete) {
  localStorage.setItem(taskKey(weekId, index), String(complete));
  updateProgress();
}

function updateProgress() {
  const total = weeks.reduce((count, week) => count + week.tasks.length, 0);
  const complete = weeks.reduce((count, week) => {
    return count + week.tasks.filter((_, index) => isTaskComplete(week.id, index)).length;
  }, 0);
  const percent = total === 0 ? 0 : Math.round((complete / total) * 100);
  const meter = document.querySelector(".phase-meter");
  const progress = document.getElementById("phase-progress");

  if (meter) {
    meter.style.setProperty("--meter", `${percent}%`);
  }
  if (progress) {
    progress.textContent = `${percent}%`;
  }
}

function renderDashboard() {
  const current = getCurrentWeek();
  document.getElementById("current-week").textContent = current.label;
  document.getElementById("current-week-dates").textContent = current.dates;
  document.getElementById("week-title").textContent = `${current.label}: ${current.dates}`;
  document.getElementById("week-primary").textContent = current.primary;
  document.getElementById("week-evidence").textContent = current.evidence;
  document.getElementById("phase-message").textContent = `${current.label} is focused on ${current.primary}`;
}

function renderWeeks() {
  const list = document.getElementById("week-list");
  const current = getCurrentWeek();
  list.innerHTML = "";

  weeks.forEach((week) => {
    const card = document.createElement("article");
    card.className = `week-card${week.id === current.id ? " current" : ""}`;

    const header = document.createElement("div");
    header.className = "week-header";
    header.innerHTML = `
      <div>
        <h3>${week.label}</h3>
        <div class="week-date">${week.dates}</div>
      </div>
      ${week.id === current.id ? '<span class="week-badge">Current</span>' : ""}
    `;

    const primary = document.createElement("p");
    primary.textContent = week.primary;

    const evidence = document.createElement("div");
    evidence.className = "callout";
    evidence.innerHTML = `<span>Evidence</span><p>${week.evidence}</p>`;

    const checks = document.createElement("div");
    week.tasks.forEach((task, index) => {
      const id = `${week.id}-${index}`;
      const row = document.createElement("label");
      row.className = "check-row";
      row.setAttribute("for", id);
      row.innerHTML = `
        <input id="${id}" type="checkbox" ${isTaskComplete(week.id, index) ? "checked" : ""}>
        <span>${task}</span>
      `;
      row.querySelector("input").addEventListener("change", (event) => {
        setTaskComplete(week.id, index, event.currentTarget.checked);
      });
      checks.appendChild(row);
    });

    card.append(header, primary, evidence, checks);
    list.appendChild(card);
  });
}

function renderPhases() {
  const list = document.getElementById("phase-list");
  list.innerHTML = "";

  phases.forEach(([id, title, description, status]) => {
    const card = document.createElement("article");
    card.className = `phase-card${id === "P0" ? " active" : ""}`;
    card.innerHTML = `
      <div>
        <h3>${id} - ${title}</h3>
        <div class="phase-status">${status}</div>
      </div>
      <p>${description}</p>
    `;
    list.appendChild(card);
  });
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
    saveState.textContent = "Saving...";
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => {
      saveState.textContent = "Notes saved locally.";
    }, 350);
  });

  copyButton.addEventListener("click", async () => {
    if (!textarea.value.trim()) {
      saveState.textContent = "Nothing to copy yet.";
      return;
    }

    try {
      await navigator.clipboard.writeText(textarea.value);
      saveState.textContent = "Notes copied.";
    } catch {
      textarea.select();
      saveState.textContent = "Select and copy the highlighted notes.";
    }
  });

  clearButton.addEventListener("click", () => {
    textarea.value = "";
    localStorage.removeItem(storageKeys.notes);
    saveState.textContent = "Notes cleared.";
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
    if (!deferredPrompt) {
      return;
    }
    deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    deferredPrompt = null;
    installButton.hidden = true;
  });
}

function setupServiceWorker() {
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("./sw.js");
    });
  }
}

renderDashboard();
renderWeeks();
renderPhases();
setupTabs();
setupNotes();
setupInstallPrompt();
setupServiceWorker();
updateProgress();
