# Build patches

Apply from the Android source root after syncing these revisions:

| Project | Source | Revision |
| --- | --- | --- |
| frameworks/base | VoltageOS/frameworks_base_new | db91bd93ad97bcb60158fcc150198ac49fcf480b |
| frameworks/native | VoltageOS/frameworks_native | fad0dc514dc08ff93c5badd7e05dc92f4b3c9db1 |
| vendor/voltage | VoltageOS/vendor_voltage | 9b9effaa73d8571fca253f4545fc6f154069a3d3 |
| hardware/qcom-caf/sm8250/display | LineageOS/android_hardware_qcom_display | 9ec8cc08004bcf005fe5c174522e1f395d3f5888 |
| hardware/qcom-caf/sm8250/audio | LineageOS/android_hardware_qcom_audio | da531fc8a1348373308ccacaca5fdbb15baf700d |

```sh
git -C frameworks/base am ../../device/oneplus/enchilada/patches/frameworks_base/0001-Synchronize-notification-background-keyguard-state.patch
git -C hardware/qcom-caf/sm8250/display apply ../../../../device/oneplus/enchilada/patches/qcom_display/0001-Handle-legacy-color-interfaces.patch
git -C frameworks/native apply ../../device/oneplus/enchilada/patches/frameworks_native/0001-Support-legacy-HDR-brightness.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0002-Support-OEM-pickup-sensors.patch
git -C vendor/voltage am ../../device/oneplus/enchilada/patches/vendor_voltage/0001-Correct-the-GameSpace-package-name.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0003-Report-HDR-ratio-without-HBM.patch
git -C hardware/qcom-caf/sm8250/audio apply ../../../../device/oneplus/enchilada/patches/qcom_audio/0001-Enable-SDM845-stereo-capture.patch
```

Do not reapply patches already present in the source tree.

## WebView

Use the arm64 WebView revision `394b243c2796e36580dd8bae7822609e1c01b1ff`
from LineageOS/android_external_chromium-webview_prebuilt_arm64. Materialize its
Git LFS APK; the object SHA-256 is
`3b98460ccd41b2a1851c5a46e6dec6f86f1d14302ff2fa4deeb1d781e32f89a4`.
