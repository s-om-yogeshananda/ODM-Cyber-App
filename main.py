name: Build ODM Premium APK
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y libsqlite3-dev lldd scons build-essential libgl1-mesa-dev libgles2-mesa-dev zlib1g-dev libgstreamer1.0-dev libcairo2-dev libpango1.0-dev libgstreamer-plugins-base1.0-dev ccache
          pip install --upgrade pip
          pip install buildozer cython virtualenv

      - name: Build with Buildozer
        run: |
          buildozer -v android debug
        env:
          ACCEPT_SDK_LICENSE: "y"

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: ODM-Cyberpunk-App
          path: bin/*.apk
