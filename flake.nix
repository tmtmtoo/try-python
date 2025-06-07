{
  description = "try-dlt-dbt";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.uv
            pkgs.duckdb
            pkgs.just
          ];
          shellHook = ''
            uv venv
            uv sync --all-packages
            source .venv/bin/activate
          '';
        };
        formatter = pkgs.nixfmt-rfc-style;
      }
    );
}