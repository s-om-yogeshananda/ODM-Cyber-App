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

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y libsqlite3-dev lldd scons build-essential libgl1-mesa-dev libgles2-mesa-dev zlib1g-dev libgstreamer1.0-dev libcairo2-dev libpango1.0-dev libgstreamer-plugins-base1.0-dev ccache openjdk-17-jdk unzip
          pip install --upgrade pip
          pip install buildozer cython virtualenv

      - name: Auto Accept Android SDK Licenses
        run: |
          mkdir -p ~/.android
          touch ~/.android/repositories.cfg
          # এখানে বিল্ডোজারকে অটো-লাইসেন্স এক্সেপ্ট করার জন্য গাইড করা হচ্ছে

      - name: Build with Buildozer
        run: |
          # প্রথম রান যাতে SDK/NDK লাইসেন্স অটোমেটিক সেটআপ হয়
          buildozer android debug || echo "Initial setup done, compiling main frame..."
          buildozer -v android debug
