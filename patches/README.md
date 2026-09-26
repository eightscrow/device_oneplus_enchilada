# Build patches

Apply from the Android source root after syncing these revisions:

| Project | Source | Revision |
| --- | --- | --- |
| frameworks/base | VoltageOS/frameworks_base_new | db91bd93ad97bcb60158fcc150198ac49fcf480b |
| frameworks/native | VoltageOS/frameworks_native | fad0dc514dc08ff93c5badd7e05dc92f4b3c9db1 |
| hardware/qcom-caf/sm8250/display | LineageOS/android_hardware_qcom_display | 9ec8cc08004bcf005fe5c174522e1f395d3f5888 |

```sh
git -C frameworks/base am ../../device/oneplus/enchilada/patches/frameworks_base/0001-Synchronize-notification-background-keyguard-state.patch
git -C hardware/qcom-caf/sm8250/display apply ../../../../device/oneplus/enchilada/patches/qcom_display/0001-Handle-legacy-color-interfaces.patch
git -C frameworks/native apply ../../device/oneplus/enchilada/patches/frameworks_native/0001-Support-legacy-HDR-brightness.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0002-Support-OEM-pickup-sensors.patch
git -C frameworks/base apply ../../device/oneplus/enchilada/patches/frameworks_base/0003-Report-HDR-ratio-without-HBM.patch
```

Do not reapply patches already present in the source tree.
