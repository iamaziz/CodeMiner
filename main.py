import subprocess
import zipfile
import os


def download_repo(url, zip_name):
    cmd = f"curl -L {url} > {zip_name}"
    subprocess.run(cmd, shell=True)


def unzip_repo(zip_name, unzip_dir):
    with zipfile.ZipFile(zip_name, "r") as zip_ref:
        zip_ref.extractall(unzip_dir)


def scrape_source_files(unzip_dir, extensions, output_file):
    for root, dirs, files in os.walk(unzip_dir):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()

                with open(output_file, "a") as out_f:
                    out_f.write(f"\n\n// ---------- {file} ----------\n\n")
                    out_f.write(content)


if __name__ == "__main__":
    # Define the GitHub URL and the zip file name
    github_url = "https://github.com/spcl/graph-of-thoughts/archive/refs/heads/main.zip"
    zip_name = "source.tar.zip"
    unzip_dir = "unzipped_source"
    output_file = "all_source_files.txt"
    extensions = [".py", ".java", ".c", ".cpp", ".js"]

    # Download the repo
    download_repo(github_url, zip_name)

    # Unzip the repo
    unzip_repo(zip_name, unzip_dir)

    # Scrape and store all source code files in a single file
    scrape_source_files(unzip_dir, extensions, output_file)
