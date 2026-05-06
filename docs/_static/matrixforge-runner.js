(function () {
  const PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v0.27.6/full/pyodide.js";
  let pyodidePromise;

  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const existing = document.querySelector(`script[src="${src}"]`);
      if (existing) {
        existing.addEventListener("load", resolve, { once: true });
        existing.addEventListener("error", reject, { once: true });
        return;
      }

      const script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.onload = resolve;
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }

  async function getPyodide() {
    if (!pyodidePromise) {
      pyodidePromise = loadScript(PYODIDE_URL).then(() => {
        return window.loadPyodide({
          indexURL: PYODIDE_URL.replace(/\/pyodide\.js$/, "/"),
        });
      });
    }

    return pyodidePromise;
  }

  function dedent(value) {
    const lines = value.replace(/^\n/, "").replace(/\s+$/, "").split("\n");
    const indents = lines
      .filter((line) => line.trim())
      .map((line) => line.match(/^\s*/)[0].length);
    const minIndent = indents.length ? Math.min(...indents) : 0;
    return lines.map((line) => line.slice(minIndent)).join("\n");
  }

  async function runExample(runner) {
    const button = runner.querySelector(".matrixforge-runner__run");
    const status = runner.querySelector(".matrixforge-runner__status");
    const code = runner.querySelector(".matrixforge-runner__code");
    const output = runner.querySelector(".matrixforge-runner__output");
    const artifacts = runner.querySelector(".matrixforge-runner__artifacts");
    const packages = (runner.dataset.packages || "")
      .split(",")
      .map((item) => item.trim())
      .filter(Boolean);

    button.disabled = true;
    status.textContent = "Loading Python...";
    output.textContent = "";
    artifacts.replaceChildren();

    try {
      const pyodide = await getPyodide();
      if (packages.length) {
        status.textContent = `Loading ${packages.join(", ")}...`;
        await pyodide.loadPackage(packages);
      }

      status.textContent = "Running...";
      pyodide.setStdout({
        batched: (text) => {
          output.textContent += text + "\n";
        },
      });
      pyodide.setStderr({
        batched: (text) => {
          output.textContent += text + "\n";
        },
      });

      pyodide.runPython(`
import base64
import io

_matrixforge_artifacts = []

def display_html(html):
    _matrixforge_artifacts.append({"type": "html", "content": str(html)})

def display_svg(svg):
    _matrixforge_artifacts.append({"type": "svg", "content": str(svg)})

def display_text(text):
    print(text)
`);

      await pyodide.runPythonAsync(dedent(code.value));
      renderArtifacts(artifacts, pyodide);
      status.textContent = "Done";
      if (!output.textContent.trim() && !artifacts.children.length) {
        output.textContent = "(no output)";
      }
    } catch (error) {
      status.textContent = "Error";
      output.textContent += String(error);
    } finally {
      button.disabled = false;
    }
  }

  function renderArtifacts(container, pyodide) {
    const artifactsJson = pyodide.runPython(`
import json

try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None

if plt is not None:
    for figure_number in plt.get_fignums():
        figure = plt.figure(figure_number)
        buffer = io.BytesIO()
        figure.savefig(buffer, format="png", bbox_inches="tight", dpi=144)
        encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
        _matrixforge_artifacts.append({
            "type": "image/png",
            "content": encoded,
            "alt": f"Matplotlib figure {figure_number}",
        })
    plt.close("all")

json.dumps(_matrixforge_artifacts)
`);
    const artifacts = JSON.parse(artifactsJson);

    artifacts.forEach((artifact) => {
      if (artifact.type === "image/png") {
        const image = document.createElement("img");
        image.src = `data:image/png;base64,${artifact.content}`;
        image.alt = artifact.alt || "Python generated figure";
        image.className = "matrixforge-runner__image";
        container.appendChild(image);
      } else if (artifact.type === "html") {
        const frame = document.createElement("iframe");
        frame.className = "matrixforge-runner__html";
        frame.setAttribute("sandbox", "allow-scripts");
        frame.srcdoc = artifact.content;
        container.appendChild(frame);
      } else if (artifact.type === "svg") {
        const wrapper = document.createElement("div");
        wrapper.className = "matrixforge-runner__svg";
        wrapper.innerHTML = artifact.content;
        container.appendChild(wrapper);
      }
    });
  }

  function initRunner(runner) {
    const code = runner.querySelector(".matrixforge-runner__code");
    const button = runner.querySelector(".matrixforge-runner__run");
    code.value = dedent(code.value);
    button.addEventListener("click", () => runExample(runner));
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".matrixforge-runner").forEach(initRunner);
  });
})();
