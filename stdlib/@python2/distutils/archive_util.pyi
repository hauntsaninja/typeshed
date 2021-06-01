from typing import Optional

def make_archive(
    base_name: str,
    format: str,
    root_dir: str | None = ...,
    base_dir: str | None = ...,
    verbose: int = ...,
    dry_run: int = ...,
) -> str: ...
def make_tarball(base_name: str, base_dir: str, compress: str | None = ..., verbose: int = ..., dry_run: int = ...) -> str: ...
def make_zipfile(base_name: str, base_dir: str, verbose: int = ..., dry_run: int = ...) -> str: ...
