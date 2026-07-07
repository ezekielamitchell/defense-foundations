const weeks = [
  {
    id: "w26",
    label: "W26 - Week 1",
    dates: "Jun 22-28",
    start: "2026-06-22",
    end: "2026-06-28",
    primary: "Toolchains, repo setup, Missing Semester lecture 1, Python Crash Course ch. 1-8, MIT 6.0001 lectures 1-4, and Rustlings batch 1.",
    evidence: "Clean environment, repo and README committed, first runnable Python scripts, and file-processing script.",
    tasks: [
      "Confirm Python, Rust, shell, and Git toolchains.",
      "Run first Python scripts from the crash course.",
      "Capture file-processing evidence in the repo."
    ]
  },
  {
    id: "w27",
    label: "W27 - Week 2",
    dates: "Jun 29-Jul 5",
    start: "2026-06-29",
    end: "2026-07-05",
    primary: "Rust Book ch. 1-6 and Rustlings batches 1-3.",
    evidence: "Rustlings batch and small Cargo program.",
    tasks: [
      "Work through Rust Book ch. 1-6.",
      "Advance Rustlings batches 1-3.",
      "Keep a small Cargo program runnable."
    ]
  },
  {
    id: "w28",
    label: "W28 - Week 3",
    dates: "Jul 6-12",
    start: "2026-07-06",
    end: "2026-07-12",
    primary: "Missing Semester lectures 2-5 and Pro Git ch. 1-3.",
    evidence: "Terminal workflow note, clean commits, and PR practice.",
    tasks: [
      "Write a terminal workflow note.",
      "Practice clean commits with readable diffs.",
      "Run through a basic PR review loop."
    ]
  },
  {
    id: "w29",
    label: "W29 - Week 4",
    dates: "Jul 13-19",
    start: "2026-07-13",
    end: "2026-07-19",
    primary: "argparse, pathlib, pytest, and uv.",
    evidence: "csv_summary v0.",
    tasks: [
      "Build argparse and pathlib reps.",
      "Add pytest coverage around a small CLI.",
      "Produce csv_summary v0 evidence."
    ]
  },
  {
    id: "w30",
    label: "W30 - Week 5",
    dates: "Jul 20-26",
    start: "2026-07-20",
    end: "2026-07-26",
    primary: "Rust Book ch. 7-10, clap v4, and Rustlings batches 4-5.",
    evidence: "wc-rs v0.",
    tasks: [
      "Study modules, collections, error handling, and generics.",
      "Build a clap v4 CLI rep.",
      "Produce wc-rs v0 evidence."
    ]
  },
  {
    id: "w31",
    label: "W31 - Week 6",
    dates: "Jul 27-Aug 2",
    start: "2026-07-27",
    end: "2026-08-02",
    primary: "README discipline, pytest, Cargo tests, and six-week gate on Sun Aug 2.",
    evidence: "Paired comparison note and tests, plus six-week review.",
    tasks: [
      "Run pytest and Cargo tests.",
      "Write the Python vs Rust comparison note.",
      "Complete the six-week confidence review."
    ]
  },
  {
    id: "w32",
    label: "W32 - Week 7",
    dates: "Aug 3-9",
    start: "2026-08-03",
    end: "2026-08-09",
    primary: "Hardening and exit-gate review.",
    evidence: "Edge cases, README polish, and dependency cleanup.",
    tasks: [
      "Add edge case checks.",
      "Polish README run instructions.",
      "Remove accidental dependencies or stale files."
    ]
  },
  {
    id: "w33",
    label: "W33 - Week 8",
    dates: "Aug 10-16",
    start: "2026-08-10",
    end: "2026-08-16",
    primary: "P0 retrospective and eight-week maximum gate on Sun Aug 16.",
    evidence: "Pass or extend decision at maximum gate.",
    tasks: [
      "Review exit criteria honestly.",
      "Write the retrospective.",
      "Record a pass or extension decision."
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
  document.getElementById("current-week").textContent = current.label.split(" - ")[0];
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
