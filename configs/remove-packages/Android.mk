LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := RemovePackages
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := \
    AdaptiveVPNPrebuilt-10307 \
    AiWallpapers \
    arcore-1.42 \
    Aperture \
    Backgrounds \
    CalculatorGooglePrebuilt \
    CalendarGooglePrebuilt \
    Camera2 \
    Chrome \
    DevicePolicyPrebuilt \
    GoogleContacts \
    Maps \
    Photos \
    PixelLiveWallpaperPrebuilt \
    PixelWallpapers2024 \
    PixelThemesStub \
    PixelThemesStub2022_and_newer \
    PrebuiltGmail \
    ScribePrebuilt \
    SoundAmplifierPrebuilt \
    SwitchAccessPrebuilt \
    Snap \
    Snap2 \
    Tycho \
    Velvet \
    YouTube \
    YouTubeMusicPrebuilt \
    YTMusic

LOCAL_UNINSTALLABLE_MODULE := true
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_SRC_FILES := /dev/null
include $(BUILD_PREBUILT)
