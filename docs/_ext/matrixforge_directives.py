from __future__ import annotations

from html import escape

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective


LEARNING_PATH = [
    ("01", "What is a Matrix?", "fundamentals/what-is-a-matrix.html"),
    ("02", "Vectors & Shapes", "fundamentals/vectors.html"),
    ("03", "Addition & Scaling", "fundamentals/matrix-addition.html"),
    ("04", "Matrix Multiplication", "fundamentals/matrix-multiplication.html"),
    ("05", "Transformations", "fundamentals/matrix-as-transform.html"),
    ("06", "Applications", "applications/index.html"),
]


class MatrixForgePathDirective(SphinxDirective):
    has_content = False

    def run(self) -> list[nodes.Node]:
        steps = "\n".join(
            (
                f'  <a class="matrixforge-path__step" href="{href}">'
                f'<span class="matrixforge-path__number">{number}</span>'
                f'<span class="matrixforge-path__title">{escape(title)}</span>'
                "</a>"
            )
            for number, title, href in LEARNING_PATH
        )
        html = (
            '<nav class="matrixforge-path" aria-label="MatrixForge learning path">\n'
            f"{steps}\n"
            "</nav>"
        )
        return [nodes.raw("", html, format="html")]


class MatrixForgeRunnerDirective(SphinxDirective):
    has_content = True
    option_spec = {
        "packages": directives.unchanged,
        "title": directives.unchanged,
    }

    def run(self) -> list[nodes.Node]:
        packages = escape(self.options.get("packages", ""))
        title = escape(self.options.get("title", "Run this Python example"))
        code = escape("\n".join(self.content))
        html = f"""
<div class="matrixforge-runner" data-packages="{packages}">
  <div class="matrixforge-runner__header">
    <div>
      <p class="matrixforge-runner__eyebrow">Python Example</p>
      <p class="matrixforge-runner__title">{title}</p>
    </div>
    <button type="button" class="matrixforge-runner__run">Run</button>
  </div>
  <div class="matrixforge-runner__body">
    <textarea class="matrixforge-runner__code" spellcheck="false" aria-label="Editable Python example">{code}</textarea>
    <section class="matrixforge-runner__result" aria-label="Python output">
      <div class="matrixforge-runner__result-header">
        <span>Output</span>
        <span class="matrixforge-runner__status" aria-live="polite">Ready</span>
      </div>
      <pre class="matrixforge-runner__output" aria-live="polite">Click Run to execute the example.</pre>
      <div class="matrixforge-runner__artifacts" aria-live="polite"></div>
    </section>
  </div>
</div>
"""
        return [nodes.raw("", html, format="html")]


def setup(app: Sphinx) -> dict[str, bool]:
    app.add_directive("matrixforge-path", MatrixForgePathDirective)
    app.add_directive("matrixforge-runner", MatrixForgeRunnerDirective)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
