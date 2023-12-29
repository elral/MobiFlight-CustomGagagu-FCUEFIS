Import("env")
import os

# Get the version number from the build environment.
firmware_version = os.environ.get('VERSION', "")
core_version = os.environ.get('CORE_VERSION', "")

# Clean up the version number
if firmware_version == "":
  # When no version is specified default to "0.0.1" for
  # compatibility with MobiFlight desktop app version checks.
  firmware_version = "0.0.1"
if core_version == "":
  # When no version is specified default to "0.0.1" for
  # compatibility with MobiFlight desktop app version checks.
  core_version = "2.4.1"

# Strip any leading "v" that might be on the version and
# any leading or trailing periods.
firmware_version = firmware_version.lstrip("v")
firmware_version = firmware_version.strip(".")
core_version = core_version.lstrip("v")
core_version = core_version.strip(".")

print(f'Using version {firmware_version} for the build')
print(f'Using Core version {core_version} for the build')

# Append the version to the build defines so it gets baked into the firmware
env.Append(CPPDEFINES=[
  f'BUILD_VERSION={firmware_version}',
  f'CORE_VERSION={core_version}'
])

# Set the output filename to the name of the board and the version
env.Replace(PROGNAME=f'{env["PIOENV"]}_{firmware_version.replace(".", "_")}')
