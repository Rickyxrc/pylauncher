{
    description = "A simple python launcher for myself.";

    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs/nixos-23.11";
        poetry2nix.url = "github:nix-community/poetry2nix";
    };

    outputs = { nixpkgs, poetry2nix, ...}: let
        system = "x86_64-linux";
        pkgs = import nixpkgs {
            inherit system;
            overlays = [ poetry2nix.overlays.default ];
        };
        app = pkgs.poetry2nix.mkPoetryApplication {
            projectDir = ./.;
        };
    in {
        devShells."${system}" = {
            default = pkgs.mkShell {
                packages = with pkgs; [ poetry ];
            };
        };
        packages."${system}".default = pkgs.writeShellApplication {
            name = "lchr";
            runtimeInputs =
                [ app.dependencyEnv ];
            text = ''
                python -m pylauncher "$@"
            '';
        };
    };
}
