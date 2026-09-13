# DeviceConfig compatibility

Override configs_base on enchilada to omit the obsolete discrete AppOps history
list in VoltageOS vendor_voltage 9b9effaa73d8571fca253f4545fc6f154069a3d3.
Keep every other upstream setting. The Android 17 platform then selects its own
supported default operations. Recheck this small copied array on upstream updates.

This product overlay must take precedence over the generated VoltageOS product
overlay; verify the resolved resource on the device after installation. Removing
an override does not delete a previously persisted DeviceConfig value. Existing
installations that received the invalid value need a separately tested migration.
