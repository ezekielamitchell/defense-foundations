const weeks = [
  {
    id: "week0",
    label: "Week 0",
    dates: "Jul 14-19",
    start: "2026-07-14",
    end: "2026-07-19",
    primary: "Establish baseline truth, inspect current CLI stubs/WIP, continue Rustlings from if2, complete the next bounded foundations increment, and review Rust ownership.",
    evidence: "Verified baseline plus a real foundations artifact. Reset administration and planning do not count.",
    tasks: [
      "Confirm the active CLI paths are stubs/WIP.",
      "Resume Rustlings from if2; do not restart batch 1.",
      "Verify one bounded foundations increment."
    ]
  },
  {
    id: "week1",
    label: "Week 1",
    dates: "Jul 20-26",
    start: "2026-07-20",
    end: "2026-07-26",
    primary: "Continue from actual Rustlings state, implement and test a bounded Project 0 slice, study Rust structs/enums, and read Command-Line Rust ch. 1-3.",
    evidence: "Runnable bounded slice with tests or reproducible output; resume and LinkedIn refreshed by Jul 26.",
    tasks: [
      "Continue Rustlings from the recorded state.",
      "Implement one bounded Project 0 slice.",
      "Refresh resume and LinkedIn by Jul 26."
    ]
  },
  {
    id: "week2",
    label: "Week 2",
    dates: "Jul 27-Aug 2",
    start: "2026-07-27",
    end: "2026-08-02",
    primary: "Shell workflow, development tools, editor workflow, Pro Git ch. 1-3, and branch/PR practice.",
    evidence: "Terminal and Git workflow proof; GitHub profile aligned by Aug 2.",
    tasks: [
      "Write a terminal workflow note.",
      "Practice clean commits with readable diffs.",
      "Align the GitHub profile by Aug 2."
    ]
  },
  {
    id: "week3",
    label: "Week 3",
    dates: "Aug 3-9",
    start: "2026-08-03",
    end: "2026-08-09",
    primary: "Build Python csv_summary v0 with argparse, pathlib, csv, pytest, and uv.",
    evidence: "Runnable Python CLI, tests, example output, and a recorded Week 4 Rust decision by Aug 9.",
    tasks: [
      "Build argparse and pathlib reps.",
      "Add pytest coverage to csv_summary.",
      "Decide the Week 4 Rust increment by Aug 9."
    ]
  },
  {
    id: "week4",
    label: "Week 4",
    dates: "Aug 10-16",
    start: "2026-08-10",
    end: "2026-08-16",
    primary: "Build csv-summary-rs or hello-stats v1 after the Aug 9 decision; study Rust Book ch. 7-10 and clap.",
    evidence: "Runnable Rust CLI slice with explicit error behavior.",
    tasks: [
      "Study modules, collections, error handling, and generics.",
      "Build the selected Rust CLI slice.",
      "Document its failure behavior."
    ]
  },
  {
    id: "week5",
    label: "Week 5",
    dates: "Aug 17-23",
    start: "2026-08-17",
    end: "2026-08-23",
    primary: "Compare Python and Rust implementations, deepen tests, run Clippy and rustfmt, and polish README proof.",
    evidence: "Comparison note, test output, and reproducible README commands.",
    tasks: [
      "Write the Python vs Rust comparison note.",
      "Run relevant test and lint commands.",
      "Make README examples match observed output."
    ]
  },
  {
    id: "week6",
    label: "Week 6",
    dates: "Aug 24-30",
    start: "2026-08-24",
    end: "2026-08-30",
    primary: "Harden error paths and edge cases, clean dependencies, verify reproducibility, and assess the six-week gate.",
    evidence: "Gate assessment on Aug 30 plus an explicit GDARS/CASEset re-decision.",
    tasks: [
      "Add edge case checks.",
      "Verify a cold reproducible run.",
      "Record the Aug 30 gate decision."
    ]
  },
  {
    id: "week7",
    label: "Week 7",
    dates: "Aug 31-Sep 6",
    start: "2026-08-31",
    end: "2026-09-06",
    primary: "Apply the gate outcome and open the gate-dependent application wave. Continue P0 hardening if the gate did not pass.",
    evidence: "Application evidence only if the gate permits it; no automatic advanced-lane activation.",
    tasks: [
      "Apply the documented gate outcome.",
      "Open Application Wave 1 only if permitted.",
      "Keep advanced lanes unscheduled."
    ]
  },
  {
    id: "week8",
    label: "Week 8",
    dates: "Sep 7-13",
    start: "2026-09-07",
    end: "2026-09-13",
    primary: "Use the contingency week for hardening, retrospective, and the pass-or-extend decision.",
    evidence: "Eight-week maximum gate decision on Sep 13.",
    tasks: [
      "Review exit criteria honestly.",
      "Write the P0 retrospective.",
      "Record a pass or written extension by Sep 13."
    ]
  }
];

const phases = [
  ["P0", "Foundations", "Python, Rust, Linux, Git", "in progress"],
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
  notes: "df-mobile-notes"
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
  return `df-mobile-task-${weekId}-${index}`;
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
