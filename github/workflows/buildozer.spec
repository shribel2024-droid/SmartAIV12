name: Build SmartAI APK

on:
  workflow_dispatch:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "17"

      - name: Install system packages
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git zip unzip wget curl \
            build-essential \
            autoconf automake libtool pkg-config \
            libffi-dev libssl-dev \
            zlib1g-dev \
            libncurses5-dev libncursesw5-dev \
            cmake

      - name: Install Python tools
        run: |
          python -m pip install --upgrade pip
          pip install buildozer cython==0.29.37

      - name: Clean previous Buildozer cache
        run: |
          rm -rf .buildozer
          rm -rf ~/.buildozer

      - name: Build Debug APK
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: SmartAI-APK
          path: bin/*.apk
