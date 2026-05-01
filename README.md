# MatrixForge

**An interactive learning website about matrix mathematics.**

MatrixForge is a beginner-friendly guide to understanding matrices and their applications in digital signal processing, graphics, beamforming, and engineering. Built with Sphinx and MyST-NB, it combines clear explanations with executable Python code and interactive Jupyter notebooks.

## 🎯 What You'll Learn

- **Matrix Fundamentals**: Understand what matrices are, how they work, and why they matter
- **Core Operations**: Addition, multiplication, and transformations explained intuitively
- **Real Applications**: DSP, graphics, least squares, system solving, and more
- **Hands-On Examples**: Interactive Python code you can run and modify

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- A virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone git@github.com:IDerrington/MatrixForge.git
cd MatrixForge

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Build the Documentation

```bash
# Build the HTML documentation
sphinx-build -b html docs docs/_build/html

# Open the documentation in your browser
# Linux/macOS:
open docs/_build/html/index.html
# Windows:
start docs/_build/html/index.html
```

## 📚 Project Structure

```
matrixforge/
├── .github/workflows/    # GitHub Actions for automatic deployment
├── docs/                 # Sphinx documentation source
│   ├── fundamentals/     # Core matrix concepts
│   ├── applications/     # Real-world applications
│   └── conf.py           # Sphinx configuration
├── src/matrixforge/      # Python helper utilities
└── requirements.txt      # Python dependencies
```

## 🌐 Deployment

This project is automatically deployed to GitHub Pages using GitHub Actions whenever changes are pushed to the `main` branch.

View the live site at: **https://iderrington.github.io/MatrixForge/**

## 🛠️ Development

```bash
# Switch to the dev branch
git checkout dev

# Make your changes...

# Build locally to test
sphinx-build -b html docs docs/_build/html

# Commit and push
git add .
git commit -m "Your descriptive commit message"
git push origin dev
```

## 📖 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

MIT License - feel free to use this project for learning and teaching.

## 🙏 Acknowledgments

Built with:
- [Sphinx](https://www.sphinx-doc.org/)
- [MyST-NB](https://myst-nb.readthedocs.io/)
- [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

---

**Start forging your matrix knowledge today!** 🔨✨
