# Build patches

Apply from the Android source root after syncing these revisions:

| Project | Source | Revision |
| --- | --- | --- |
| frameworks/base | VoltageOS/frameworks_base_new | d4c1e14903c7bc20d7524462263772b7767855c1 |
| frameworks/native | VoltageOS/frameworks_native | 35870619d3d7d23675438f7dd77c6566e5d67ef7 |
| frameworks/av | VoltageOS/frameworks_av | 3f9901cd806484e00004b5a7d8ec2ce41700d711 |
| packages/apps/Settings | VoltageOS/packages_apps_Settings | a75b43383ae44b98144398caa3d1dd22fc7ee133 |
| hardware/qcom-caf/sm8250/display | LineageOS/android_hardware_qcom_display | bf8aef12e2e95153f497e30d1791555cf7ff9b07 |
| vendor/qcom/opensource/vibrator | LineageOS/android_vendor_qcom_opensource_vibrator | 9d748eb141ebbdc39b8969f558c2a83391a39a77 |
| hardware/oneplus | LineageOS/android_hardware_oneplus | 3978f537f364fa8c8b23bab1ec870bd1eac17bc9 |
| hardware/interfaces | VoltageOS/hardware_interfaces | 6b3a497afc74b57d4296b2ff108839f5cf3265ea |
| vendor/oneplus/sdm845-common | OnePlus-6T-Development/vendor_oneplus_sdm845-common | 9ba1d09f1cfe715363856f34ab1aadba7032a87a |
| kernel/oneplus/sdm845 | eightscrow/android_kernel_oneplus_sdm845 | add4fb4356c4ffff7949a9c8d8d927f21d37e34f |

```sh
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0002-Support-OEM-pickup-sensors.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0003-Report-HDR-ratio-without-HBM.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0004-Configure-notification-and-battery-lights.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0005-Scale-touch-vibration-amplitudes.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0006-Camera2-Notify-fps-as-Session-Based-Parameter.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0007-Camera2-Apply-the-vendor-stream-configuration-mode.patch
git -C frameworks/native apply ../../device/oneplus/enchilada/patches/frameworks_native/0001-Support-legacy-HDR-brightness.patch
git -C frameworks/av apply ../../device/oneplus/enchilada/patches/frameworks_av/0001-Camera-Ignore-results-and-shutters-for-frames-no-lon.patch
git -C packages/apps/Settings apply ../../../device/oneplus/enchilada/patches/settings/0001-Add-notification-light-controls.patch
git -C hardware/qcom-caf/sm8250/display apply ../../../../device/oneplus/enchilada/patches/qcom_display/0001-Handle-legacy-color-interfaces.patch
git -C vendor/qcom/opensource/vibrator apply ../../../../device/oneplus/enchilada/patches/qcom_vibrator/0001-Control-QPNP-haptic-amplitude.patch
git -C hardware/oneplus apply ../../device/oneplus/enchilada/patches/oneplus/0001-Add-touch-vibration-intensity-setting.patch
git -C hardware/oneplus apply ../../device/oneplus/enchilada/patches/oneplus/0002-doze-Use-wakeUp-instead-of-wakeUpWithProximityCheck.patch
git -C hardware/oneplus apply ../../device/oneplus/enchilada/patches/oneplus/0003-KeyHandler-Add-the-process-to-the-whitelist.patch
git -C hardware/oneplus apply ../../device/oneplus/enchilada/patches/oneplus/0004-interfaces-Build-camera-HALs-from-source.patch
git -C hardware/oneplus apply ../../device/oneplus/enchilada/patches/oneplus/0005-oneplus-fwk-Sync-OpFeatures-with-OxygenOS-11.1.2.2.patch
git -C hardware/interfaces apply ../../device/oneplus/enchilada/patches/hardware_interfaces/0001-Camera-Do-not-hold-the-inflight-lock-across-configur.patch
git -C vendor/oneplus/sdm845-common apply ../../../device/oneplus/enchilada/patches/vendor_oneplus_sdm845-common/0001-sdm845-common-camera-Build-camera-HALs-from-source-3-3.patch
git -C vendor/oneplus/sdm845-common apply ../../../device/oneplus/enchilada/patches/vendor_oneplus_sdm845-common/0002-sdm845-common-camera-Drop-the-EIS-node.patch
```

Do not reapply patches already present in the source tree.

`vendor_oneplus_sdm845-common/0002` requires `vendor/oneplus/camera`, which
provides the replacement EIS node.

## WebView

Use the arm64 WebView revision `604ad4cbc41d3b894065ee6e83189c76e1ec06a1`
from LineageOS/android_external_chromium-webview_prebuilt_arm64. Materialize its
Git LFS APK; the object SHA-256 is
`e91bced008fa9a2976997072cd9168c653905b538217530994f20d73276e72d9`.
