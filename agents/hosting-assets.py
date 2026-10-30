#!/usr/bin/env python3
"""
Agente de Hosting Assets para Lia Morano
Recebe path local de imagem gerada, faz commit em /images/ e retorna raw.githubusercontent.com URL.
Uso: python hosting-assets.py <local_image_path> <target_filename>
"""
import os
import sys
import base64
import requests

# Placeholder - requer GITHUB_TOKEN no env
def main():
    if len(sys.argv) < 3:
        print("Uso: python hosting-assets.py <image_path> <filename.jpg>")
        return
    image_path = sys.argv[1]
    filename = sys.argv[2]
    # TODO: implementar upload via GitHub API
    print(f"Hosting agent ready for {filename}. Implement upload logic.")
    print(f"Expected raw URL: https://raw.githubusercontent.com/NARCHVILLE/lia-morano-assets/main/images/{filename}")

if __name__ == "__main__":
    main()
