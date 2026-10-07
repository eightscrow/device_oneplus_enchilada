# Build patches

These patches accompany the unofficial VoltageOS enchilada device configuration.
Apply them after syncing the specified upstream revisions and before building.
Android's build system does not apply these files automatically. Preserve local
work and stop on conflicts or a different upstream base.

## Framework base and notification background

Use [VoltageOS/frameworks_base_new](https://github.com/VoltageOS/frameworks_base_new)
at `db91bd93ad97bcb60158fcc150198ac49fcf480b`. This includes the upstream
multi-audio ducking and mobile-data, Bluetooth and ringtone dialog fixes.

The existing notification patch synchronizes the background with its parent
keyguard state when initializing the background. Its original change is
`81a82daa39f2e3816e6f5c5119374dbe5a92e62d`; the patch content is unchanged.

From the Android source root, starting with the clean upstream framework base:

```sh
git -C frameworks/base am ../../device/oneplus/enchilada/patches/frameworks_base/0001-Synchronize-notification-background-keyguard-state.patch
```

Do not reapply a patch that is already present. Keep the manifest pinned to the
public upstream revision; preserve local commits or patches before syncing again.
No framework fork is required.

## Legacy display color and HDR brightness

Use [LineageOS/android_hardware_qcom_display](https://github.com/LineageOS/android_hardware_qcom_display)
at `9ec8cc08004bcf005fe5c174522e1f395d3f5888` for the sm8250 display path and
[VoltageOS/frameworks_native](https://github.com/VoltageOS/frameworks_native)
at `fad0dc514dc08ff93c5badd7e05dc92f4b3c9db1`.

```sh
git -C hardware/qcom-caf/sm8250/display apply ../../../../device/oneplus/enchilada/patches/qcom_display/0001-Handle-legacy-color-interfaces.patch
git -C frameworks/native apply ../../device/oneplus/enchilada/patches/frameworks_native/0001-Support-legacy-HDR-brightness.patch
```

The color patch preserves the display ID used by the legacy color library and
normalizes legacy render-intent metadata. The brightness patch propagates
successful HIDL backlight updates into composition luminance. HIDL cannot dim
individual layers, so boosted frames use GPU composition to preserve SDR white.
The device opts in through `debug.sf.legacy_hdr_brightness`; other devices retain
the existing default path. HIDL backlight updates remain non-atomic with frame
composition.

The display configuration caps HDR boost at 2x SDR luminance within the existing
normal brightness range. It reuses the panel brightness and automatic-brightness
resources and does not enable a new HBM mode. The standard HDR brightness toggle
and slider use Android's normal capability checks.

## Native pickup gesture

After the notification patch, apply the pickup adapter to the same framework base:

```sh
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0002-Support-OEM-pickup-sensors.patch
```

This connects the OEM on-change pickup sensor to SystemUI's existing per-user
pickup setting and proximity checks. The device selects `oneplus.sensor.pickup`
and exposes the existing Gestures and Lock screen settings. Pickup is disabled
by default; the existing ambient/full-wake choice is retained. No additional
sensor-polling service is required.

## GameSpace package references

Use [VoltageOS/vendor_voltage](https://github.com/VoltageOS/vendor_voltage)
at `9b9effaa73d8571fca253f4545fc6f154069a3d3` with the isolated upstream change
`02f2c7f74a8a7bce90766828f7c11061ededb964` by Frost. The supplied format-patch
preserves its original commit, author and message. It changes the two package
references only.

```sh
git -C vendor/voltage am ../../device/oneplus/enchilada/patches/vendor_voltage/0001-Correct-the-GameSpace-package-name.patch
```

## WebView

The accompanying arm64 WebView pin is
`394b243c2796e36580dd8bae7822609e1c01b1ff` (154.0.8037.57) in
[LineageOS/android_external_chromium-webview_prebuilt_arm64](https://github.com/LineageOS/android_external_chromium-webview_prebuilt_arm64).
Materialize its Git LFS APK. The object SHA-256 is
`3b98460ccd41b2a1851c5a46e6dec6f86f1d14302ff2fa4deeb1d781e32f89a4`.

## HDR ratio reporting without HBM

Apply to the same framework base:

```sh
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0003-Report-HDR-ratio-without-HBM.patch
```

This allows the display service to report HDR/SDR luminance ratios when the ratio
curve is supplied by HDR brightness configuration without enabling HBM. The
Settings capability check is unchanged. For the legacy OnePlus profile family,
the color patch preserves native SDR composition and the panel gamut selection
provided by LiveDisplay, while advertising explicit PQ and HLG profiles for HDR.
Adjustment profiles cannot overwrite those mappings during enumeration.

Native SDR profiles are selected from their color-gamut and dynamic-range
attributes. The legacy `zhal_native` profile contains calibrated color
processing and is not treated as a native bypass based on its name.

## SDM845 stereo audio capture

Use [LineageOS/android_hardware_qcom_audio](https://github.com/LineageOS/android_hardware_qcom_audio)
at `da531fc8a1348373308ccacaca5fdbb15baf700d` for the sm8250 audio path.

```sh
git -C hardware/qcom-caf/sm8250/audio apply ../../../../device/oneplus/enchilada/patches/qcom_audio/0001-Enable-SDM845-stereo-capture.patch
```

This patch selects the existing SDM845 platform definitions and permits up to
two input channels, matching the device audio policy and camera profiles.

## Notification and battery light controls

Use [VoltageOS/packages_apps_Settings](https://github.com/VoltageOS/packages_apps_Settings)
at `0f5c44f7f54f30c078817ae6310f274156ce35e8` and the framework base above.
Apply both patches together:

```sh
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0004-Configure-notification-and-battery-lights.patch
git -C packages/apps/Settings apply ../../../device/oneplus/enchilada/patches/settings/0001-Add-notification-light-controls.patch
```

## Touch vibration intensity

Use the framework base above, QCOM vibrator
`7ec51495bebe272097fc5b7f95cbf5ff92180e71`, OnePlus hardware
`1491bd7c03e831d0df90e00377ade708f32888ab` and SDM845 kernel
`4c0b4d6af5a511fc81269e278759fb0e640568f8`.

```sh
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0005-Scale-touch-vibration-amplitudes.patch
git -C vendor/qcom/opensource/vibrator apply ../../../../device/oneplus/enchilada/patches/qcom_vibrator/0001-Control-QPNP-haptic-amplitude.patch
git -C hardware/oneplus apply ../../device/oneplus/enchilada/patches/oneplus/0001-Add-touch-vibration-intensity-setting.patch
git -C kernel/oneplus/sdm845 apply ../../../device/oneplus/enchilada/patches/kernel/0001-Serialize-QPNP-haptic-activation.patch
```
