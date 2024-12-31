import os

def create_portfolio_structure():
    base_dir = "portfolio"
    sub_dirs = [
        "content/pages",
    ]
    files = {
        "content/pages/about.md": "",
        "content/pages/jobs.md": "",
        "content/pages/publications.md": "",
        "content/pages/certifications.md": "",
        "content/pages/projects.md": "",
        "content/pages/keywords.md": "",
        "pelicanconf.py": "",
        "publishconf.py": "",
    }

    # Create directories
    for sub_dir in sub_dirs:
        os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)

    # Create files
    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, "w") as f:
            f.write(content)

create_portfolio_structure()
