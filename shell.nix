let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = with pkgs; [
    (python312.withPackages(packages: with packages; [
      matplotlib
      pandas
      tabulate
    ]))
    ffmpeg
    gImageReader
  ];
}