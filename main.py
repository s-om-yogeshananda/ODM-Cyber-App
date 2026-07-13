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

      - name: Setup Android SDK Path & Auto-Accept Licenses
        run: |
          # বিল্ডোজার রান করার আগে অটোমেটিক অ্যান্ড্রয়েড SDK লাইসেন্স এক্সেপ্ট করার ট্রিক
          mkdir -p ~/.android
          touch ~/.android/repositories.cfg
          mkdir -p ~/.buildozer/android/platform/android-sdk/licenses
          echo -e "\n24333f8a63b6825ea9c5514f83c2829b004d1fee" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
          echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-preview-license

      - name: Build with Buildozer
        run: |
          # এখানে আমরা সরাসরি বিল্ডোজার রান করব এবং এটি কোনো ইনপুট ছাড়াই এগোবে
          buildozer -v android debug
        env:
          ACCEPT_SDK_LICENSE: "y"

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: ODM-Cyberpunk-App
          path: bin/*.apk
